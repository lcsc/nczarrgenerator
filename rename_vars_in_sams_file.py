import xarray as xr
import zarr
import numpy as np
import os
import pyproj
import time
import argparse

def rename_vars_in_netcdf(input_file, var_map, dim_map=None, output_file=None):
    """
    Rename the main variable and spatial dimensions in a netCDF file.
    
    Parameters:
    -----------
    input_file : str
        Path to the input netCDF file
    var_map : dict
        Dictionary mapping current variable names to new variable names
    dim_map : dict, optional
        Dictionary mapping current dimension names to new dimension names
    output_file : str, optional
        Path to save the output file. If None, will modify the original filename
    
    Returns:
    --------
    str
        Path to the output file
    """
    # Set default dimension mapping if not provided
    if dim_map is None:
        dim_map = {}
    
    # Set default output filename if not provided
    if output_file is None:
        base, ext = os.path.splitext(input_file)
        output_file = f"{base}_renamed{ext}"
    
    print(f"Loading {input_file}...")
    start_time = time.time()
    
    # Open the netCDF file
    ds = xr.open_dataset(input_file)
    
    print(f"File loaded in {time.time() - start_time:.2f} seconds")
    print(f"Original dimensions: {list(ds.dims)}")
    print(f"Original variables: {list(ds.data_vars)}")
    
    # Rename variables
    ds = ds.rename(var_map)
    print(f"Variables renamed: {var_map}")
    
    # Rename dimensions
    if dim_map:
        ds = ds.rename(dim_map)
        print(f"Dimensions renamed: {dim_map}")
    
    # Save the modified dataset
    print(f"Saving to {output_file}...")
    start_time = time.time()
    ds.to_netcdf(output_file)
    print(f"File saved in {time.time() - start_time:.2f} seconds")
    
    return output_file

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Rename variables and dimensions in a netCDF file")
    parser.add_argument("input_file", help="Path to the input netCDF file")
    parser.add_argument("-v", "--vars", nargs=2, action="append", metavar=("OLD", "NEW"),
                      help="Variable to rename in format: old_name new_name. Can be used multiple times.")
    parser.add_argument("-d", "--dims", nargs=2, action="append", metavar=("OLD", "NEW"),
                      help="Dimension to rename in format: old_name new_name. Can be used multiple times.")
    parser.add_argument("-o", "--output", help="Path for output file")
    
    args = parser.parse_args()
    
    var_map = dict(args.vars) if args.vars else {}
    dim_map = dict(args.dims) if args.dims else {}
    
    rename_vars_in_netcdf(args.input_file, var_map, dim_map, args.output)