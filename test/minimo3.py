import numpy as np
from scipy.interpolate import RegularGridInterpolator

# Valores originales de filas y columnas
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
interp_A = RegularGridInterpolator((filas, columnas), A)
interp_B = RegularGridInterpolator((filas, columnas), B)

# Generar nuevos valores entre 4 y 64 para filas y columnas
nuevas_filas = np.linspace(4, 64, 601)
nuevas_columnas = np.linspace(4, 64, 601)

# Crear una malla de puntos
X, Y = np.meshgrid(nuevas_filas, nuevas_columnas, indexing='ij')
puntos = np.vstack((X.ravel(), Y.ravel())).T

# Interpolar las tablas A y B en los nuevos puntos
A_interp = interp_A(puntos).reshape(601, 601)
B_interp = interp_B(puntos).reshape(601, 601)

# Sumar las tablas interpoladas
Suma = A_interp + B_interp

# Encontrar el valor mínimo y su posición
indice_minimo = np.unravel_index(np.argmin(Suma), Suma.shape)
fila_minima = nuevas_filas[indice_minimo[0]]
columna_minima = nuevas_columnas[indice_minimo[1]]
valor_minimo = Suma[indice_minimo]

print(f"El valor mínimo es {valor_minimo:.2f} y se encuentra en fila = {fila_minima:.2f}, columna = {columna_minima:.2f}")