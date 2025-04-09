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
beginning : bool, optional
    Whether to create a new Zarr store or update an existing one. Default is True.
    If True, a new Zarr store will be created. If False, the existing store will be updated.
    This parameter is ignored if the Zarr store does not exist.
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
    {'path': ['/path/to/kndvi.nc'], 'nc_var': 'KNDVI', 'var': 'kndvi', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (17, 52, 92)},
    {'path': ['/path/to/ndvi.nc'], 'nc_var': 'NDVI', 'var': 'ndvi', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (17, 52, 92)},
    {'path': ['/path/to/skndvi.nc'], 'nc_var': 'SKNDVI', 'var': 'skndvi', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (17, 52, 92)},
    {'path': ['/path/to/sndvi.nc'], 'nc_var': 'SNDVI', 'var': 'sndvi', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (17, 52, 92)},
]
zarr_path = '/path/to/vi-anomalies.zarr'
ncs2zarr(netcdfs, zarr_path, beginning=True)
"""

import xarray as xr
import zarr
import os
import math
import numpy as np
import time
import pyproj

# Constants for dimensions names to be used in the Zarr store
X_DIM = 'x'
Y_DIM = 'y'
T_DIM = 'time'

def ncs2zarr(nc_paths, zarr_path, beginning=True):
    total_start_time = time.time()
    store = _initialize_zarr_store(zarr_path, beginning)

    for nc_info in nc_paths:
        var_start_time = time.time()
        var = nc_info['var']
        print(f"== Processing {var} ==")

        if beginning:
            time_attrs_original, var_attrs_original = _process_beginning_mode(store, nc_info)
        else:
            _process_append_mode(store, nc_info)
            time_attrs_original = {}  # In append mode, we don't modify time attributes
            var_attrs_original = {}   # In append mode, we don't modify variable attributes

        print("Consolidating time dimension and restoring/adding attributes...")
        var_group = zarr.open_group(store=store, mode='a', path=var)
        _consolidate_time(var_group, var, time_attrs_original)
        _restore_variable_attrs(var_group, var, var_attrs_original)
        _add_var_attributes(var_group, nc_info)
        print(f"Total processing time for {var}: {(time.time() - var_start_time):.2f} seconds")

    z_group = zarr.open_group(store=store, mode='a')
    # Add root attributes
    _update_root_attributes(z_group, nc_paths)
    # Update geographical attributes
    if beginning:
        _add_root_attributes(z_group, nc_paths)

    # Consolidate Zarr metadata (to avoid errors when calling xr.open_zarr())
    zarr.consolidate_metadata(store)
    print(f"Conversion completed. Total processing time: {(time.time() - total_start_time):.2f} seconds")

def _initialize_zarr_store(zarr_path, beginning):
    """Initialize or open the Zarr store."""
    if beginning or not os.path.exists(zarr_path):
        print(f"Creating new Zarr store at {zarr_path}")
        beginning = True
    else:
        print(f"Updating Zarr store at {zarr_path}")

    store = zarr.DirectoryStore(zarr_path)
    zarr.group(store=store, overwrite=beginning)
    return store

def _sort_dim(ds, dim):
    if ds[dim][0] > ds[dim][-1]:
        ds = ds.reindex({dim: ds[dim][::-1]})
    return ds

def _my_open_dataset(nc_path, ver_dim, hor_dim, chunks=None, decode_times=False):
    ds_portion = xr.open_dataset(nc_path, chunks=chunks, decode_times=decode_times)
    ds_portion = _sort_dim(ds_portion, ver_dim)
    return _sort_dim(ds_portion, hor_dim)

def _process_beginning_mode(store, nc_info):
    """Process NetCDF in beginning mode with temporal chunking."""
    nc_portions_path = nc_info['path']
    nc_var = nc_info['nc_var']
    var = nc_info['var']
    time_dim = nc_info.get('time_dim', 'time')
    ver_dim = nc_info.get('ver_dim', 'lat')
    hor_dim = nc_info.get('hor_dim', 'lon')
    chunk_shape = nc_info.get('chunk_shape', (16, 128, 128))

    # Dimension mapping
    dims_mapping = {time_dim: T_DIM, ver_dim: Y_DIM, hor_dim: X_DIM}

    # Open all NetCDF portions
    nc_datasets = []
    for nc_path in nc_portions_path:
        ds = _my_open_dataset(nc_path, ver_dim, hor_dim, decode_times=False)
        nc_datasets.append(ds)

    # Save original variable attributes
    var_attrs_original = dict(nc_datasets[0][nc_var].attrs) if nc_var in nc_datasets[0] else {}

    for nc_ds in nc_datasets:
        # Remove _FillValue, missing_value, and units in variable attributes and encoding
        for attr_name in ['_FillValue', 'missing_value', 'units']:
            if attr_name in nc_ds[nc_var].attrs:
                del nc_ds[nc_var].attrs[attr_name]
            if hasattr(nc_ds[nc_var], 'encoding') and attr_name in nc_ds[nc_var].encoding:
                del nc_ds[nc_var].encoding[attr_name]

    time_coords = nc_datasets[0][time_dim].values
    time_steps = len(time_coords)

    # Save original time attributes
    time_attrs_original = dict(nc_datasets[0][time_dim].attrs) if time_dim in nc_datasets[0].coords else {}

    # Configure chunking
    time_chunk_size = chunk_shape[0]
    num_chunks = math.ceil(time_steps / time_chunk_size)
    print(f"Processing in {num_chunks} temporal chunks of size {time_chunk_size}:")

    # Process each temporal chunk
    for chunk_idx in range(num_chunks):
        _process_time_chunk(nc_datasets, store, chunk_idx, time_chunk_size, time_steps,
                            time_dim, ver_dim, hor_dim, nc_var, var, dims_mapping, chunk_shape, nc_info)

    return time_attrs_original, var_attrs_original

def _combine_netcdf_portions(datasets, ver_dim, hor_dim):
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
    reindexed_datasets = []
    for ds in datasets:
        # Add an additional step to each end of the coordinates
        ver_ds_vals = ds[ver_dim].values
        hor_ds_vals = ds[hor_dim].values
        ver_ds_step = abs(ver_ds_vals[1] - ver_ds_vals[0]) if len(ver_ds_vals) > 1 else 1.0
        hor_ds_step = abs(hor_ds_vals[1] - hor_ds_vals[0]) if len(hor_ds_vals) > 1 else 1.0

        # Create extended coordinates
        extended_ver = np.concatenate([[ver_ds_vals.min() - ver_ds_step], ver_ds_vals, [ver_ds_vals.max() + ver_ds_step]])
        extended_hor = np.concatenate([[hor_ds_vals.min() - hor_ds_step], hor_ds_vals, [hor_ds_vals.max() + hor_ds_step]])

        # Extend the dataset with NaNs at the edges
        extended_ds = ds.reindex({ver_dim: extended_ver, hor_dim: extended_hor})

        # Reindex the extended dataset to the common grid
        reindexed_ds = extended_ds.reindex({ver_dim: all_ver, hor_dim: all_hor}, method='nearest')
        reindexed_datasets.append(reindexed_ds)

    return xr.merge(reindexed_datasets, join="outer", combine_attrs='override')

def _process_time_chunk(nc_datasets, store, chunk_idx, time_chunk_size, time_steps,
                       time_dim, ver_dim, hor_dim, nc_var, var, dims_mapping, chunk_shape, nc_info):
    """Process a single time chunk and write to Zarr."""
    chunk_start = chunk_idx * time_chunk_size
    chunk_end = min((chunk_idx + 1) * time_chunk_size, time_steps) - 1
    time_slice = slice(chunk_start, chunk_end + 1)

    print(f"* Processing time chunk {chunk_idx+1}/{math.ceil(time_steps/time_chunk_size)} (indices {chunk_start}:{chunk_end})...")

    nc_datasets_sliced = []
    for nc_ds in nc_datasets:
        ds = nc_ds.isel({time_dim: time_slice})
        nc_datasets_sliced.append(ds)

    if len(nc_datasets_sliced) > 1:
        ds = _combine_netcdf_portions(nc_datasets_sliced, ver_dim, hor_dim)
    else:
        ds = nc_datasets_sliced[0]

    # Clean problematic time attributes
    if time_dim in ds.coords:
        ds[time_dim].attrs.pop('units', None)
        ds[time_dim].attrs.pop('calendar', None)

    # Rename variable if needed
    if nc_var != var:
        ds = ds.rename_vars({nc_var: var})

    # Calculate min and max values per time step if requested
    calc_min_max = nc_info.get('calc_min_max', True)
    if calc_min_max:
        min_var_name = f"{var}_min"
        max_var_name = f"{var}_max"

        # Calculate min/max for each time step
        time_values = ds[time_dim].values
        min_values = []
        max_values = []

        for i, _ in enumerate(time_values):
            time_slice_data = ds[var].isel({time_dim: i})
            # Ignore NaN values in min/max calculation
            min_val = float(np.nanmin(time_slice_data))
            max_val = float(np.nanmax(time_slice_data))
            min_values.append(min_val)
            max_values.append(max_val)

        # Create DataArrays for min and max values
        min_da = xr.DataArray(
            data=np.array(min_values),
            dims=[time_dim],
            coords={time_dim: time_values},
            name=min_var_name
        )

        max_da = xr.DataArray(
            data=np.array(max_values),
            dims=[time_dim],
            coords={time_dim: time_values},
            name=max_var_name
        )

        # Add min/max arrays to dataset
        ds[min_var_name] = min_da
        ds[max_var_name] = max_da

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

def _process_append_mode(store, nc_info):
    """Process NetCDF in append mode, updating or adding time slices."""
    nc_portions_path = nc_info['path']
    nc_var = nc_info['nc_var']
    var = nc_info['var']
    time_dim = nc_info.get('time_dim', 'time')
    ver_dim = nc_info.get('ver_dim', 'lat')
    hor_dim = nc_info.get('hor_dim', 'lon')

    # Open all NetCDF portions
    nc_datasets = []
    for nc_path in nc_portions_path:
        ds = _my_open_dataset(nc_path, ver_dim, hor_dim, decode_times=False)
        nc_datasets.append(ds)

    # Get time coordinates from first dataset (assuming all have same temporal coords)
    time_coords = nc_datasets[0][time_dim].values
    time_steps = len(time_coords)

    # Get existing time coordinates from zarr
    zarr_ds = xr.open_zarr(store, group=var, decode_times=False)
    existing_times = zarr_ds[T_DIM].values
    print(f"Processing {time_steps} dates:")

    # Process each date
    for i, time_val in enumerate(time_coords):
        print(f"* Processing date: {i}: {time_val}")

        # Extract this time slice from all datasets and sort dimensions
        nc_datasets_sliced = []
        for nc_ds in nc_datasets:
            ds = nc_ds.isel({time_dim: i})
            nc_datasets_sliced.append(ds)

        # Combine portions if more than one
        if len(nc_datasets_sliced) > 1:
            combined_ds = _combine_netcdf_portions(nc_datasets_sliced, ver_dim, hor_dim)
            time_slice = combined_ds[nc_var]
        else:
            time_slice = nc_datasets_sliced[0][nc_var]

        if time_val in existing_times:
            _update_existing_time(store, var, time_val, time_slice, existing_times)
        else:
            _add_new_time(store, var, time_val, time_slice, zarr_ds)

    # Close datasets
    for nc_ds in nc_datasets:
        nc_ds.close()

def _update_existing_time(store, var, time_val, time_slice, existing_times):
    """Update an existing time slice in the Zarr store."""
    print(f"  Date {time_val} already exists in Zarr, updating...")
    existing_index = list(existing_times).index(time_val)

    var_group = zarr.open_group(store)[var]

    # Update the main variable
    var_array = var_group[var]
    var_array[existing_index, :, :] = time_slice.values

    min_var_name = f"{var}_min"
    max_var_name = f"{var}_max"

    # Calculate and update min/max if they exist
    if min_var_name in var_group and max_var_name in var_group:
        # Calculate the new minimum and maximum values
        min_val = float(np.nanmin(time_slice.values))
        max_val = float(np.nanmax(time_slice.values))

        # Update the min/max arrays
        min_array = var_group[min_var_name]
        max_array = var_group[max_var_name]

        min_array[existing_index] = min_val
        max_array[existing_index] = max_val

def _add_new_time(store, var, time_val, time_slice, zarr_ds):
    print(f"  Date {time_val} not exists in Zarr, adding...")

    # Access Zarr arrays directly
    z_group = zarr.open_group(store=store, mode='a')
    var_group = z_group[var]
    var_array = var_group[var]
    time_array = var_group[T_DIM]

    # Get current position for appending
    current_length = time_array.shape[0]

    # Resize arrays to include the new timestep
    new_shape = list(var_array.shape)
    new_shape[0] = current_length + 1
    var_array.resize(new_shape)
    time_array.resize(current_length + 1)

    # Add the new data
    var_array[current_length, :, :] = time_slice.values
    time_array[current_length] = time_val

    min_var_name = f"{var}_min"
    max_var_name = f"{var}_max"

    # Process the min/max arrays if they exist
    if min_var_name in var_group and max_var_name in var_group:
        # Calculate the new minimum and maximum values
        min_val = float(np.nanmin(time_slice.values))
        max_val = float(np.nanmax(time_slice.values))

        # Get the min/max arrays
        min_array = var_group[min_var_name]
        max_array = var_group[max_var_name]

        # Resize the arrays to include the new timestep
        min_array.resize(current_length + 1)
        max_array.resize(current_length + 1)

        # Add the new values
        min_array[current_length] = min_val
        max_array[current_length] = max_val

def _restore_variable_attrs(var_group, var, var_attrs_original=None):
    if not var_attrs_original:
        return

    if var in var_group:
        var_array = var_group[var]
        # Update with original attributes
        for key, value in var_attrs_original.items():
            var_array.attrs[key] = value

def _consolidate_time(var_group, var, time_attrs_original=None):
    # Reconfigure only the chunking of the time coordinates array
    if T_DIM in var_group:
        # Save original data
        time_data = var_group[T_DIM][:]
        time_attrs = dict(var_group[T_DIM].attrs)

        # Preserve original attributes if they exist
        if time_attrs_original:
            # Merge current attributes with original ones, prioritizing original attributes
            for key, value in time_attrs_original.items():
                time_attrs[key] = value

        # Delete the original array
        del var_group[T_DIM]

        # Get original fill_value or use NaN
        original_fill_value = None  # Default value
        if '_FillValue' in time_attrs:
            original_fill_value = time_attrs['_FillValue']
        elif 'missing_value' in time_attrs:
            original_fill_value = time_attrs['missing_value']

        # Recreate the array with a single chunk
        var_group.create_dataset(
            T_DIM,
            data=time_data,
            chunks=(len(time_data),),  # A single chunk for the entire dimension
            dtype=time_data.dtype,
            fill_value=original_fill_value
        )

        # Restore attributes
        for key, value in time_attrs.items():
            var_group[T_DIM].attrs[key] = value

def _add_var_attributes(var_group, nc_info):
    nc_portions_path = nc_info['path']
    nc_var = nc_info['nc_var']
    nc_projection = nc_info.get('nc_projection', 'EPSG:4326')

    # Open the first NetCDF portion to get metadata
    first_ds = xr.open_dataset(nc_portions_path[0], decode_times=False)

    # Get metadata
    varTitle = first_ds[nc_var].attrs.get('long_name', nc_var)
    legendTitle = first_ds[nc_var].attrs.get('short_name', nc_var)

    # Add attributes to the group
    var_group.attrs['varTitle'] = varTitle
    var_group.attrs['legendTitle'] = legendTitle
    var_group.attrs['projection'] = nc_projection

    # Close the dataset
    first_ds.close()

def _update_root_attributes(z_group, nc_paths):
    # Add list of variables
    z_group.attrs['variables'] = [nc_info['var'] for nc_info in nc_paths]

    # Additional global attributes could be added here
    z_group.attrs['creation_date'] = time.strftime("%Y-%m-%d %H:%M:%S")
    z_group.attrs['version'] = '1.0'

def _calculate_zoom_level(lat_min, lat_max, lon_min, lon_max):
    # Calculate distances
    lat_distance = abs(lat_max - lat_min)
    lon_distance = abs(lon_max - lon_min)

    # Calculate zoom level based on the larger dimension
    # This formula approximates the zoom level needed to fit the extent in a view
    zoom_lat = math.log(360 / lat_distance) / math.log(2)
    zoom_lon = math.log(360 / lon_distance) / math.log(2)

    # Use the smaller zoom level to ensure entire area is visible
    zoom = min(zoom_lat, zoom_lon)

    # Round down to integer and apply some constraints
    zoom = max(1, min(20, math.floor(zoom)))

    return zoom

def _add_root_attributes(z_group, nc_paths):
    # Initialize variables for global extent
    lat_min_global = np.inf
    lat_max_global = -np.inf
    lon_min_global = np.inf
    lon_max_global = -np.inf

    # Process files that should be included in center calculation
    include_files = [info for info in nc_paths if info.get('include_center_calc', False)]

    if include_files:
        for info in include_files:
            # Get variable and dimension info
            var = info['var']

            # Open the Zarr dataset to use the already combined data
            try:
                lat_vals = z_group[var][Y_DIM][:]
                lon_vals = z_group[var][X_DIM][:]

                lat_min = np.min(lat_vals)
                lat_max = np.max(lat_vals)
                lon_min = np.min(lon_vals)
                lon_max = np.max(lon_vals)

                # Get projection from the group attributes
                projection = z_group[var].attrs.get('projection', 'EPSG:4326')

                # Convert to EPSG:4326 if needed
                if projection != 'EPSG:4326':
                    # Create coordinate transformer
                    crs = pyproj.CRS.from_string(projection)
                    transformer = pyproj.Transformer.from_crs(crs, 'EPSG:4326', always_xy=True)

                    # Transform corners
                    lon1, lat1 = transformer.transform(lon_min, lat_min)
                    lon2, lat2 = transformer.transform(lon_max, lat_min)
                    lon3, lat3 = transformer.transform(lon_min, lat_max)
                    lon4, lat4 = transformer.transform(lon_max, lat_max)

                    # Update min/max values
                    lat_min = min(lat1, lat2, lat3, lat4)
                    lat_max = max(lat1, lat2, lat3, lat4)
                    lon_min = min(lon1, lon2, lon3, lon4)
                    lon_max = max(lon1, lon2, lon3, lon4)

                # Update global extents
                lat_min_global = min(lat_min_global, lat_min)
                lat_max_global = max(lat_max_global, lat_max)
                lon_min_global = min(lon_min_global, lon_min)
                lon_max_global = max(lon_max_global, lon_max)

            except Exception as e:
                print(f"* Warning: Could not include {var} in geographic extent calculation: {e}")

        # Calculate center coordinates
        center_lat = (lat_min_global + lat_max_global) / 2
        center_lon = (lon_min_global + lon_max_global) / 2

        # Calculate appropriate zoom level
        zoom_level = _calculate_zoom_level(lat_min_global, lat_max_global, lon_min_global, lon_max_global)

        # Add to root group attributes
        z_group.attrs['center_lat'] = center_lat
        z_group.attrs['center_lon'] = center_lon
        z_group.attrs['zoom'] = zoom_level
    else:
        # If no files are included, set default values
        z_group.attrs['center_lat'] = 0.0
        z_group.attrs['center_lon'] = 0.0
        z_group.attrs['zoom'] = 1
