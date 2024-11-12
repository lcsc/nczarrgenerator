import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: fwi12_pen desde el fichero fwi12_ERA5-Land_pen.nc"           time = 22280; lat = 101 ; lon = 161 => 'chunk_shape': (349, 16, 28)
# [X] "Procesando: fwi12_can desde el fichero fwi12_ERA5-Land_can.nc"           time = 22280; lat = 24 ; lon = 56
# [X] "Procesando: fwi12_p_pen desde el fichero percentiles/fwi12_pen.nc"       time = 4; lat = 101 ; lon = 161 => 'chunk_shape': (4, 16, 28)
# [X] "Procesando: fwi12_p_can desde el fichero percentiles/fwi12_can.nc"       time = 4; lat = 24 ; lon = 56

netcdfs = [
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/fri/fwi12_ERA5-Land_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/fri/fwi12_ERA5-Land_can.nc'], 'nc_var': 'fwi12', 'var': 'fwi12', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (349, 16, 28)},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/fri/percentiles/fwi12_pen.nc', '/home/edumoreno/git/nczarrgenerator/nc/fri/percentiles/fwi12_can.nc'], 'nc_var': 'fwi12_percentiles', 'var': 'fwi12_p', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (4, 16, 28)},
]
zarr_path = '/home/edumoreno/git/nczarrgenerator/nc/fri.zarr'
ncs2zarr(netcdfs, zarr_path)

# 6m14s minutos con max/min