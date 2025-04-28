import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: 1d/ssrd_1_pen desde el fichero 1d/ssrd_ERA5-Land_pen.nc"                 time = 22280; lat = 101 ; lon = 161 => 'chunk_shape': (349, 16, 28)
# [X] "Procesando: 1d/ssrd_1_can desde el fichero 1d/ssrd_ERA5-Land_can.nc"                 time = 22280; lat = 24 ; lon = 56
# [X] "Procesando: 1d/ssrd_1_p95_pen desde el fichero 1d/p95_ssrd_pen.nc"                   time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 1d/ssrd_1_p95_can desde el fichero 1d/p95_ssrd_can.nc"                   time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 1d/ssrd_1_p90_pen desde el fichero 1d/p90_ssrd_pen.nc"                   time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 1d/ssrd_1_p90_can desde el fichero 1d/p90_ssrd_can.nc"                   time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 1d/ssrd_1_p97_pen desde el fichero 1d/p97_ssrd_pen.nc"                   time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 1d/ssrd_1_p97_can desde el fichero 1d/p97_ssrd_can.nc"                   time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 1d/ssrd_1_p99_pen desde el fichero 1d/p99_ssrd_pen.nc"                   time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 1d/ssrd_1_p99_can desde el fichero 1d/p99_ssrd_can.nc"                   time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 1d/ssrd_1_p5_pen desde el fichero 1d/p5_ssrd_pen.nc"                     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 1d/ssrd_1_p5_can desde el fichero 1d/p5_ssrd_can.nc"                     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 1d/ssrd_1_p3_pen desde el fichero 1d/p3_ssrd_pen.nc"                     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 1d/ssrd_1_p3_can desde el fichero 1d/p3_ssrd_can.nc"                     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 1d/ssrd_1_p1_pen desde el fichero 1d/p1_ssrd_pen.nc"                     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 1d/ssrd_1_p1_can desde el fichero 1d/p1_ssrd_can.nc"                     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 1d/ssrd_1_p10_pen desde el fichero 1d/p10_ssrd_pen.nc"                   time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 1d/ssrd_1_p10_can desde el fichero 1d/p10_ssrd_can.nc"                   time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 3d/ssrd_3_pen desde el fichero 3d/3d_cumulative_pen.nc"                  time = 22280; lat = 101 ; lon = 161 => 'chunk_shape': (349, 16, 28)
# [X] "Procesando: 3d/ssrd_3_can desde el fichero 3d/3d_cumulative_can.nc"                  time = 22280; lat = 24 ; lon = 56
# [X] "Procesando: 3d/ssrd_3_p95_pen desde el fichero 3d/3d_cumulative_p95_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 3d/ssrd_3_p95_can desde el fichero 3d/3d_cumulative_p95_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 3d/ssrd_3_p90_pen desde el fichero 3d/3d_cumulative_p90_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 3d/ssrd_3_p90_can desde el fichero 3d/3d_cumulative_p90_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 3d/ssrd_3_p97_pen desde el fichero 3d/3d_cumulative_p97_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 3d/ssrd_3_p97_can desde el fichero 3d/3d_cumulative_p97_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 3d/ssrd_3_p99_pen desde el fichero 3d/3d_cumulative_p99_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 3d/ssrd_3_p99_can desde el fichero 3d/3d_cumulative_p99_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 3d/ssrd_3_p5_pen desde el fichero 3d/3d_cumulative_p5_ssrd_pen.nc"       time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 3d/ssrd_3_p5_can desde el fichero 3d/3d_cumulative_p5_ssrd_can.nc"       time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 3d/ssrd_3_p3_pen desde el fichero 3d/3d_cumulative_p3_ssrd_pen.nc"       time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 3d/ssrd_3_p3_can desde el fichero 3d/3d_cumulative_p3_ssrd_can.nc"       time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 3d/ssrd_3_p1_pen desde el fichero 3d/3d_cumulative_p1_ssrd_pen.nc"       time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 3d/ssrd_3_p1_can desde el fichero 3d/3d_cumulative_p1_ssrd_can.nc"       time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 3d/ssrd_3_p10_pen desde el fichero 3d/3d_cumulative_p10_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 3d/ssrd_3_p10_can desde el fichero 3d/3d_cumulative_p10_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 5d/ssrd_5_pen desde el fichero 5d/5d_cumulative_pen.nc"                  time = 22280; lat = 101 ; lon = 161 => 'chunk_shape': (349, 16, 28)
# [X] "Procesando: 5d/ssrd_5_can desde el fichero 5d/5d_cumulative_can.nc"                  time = 22280; lat = 24 ; lon = 56
# [X] "Procesando: 5d/ssrd_5_p95_pen desde el fichero 5d/5d_cumulative_p95_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 5d/ssrd_5_p95_can desde el fichero 5d/5d_cumulative_p95_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 5d/ssrd_5_p90_pen desde el fichero 5d/5d_cumulative_p90_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 5d/ssrd_5_p90_can desde el fichero 5d/5d_cumulative_p90_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 5d/ssrd_5_p97_pen desde el fichero 5d/5d_cumulative_p97_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 5d/ssrd_5_p97_can desde el fichero 5d/5d_cumulative_p97_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 5d/ssrd_5_p99_pen desde el fichero 5d/5d_cumulative_p99_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 5d/ssrd_5_p99_can desde el fichero 5d/5d_cumulative_p99_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 5d/ssrd_5_p5_pen desde el fichero 5d/5d_cumulative_p5_ssrd_pen.nc"       time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 5d/ssrd_5_p5_can desde el fichero 5d/5d_cumulative_p5_ssrd_can.nc"       time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 5d/ssrd_5_p3_pen desde el fichero 5d/5d_cumulative_p3_ssrd_pen.nc"       time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 5d/ssrd_5_p3_can desde el fichero 5d/5d_cumulative_p3_ssrd_can.nc"       time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 5d/ssrd_5_p1_pen desde el fichero 5d/5d_cumulative_p1_ssrd_pen.nc"       time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 5d/ssrd_5_p1_can desde el fichero 5d/5d_cumulative_p1_ssrd_can.nc"       time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 5d/ssrd_5_p10_pen desde el fichero 5d/5d_cumulative_p10_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 5d/ssrd_5_p10_can desde el fichero 5d/5d_cumulative_p10_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 7d/ssrd_7_pen desde el fichero 7d/7d_cumulative_pen.nc"                  time = 22280; lat = 101 ; lon = 161 => 'chunk_shape': (349, 16, 28)
# [X] "Procesando: 7d/ssrd_7_can desde el fichero 7d/7d_cumulative_can.nc"                  time = 22280; lat = 24 ; lon = 56
# [X] "Procesando: 7d/ssrd_7_p95_pen desde el fichero 7d/7d_cumulative_p95_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 7d/ssrd_7_p95_can desde el fichero 7d/7d_cumulative_p95_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 7d/ssrd_7_p90_pen desde el fichero 7d/7d_cumulative_p90_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 7d/ssrd_7_p90_can desde el fichero 7d/7d_cumulative_p90_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 7d/ssrd_7_p97_pen desde el fichero 7d/7d_cumulative_p97_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 7d/ssrd_7_p97_can desde el fichero 7d/7d_cumulative_p97_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 7d/ssrd_7_p99_pen desde el fichero 7d/7d_cumulative_p99_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 7d/ssrd_7_p99_can desde el fichero 7d/7d_cumulative_p99_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 7d/ssrd_7_p5_pen desde el fichero 7d/7d_cumulative_p5_ssrd_pen.nc"       time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 7d/ssrd_7_p5_can desde el fichero 7d/7d_cumulative_p5_ssrd_can.nc"       time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 7d/ssrd_7_p3_pen desde el fichero 7d/7d_cumulative_p3_ssrd_pen.nc"       time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 7d/ssrd_7_p3_can desde el fichero 7d/7d_cumulative_p3_ssrd_can.nc"       time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 7d/ssrd_7_p1_pen desde el fichero 7d/7d_cumulative_p1_ssrd_pen.nc"       time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 7d/ssrd_7_p1_can desde el fichero 7d/7d_cumulative_p1_ssrd_can.nc"       time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 7d/ssrd_7_p10_pen desde el fichero 7d/7d_cumulative_p10_ssrd_pen.nc"     time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 7d/ssrd_7_p10_can desde el fichero 7d/7d_cumulative_p10_ssrd_can.nc"     time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 10d/ssrd_10_pen desde el fichero 10d/10d_cumulative_pen.nc"              time = 22280; lat = 101 ; lon = 161 => 'chunk_shape': (349, 16, 28)
# [X] "Procesando: 10d/ssrd_10_can desde el fichero 10d/10d_cumulative_can.nc"              time = 22280; lat = 24 ; lon = 56
# [X] "Procesando: 10d/ssrd_10_p95_pen desde el fichero 10d/10d_cumulative_p95_ssrd_pen.nc" time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 10d/ssrd_10_p95_can desde el fichero 10d/10d_cumulative_p95_ssrd_can.nc" time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 10d/ssrd_10_p90_pen desde el fichero 10d/10d_cumulative_p90_ssrd_pen.nc" time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 10d/ssrd_10_p90_can desde el fichero 10d/10d_cumulative_p90_ssrd_can.nc" time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 10d/ssrd_10_p97_pen desde el fichero 10d/10d_cumulative_p97_ssrd_pen.nc" time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 10d/ssrd_10_p97_can desde el fichero 10d/10d_cumulative_p97_ssrd_can.nc" time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 10d/ssrd_10_p99_pen desde el fichero 10d/10d_cumulative_p99_ssrd_pen.nc" time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 10d/ssrd_10_p99_can desde el fichero 10d/10d_cumulative_p99_ssrd_can.nc" time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 10d/ssrd_10_p5_pen desde el fichero 10d/10d_cumulative_p5_ssrd_pen.nc"   time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 10d/ssrd_10_p5_can desde el fichero 10d/10d_cumulative_p5_ssrd_can.nc"   time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 10d/ssrd_10_p3_pen desde el fichero 10d/10d_cumulative_p3_ssrd_pen.nc"   time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 10d/ssrd_10_p3_can desde el fichero 10d/10d_cumulative_p3_ssrd_can.nc"   time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 10d/ssrd_10_p1_pen desde el fichero 10d/10d_cumulative_p1_ssrd_pen.nc"   time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 10d/ssrd_10_p1_can desde el fichero 10d/10d_cumulative_p1_ssrd_can.nc"   time = 12; lat = 24 ; lon = 56
# [X] "Procesando: 10d/ssrd_10_p10_pen desde el fichero 10d/10d_cumulative_p10_ssrd_pen.nc" time = 12; lat = 101 ; lon = 161 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: 10d/ssrd_10_p10_can desde el fichero 10d/10d_cumulative_p10_ssrd_can.nc" time = 12; lat = 24 ; lon = 56

