"""
Convert multiple NetCDF files to a Zarr store with additional metadata and chunking.
Parameters
----------
nc_paths : list of dict
    A list of dictionaries where each dictionary contains the following keys:
    - 'path' (list of str): Paths to the NetCDF file portions.
    - 'nc_var' (str): Name of the variable in the NetCDF file.
    - 'var' (str): Name to be used for the variable in the Zarr store.
    - 'time_dim' (str, optional): Name of the time dimension in the NetCDF file. Default is 'time'.
    - 'ver_dim' (str, optional): Name of the vertical dimension in the NetCDF file. Default is 'lat'.
    - 'hor_dim' (str, optional): Name of the horizontal dimension in the NetCDF file. Default is 'lon'.
    - 'nc_projection' (str, optional): Projection information for the dataset. Default is 'EPSG:4326'.
    - 'calc_min_max' (bool, optional): Whether to calculate minimum and maximum values for each variable over time. Default is True.
    - 'include_center_calc' (bool, optional): Whether to include the file in the calculation of the center of the global geographical extent. Default is False.
    - 'chunk_shape' (tuple of int, optional): Shape of chunks for each dimension (time, latitude, longitude). Default is (16, 128, 128).
zarr_path : str
    Path to the output Zarr store.
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
netcdfs = [
    {'path': ['/path/to/kndvi.nc'], 'nc_var': 'KNDVI', 'var': 'kndvi', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (17, 52, 92)},
    {'path': ['/path/to/ndvi.nc'], 'nc_var': 'NDVI', 'var': 'ndvi', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (17, 52, 92)},
    {'path': ['/path/to/skndvi.nc'], 'nc_var': 'SKNDVI', 'var': 'skndvi', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (17, 52, 92)},
    {'path': ['/path/to/sndvi.nc'], 'nc_var': 'SNDVI', 'var': 'sndvi', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (17, 52, 92)},
]
zarr_path = '/path/to/vi-anomalies.zarr'
ncs2zarr(netcdfs, zarr_path)
"""

import xarray as xr
import zarr
import numpy as np
import os
import pyproj
import time

# Constants for dimensions names to be used in the Zarr store
X_DIM = 'x'
Y_DIM = 'y'
T_DIM = 'time'

