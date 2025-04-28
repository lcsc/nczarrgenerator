import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: ai_clim_cv_anu_1961_1990_pen desde el fichero ai_clim_cv_anu_1961_1990_pen.nc"   time = 1; north = 834 ; east = 1115 => 'chunk_shape': (1, 126, 197)
# [X] "Procesando: ai_clim_cv_anu_1961_1990_can desde el fichero ai_clim_cv_anu_1961_1990_can.nc"   time = 1; north = 168 ; east = 455
# [X] "Procesando: ai_clim_cv_anu_1991_2020_pen desde el fichero ai_clim_cv_anu_1991_2020_pen.nc"   time = 1; north = 834 ; east = 1115 => 'chunk_shape': (1, 126, 197)
# [X] "Procesando: ai_clim_cv_anu_1991_2020_can desde el fichero ai_clim_cv_anu_1991_2020_can.nc"   time = 1; north = 168 ; east = 455
# [X] "Procesando: ai_clim_cv_anu_1961_2020_pen desde el fichero ai_clim_cv_anu_1961_2020_pen.nc"   time = 1; north = 834 ; east = 1115 => 'chunk_shape': (1, 126, 197)
# [X] "Procesando: ai_clim_cv_anu_1961_2020_can desde el fichero ai_clim_cv_anu_1961_2020_can.nc"   time = 1; north = 168 ; east = 455
# [X] "Procesando: ai_clim_cv_est_1961_1990_pen desde el ai_clim_cv_est_1961_1990_pen.nc"           time = 4; north = 834 ; east = 1115 => 'chunk_shape': (4, 126, 197)
# [X] "Procesando: ai_clim_cv_est_1961_1990_can desde el ai_clim_cv_est_1961_1990_can.nc"           time = 4; north = 168 ; east = 455
# [X] "Procesando: ai_clim_cv_est_1961_2020_pen desde el fichero ai_clim_cv_est_1961_2020_pen.nc"   time = 4; north = 834 ; east = 1115 => 'chunk_shape': (4, 126, 197)
# [X] "Procesando: ai_clim_cv_est_1961_2020_can desde el fichero ai_clim_cv_est_1961_2020_can.nc"   time = 4; north = 168 ; east = 455
# [X] "Procesando: ai_clim_cv_est_1991_2020_pen desde el fichero ai_clim_cv_est_1991_2020_pen.nc"   time = 4; north = 834 ; east = 1115 => 'chunk_shape': (4, 126, 197)
# [X] "Procesando: ai_clim_cv_est_1991_2020_can desde el fichero ai_clim_cv_est_1991_2020_can.nc"   time = 4; north = 168 ; east = 455
# [X] "Procesando: ai_clim_cv_men_1961_1990_pen desde el fichero ai_clim_cv_men_1961_1990_pen.nc"   time = 12; north = 834 ; east = 1115 => 'chunk_shape': (12, 126, 197)
# [X] "Procesando: ai_clim_cv_men_1961_1990_can desde el fichero ai_clim_cv_men_1961_1990_can.nc"   time = 12; north = 168 ; east = 455
# [X] "Procesando: ai_clim_cv_men_1961_2020_pen desde el fichero ai_clim_cv_men_1961_2020_pen.nc"   time = 12; north = 834 ; east = 1115 => 'chunk_shape': (12, 126, 197)
# [X] "Procesando: ai_clim_cv_men_1961_2020_can desde el fichero ai_clim_cv_men_1961_2020_can.nc"   time = 12; north = 168 ; east = 455
# [X] "Procesando: ai_clim_cv_men_1991_2020_pen desde el fichero ai_clim_cv_men_1991_2020_pen.nc"   time = 12; north = 834 ; east = 1115 => 'chunk_shape': (12, 126, 197)
# [X] "Procesando: ai_clim_cv_men_1991_2020_can desde el fichero ai_clim_cv_men_1991_2020_can.nc"   time = 12; north = 168 ; east = 455
# [X] "Procesando: ai_clim_pr_anu_1961_1990_pen desde el fichero ai_clim_pr_anu_1961_1990_pen.nc"   time = 1; north = 834 ; east = 1115 => 'chunk_shape': (1, 126, 197)
# [X] "Procesando: ai_clim_pr_anu_1961_1990_can desde el fichero ai_clim_pr_anu_1961_1990_can.nc"   time = 1; north = 168 ; east = 455
# [X] "Procesando: ai_clim_pr_anu_1961_2020_pen desde el fichero ai_clim_pr_anu_1961_2020_pen.nc"   time = 1; north = 834 ; east = 1115 => 'chunk_shape': (1, 126, 197)
# [X] "Procesando: ai_clim_pr_anu_1961_2020_can desde el fichero ai_clim_pr_anu_1961_2020_can.nc"   time = 1; north = 168 ; east = 455
# [X] "Procesando: ai_clim_pr_anu_1991_2020_pen desde el fichero ai_clim_pr_anu_1991_2020_pen.nc"   time = 1; north = 834 ; east = 1115 => 'chunk_shape': (1, 126, 197)
# [X] "Procesando: ai_clim_pr_anu_1991_2020_can desde el fichero ai_clim_pr_anu_1991_2020_can.nc"   time = 1; north = 168 ; east = 455
# [X] "Procesando: ai_clim_pr_est_1961_1990_pen desde el fichero ai_clim_pr_est_1961_1990_pen.nc"   time = 4; north = 834 ; east = 1115 => 'chunk_shape': (4, 126, 197)
# [X] "Procesando: ai_clim_pr_est_1961_1990_can desde el fichero ai_clim_pr_est_1961_1990_can.nc"   time = 4; north = 168 ; east = 455
# [X] "Procesando: ai_clim_pr_est_1961_2020_pen desde el fichero ai_clim_pr_est_1961_2020_pen.nc"   time = 4; north = 834 ; east = 1115 => 'chunk_shape': (4, 126, 197)
# [X] "Procesando: ai_clim_pr_est_1961_2020_can desde el fichero ai_clim_pr_est_1961_2020_can.nc"   time = 4; north = 168 ; east = 455
# [X] "Procesando: ai_clim_pr_est_1991_2020_pen desde el fichero ai_clim_pr_est_1991_2020_pen.nc"   time = 4; north = 834 ; east = 1115 => 'chunk_shape': (4, 126, 197)
# [X] "Procesando: ai_clim_pr_est_1991_2020_can desde el fichero ai_clim_pr_est_1991_2020_can.nc"   time = 4; north = 168 ; east = 455
# [X] "Procesando: ai_clim_pr_men_1961_1990_pen desde el fichero ai_clim_pr_men_1961_1990_pen.nc"   time = 12; north = 834 ; east = 1115 => 'chunk_shape': (12, 126, 197)
# [X] "Procesando: ai_clim_pr_men_1961_1990_can desde el fichero ai_clim_pr_men_1961_1990_can.nc"   time = 12; north = 168 ; east = 455
# [X] "Procesando: ai_clim_pr_men_1961_2020_pen desde el fichero ai_clim_pr_men_1961_2020_pen.nc"   time = 12; north = 834 ; east = 1115 => 'chunk_shape': (12, 126, 197)
# [X] "Procesando: ai_clim_pr_men_1961_2020_can desde el fichero ai_clim_pr_men_1961_2020_can.nc"   time = 12; north = 168 ; east = 455
# [X] "Procesando: ai_clim_pr_men_1991_2020_pen desde el fichero ai_clim_pr_men_1991_2020_pen.nc"   time = 12; north = 834 ; east = 1115 => 'chunk_shape': (12, 126, 197)
# [X] "Procesando: ai_clim_pr_men_1991_2020_can desde el fichero ai_clim_pr_men_1991_2020_can.nc"   time = 12; north = 168 ; east = 455
# [X] "Procesando: ai_serie_anu_pen desde el fichero ai_serie_anu_pen.nc"                           time = 63; north = 834 ; east = 1115 => 'chunk_shape': (12, 126, 197)
# [X] "Procesando: ai_serie_anu_can desde el fichero ai_serie_anu_can.nc"                           time = 63; north = 168 ; east = 455
# [X] "Procesando: ai_serie_est_pen desde el fichero ai_serie_est_pen.nc"                           time = 252; north = 834 ; east = 1115 => 'chunk_shape': (12, 126, 197)
# [X] "Procesando: ai_serie_est_can desde el fichero ai_serie_est_can.nc"                           time = 252; north = 168 ; east = 455
# [X] "Procesando: ai_serie_men_pen desde el fichero ai_serie_men_pen.nc"                           time = 756; north = 834 ; east = 1115 => 'chunk_shape': (12, 126, 197)
# [X] "Procesando: ai_serie_men_can desde el fichero ai_serie_men_can.nc"                           time = 756; north = 168 ; east = 455

