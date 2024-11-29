import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: aiv_1990 desde el fichero aiv_1990.nc"                                       time = 1; lat = 721 ; lon = 1440 => 'chunk_shape': (1, 91, 180)
# [X] "Procesando: aiv_2020 desde el fichero aiv_2020.nc"                                       time = 1; lat = 721 ; lon = 1440 => 'chunk_shape': (1, 91, 180)
# [X] "Procesando: sim_ssp1_2100 desde el fichero sim_ssp1_2100.nc"                             times = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp5_2100 desde el fichero sim_ssp5_2100.nc"                             times = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp1_2100_uncertainty desde el fichero sim_ssp1_2100_uncertainty.nc"     time = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp5_2100_uncertainty desde el fichero sim_ssp5_2100_uncertainty.nc"     time = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: aiv_1990_classes desde el fichero aiv_1990_classes.nc"                       time = 1; lat = 721 ; lon = 1440 => 'chunk_shape': (1, 91, 180)
# [X] "Procesando: aiv_2020_classes desde el fichero aiv_2020_classes.nc"                       time = 1; lat = 721 ; lon = 1440 => 'chunk_shape': (1, 91, 180)
# [X] "Procesando: sim_ssp1_2100_classes desde el fichero sim_ssp1_2100_classes.nc"             times = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp5_2100_classes desde el fichero sim_ssp5_2100_classes.nc"             times = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp1_2100_classes_uncertainty desde el fichero sim_ssp1_2100_classes_uncertainty.nc"     time = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp5_2100_classes_uncertainty desde el fichero sim_ssp5_2100_classes_uncertainty.nc"     time = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: aridity desde el fichero aridity.nc"                                         time = 41; lat = 361 ; lon = 720 => 'chunk_shape': (10, 46, 90)
# [X] "Procesando: aridity_classes desde el fichero aridity_classes.nc"                         time = 41; lat = 361 ; lon = 720 => 'chunk_shape': (10, 46, 90)

netcdfs = [
    {'path': ['nc/gams/aiv_1990.nc'], 'nc_var': 'AIv', 'var': 'aiv_1990', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (1, 91, 180)},
    {'path': ['nc/gams/aiv_2020.nc'], 'nc_var': 'AIv', 'var': 'aiv_2020', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 91, 180)},
    {'path': ['nc/gams/sim_ssp1_2100.nc'], 'nc_var': 'AIv', 'var': 'sim_ssp1_2100', 'time_dim': 'times', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp5_2100.nc'], 'nc_var': 'AIv', 'var': 'sim_ssp5_2100', 'time_dim': 'times', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp1_2100_uncertainty.nc'], 'nc_var': 'unc', 'var': 'sim_ssp1_2100_uncertainty', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp5_2100_uncertainty.nc'], 'nc_var': 'unc', 'var': 'sim_ssp5_2100_uncertainty', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/aiv_1990_classes.nc'], 'nc_var': 'AIc', 'var': 'aiv_1990_classes', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 91, 180)},
    {'path': ['nc/gams/aiv_2020_classes.nc'], 'nc_var': 'AIc', 'var': 'aiv_2020_classes', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 91, 180)},
    {'path': ['nc/gams/sim_ssp1_2100_classes.nc'], 'nc_var': 'AIc', 'var': 'sim_ssp1_2100_classes', 'time_dim': 'times', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp5_2100_classes.nc'], 'nc_var': 'AIc', 'var': 'sim_ssp5_2100_classes', 'time_dim': 'times', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp1_2100_classes_uncertainty.nc'], 'nc_var': 'unc', 'var': 'sim_ssp1_2100_classes_uncertainty', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp5_2100_classes_uncertainty.nc'], 'nc_var': 'unc', 'var': 'sim_ssp5_2100_classes_uncertainty', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/aridity.nc'], 'nc_var': 'aridity', 'var': 'aridity', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (10, 46, 90)},
    {'path': ['nc/gams/aridity_classes.nc'], 'nc_var': 'aridity', 'var': 'aridity_classes', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (10, 46, 90)},
]
zarr_path = 'nc/gams.zarr'
ncs2zarr(netcdfs, zarr_path)

# 2s minutos con max/min