import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: eto desde el fichero ETo.nc"             time = 2592; lat = 834 ; lon = 1115 => 'chunk_shape': (41, 105, 140)
# [X] "Procesando: eto_ae desde el fichero ETo_Ae.nc"       time = 2592; lat = 834 ; lon = 1115 => 'chunk_shape': (41, 105, 140)
# [X] "Procesando: eto_ra desde el fichero ETo_Ra.nc"       time = 2592; lat = 834 ; lon = 1115 => 'chunk_shape': (41, 105, 140)
# [X] "Procesando: eto_var desde el fichero ETo_var.nc"     time = 2592; lat = 834 ; lon = 1115 => 'chunk_shape': (41, 105, 140)

netcdfs = [
    {'path': ['nc/eto/ETo.nc'], 'nc_var': 'ETo', 'var': 'eto', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (41, 105, 140)},
    {'path': ['nc/eto/ETo_Ae.nc'], 'nc_var': 'ETo', 'var': 'eto_ae', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (41, 105, 140)},
    {'path': ['nc/eto/ETo_Ra.nc'], 'nc_var': 'ETo', 'var': 'eto_ra', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (41, 105, 140)},
    {'path': ['nc/eto/ETo_var.nc'], 'nc_var': 'ETo', 'var': 'eto_var', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (41, 105, 140)},
]
zarr_path = 'nc/eto.zarr'
ncs2zarr(netcdfs, zarr_path)

# 16m54s minutos con max/min