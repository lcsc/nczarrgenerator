import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: pr desde el fichero MOTEDAS_century.nc"           time = 1260; lat = 77 ; lon = 125 => 'chunk_shape': (20, 10, 16)

netcdfs = [
    {'path': ['nc/mopredas/MOPREDAS_century_8-11.nc'], 'nc_var': 'p', 'var': 'pr', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (5, 10, 16)},
]
zarr_path = 'nc/mopredas_proto.zarr'
ncs2zarr(netcdfs, zarr_path, beginning=False)

# 2s con max/min; nczarrgenerator_all
# 10s sin max/min; nczarrgenerator