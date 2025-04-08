import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: t desde el fichero MOTEDAS_century.nc"           time = 1260; lat = 77 ; lon = 125 => 'chunk_shape': (20, 10, 16)
# [X] "Procesando: tn desde el fichero MOTEDAS_century-tn.nc"       time = 1260; lat = 77 ; lon = 125 => 'chunk_shape': (20, 10, 16)
# [X] "Procesando: tx desde el fichero MOTEDAS_century-tx.nc"       time = 1260; lat = 77 ; lon = 125 => 'chunk_shape': (20, 10, 16)

netcdfs = [
    {'path': ['nc/motedas/MOTEDAS_century.nc'], 'nc_var': 't', 'var': 't', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (20, 10, 16)},
    {'path': ['nc/motedas/MOTEDAS_century-tn.nc'], 'nc_var': 'tn', 'var': 'tn', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (20, 10, 16)},
    {'path': ['nc/motedas/MOTEDAS_century-tx.nc'], 'nc_var': 'tx', 'var': 'tx', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (20, 10, 16)},
]
zarr_path = 'nc/motedas.zarr'
ncs2zarr(netcdfs, zarr_path)

# 7s con max/min; nczarrgenerator_all
# 46s sin max/min; nczarrgenerator