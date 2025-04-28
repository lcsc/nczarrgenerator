import xarray as xr
import zarr
import numpy as np
import os
import pyproj
import time

def main(input_file, output_file):
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    print(f"Reading data from {input_file}...")
    
    # Open the original dataset
    try:
        ds = xr.open_dataset(input_file, decode_times=False)
        
        # Create subset with all x and y values but only the first 10 time values
        print("Creating subset with the first 10 time values...")
        subset = ds.isel(time=slice(0, 10))
        
        # Save the result to a new NetCDF file
        print(f"Saving subset to {output_file}...")
        subset.to_netcdf(output_file)
        
        print("Done!")
    
    except FileNotFoundError:
        print(f"Error: File {input_file} not found.")
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Close the datasets if they've been opened
        if 'ds' in locals():
            ds.close()
        if 'subset' in locals():
            subset.close()

if __name__ == "__main__":
    main(input_file = "nc/amm/primera_helada/ff_can.nc", output_file = "nc/amm/primera_helada/ff_0-9_can.nc")
    main(input_file = "nc/amm/primera_helada/ff_pen.nc", output_file = "nc/amm/primera_helada/ff_0-9_pen.nc")