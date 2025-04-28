# Description: Script to convert a NetCDF file to Zarr format
# haciéndolo por lotes de 10 en 10 fechas para evitar problemas de memoria

import xarray as xr
import rioxarray
import numpy as np
import math

# Ruta del fichero netCDF
netcdf_file = 'nc/dAI_SSP5_2100_ISIMIP3b_05.nc'
netcdf_u_file = 'nc/dAIu_SSP5_2100_ISIMIP3b_05.nc'
# Ruta del almacenamiento Zarr
zarr_store = 'nc/gams_1x8x8.zarr'

# Número de chunks para dividir el dataset
chunks = {'time': 1, 'lat': 8, 'lon': 8}

# Cargar el dataset sin chunks para poder iterar sobre las fechas
data = xr.open_dataset(netcdf_file)
data_u = xr.open_dataset(netcdf_u_file)
# data = data.rio.set_spatial_dims('lon', 'lat')        # No necesario, ya que las dimensiones geográficas ya se llaman así
# data = data.rio.write_crs('EPSG:25830')               # No necesario, ya que el netcdf incluye campo CRS

# Dividir el dataset en lotes por tiempo
time_chunks = 1  # Número de pasos temporales por lote
num_times = data.sizes['time']
time_indices = np.arange(0, num_times, time_chunks)

# Guardar los lotes reproyectados en Zarr
for start in time_indices:
    end = min(start + time_chunks, num_times)
    subset = data.isel(time=slice(start, end))
    subset_u = data_u.isel(time=slice(start, end))
    #subset = subset.rio.set_spatial_dims('lon', 'lat')  # No necesario, ya que las dimensiones geográficas ya se llaman así

    # Eliminar el atributo grid_mapping de las variables reproyectadas
    for var in subset.variables:
        subset[var].attrs.pop('grid_mapping', None)
    for var_u in subset_u.variables:
        subset_u[var_u].attrs.pop('grid_mapping', None)

    subset['AIv'].encoding = {'chunks': (math.trunc(data.sizes['time']/chunks['time']) + 1,
                                         math.trunc(subset.sizes['lat']/chunks['lat']) + 1,
                                         math.trunc(subset.sizes['lon']/chunks['lon']) + 1)}
    subset_u['unc'].encoding = {'chunks': (math.trunc(data.sizes['time']/chunks['time']) + 1,
                                           math.trunc(subset.sizes['lat']/chunks['lat']) + 1,
                                           math.trunc(subset.sizes['lon']/chunks['lon']) + 1)}

    # Guardar el lote reproyectado en Zarr
    if start == 0:
        # Crear un nuevo archivo Zarr en el primer lote
        subset.to_zarr(zarr_store, mode='w', consolidated=True)
        subset_u.to_zarr(zarr_store, mode='a', consolidated=True)
    else:
        # Eliminar el atributo _FillValue de las variables reproyectadas
        for var in subset.variables:
            subset[var].attrs.pop('_FillValue', None)
        for var_u in subset_u.variables:
            subset_u[var_u].attrs.pop('_FillValue', None)
        # Añadir al archivo Zarr existente en los siguientes lotes
        subset.to_zarr(zarr_store, mode='a', append_dim='time', consolidated=True)
        subset_u.to_zarr(zarr_store, mode='a', append_dim='time', consolidated=True)

print("Guardado en Zarr completado.")