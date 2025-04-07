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
    {'path': ['/path/to/kndvi.nc'], 'nc_var': 'KNDVI', 'var': 'kndvi', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (17, 52, 92)},
    {'path': ['/path/to/ndvi.nc'], 'nc_var': 'NDVI', 'var': 'ndvi', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (17, 52, 92)},
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

# Constants for dimensions names to be used in the Zarr store
X_DIM = 'x'
Y_DIM = 'y'
T_DIM = 'time'

def ncs2zarr(nc_paths, zarr_path, beginning=True):
    """Convert NetCDF files to Zarr store with proper organization."""
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

        _consolidate_time_and_restore_attrs(store, var, time_attrs_original, var_attrs_original)
        print(f"Total processing time for {var}: {(time.time() - var_start_time):.2f} seconds")

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

    nc_ds = xr.open_dataset(nc_portions_path[0], chunks=None, decode_times=False)
    nc_ds = _sort_dim(nc_ds, hor_dim)
    nc_ds = _sort_dim(nc_ds, ver_dim)

    # Save original variable attributes
    var_attrs_original = dict(nc_ds[nc_var].attrs) if nc_var in nc_ds else {}

    # Remove _FillValue, missing_value, and units in variable attributes and encoding
    for attr_name in ['_FillValue', 'missing_value', 'units']:
        if attr_name in nc_ds[nc_var].attrs:
            del nc_ds[nc_var].attrs[attr_name]
        if hasattr(nc_ds[nc_var], 'encoding') and attr_name in nc_ds[nc_var].encoding:
            del nc_ds[nc_var].encoding[attr_name]

    time_coords = nc_ds[time_dim].values
    time_steps = len(time_coords)

    # Save original time attributes
    time_attrs_original = dict(nc_ds[time_dim].attrs) if time_dim in nc_ds.coords else {}

    # Configure chunking
    time_chunk_size = chunk_shape[0]
    num_chunks = math.ceil(time_steps / time_chunk_size)
    print(f"Processing in {num_chunks} temporal chunks of size {time_chunk_size}:")

    # Process each temporal chunk
    for chunk_idx in range(num_chunks):
        _process_time_chunk(nc_ds, store, chunk_idx, time_chunk_size, time_steps,
                           time_dim, ver_dim, hor_dim, nc_var, var, dims_mapping, chunk_shape)

    nc_ds.close()
    return time_attrs_original, var_attrs_original

def _process_time_chunk(nc_ds, store, chunk_idx, time_chunk_size, time_steps,
                       time_dim, ver_dim, hor_dim, nc_var, var, dims_mapping, chunk_shape):
    """Process a single time chunk and write to Zarr."""
    chunk_start = chunk_idx * time_chunk_size
    chunk_end = min((chunk_idx + 1) * time_chunk_size, time_steps) - 1
    time_slice = slice(chunk_start, chunk_end + 1)

    print(f"* Processing time chunk {chunk_idx+1}/{math.ceil(time_steps/time_chunk_size)} (indices {chunk_start}:{chunk_end})...")

    ds = nc_ds.isel({time_dim: time_slice})

    # Clean problematic time attributes
    if time_dim in ds.coords:
        ds[time_dim].attrs.pop('units', None)
        ds[time_dim].attrs.pop('calendar', None)

    # Rename variable if needed
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

def _process_append_mode(store, nc_info):
    """Process NetCDF in append mode, updating or adding time slices."""
    nc_portions_path = nc_info['path']
    nc_var = nc_info['nc_var']
    var = nc_info['var']
    time_dim = nc_info.get('time_dim', 'time')
    ver_dim = nc_info.get('ver_dim', 'lat')
    hor_dim = nc_info.get('hor_dim', 'lon')

    nc_ds = xr.open_dataset(nc_portions_path[0], chunks=None, decode_times=False)
    nc_ds = _sort_dim(nc_ds, hor_dim)
    nc_ds = _sort_dim(nc_ds, ver_dim)

    time_coords = nc_ds[time_dim].values
    time_steps = len(time_coords)

    # Get existing time coordinates
    zarr_ds = xr.open_zarr(store, group=var, decode_times=False)
    existing_times = zarr_ds[T_DIM].values
    print(f"Processing {time_steps} dates:")

    # Process each date
    for i, time_val in enumerate(time_coords):
        print(f"* Processing date: {i}: {time_val}")
        time_slice = nc_ds[nc_var].isel({time_dim: i})

        if time_val in existing_times:
            _update_existing_time(store, var, time_val, time_slice, existing_times)
        else:
            _add_new_time(store, var, time_val, time_slice, zarr_ds)

    nc_ds.close()

def _update_existing_time(store, var, time_val, time_slice, existing_times):
    """Update an existing time slice in the Zarr store."""
    print(f"  Date {time_val} already exists in Zarr, updating...")
    existing_index = list(existing_times).index(time_val)
    var_array = zarr.open_group(store)[var][var]
    var_array[existing_index, :, :] = time_slice.values

def _add_new_time(store, var, time_val, time_slice, zarr_ds):
    """Add a new time slice to the Zarr store using low-level Zarr API."""
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

    print(f"  Added new date at index {current_length}")

def _consolidate_time_and_restore_attrs(store, var, time_attrs_original=None, var_attrs_original=None):
    """
    Consolidate the time dimension of a Zarr dataset into a single chunk and restore original attributes.
    """
    # After processing all chunks
    print("Consolidating time dimension and restore original attributes...")

    # Get direct access to the Zarr array
    z_group = zarr.open_group(store=store, mode='a')
    var_group = z_group[var]

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

    # Restore original variable attributes if they exist
    if var_attrs_original and var in var_group:
        var_array = var_group[var]

        # Update with original attributes
        for key, value in var_attrs_original.items():
            var_array.attrs[key] = value