netcdfs = [
    {'path': ['nc/sams/ai_clim_cv_anu_1961_1990_pen.nc', 'nc/sams/ai_clim_cv_anu_1961_1990_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_cv_anu_1961_1990', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (1, 126, 197)},
    {'path': ['nc/sams/ai_clim_cv_anu_1991_2020_pen.nc', 'nc/sams/ai_clim_cv_anu_1991_2020_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_cv_anu_1991_2020', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 126, 197)},
    {'path': ['nc/sams/ai_clim_cv_anu_1961_2020_pen.nc', 'nc/sams/ai_clim_cv_anu_1961_2020_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_cv_anu_1961_2020', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 126, 197)},
    {'path': ['nc/sams/ai_clim_cv_est_1961_1990_pen.nc', 'nc/sams/ai_clim_cv_est_1961_1990_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_cv_est_1961_1990', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (4, 126, 197)},
    {'path': ['nc/sams/ai_clim_cv_est_1961_2020_pen.nc', 'nc/sams/ai_clim_cv_est_1961_2020_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_cv_est_1961_2020', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (4, 126, 197)},
    {'path': ['nc/sams/ai_clim_cv_est_1991_2020_pen.nc', 'nc/sams/ai_clim_cv_est_1991_2020_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_cv_est_1991_2020', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (4, 126, 197)},
    {'path': ['nc/sams/ai_clim_cv_men_1961_1990_pen.nc', 'nc/sams/ai_clim_cv_men_1961_1990_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_cv_men_1961_1990', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 126, 197)},
    {'path': ['nc/sams/ai_clim_cv_men_1961_2020_pen.nc', 'nc/sams/ai_clim_cv_men_1961_2020_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_cv_men_1961_2020', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 126, 197)},
    {'path': ['nc/sams/ai_clim_cv_men_1991_2020_pen.nc', 'nc/sams/ai_clim_cv_men_1991_2020_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_cv_men_1991_2020', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 126, 197)},
    {'path': ['nc/sams/ai_clim_pr_anu_1961_1990_pen.nc', 'nc/sams/ai_clim_pr_anu_1961_1990_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_pr_anu_1961_1990', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 126, 197)},
    {'path': ['nc/sams/ai_clim_pr_anu_1961_2020_pen.nc', 'nc/sams/ai_clim_pr_anu_1961_2020_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_pr_anu_1961_2020', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 126, 197)},
    {'path': ['nc/sams/ai_clim_pr_anu_1991_2020_pen.nc', 'nc/sams/ai_clim_pr_anu_1991_2020_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_pr_anu_1991_2020', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (1, 126, 197)},
    {'path': ['nc/sams/ai_clim_pr_est_1961_1990_pen.nc', 'nc/sams/ai_clim_pr_est_1961_1990_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_pr_est_1961_1990', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (4, 126, 197)},
    {'path': ['nc/sams/ai_clim_pr_est_1961_2020_pen.nc', 'nc/sams/ai_clim_pr_est_1961_2020_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_pr_est_1961_2020', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (4, 126, 197)},
    {'path': ['nc/sams/ai_clim_pr_est_1991_2020_pen.nc', 'nc/sams/ai_clim_pr_est_1991_2020_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_pr_est_1991_2020', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (4, 126, 197)},
    {'path': ['nc/sams/ai_clim_pr_men_1961_1990_pen.nc', 'nc/sams/ai_clim_pr_men_1961_1990_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_pr_men_1961_1990', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 126, 197)},
    {'path': ['nc/sams/ai_clim_pr_men_1961_2020_pen.nc', 'nc/sams/ai_clim_pr_men_1961_2020_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_pr_men_1961_2020', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 126, 197)},
    {'path': ['nc/sams/ai_clim_pr_men_1991_2020_pen.nc', 'nc/sams/ai_clim_pr_men_1991_2020_can.nc'], 'nc_var': 'AI', 'var': 'ai_clim_pr_men_1991_2020', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 126, 197)},
    {'path': ['nc/sams/ai_serie_anu_pen.nc', 'nc/sams/ai_serie_anu_can.nc'], 'nc_var': 'AI', 'var': 'ai_serie_anu', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 126, 197)},
    {'path': ['nc/sams/ai_serie_est_pen.nc', 'nc/sams/ai_serie_est_can.nc'], 'nc_var': 'AI', 'var': 'ai_serie_est', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 126, 197)},
    {'path': ['nc/sams/ai_serie_men_pen.nc', 'nc/sams/ai_serie_men_can.nc'], 'nc_var': 'AI', 'var': 'ai_serie_men', 'time_dim': 'time', 'ver_dim': 'north', 'hor_dim': 'east', 'nc_projection': 'EPSG:25830', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 126, 197)},
]
zarr_path = 'nc/sams.zarr'
ncs2zarr(netcdfs, zarr_path, beginning=True)

# 48s con max/min; nczarrgenerator_all
# 79s con max/min; nczarrgenerator