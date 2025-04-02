import xarray as xr
import zarr
import os
import math
import numpy as np
import time

# Constants for dimensions names to be used in the Zarr store
X_DIM = 'x'
Y_DIM = 'y'
T_DIM = 'time'

def ncs2zarr(nc_paths, zarr_path, beginning=True):
    total_start_time = time.time()

    if beginning or not os.path.exists(zarr_path):
        print(f"Creating new Zarr store at {zarr_path}")
        beginning = True
    else:
        print(f"Updating Zarr store at {zarr_path}")
    store = zarr.DirectoryStore(zarr_path)
    root_group = zarr.group(store=store, overwrite=beginning)

    for nc_info in nc_paths:
        var_start_time = time.time()
        nc_portions_path = nc_info['path']
        nc_var = nc_info['nc_var']
        var = nc_info['var']
        time_dim = nc_info.get('time_dim', 'time')
        ver_dim = nc_info.get('ver_dim', 'lat')
        hor_dim = nc_info.get('hor_dim', 'lon')
        nc_projection = nc_info.get('nc_projection', 'EPSG:4326')
        calc_min_max = nc_info.get('calc_min_max', True)
        include_center_calc = nc_info.get('include_center_calc', False)
        chunk_shape = nc_info.get('chunk_shape', (16, 128, 128))

        print(f"== Processing {var} ==")

        # Dimension renaming
        dims_mapping = {
            time_dim: T_DIM,
            ver_dim: Y_DIM,
            hor_dim: X_DIM
        }

        nc_ds = xr.open_dataset(nc_portions_path[0], chunks=None, decode_times=False)
        time_coords = nc_ds[time_dim].values                                                    # Valores de las fechas a procesar del nc
        time_steps = len(time_coords)                                                           # Número de fechas a procesar del nc

        if beginning:
            time_chunk_size = chunk_shape[0]
            num_chunks = math.ceil(time_steps / time_chunk_size)                                    # Número de lotes de fechas a procesar del nc
            print(f"Processing in {num_chunks} temporal chunks of size {time_chunk_size}:")

            # Procesar cada chunk temporal
            for chunk_idx in range(num_chunks):
                chunk_start = chunk_idx * time_chunk_size                                           # Índice inicial del lote de fechas a procesar del nc
                chunk_end = min((chunk_idx + 1) * time_chunk_size, time_steps) - 1                  # Índice final del lote de fechas a procesar del nc
                time_slice = slice(chunk_start, chunk_end + 1)
                
                print(f"* Processing time chunk {chunk_idx+1}/{num_chunks} (indices {chunk_start}:{chunk_end})...")

                ds = nc_ds.isel({time_dim: time_slice})                                                  # Selecciona el chunk de tiempo

                if nc_var != var:
                    ds = ds.rename_vars({nc_var: var})

                zarr_kwargs = {
                    'store': store,
                    'group': var,
                    'mode': 'w' if chunk_idx == 0 else 'a',
                    'write_empty_chunks': False
                }
                if chunk_idx > 0:
                    zarr_kwargs['append_dim'] = T_DIM

                ds.chunk({time_dim: chunk_shape[0], ver_dim: chunk_shape[1], hor_dim: chunk_shape[2]}) \
                    .rename(dims_mapping) \
                    .to_zarr(**zarr_kwargs)
        else:
            # Abrir el Zarr existente para obtener coordenadas temporales
            zarr_ds = xr.open_zarr(store, group=var, decode_times=False)
            existing_times = zarr_ds[T_DIM].values
            print(f"Processing {time_steps} dates:")
            
            # Procesar cada feecha
            for i, time_val in enumerate(time_coords):
                print(f"* Processing date: {i}: {time_val}")
                
                # Extract data for this specific time slice
                time_slice = nc_ds[nc_var].isel({time_dim: i})
                if time_val in existing_times:
                    print(f"  Date {time_val} already exists in Zarr, updating...")
                    existing_index = list(existing_times).index(time_val)
                    var_array = zarr.open_group(store)[var][var]
                    var_array[existing_index, :, :] = time_slice.values
                else:
                    print(f"  Date {time_val} not exists in Zarr, adding...")
                    new_slice_ds = xr.Dataset(
                        {var: ([T_DIM, Y_DIM, X_DIM], time_slice.values[np.newaxis, :, :])},
                        coords={
                            T_DIM: [time_val],
                            Y_DIM: zarr_ds[Y_DIM].values,
                            X_DIM: zarr_ds[X_DIM].values
                        }
                    )
                    new_slice_ds.to_zarr(store, group=var, append_dim=T_DIM)

                    existing_times = np.append(existing_times, time_val)

        # Close the dataset to free up resources
        nc_ds.close()

        consolidate_time_dimension(store, var)
        print(f"Total processing time for {var}: {(time.time() - var_start_time):.2f} seconds")

    print(f"Conversion completed. Total processing time: {(time.time() - total_start_time):.2f} seconds")

def consolidate_time_dimension(store, var):
    """
    Consolidate the time dimension of a Zarr dataset into a single chunk."
    """
    # Al final, después de procesar todos los chunks
    print("Consolidando dimensión temporal...")

    # Obtener acceso directo al array Zarr
    z_group = zarr.open_group(store=store, mode='a')
    var_group = z_group[var]

    # Reconfigurar solo el chunking del array de coordenadas temporales
    if T_DIM in var_group:
        # Guardar datos originales
        time_data = var_group[T_DIM][:]
        time_attrs = dict(var_group[T_DIM].attrs)
        
        # Eliminar el array original
        del var_group[T_DIM]
        
        # Recrear el array con un único chunk
        var_group.create_dataset(
            T_DIM, 
            data=time_data,
            chunks=(len(time_data),),  # Un único chunk para toda la dimensión
            dtype=time_data.dtype
        )
        
        # Restaurar atributos
        for key, value in time_attrs.items():
            var_group[T_DIM].attrs[key] = value
        
        print("Dimensión temporal consolidada en un único chunk")

    # Consolidar metadatos de Zarr (si no da error al hacer xr.open_zarr())
    zarr.consolidate_metadata(store)