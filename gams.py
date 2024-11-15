import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: aiv_1990_all desde el fichero aiv_1990_all.nc"                                       time = 1; lat = 721 ; lon = 1440 => 'chunk_shape': (1, 91, 180)
# [X] "Procesando: aiv_1990_categorised_all desde el fichero aiv_1990_categorised_all.nc"               time = 1; lat = 721 ; lon = 1440 => 'chunk_shape': (1, 91, 180)
# [X] "Procesando: aiv_2020_all desde el fichero aiv_2020_all.nc"                                       time = 1; lat = 721 ; lon = 1440 => 'chunk_shape': (1, 91, 180)
# [X] "Procesando: aiv_2020_categorised_all desde el fichero aiv_2020_categorised_all.nc"               time = 1; lat = 721 ; lon = 1440 => 'chunk_shape': (1, 91, 180)
# [X] "Procesando: aridity_all desde el fichero aridity_all.nc"                                         time = 41; lat = 361 ; lon = 720 => 'chunk_shape': (10, 46, 90)
# [X] "Procesando: aridity_classes_all desde el fichero aridity_classes_all.nc"                         time = 41; lat = 361 ; lon = 720 => 'chunk_shape': (10, 46, 90)
# [X] "Procesando: sim_ssp1_2100_all desde el fichero sim_ssp1_2100_all.nc"                             times = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp1_2100_uncertainty_all desde el fichero sim_ssp1_2100_uncertainty_all.nc"     time = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp1_2100_categorised_all desde el fichero sim_ssp1_2100_categorised_all.nc"     times = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp1_2100_categorised_uncertainty_all desde el fichero sim_ssp1_2100_categorised_uncertainty_all.nc"     time = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp5_2100_all desde el fichero sim_ssp5_2100_all.nc"                             times = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp5_2100_uncertainty_all desde el fichero sim_ssp5_2100_uncertainty_all.nc"     time = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp5_2100_categorised_all desde el fichero sim_ssp5_2100_categorised_all.nc"     times = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)
# [X] "Procesando: sim_ssp5_2100_categorised_uncertainty_all desde el fichero sim_ssp5_2100_categorised_uncertainty_all.nc"     time = 1; lat = 360 ; lon = 720 => 'chunk_shape': (1, 45, 90)

netcdfs = [
    {'path': ['nc/gams/aiv_1990_all.nc'], 'nc_var': 'AIv', 'var': 'aiv_1990', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (1, 91, 180)},
    {'path': ['nc/gams/aiv_1990_categorised_all.nc'], 'nc_var': 'AIc', 'var': 'aiv_1990_categorised', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 91, 180)},
    {'path': ['nc/gams/aiv_2020_all.nc'], 'nc_var': 'AIv', 'var': 'aiv_2020', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 91, 180)},
    {'path': ['nc/gams/aiv_2020_categorised_all.nc'], 'nc_var': 'AIc', 'var': 'aiv_2020_categorised', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 91, 180)},
    {'path': ['nc/gams/aridity_all.nc'], 'nc_var': 'aridity', 'var': 'aridity', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (10, 46, 90)},
    {'path': ['nc/gams/aridity_classes_all.nc'], 'nc_var': 'aridity', 'var': 'aridity_classes', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (10, 46, 90)},
    {'path': ['nc/gams/sim_ssp1_2100_all.nc'], 'nc_var': 'AIv', 'var': 'sim_ssp1_2100', 'time_dim': 'times', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp1_2100_uncertainty_all.nc'], 'nc_var': 'unc', 'var': 'sim_ssp1_2100_uncertainty', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp1_2100_categorised_all.nc'], 'nc_var': 'AIc', 'var': 'sim_ssp1_2100_categorised', 'time_dim': 'times', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp1_2100_categorised_uncertainty_all.nc'], 'nc_var': 'unc', 'var': 'sim_ssp1_2100_categorised_uncertainty', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp5_2100_all.nc'], 'nc_var': 'AIv', 'var': 'sim_ssp5_2100', 'time_dim': 'times', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp5_2100_uncertainty_all.nc'], 'nc_var': 'unc', 'var': 'sim_ssp5_2100_uncertainty', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp5_2100_categorised_all.nc'], 'nc_var': 'AIc', 'var': 'sim_ssp5_2100_categorised', 'time_dim': 'times', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
    {'path': ['nc/gams/sim_ssp5_2100_categorised_uncertainty_all.nc'], 'nc_var': 'unc', 'var': 'sim_ssp5_2100_categorised_uncertainty', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 45, 90)},
]
zarr_path = 'nc/gams.zarr'
ncs2zarr(netcdfs, zarr_path)

# 2s minutos con max/min