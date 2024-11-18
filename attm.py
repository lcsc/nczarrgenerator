import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: mag_m0.3_pen desde el fichero mag_m0.3_pen.nc"               time = 7; lat = 341 ; lon = 545 => 'chunk_shape': (7, 81, 113)
# [X] "Procesando: mag_m0.3_can desde el fichero mag_m0.3_can.nc"               time = 7; lat = 71 ; lon = 189
# [X] "Procesando: deltamag_m0.3_pen desde el fichero deltamag_m0.3_pen.nc"     time = 7; lat = 341 ; lon = 545 => 'chunk_shape': (7, 81, 113)
# [X] "Procesando: deltamag_m0.3_can desde el fichero deltamag_m0.3_can.nc"     time = 7; lat = 71 ; lon = 189
# [X] "Procesando: mag_p0.9_pen desde el fichero mag_p0.9_pen.nc"               time = 7; lat = 341 ; lon = 545 => 'chunk_shape': (7, 81, 113)
# [X] "Procesando: mag_p0.9_can desde el fichero mag_p0.9_can.nc"               time = 7; lat = 71 ; lon = 189
# [X] "Procesando: deltamag_p0.9_pen desde el fichero deltamag_p0.9_pen.nc"     time = 7; lat = 341 ; lon = 545 => 'chunk_shape': (7, 81, 113)
# [X] "Procesando: deltamag_p0.9_can desde el fichero deltamag_p0.9_can.nc"     time = 7; lat = 71 ; lon = 189
# [X] "Procesando: mag_p1.5_pen desde el fichero mag_p1.5_pen.nc"               time = 7; lat = 341 ; lon = 545 => 'chunk_shape': (7, 81, 113)
# [X] "Procesando: mag_p1.5_can desde el fichero mag_p1.5_can.nc"               time = 7; lat = 71 ; lon = 189
# [X] "Procesando: deltamag_p1.5_pen desde el fichero deltamag_p1.5_pen.nc"     time = 7; lat = 341 ; lon = 545 => 'chunk_shape': (7, 81, 113)
# [X] "Procesando: deltamag_p1.5_can desde el fichero deltamag_p1.5_can.nc"     time = 7; lat = 71 ; lon = 189
# [X] "Procesando: mag_p2.0_pen desde el fichero mag_p2.0_pen.nc"               time = 7; lat = 341 ; lon = 545 => 'chunk_shape': (7, 81, 113)
# [X] "Procesando: mag_p2.0_can desde el fichero mag_p2.0_can.nc"               time = 7; lat = 71 ; lon = 189
# [X] "Procesando: deltamag_p2.0_pen desde el fichero deltamag_p2.0_pen.nc"     time = 7; lat = 341 ; lon = 545 => 'chunk_shape': (7, 81, 113)
# [X] "Procesando: deltamag_p2.0_can desde el fichero deltamag_p2.0_can.nc"     time = 7; lat = 71 ; lon = 189

netcdfs = [
    {'path': ['nc/attm/mag_m0.3_pen.nc', 'nc/attm/mag_m0.3_can.nc'], 'nc_var': 'mag', 'var': 'mag_m0.3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': False, 'include_center_calc': True, 'chunk_shape': (7, 81, 113)},
    {'path': ['nc/attm/deltamag_m0.3_pen.nc', 'nc/attm/deltamag_m0.3_can.nc'], 'nc_var': 'deltamag', 'var': 'deltamag_m0.3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': False, 'include_center_calc': False, 'chunk_shape': (7, 81, 113)},
    {'path': ['nc/attm/mag_p0.9_pen.nc', 'nc/attm/mag_p0.9_can.nc'], 'nc_var': 'mag', 'var': 'mag_p0.9', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': False, 'include_center_calc': False, 'chunk_shape': (7, 81, 113)},
    {'path': ['nc/attm/deltamag_p0.9_pen.nc', 'nc/attm/deltamag_p0.9_can.nc'], 'nc_var': 'deltamag', 'var': 'deltamag_p0.9', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': False, 'include_center_calc': False, 'chunk_shape': (7, 81, 113)},
    {'path': ['nc/attm/mag_p1.5_pen.nc', 'nc/attm/mag_p1.5_can.nc'], 'nc_var': 'mag', 'var': 'mag_p1.5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': False, 'include_center_calc': False, 'chunk_shape': (7, 81, 113)},
    {'path': ['nc/attm/deltamag_p1.5_pen.nc', 'nc/attm/deltamag_p1.5_can.nc'], 'nc_var': 'deltamag', 'var': 'deltamag_p1.5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': False, 'include_center_calc': False, 'chunk_shape': (7, 81, 113)},
    {'path': ['nc/attm/mag_p2.0_pen.nc', 'nc/attm/mag_p2.0_can.nc'], 'nc_var': 'mag', 'var': 'mag_p2.0', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': False, 'include_center_calc': False, 'chunk_shape': (7, 81, 113)},
    {'path': ['nc/attm/deltamag_p2.0_pen.nc', 'nc/attm/deltamag_p2.0_can.nc'], 'nc_var': 'deltamag', 'var': 'deltamag_p2.0', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': False, 'include_center_calc': False, 'chunk_shape': (7, 81, 113)},
]
zarr_path = 'nc/attm.zarr'
ncs2zarr(netcdfs, zarr_path)

# 1s sin max/min (ya que si se activan los máximos y mínimos aparece un error por ser la unidad de time 'years since...')