import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

netcdfs = [
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/kndvi.nc'], 'nc_var': 'KNDVI', 'var': 'kndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/ndvi.nc'], 'nc_var': 'NDVI', 'var': 'ndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': True},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/skndvi.nc'], 'nc_var': 'SKNDVI', 'var': 'skndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False},
    {'path': ['/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies/sndvi.nc'], 'nc_var': 'SNDVI', 'var': 'sndvi', 'time_dim': 'time', 'lat_dim': 'y', 'lon_dim': 'x', 'nc_projection': 'EPSG:23030', 'calc_min_max': True, 'include_center_calc': False},
]
zarr_path = '/home/edumoreno/git/nczarrgenerator/nc/vi-anomalies.zarr'
ncs2zarr(netcdfs, zarr_path, chunk_shape=(17, 52, 92))