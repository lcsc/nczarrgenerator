import warnings
from nczarrgenerator2 import ncs2zarr

warnings.filterwarnings('ignore')

netcdfs = [
    {'path': ['nc/vi-anomalies/kndvi_8-11.nc'], 'nc_var': 'KNDVI', 'var': 'KNDVI', 'time_dim': 'time', 'ver_dim': 'y', 'hor_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (17, 52, 92)},
]
zarr_path = 'nc/vi-anomalies_mini.zarr'
ncs2zarr(netcdfs, zarr_path, beginning=False)