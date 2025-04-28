import xarray as xr
import zarr
import numpy as np
import os
import pyproj
import time

def main():
    # Input and output file paths
    input_file = "nc/sedi/SEDI.nc"
    output_file = "nc/sedi/SEDI_8-11.nc"
    
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    print(f"Reading data from {input_file}...")
    
    # Open the original dataset
    #try:
    ds = xr.open_dataset(input_file, decode_times=False)
    
    # Create subset
    print("Creating subset...")
    subset = ds.isel(time=slice(8, 12))
    
    # Get variable name
    var_name = "SEDI"
    
    # Mapeo de índices originales a nuevos valores
    value_map = {
        8: 0.0, 
        9: 0.1, 
        10: 0.2, 
        11: 0.3
    }
    
    # Crear una copia del subset para modificar
    modified_subset = subset.copy(deep=True)
    
    # Sustituir valores para cada tiempo mientras se mantiene NaN donde ya había NaN
    print("Sustituyendo valores...")
    for i, original_idx in enumerate(range(8, 12)):
        # Extraer la rebanada temporal
        time_slice = modified_subset.isel(time=i)
        
        # Crear una máscara para identificar valores no-NaN
        mask = ~np.isnan(time_slice[var_name])
        
        # Aplicar el valor constante donde la máscara es True (no-NaN)
        new_value = value_map[original_idx]
        modified_subset[var_name][i] = xr.where(mask, new_value, time_slice[var_name])
        
        print(f"  * Índice original {original_idx}: valores no-NaN reemplazados por {new_value}")
    
    # Save the result to a new NetCDF file
    print(f"Guardando dataset modificado en {output_file}...")
    
    # Asegurar que se conserven todos los metadatos
    modified_subset.attrs = ds.attrs  # Atributos globales
    
    # Garantizar que los atributos de la variable se mantengan
    for var in modified_subset.data_vars:
        modified_subset[var].attrs = subset[var].attrs
    
    # Garantizar que los atributos de las dimensiones se mantengan
    for dim in modified_subset.dims:
        if dim in modified_subset.coords:
            modified_subset[dim].attrs = subset[dim].attrs
    
    modified_subset.to_netcdf(output_file)
    
    print("¡Completado!")
    
    # except FileNotFoundError:
    #     print(f"Error: Archivo {input_file} no encontrado.")
    # except Exception as e:
    #     print(f"Error: {str(e)}")
    # finally:
    #     # Close the datasets if they've been opened
    #     if 'ds' in locals():
    #         ds.close()
    #     if 'subset' in locals():
    #         subset.close()
    #     if 'modified_subset' in locals():
    #         modified_subset.close()

if __name__ == "__main__":
    main()