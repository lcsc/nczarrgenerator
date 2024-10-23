"""
Convert multiple NetCDF files to a Zarr store with additional metadata and chunking.
Parameters
----------
nc_paths : list of dict
    A list of dictionaries where each dictionary contains the following keys:
    - 'path' (str): Path to the NetCDF file.
    - 'nc_var' (str): Name of the variable in the NetCDF file.
    - 'var' (str): Name to be used for the variable in the Zarr store.
    - 'time_dim' (str, optional): Name of the time dimension in the NetCDF file. Default is 'time'.
    - 'lat_dim' (str, optional): Name of the latitude dimension in the NetCDF file. Default is 'lat'.
    - 'lon_dim' (str, optional): Name of the longitude dimension in the NetCDF file. Default is 'lon'.
    - 'projection' (str, optional): Projection information for the dataset. Default is 'desconocida'.
zarr_path : str
    Path to the output Zarr store.
chunk_num : tuple of int, optional
    Number of chunks for each dimension (time, latitude, longitude). Default is (64, 8, 8).
Returns
-------
None
Notes
-----
- The function calculates global geographical extents (latitude and longitude) and adds them as metadata to the root group.
- It also calculates the minimum and maximum values for each variable over time and adds them as new variables in the Zarr store.
- Additional metadata such as variable titles, legend titles, and projection information are also added to the Zarr store.
- The function calculates an approximate zoom level based on the geographical extents and adds it as metadata to the root group.
Example
-------
    {'path': '/path/to/kndvi.nc', 'nc_var': 'KNDVI', 'var': 'kndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'projection': 'EPSG:23030'},
    {'path': '/path/to/ndvi.nc', 'nc_var': 'NDVI', 'var': 'ndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'projection': 'EPSG:23030'},
    {'path': '/path/to/skndvi.nc', 'nc_var': 'SKNDVI', 'var': 'skndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'projection': 'EPSG:23030'},
    {'path': '/path/to/sndvi.nc', 'nc_var': 'SNDVI', 'var': 'sndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'projection': 'EPSG:23030'},
zarr_path = '/path/to/output.zarr'
"""

import xarray as xr
import zarr
import numpy as np
import os
import pyproj

def ncs2zarr(nc_paths, zarr_path, chunk_num=(64, 8, 8)):
    # Initialize variables for global extent
    lat_min_global = np.inf
    lat_max_global = -np.inf
    lon_min_global = np.inf
    lon_max_global = -np.inf

    # Create a root Zarr group
    store = zarr.DirectoryStore(zarr_path)
    root_group = zarr.group(store=store, overwrite=True)

    for nc_info in nc_paths:
        nc_path = nc_info['path']
        nc_var = nc_info['nc_var']
        var = nc_info['var']
        time_dim = nc_info.get('time_dim', 'time')
        lat_dim = nc_info.get('lat_dim', 'lat')
        lon_dim = nc_info.get('lon_dim', 'lon')
        
        print(f"Processing {var}...")

        # Open the NetCDF dataset with chunks
        ds = xr.open_dataset(nc_path, chunks='auto')
        # Rename the variable nc_var in the dataset
        ds = ds.rename_vars({nc_var: var})

        # Update the global geographical extent
        lat_min = ds[lat_dim].min(skipna=True).compute().item()
        lat_max = ds[lat_dim].max(skipna=True).compute().item()
        lon_min = ds[lon_dim].min(skipna=True).compute().item()
        lon_max = ds[lon_dim].max(skipna=True).compute().item()

        # Convert to EPSG:4326 with pyproj
        crs = pyproj.CRS.from_string(nc_info['projection'])
        transformer = pyproj.Transformer.from_crs(crs, 'EPSG:4326')
        lon_min, lat_min = transformer.transform(lon_min, lat_min)
        lon_max, lat_max = transformer.transform(lon_max, lat_max)

        lat_min_global = min(lat_min_global, lat_min)
        lat_max_global = max(lat_max_global, lat_max)
        lon_min_global = min(lon_min_global, lon_min)
        lon_max_global = max(lon_max_global, lon_max)

        var_data = ds[var]

        # Calculate varMin and varMax for each date
        varMin = var_data.min(dim=[lat_dim, lon_dim]).compute()
        varMax = var_data.max(dim=[lat_dim, lon_dim]).compute()

        # Create DataArray for varMin and varMax
        varMin_da = xr.DataArray(varMin, dims=[time_dim], name=f'{var}_min')
        varMax_da = xr.DataArray(varMax, dims=[time_dim], name=f'{var}_max')

        # Add the dataarrays varMin_da and varMax_da to the dataset
        ds[var+'_min'] = varMin_da
        ds[var+'_max'] = varMax_da

        # Calculate global minVal and maxVal
        minVal = varMin.min().item()
        maxVal = varMax.max().item()

        # Get metadata
        varTitle = var_data.attrs.get('long_name', nc_var)
        legendTitle = var_data.attrs.get('short_name', nc_var)
        projection = ds.attrs.get('projection', 'desconocida')

        # Calculate chunk sizes based on the desired number of chunks
        time_len = ds.sizes[time_dim]
        lat_len = ds.sizes[lat_dim]
        lon_len = ds.sizes[lon_dim]

        chunk_sizes = (
            max(1, time_len // chunk_num[0] + 1),
            max(1, lat_len // chunk_num[1] + 1),
            max(1, lon_len // chunk_num[2] + 1)
        )

        # Write the dataset to Zarr in the corresponding group
        zarr_group = os.path.join('/', var)
        ds[var].chunk({time_dim: chunk_sizes[0], lat_dim: chunk_sizes[1], lon_dim: chunk_sizes[2]}).to_zarr(store, group=zarr_group, mode='w')
        ds[var+'_min'].chunk({time_dim: -1}).to_zarr(store, group=zarr_group, mode='a')
        ds[var+'_max'].chunk({time_dim: -1}).to_zarr(store, group=zarr_group, mode='a')

        # Add metadata to the group
        group = root_group[zarr_group]
        group.attrs['varTitle'] = varTitle
        group.attrs['legendTitle'] = legendTitle
        group.attrs['minVal'] = minVal
        group.attrs['maxVal'] = maxVal
        group.attrs['projection'] = projection

    # Calculate the center of the global geographical extent
    center_lat = (lat_min_global + lat_max_global) / 2
    center_lon = (lon_min_global + lon_max_global) / 2

    # Calculate zoom level (this is an approximation)
    def calculate_zoom(lat_min, lat_max, lon_min, lon_max):
        lat_extent = lat_max - lat_min
        lon_extent = lon_max - lon_min
        max_extent = max(lat_extent, lon_extent)
        # Assume zoom level is based on the maximum extent
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

    # Add metadata to the root group
    root_group.attrs['center_lat'] = center_lat
    root_group.attrs['center_lon'] = center_lon
    root_group.attrs['zoom_level'] = zoom_level

    print("Conversion completed.")

# Example usage
netcdfs = [
    {'path': '/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/kndvi.nc', 'nc_var': 'KNDVI', 'var': 'kndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'projection': 'EPSG:23030'},
    {'path': '/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/ndvi.nc', 'nc_var': 'NDVI', 'var': 'ndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'projection': 'EPSG:23030'},
    {'path': '/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/skndvi.nc', 'nc_var': 'SKNDVI', 'var': 'skndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'projection': 'EPSG:23030'},
    {'path': '/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/sndvi.nc', 'nc_var': 'SNDVI', 'var': 'sndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'projection': 'EPSG:23030'},
]
zarr_path = '/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies.zarr'
ncs2zarr(netcdfs, zarr_path)