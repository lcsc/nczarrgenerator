import xarray as xr
import zarr
import dask
import numpy as np
import os

def ncs2zarr(nc_paths, zarr_path, chunk_num=(64, 8, 8)):
    # Inicializar variables para la extensión global
    lat_min_global = np.inf
    lat_max_global = -np.inf
    lon_min_global = np.inf
    lon_max_global = -np.inf

    # Crear un grupo raíz Zarr
    store = zarr.DirectoryStore(zarr_path)
    root_group = zarr.group(store=store, overwrite=True)

    for nc_info in nc_paths:
        nc_path = nc_info['path']
        nc_var = nc_info['nc_var']
        var = nc_info['var']
        time_dim = nc_info.get('time_dim', 'time')
        lat_dim = nc_info.get('lat_dim', 'lat')
        lon_dim = nc_info.get('lon_dim', 'lon')
        
        print(f"Procesando {var}...")

        # Abrir el dataset netCDF con chunks
        ds = xr.open_dataset(nc_path, chunks='auto')
        # Renombramos el nombre de la variable nc_var del dataset
        ds = ds.rename_vars({nc_var: var})

        # Actualizar la extensión geográfica global
        lat_min = ds[lat_dim].min(skipna=True).compute().item()
        lat_max = ds[lat_dim].max(skipna=True).compute().item()
        lon_min = ds[lon_dim].min(skipna=True).compute().item()
        lon_max = ds[lon_dim].max(skipna=True).compute().item()

        lat_min_global = min(lat_min_global, lat_min)
        lat_max_global = max(lat_max_global, lat_max)
        lon_min_global = min(lon_min_global, lon_min)
        lon_max_global = max(lon_max_global, lon_max)

        var_data = ds[var]

        # Calcular varMin y varMax para cada fecha
        varMin = var_data.min(dim=[lat_dim, lon_dim]).compute()
        varMax = var_data.max(dim=[lat_dim, lon_dim]).compute()

        # Crear DataArray para varMin y varMax
        varMin_da = xr.DataArray(varMin, dims=[time_dim], name=f'{var}_min')
        varMax_da = xr.DataArray(varMax, dims=[time_dim], name=f'{var}_max')

        # Añadir los dataarrays varMin_da y varMax_da al dataset
        ds[var+'_min'] = varMin_da
        ds[var+'_max'] = varMax_da


        # Calcular minVal y maxVal globales
        minVal = varMin.min().item()
        maxVal = varMax.max().item()

        # Obtener metadatos
        varTitle = var_data.attrs.get('long_name', nc_var)
        legendTitle = var_data.attrs.get('short_name', nc_var)
        projection = ds.attrs.get('projection', 'desconocida')

        # Calcular tamaños de chunks basados en el número de chunks deseado
        time_len = ds.sizes[time_dim]
        lat_len = ds.sizes[lat_dim]
        lon_len = ds.sizes[lon_dim]

        chunk_sizes = (
            max(1, time_len // chunk_num[0] + 1),
            max(1, lat_len // chunk_num[1] + 1),
            max(1, lon_len // chunk_num[2] + 1)
        )

        # Escribir el dataset al Zarr en el grupo correspondiente
        zarr_group = os.path.join('/', var)
        ds[var].chunk({time_dim: chunk_sizes[0], lat_dim: chunk_sizes[1], lon_dim: chunk_sizes[2]}).to_zarr(store, group=zarr_group, mode='w')
        ds[var+'_min'].chunk({time_dim: -1}).to_zarr(store, group=zarr_group, mode='a')
        ds[var+'_max'].chunk({time_dim: -1}).to_zarr(store, group=zarr_group, mode='a')

        # Agregar metadatos al grupo
        group = root_group[zarr_group]
        group.attrs['varTitle'] = varTitle
        group.attrs['legendTitle'] = legendTitle
        group.attrs['minVal'] = minVal
        group.attrs['maxVal'] = maxVal
        group.attrs['projection'] = projection

    # Calcular centro de la extensión geográfica global
    center_lat = (lat_min_global + lat_max_global) / 2
    center_lon = (lon_min_global + lon_max_global) / 2

    # Calcular nivel de zoom (esto es una aproximación)
    def calculate_zoom(lat_min, lat_max, lon_min, lon_max):
        lat_extent = lat_max - lat_min
        lon_extent = lon_max - lon_min
        max_extent = max(lat_extent, lon_extent)
        # Supongamos que nivel de zoom se basa en la extensión máxima
        if max_extent >= 180:
            zoom = 1
        elif max_extent >= 90:
            zoom = 2
        elif max_extent >= 45:
            zoom = 3
        elif max_extent >= 22.5:
            zoom = 4
        elif max_extent >= 11.25:
            zoom = 5
        elif max_extent >= 5.625:
            zoom = 6
        elif max_extent >= 2.813:
            zoom = 7
        elif max_extent >= 1.406:
            zoom = 8
        elif max_extent >= 0.703:
            zoom = 9
        else:
            zoom = 10
        return zoom

    zoom_level = calculate_zoom(lat_min_global, lat_max_global, lon_min_global, lon_max_global)

    # Agregar metadatos al grupo raíz
    root_group.attrs['lat_centro'] = center_lat
    root_group.attrs['lon_centro'] = center_lon
    root_group.attrs['nivel_zoom'] = zoom_level

    print("Conversión completada.")

# Ejemplo de uso
netcdfs = [
    {'path': '/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/kndvi.nc', 'nc_var': 'KNDVI', 'var': 'kndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x'},
    {'path': '/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/ndvi.nc', 'nc_var': 'NDVI', 'var': 'ndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x'},
    {'path': '/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/skndvi.nc', 'nc_var': 'SKNDVI', 'var': 'skndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x'},
    {'path': '/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/sndvi.nc', 'nc_var': 'SNDVI', 'var': 'sndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x'},
]
zarr_path = '/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies.zarr'
ncs2zarr(netcdfs, zarr_path)