def ncs2zarr(nc_paths, zarr_path):
    total_start_time = time.time()

    # Initialize variables for global extent
    lat_min_global = np.inf
    lat_max_global = -np.inf
    lon_min_global = np.inf
    lon_max_global = -np.inf
    default_center = True

    # Create a root Zarr group
    store = zarr.DirectoryStore(zarr_path)
    root_group = zarr.group(store=store, overwrite=True)

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

        print(f"Processing {var}...")

        def my_open_dataset(nc_path):
            # Open the NetCDF file
            ds = xr.open_dataset(nc_path, chunks={time_dim: chunk_shape[0], ver_dim: None, hor_dim: None}, decode_times=False)
            # Replace fillvalue with NaN
            fillvalue = ds[nc_var].encoding.get('_FillValue', None)
            if fillvalue is not None and not np.isnan(fillvalue):
                elapsed_time = time.time()
                print(f"  * Replacing fillvalue {fillvalue} with NaN for {var} in {nc_path}...", end=" ")
                ds[nc_var] = ds[nc_var].astype(fillvalue.dtype).where(ds[nc_var].astype(fillvalue.dtype) != fillvalue, np.nan)
                print(f"[{(time.time() - elapsed_time):.2f} seconds]")
            return ds

        # Check if the spatial dimensions are ordered from smallest to largest and if not, invert them
        def sort_dim(ds, dim, nc_path):
            if ds[dim][0] > ds[dim][-1]:
                elapsed_time = time.time()
                print(f"  * Inverting {dim} in {nc_path}...", end=" ")
                ds = ds.reindex({dim: ds[dim][::-1]})
                print(f"[{(time.time() - elapsed_time):.2f} seconds]")
            return ds

        if len(nc_portions_path) > 1:
            # Open each portion of the NetCDF file and combine them
            datasets = []
            for nc_path in nc_portions_path:
                ds_portion = my_open_dataset(nc_path)
                ds_portion = sort_dim(ds_portion, ver_dim, nc_path)
                ds_portion = sort_dim(ds_portion, hor_dim, nc_path)
                ds_portion = ds_portion[[nc_var]]   # Keep only the variable of interest
                datasets.append(ds_portion)

            # Find min, max coordinates across all datasets
            ver_min = min([ds[ver_dim].min().item() for ds in datasets])
            ver_max = max([ds[ver_dim].max().item() for ds in datasets])
            hor_min = min([ds[hor_dim].min().item() for ds in datasets])
            hor_max = max([ds[hor_dim].max().item() for ds in datasets])

            # Find the smallest step size across all datasets
            ver_steps = []
            hor_steps = []
            for ds in datasets:
                if len(ds[ver_dim]) > 1:
                    diffs = np.diff(np.sort(ds[ver_dim].values))
                    min_diff = np.min(diffs[diffs > 0]) if np.any(diffs > 0) else None
                    if min_diff is not None:
                        ver_steps.append(min_diff)

                if len(ds[hor_dim]) > 1:
                    diffs = np.diff(np.sort(ds[hor_dim].values))
                    min_diff = np.min(diffs[diffs > 0]) if np.any(diffs > 0) else None
                    if min_diff is not None:
                        hor_steps.append(min_diff)

            # Get smallest step size for each dimension
            ver_step = min(ver_steps) if ver_steps else 1.0
            hor_step = min(hor_steps) if hor_steps else 1.0

            # Create regular grid from min to max with the step size
            all_ver = np.arange(ver_min, ver_max + ver_step*0.5, ver_step)
            all_hor = np.arange(hor_min, hor_max + hor_step*0.5, hor_step)

            # Reindex each dataset on the complete grid with nearest neighbor interpolation to avoid NaNs
            elapsed_time = time.time()
            print(f"  * Reindexing portions {nc_var}...", end=" ")
            datasets = [ ds.reindex({ver_dim: all_ver, hor_dim: all_hor}, method='nearest') for ds in datasets ]
            print(f"[{(time.time() - elapsed_time):.2f} seconds]")

            elapsed_time = time.time()
            print(f"  * Combining portions {nc_var}...", end=" ")
            ds = xr.merge(datasets, join="outer", combine_attrs='override')
            print(f"[{(time.time() - elapsed_time):.2f} seconds]")
        else:
            # Open the NetCDF file
            ds = my_open_dataset(nc_portions_path[0])
            ds = sort_dim(ds, ver_dim, nc_portions_path[0])
            ds = sort_dim(ds, hor_dim, nc_portions_path[0])

        # Rename the variable nc_var in the dataset
        if nc_var != var:
            elapsed_time = time.time()
            print(f"  * Renaming {nc_var} to {var}...", end=" ")
            ds = ds.rename_vars({nc_var: var})
            print(f"[{(time.time() - elapsed_time):.2f} seconds]")

        if include_center_calc:
            default_center = False
            # Update the global geographical extent
            lat_min = ds[ver_dim].min(skipna=True).compute().item()
            lat_max = ds[ver_dim].max(skipna=True).compute().item()
            lon_min = ds[hor_dim].min(skipna=True).compute().item()
            lon_max = ds[hor_dim].max(skipna=True).compute().item()

            # Convert to EPSG:4326 with pyproj
            crs = pyproj.CRS.from_string(nc_projection)
            transformer = pyproj.Transformer.from_crs(crs, 'EPSG:4326', always_xy=True)
            lon_min, lat_min = transformer.transform(lon_min, lat_min)
            lon_max, lat_max = transformer.transform(lon_max, lat_max)

            lat_min_global = min(lat_min_global, lat_min)
            lat_max_global = max(lat_max_global, lat_max)
            lon_min_global = min(lon_min_global, lon_min)
            lon_max_global = max(lon_max_global, lon_max)

        if calc_min_max:
            # Calculate varMin and varMax for each date
            elapsed_time = time.time()
            print(f"  * Calculating {var}_min and {var}_max for each date...", end=" ")
            varMin = ds[var].min(dim=[ver_dim, hor_dim], skipna=True).compute()
            varMax = ds[var].max(dim=[ver_dim, hor_dim], skipna=True).compute()
            print(f"[{(time.time() - elapsed_time):.2f} seconds]")

            # Create DataArray for varMin and varMax
            elapsed_time = time.time()
            print(f"  * Creating DataArrays for {var}_min and {var}_max...", end=" ")
            varMin_da = xr.DataArray(varMin, dims=[time_dim], name=f'{var}_min')
            varMax_da = xr.DataArray(varMax, dims=[time_dim], name=f'{var}_max')
            print(f"[{(time.time() - elapsed_time):.2f} seconds]")

            # Add the dataarrays varMin_da and varMax_da to the dataset
            elapsed_time = time.time()
            print(f"  * Adding {var}_min and {var}_max to the dataset...", end=" ")
            ds[var+'_min'] = varMin_da
            ds[var+'_max'] = varMax_da
            print(f"[{(time.time() - elapsed_time):.2f} seconds]")

            # Calculate global minVal and maxVal
            elapsed_time = time.time()
            print(f"  * Calculating global minVal and maxVal for {var}...", end=" ")
            minVal = varMin.min().item()
            maxVal = varMax.max().item()
            print(f"[{(time.time() - elapsed_time):.2f} seconds]")

        # Get metadata
        varTitle = ds[var].attrs.get('long_name', nc_var)
        legendTitle = ds[var].attrs.get('short_name', nc_var)

        # Dimension renaming
        dims_mapping = {
            time_dim: T_DIM,
            ver_dim: Y_DIM,
            hor_dim: X_DIM
        }

        # Write the dataset to Zarr in the corresponding group
        zarr_group = os.path.join('/', var)
        elapsed_time = time.time()
        print(f"  * Writing {var} to Zarr...", end=" ")
        ds[var] \
            .chunk({time_dim: chunk_shape[0], ver_dim: chunk_shape[1], hor_dim: chunk_shape[2]}) \
            .to_dataset(name=var) \
            .rename(dims_mapping) \
            .to_zarr(store, group=zarr_group, mode='w', write_empty_chunks=False)
        print(f"[{(time.time() - elapsed_time):.2f} seconds]")
        if calc_min_max:
            # Write varMin and varMax to Zarr
            elapsed_time = time.time()
            print(f"  * Writing {var}_min and {var}_max to Zarr...", end=" ")
            ds[var+'_min'] \
                .chunk({time_dim: -1}) \
                .to_dataset(name=var+'_min') \
                .rename({time_dim: T_DIM}) \
                .to_zarr(store, group=zarr_group, mode='a', write_empty_chunks=False)
            ds[var+'_max'] \
                .chunk({time_dim: -1}) \
                .to_dataset(name=var+'_max') \
                .rename({time_dim: T_DIM}) \
                .to_zarr(store, group=zarr_group, mode='a', write_empty_chunks=False)
            print(f"[{(time.time() - elapsed_time):.2f} seconds]")

        # Add metadata to the group
        group = root_group[zarr_group]
        group.attrs['varTitle'] = varTitle
        group.attrs['legendTitle'] = legendTitle
        if calc_min_max:
            group.attrs['minVal'] = minVal
            group.attrs['maxVal'] = maxVal
        group.attrs['projection'] = nc_projection

        print(f"Total processing time for {var}: {(time.time() - var_start_time):.2f} seconds")

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

    # Calculate the center of the global geographical extent
    if default_center:
        center_lat = 0
        center_lon = 0
        zoom_level = 1
    else:
        center_lat = (lat_min_global + lat_max_global) / 2
        center_lon = (lon_min_global + lon_max_global) / 2
        zoom_level = calculate_zoom(lat_min_global, lat_max_global, lon_min_global, lon_max_global)

    # Add metadata to the root group
    root_group.attrs['center_lat'] = center_lat
    root_group.attrs['center_lon'] = center_lon
    root_group.attrs['zoom_level'] = zoom_level
    root_group.attrs['variables'] = [nc_info['var'] for nc_info in nc_paths]

    print(f"Conversion completed. Total processing time: {(time.time() - total_start_time):.2f} seconds")