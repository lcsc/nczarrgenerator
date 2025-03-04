import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

netcdfs = [
    {'path': ['nc/vi-anomalies/kndvi.nc'], 'nc_var': 'KNDVI', 'var': 'KNDVI', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (17, 52, 92)},
    {'path': ['nc/vi-anomalies/ndvi.nc'], 'nc_var': 'NDVI', 'var': 'NDVI', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (17, 52, 92)},
    {'path': ['nc/vi-anomalies/skndvi.nc'], 'nc_var': 'SKNDVI', 'var': 'SKNDVI', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (17, 52, 92)},
    {'path': ['nc/vi-anomalies/sndvi.nc'], 'nc_var': 'SNDVI', 'var': 'SNDVI', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (17, 52, 92)},
]
zarr_path = 'nc/vi-anomalies.zarr'
ncs2zarr(netcdfs, zarr_path)