import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: ffd_pen desde el fichero primera_helada/ff_pen.nc"                           time = 62; lat = 341 ; lon = 545 => 'chunk_shape': (31, 81, 113)
# [X] "Procesando: ffd_can desde el fichero primera_helada/ff_can.nc"                           time = 62; lat = 71 ; lon = 189

netcdfs = [
    {'path': ['nc/amm/primera_helada/ff_0-9_pen.nc', 'nc/amm/primera_helada/ff_0-9_can.nc'], 'nc_var': 'ffd', 'var': 'ffd', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (5, 81, 113)},
]
zarr_path = 'nc/amm_proto.zarr'
ncs2zarr(netcdfs, zarr_path, beginning=True)

# 3s con max/min