netcdfs = [
    {'path': ['nc/sri/1d/ssrd_ERA5-Land_pen.nc', 'nc/sri/1d/ssrd_ERA5-Land_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_1', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (349, 16, 28)},
    {'path': ['nc/sri/1d/p95_ssrd_pen.nc', 'nc/sri/1d/p95_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_1_p95', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/1d/p90_ssrd_pen.nc', 'nc/sri/1d/p90_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_1_p90', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/1d/p97_ssrd_pen.nc', 'nc/sri/1d/p97_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_1_p97', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/1d/p99_ssrd_pen.nc', 'nc/sri/1d/p99_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_1_p99', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/1d/p5_ssrd_pen.nc', 'nc/sri/1d/p5_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_1_p5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/1d/p3_ssrd_pen.nc', 'nc/sri/1d/p3_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_1_p3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/1d/p1_ssrd_pen.nc', 'nc/sri/1d/p1_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_1_p1', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/1d/p10_ssrd_pen.nc', 'nc/sri/1d/p10_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_1_p10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/3d/3d_cumulative_pen.nc', 'nc/sri/3d/3d_cumulative_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (349, 16, 28)},
    {'path': ['nc/sri/3d/3d_cumulative_p95_ssrd_pen.nc', 'nc/sri/3d/3d_cumulative_p95_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_3_p95', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/3d/3d_cumulative_p90_ssrd_pen.nc', 'nc/sri/3d/3d_cumulative_p90_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_3_p90', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/3d/3d_cumulative_p97_ssrd_pen.nc', 'nc/sri/3d/3d_cumulative_p97_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_3_p97', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/3d/3d_cumulative_p99_ssrd_pen.nc', 'nc/sri/3d/3d_cumulative_p99_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_3_p99', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/3d/3d_cumulative_p5_ssrd_pen.nc', 'nc/sri/3d/3d_cumulative_p5_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_3_p5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/3d/3d_cumulative_p3_ssrd_pen.nc', 'nc/sri/3d/3d_cumulative_p3_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_3_p3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/3d/3d_cumulative_p1_ssrd_pen.nc', 'nc/sri/3d/3d_cumulative_p1_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_3_p1', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/3d/3d_cumulative_p10_ssrd_pen.nc', 'nc/sri/3d/3d_cumulative_p10_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_3_p10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/5d/5d_cumulative_pen.nc', 'nc/sri/5d/5d_cumulative_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (349, 16, 28)},
    {'path': ['nc/sri/5d/5d_cumulative_p95_ssrd_pen.nc', 'nc/sri/5d/5d_cumulative_p95_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_5_p95', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/5d/5d_cumulative_p90_ssrd_pen.nc', 'nc/sri/5d/5d_cumulative_p90_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_5_p90', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/5d/5d_cumulative_p97_ssrd_pen.nc', 'nc/sri/5d/5d_cumulative_p97_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_5_p97', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/5d/5d_cumulative_p99_ssrd_pen.nc', 'nc/sri/5d/5d_cumulative_p99_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_5_p99', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/5d/5d_cumulative_p5_ssrd_pen.nc', 'nc/sri/5d/5d_cumulative_p5_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_5_p5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/5d/5d_cumulative_p3_ssrd_pen.nc', 'nc/sri/5d/5d_cumulative_p3_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_5_p3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/5d/5d_cumulative_p1_ssrd_pen.nc', 'nc/sri/5d/5d_cumulative_p1_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_5_p1', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/5d/5d_cumulative_p10_ssrd_pen.nc', 'nc/sri/5d/5d_cumulative_p10_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_5_p10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/7d/7d_cumulative_pen.nc', 'nc/sri/7d/7d_cumulative_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_7', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (349, 16, 28)},
    {'path': ['nc/sri/7d/7d_cumulative_p95_ssrd_pen.nc', 'nc/sri/7d/7d_cumulative_p95_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_7_p95', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/7d/7d_cumulative_p90_ssrd_pen.nc', 'nc/sri/7d/7d_cumulative_p90_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_7_p90', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/7d/7d_cumulative_p97_ssrd_pen.nc', 'nc/sri/7d/7d_cumulative_p97_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_7_p97', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/7d/7d_cumulative_p99_ssrd_pen.nc', 'nc/sri/7d/7d_cumulative_p99_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_7_p99', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/7d/7d_cumulative_p5_ssrd_pen.nc', 'nc/sri/7d/7d_cumulative_p5_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_7_p5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/7d/7d_cumulative_p3_ssrd_pen.nc', 'nc/sri/7d/7d_cumulative_p3_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_7_p3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/7d/7d_cumulative_p1_ssrd_pen.nc', 'nc/sri/7d/7d_cumulative_p1_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_7_p1', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/7d/7d_cumulative_p10_ssrd_pen.nc', 'nc/sri/7d/7d_cumulative_p10_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_7_p10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/10d/10d_cumulative_pen.nc', 'nc/sri/10d/10d_cumulative_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (349, 16, 28)},
    {'path': ['nc/sri/10d/10d_cumulative_p95_ssrd_pen.nc', 'nc/sri/10d/10d_cumulative_p95_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_10_p95', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/10d/10d_cumulative_p90_ssrd_pen.nc', 'nc/sri/10d/10d_cumulative_p90_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_10_p90', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/10d/10d_cumulative_p97_ssrd_pen.nc', 'nc/sri/10d/10d_cumulative_p97_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_10_p97', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/10d/10d_cumulative_p99_ssrd_pen.nc', 'nc/sri/10d/10d_cumulative_p99_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_10_p99', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/10d/10d_cumulative_p5_ssrd_pen.nc', 'nc/sri/10d/10d_cumulative_p5_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_10_p5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/10d/10d_cumulative_p3_ssrd_pen.nc', 'nc/sri/10d/10d_cumulative_p3_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_10_p3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/10d/10d_cumulative_p1_ssrd_pen.nc', 'nc/sri/10d/10d_cumulative_p1_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_10_p1', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['nc/sri/10d/10d_cumulative_p10_ssrd_pen.nc', 'nc/sri/10d/10d_cumulative_p10_ssrd_can.nc'], 'nc_var': 'ssrd', 'var': 'ssrd_10_p10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
]
zarr_path = 'nc/sri.zarr'
ncs2zarr(netcdfs, zarr_path, beginning=True)

# 7m6s con max/min; nczarrgenerator_all
# 2m24s con max/min; nczarrgenerator