import xarray as xr
import zarr
import numpy as np
import os
import pyproj

# Niveles de iteración: nc_paths > nc_paths.path > Bloques de fechas
def ncs2zarr(nc_paths, zarr_path, chunk_shape=(16, 128, 128)):
    # Create a root Zarr group
    store = zarr.DirectoryStore(zarr_path)
    root_group = zarr.group(store=store, overwrite=True)

    for nc_info in nc_paths:
        nc_portions_path = nc_info['path']
        nc_var = nc_info['nc_var']
        var = nc_info['var']
        time_dim = nc_info.get('time_dim', 'time')
        lat_dim = nc_info.get('lat_dim', 'lat')
        lon_dim = nc_info.get('lon_dim', 'lon')
        
        print(f"Processing {var}...")

        datasets = []
        for nc_path in nc_portions_path:
            ds_portion = xr.open_dataset(nc_path, chunks='auto')
            datasets.append(ds_portion)
        ds = xr.combine_by_coords(datasets, data_vars=[nc_var], combine_attrs='override')

        # Rename the variable nc_var in the dataset
        ds = ds.rename_vars({nc_var: var})

        # Obtener dimensiones
        time_len = ds.sizes[time_dim]
        lat_len = ds.sizes[lat_dim]
        lon_len = ds.sizes[lon_dim]

        # Crear arreglo de índices para iterar por chunks
        time_chunk_size = chunk_shape[0]
        time_indices = np.arange(0, time_len, time_chunk_size)

        zarr_group = os.path.join('/', var)
        for i in range(len(time_indices)):
            start = time_indices[i]
            end = time_indices[i] + time_chunk_size
            if end > time_len:
                end = time_len

            # Seleccionar el subset del dataset
            ds_subset = ds.isel({time_dim: slice(start, end)})

            # Especificar la región donde escribir los datos
            region = {time_dim: slice(start, end), lat_dim: slice(0, lat_len), lon_dim: slice(0, lon_len)}

            # Escribir al Zarr usando region
            #ds_subset.drop_vars(['crs']).to_zarr(store, group=zarr_group, region=region, compute=True, mode='a', consolidated=False)
            #ds_subset[var].chunk({time_dim: chunk_shape[0], lat_dim: chunk_shape[1], lon_dim: chunk_shape[2]}).to_dataset(name=var).to_zarr(store, group=zarr_group, region=region, compute=True, mode='a', write_empty_chunks=False)
            ds_subset.drop_vars(['crs']).chunk({time_dim: chunk_shape[0], lat_dim: chunk_shape[1], lon_dim: chunk_shape[2]}).to_zarr(store, group=zarr_group, append_dim=time_dim, compute=True, mode='a', write_empty_chunks=False)

    print("Conversion completed.")


# Example usage
# netcdfs = [
#     {'path': ['/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/kndvi.nc'], 'nc_var': 'KNDVI', 'var': 'kndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'projection': 'EPSG:23030'},
#     {'path': ['/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/ndvi.nc'], 'nc_var': 'NDVI', 'var': 'ndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'projection': 'EPSG:23030'},
#     {'path': ['/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/skndvi.nc'], 'nc_var': 'SKNDVI', 'var': 'skndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'projection': 'EPSG:23030'},
#     {'path': ['/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/sndvi.nc'], 'nc_var': 'SNDVI', 'var': 'sndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'projection': 'EPSG:23030'},
# ]
# zarr_path = '/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies.zarr'


netcdfs = [
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/etm/tmin_daily_grid_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/etm/tmin_daily_grid_can.nc'], 'nc_var': 'tmin', 'var': 'tmin', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'projection': 'EPSG:4326'},
    #{'path': ['/home/edumoreno/git/nczarrgenerator/nc/etm/tmax_daily_grid_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/etm/tmax_daily_grid_can.nc'], 'nc_var': 'tmax', 'var': 'tmax', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'projection': 'EPSG:4326'},
]
zarr_path = '/home/edumoreno/git/nczarrgenerator/nc/etm.zarr'


#ncs2zarr(netcdfs, zarr_path, chunk_shape=(354, 52, 92))
ncs2zarr(netcdfs, zarr_path, chunk_shape=(354, 43, 69))
