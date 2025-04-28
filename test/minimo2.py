import numpy as np
from scipy.interpolate import interp2d

# Valores de las filas y columnas
filas = np.array([4, 8, 16, 32, 64])
columnas = np.array([4, 8, 16, 32, 64])

# Datos de la tabla A
A = np.array([
    [6839, 7957, 8951, 12020, 17788],
    [3590, 3970, 4834, 6473, 12399],
    [1750, 2293, 2450, 4025, 11010],
    [980, 1106, 1374, 3353, 10977],
    [495, 560, 878, 3022, 10095]
])

# Datos de la tabla B
B = np.array([
    [2330, 551, 202, 76, 31],
    [2230, 733, 218, 73, 52],
    [2466, 652, 202, 95, 80],
    [2296, 669, 233, 153, 146],
    [2140, 715, 363, 260, 212]
])

# Crear funciones de interpolación para A y B
interp_A = interp2d(columnas, filas, A, kind='cubic')
interp_B = interp2d(columnas, filas, B, kind='cubic')

# Crear una malla de valores entre 4 y 64 para filas y columnas
nuevas_columnas = np.linspace(4, 64, 601)
nuevas_filas = np.linspace(4, 64, 601)

# Interpolar los datos de A y B
A_interp = interp_A(nuevas_columnas, nuevas_filas)
B_interp = interp_B(nuevas_columnas, nuevas_filas)

# Sumar las tablas interpoladas
Suma = A_interp + B_interp

# Encontrar el valor mínimo y su posición
valor_minimo = np.min(Suma)
indice_minimo = np.unravel_index(np.argmin(Suma), Suma.shape)
columna_minima = nuevas_columnas[indice_minimo[1]]
fila_minima = nuevas_filas[indice_minimo[0]]

print(f"El valor mínimo es {valor_minimo} y se encuentra en columna = {columna_minima}, fila = {fila_minima}")