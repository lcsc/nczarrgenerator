import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: SEDI desde el fichero SEDI.nc"           time = 516; lat = 720 ; lon = 1440 => 'chunk_shape': (9, 90, 180)

netcdfs = [
    {'path': ['nc/sedi/SEDI.nc'], 'nc_var': 'SEDI', 'var': 'sedi', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': False, 'include_center_calc': True, 'chunk_shape': (9, 90, 180)},
]
zarr_path = 'nc/sedi.zarr'
ncs2zarr(netcdfs, zarr_path)

# 3s sin max/min (ya que si se activan los máximos y mínimos aparece un error por ser la unidad de time 'months since...')