import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: ffd_pen desde el fichero primera_helada/ff_pen.nc"                           time = 62; lat = 341 ; lon = 545 => 'chunk_shape': (31, 81, 113)
# [X] "Procesando: ffd_can desde el fichero primera_helada/ff_can.nc"                           time = 62; lat = 71 ; lon = 189
# [X] "Procesando: lfd_pen desde el fichero ultima_helada/lf_pen.nc"                            time = 62; lat = 341 ; lon = 545 => 'chunk_shape': (31, 81, 113)
# [X] "Procesando: lfd_can desde el fichero ultima_helada/lf_can.nc"                            time = 62; lat = 71 ; lon = 189
# [X] "Procesando: gdd_corn_pen desde el fichero acum_calor/gdd_corn_pen.nc"                    time = 62; lat = 341 ; lon = 545 => 'chunk_shape': (31, 81, 113)
# [X] "Procesando: gdd_corn_can desde el fichero acum_calor/gdd_corn_can.nc"                    time = 62; lat = 71 ; lon = 189
# [X] "Procesando: gdd_wine_pen desde el fichero acum_calor/gdd_wine_pen.nc"                    time = 62; lat = 341 ; lon = 545 => 'chunk_shape': (31, 81, 113)
# [X] "Procesando: gdd_wine_can desde el fichero acum_calor/gdd_wine_can.nc"                    time = 62; lat = 71 ; lon = 189
# [X] "Procesando: gdd_winter_cereal_pen desde el fichero acum_calor/gdd_winter_cereal_pen.nc"  time = 62; lat = 341 ; lon = 545 => 'chunk_shape': (31, 81, 113)
# [X] "Procesando: gdd_winter_cereal_can desde el fichero acum_calor/gdd_winter_cereal_can.nc"  time = 62; lat = 71 ; lon = 189

netcdfs = [
    {'path': ['nc/amm/primera_helada/ff_pen.nc', 'nc/amm/primera_helada/ff_can.nc'], 'nc_var': 'ffd', 'var': 'ffd', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (31, 81, 113)},
    {'path': ['nc/amm/ultima_helada/lf_pen.nc', 'nc/amm/ultima_helada/lf_can.nc'], 'nc_var': 'lfd', 'var': 'lfd', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (31, 81, 113)},
    {'path': ['nc/amm/acum_calor/gdd_corn_pen.nc', 'nc/amm/acum_calor/gdd_corn_can.nc'], 'nc_var': 'gdd', 'var': 'gdd_corn', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (31, 81, 113)},
    {'path': ['nc/amm/acum_calor/gdd_wine_pen.nc', 'nc/amm/acum_calor/gdd_wine_can.nc'], 'nc_var': 'gdd', 'var': 'gdd_wine', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (31, 81, 113)},
    {'path': ['nc/amm/acum_calor/gdd_winter_cereal_pen.nc', 'nc/amm/acum_calor/gdd_winter_cereal_can.nc'], 'nc_var': 'gdd', 'var': 'gdd_winter_cereal', 'time_dim': 'time', 'lat_dim': 'lat', 'lon_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (31, 81, 113)},
]
zarr_path = 'nc/amm.zarr'
ncs2zarr(netcdfs, zarr_path)

# 3s con max/min