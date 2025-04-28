import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp2d

# Tablas originales
time_lat_lon_data_pos = np.array([
    [6839, 7957, 8951, 12020, 17788],  # time = 4
    [3590, 3970, 4834, 6473, 12399],   # time = 8
    [1750, 2293, 2450, 4025, 11010],   # time = 16
    [980, 1106, 1374, 3353, 10977],    # time = 32
    [495, 560, 878, 3022, 10095]       # time = 64
])

time_lat_lon_data_time = np.array([
    [2330, 551, 202, 76, 31],  # time = 4
    [2230, 733, 218, 73, 52],  # time = 8
    [2466, 652, 202, 95, 80],  # time = 16
    [2296, 669, 233, 153, 146],# time = 32
    [2140, 715, 363, 260, 212] # time = 64
])

# Chunk sizes
chunk_time = np.array([4, 8, 16, 32, 64])
chunk_lat_lon = np.array([4, 8, 16, 32, 64])

# Interpolación de las tablas
interp_pos = interp2d(chunk_lat_lon, chunk_time, time_lat_lon_data_pos, kind='linear')
interp_time = interp2d(chunk_lat_lon, chunk_time, time_lat_lon_data_time, kind='linear')

# Crear un grid de mayor densidad
fine_grid = np.linspace(4, 64, 61)  # más valores entre 4 y 64
print(fine_grid)

# Interpolamos los datos para ese grid fino
fine_time_lat_lon_data_pos = interp_pos(fine_grid, fine_grid)
fine_time_lat_lon_data_time = interp_time(fine_grid, fine_grid)

# Suma de los tiempos de ambas tablas
combined_times = fine_time_lat_lon_data_pos + fine_time_lat_lon_data_time

# Encontrar el mínimo y su posición
min_val = np.min(combined_times)
min_pos = np.unravel_index(np.argmin(combined_times), combined_times.shape)

# Convertir el índice del grid a los valores de chunk
optimal_time_chunk = fine_grid[min_pos[0]]
optimal_lat_lon_chunk = fine_grid[min_pos[1]]

print(optimal_time_chunk, optimal_lat_lon_chunk, min_val)
