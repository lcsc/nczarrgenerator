import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: vmed_pen desde el fichero wind_daily_grid_pen.nc"                time = 22280; lat = 144 ; lon = 144 => 'chunk_shape': (349, 16, 28)
# [X] "Procesando: vmed_can desde el fichero wind_daily_grid_can.nc"                time = 22280; lat = 56 ; lon = 56
# [X] "Procesando: vmed_beaufort_pen desde el fichero beaufort/beaufort_pen.nc"     time = 22280; lat = 144 ; lon = 144 => 'chunk_shape': (349, 16, 28)
# [X] "Procesando: vmed_beaufort_can desde el fichero beaufort/beaufort_can.nc"     time = 22280; lat = 56 ; lon = 56
# [X] "Procesando: vmed_q95_pen desde el fichero percentiles/p95_wind_pen.nc"       time = 12; lat = 144 ; lon = 144 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: vmed_q95_can desde el fichero percentiles/p95_wind_can.nc"       time = 12; lat = 56 ; lon = 56
# [X] "Procesando: vmed_q90_pen desde el fichero percentiles/p90_wind_pen.nc"       time = 12; lat = 144 ; lon = 144 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: vmed_q90_can desde el fichero percentiles/p90_wind_can.nc"
# [X] "Procesando: vmed_q97_pen desde el fichero percentiles/p97_wind_pen.nc"       time = 12; lat = 144 ; lon = 144 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: vmed_q97_can desde el fichero percentiles/p97_wind_can.nc"
# [X] "Procesando: vmed_q99_pen desde el fichero percentiles/p99_wind_pen.nc"       time = 12; lat = 144 ; lon = 144 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: vmed_q99_can desde el fichero percentiles/p99_wind_can.nc"
# [X] "Procesando: vmed_q5_pen desde el fichero percentiles/p5_wind_pen.nc"         time = 12; lat = 144 ; lon = 144 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: vmed_q5_can desde el fichero percentiles/p5_wind_can.nc"
# [X] "Procesando: vmed_q3_pen desde el fichero percentiles/p3_wind_pen.nc"         time = 12; lat = 144 ; lon = 144 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: vmed_q3_can desde el fichero percentiles/p3_wind_can.nc"
# [X] "Procesando: vmed_q1_pen desde el fichero percentiles/p1_wind_pen.nc"         time = 12; lat = 144 ; lon = 144 => 'chunk_shape': (12, 16, 28)
# [X] "Procesando: vmed_q1_can desde el fichero percentiles/p1_wind_can.nc"
# [ ] "Procesando: vmed_q10_pen desde el fichero percentiles/p10_wind_pen.nc"       time = 12; lat = 144 ; lon = 144 => 'chunk_shape': (12, 16, 28)
# [ ] "Procesando: vmed_q10_can desde el fichero percentiles/p10_wind_can.nc"

netcdfs = [
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/wind/wind_daily_grid_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/wind/wind_daily_grid_can.nc'], 'nc_var': 'ws', 'var': 'vmed', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (349, 16, 28)},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/wind/beaufort/beaufort_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/wind/beaufort/beaufort_can.nc'], 'nc_var': 'beaufort', 'var': 'vmed_beaufort', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (349, 16, 28)},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p95_wind_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p95_wind_can.nc'], 'nc_var': 'ws', 'var': 'vmed_q95', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p90_wind_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p90_wind_can.nc'], 'nc_var': 'ws', 'var': 'vmed_q90', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p97_wind_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p97_wind_can.nc'], 'nc_var': 'ws', 'var': 'vmed_q97', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p99_wind_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p99_wind_can.nc'], 'nc_var': 'ws', 'var': 'vmed_q99', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p5_wind_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p5_wind_can.nc'], 'nc_var': 'ws', 'var': 'vmed_q5', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p3_wind_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p3_wind_can.nc'], 'nc_var': 'ws', 'var': 'vmed_q3', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p1_wind_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p1_wind_can.nc'], 'nc_var': 'ws', 'var': 'vmed_q1', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p10_wind_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/wind/percentiles/p10_wind_can.nc'], 'nc_var': 'ws', 'var': 'vmed_q10', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 16, 28)},
]
zarr_path = '/home/edumoreno/git/nczarrgenerator/nc/wind.zarr'
ncs2zarr(netcdfs, zarr_path)

# 27s minutos con max/min