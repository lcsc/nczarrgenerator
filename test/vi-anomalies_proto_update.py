import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

nc_paths = [
    # {'path': ['nc/vi-anomalies/kndvi.nc'], 'nc_var': 'KNDVI', 'var': 'KNDVI', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (17, 52, 92)},
    # {'path': ['nc/vi-anomalies/ndvi.nc'], 'nc_var': 'NDVI', 'var': 'NDVI', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (17, 52, 92)},
    {'path': ['nc/vi-anomalies/kndvi_8-11.nc'], 'nc_var': 'KNDVI', 'var': 'KNDVI', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (5, 52, 92)},
]
zarr_path = 'nc/vi-anomalies_proto.zarr'

ncs2zarr(nc_paths, zarr_path, beginning=False)