import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: pr_pen desde el fichero pr_daily_grid_pen.nc"                    time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: pr_can desde el fichero pr_daily_grid_can.nc"                    time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: pr_q95_pen desde el fichero pr_clim_q95_pen.nc"                  time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: pr_q95_can desde el fichero pr_clim_q95_can.nc"                  time = 12; lat = 71 ; lon = 189
# [X] "Procesando: pr_q90_pen desde el fichero pr_clim_q90_pen.nc"                  time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: pr_q90_can desde el fichero pr_clim_q90_can.nc"                  time = 12; lat = 71 ; lon = 189
# [X] "Procesando: pr_q97_pen desde el fichero pr_clim_q97_pen.nc"                  time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: pr_q97_can desde el fichero pr_clim_q97_can.nc"                  time = 12; lat = 71 ; lon = 189
# [X] "Procesando: pr_q99_pen desde el fichero pr_clim_q99_pen.nc"                  time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: pr_q99_can desde el fichero pr_clim_q99_can.nc"                  time = 12; lat = 71 ; lon = 189
# [X] "Procesando: pr_q5_pen desde el fichero pr_clim_q5_pen.nc"                    time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: pr_q5_can desde el fichero pr_clim_q5_can.nc"                    time = 12; lat = 71 ; lon = 189
# [X] "Procesando: pr_q3_pen desde el fichero pr_clim_q3_pen.nc"                    time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: pr_q3_can desde el fichero pr_clim_q3_can.nc"                    time = 12; lat = 71 ; lon = 189
# [X] "Procesando: pr_q1_pen desde el fichero pr_clim_q1_pen.nc"                    time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: pr_q1_can desde el fichero pr_clim_q1_can.nc"                    time = 12; lat = 71 ; lon = 189
# [X] "Procesando: pr_q10_pen desde el fichero pr_clim_q10_pen.nc"                  time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: pr_q10_can desde el fichero pr_clim_q10_can.nc"                  time = 12; lat = 71 ; lon = 189
# [X] "Procesando: acc/pr_d3_pen desde el fichero acc/pr_cumulative_3_pen.nc"       time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: acc/pr_d3_can desde el fichero acc/pr_cumulative_3_can.nc"       time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: acc/pr_d5_pen desde el fichero acc/pr_cumulative_5_pen.nc"       time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: acc/pr_d5_can desde el fichero acc/pr_cumulative_5_can.nc"       time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: acc/pr_d7_pen desde el fichero acc/pr_cumulative_7_pen.nc"       time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: acc/pr_d7_can desde el fichero acc/pr_cumulative_7_can.nc"       time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: acc/pr_d10_pen desde el fichero acc/pr_cumulative_10_pen.nc"     time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: acc/pr_d10_can desde el fichero acc/pr_cumulative_10_can.nc"     time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: acc/d5/pr_d5_q95_all desde el fichero /acc/p_d5/pr_p95_cumulative_5d_all.nc"     time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/pr_d5_q90_all desde el fichero /acc/p_d5/pr_p90_cumulative_5d_all.nc"     time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/pr_d5_q97_all desde el fichero /acc/p_d5/pr_p97_cumulative_5d_all.nc"     time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/pr_d5_q99_all desde el fichero /acc/p_d5/pr_p99_cumulative_5d_all.nc"     time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/pr_d5_q5_all desde el fichero /acc/p_d5/pr_p5_cumulative_5d_all.nc"       time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/pr_d5_q3_all desde el fichero /acc/p_d5/pr_p3_cumulative_5d_all.nc"       time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/pr_d5_q1_all desde el fichero /acc/p_d5/pr_p1_cumulative_5d_all.nc"       time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/pr_d5_q10_all desde el fichero /acc/p_d5/pr_p10_cumulative_5d_all.nc"     time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)

netcdfs = [
    {'path': ['nc/epm/pr_daily_grid_pen.nc', 'nc/epm/pr_daily_grid_can.nc'], 'nc_var': 'pr', 'var': 'pr', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/epm/pr_clim_q95_pen.nc', 'nc/epm/pr_clim_q95_can.nc'], 'nc_var': 'pr_q95', 'var': 'pr_q95', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/pr_clim_q90_pen.nc', 'nc/epm/pr_clim_q90_can.nc'], 'nc_var': 'pr_q90', 'var': 'pr_q90', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/pr_clim_q97_pen.nc', 'nc/epm/pr_clim_q97_can.nc'], 'nc_var': 'pr_q97', 'var': 'pr_q97', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/pr_clim_q99_pen.nc', 'nc/epm/pr_clim_q99_can.nc'], 'nc_var': 'pr_q99', 'var': 'pr_q99', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/pr_clim_q5_pen.nc', 'nc/epm/pr_clim_q5_can.nc'], 'nc_var': 'pr_q5', 'var': 'pr_q5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/pr_clim_q3_pen.nc', 'nc/epm/pr_clim_q3_can.nc'], 'nc_var': 'pr_q3', 'var': 'pr_q3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/pr_clim_q1_pen.nc', 'nc/epm/pr_clim_q1_can.nc'], 'nc_var': 'pr_q1', 'var': 'pr_q1', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/pr_clim_q10_pen.nc', 'nc/epm/pr_clim_q10_can.nc'], 'nc_var': 'pr_q10', 'var': 'pr_q10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/acc/pr_cumulative_3_pen.nc', 'nc/epm/acc/pr_cumulative_3_can.nc'], 'nc_var': 'Precipitations', 'var': 'acc_pr_d3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/epm/acc/pr_cumulative_5_pen.nc', 'nc/epm/acc/pr_cumulative_5_can.nc'], 'nc_var': 'Precipitations', 'var': 'acc_pr_d5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/epm/acc/pr_cumulative_7_pen.nc', 'nc/epm/acc/pr_cumulative_7_can.nc'], 'nc_var': 'Precipitations', 'var': 'acc_pr_d7', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/epm/acc/pr_cumulative_10_pen.nc', 'nc/epm/acc/pr_cumulative_10_can.nc'], 'nc_var': 'Precipitations', 'var': 'acc_pr_d10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/epm/acc/p_d5/pr_p95_cumulative_5d_all.nc'], 'nc_var': 'Precipitations', 'var': 'acc_pr_d5_q95', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/acc/p_d5/pr_p90_cumulative_5d_all.nc'], 'nc_var': 'Precipitations', 'var': 'acc_pr_d5_q90', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/acc/p_d5/pr_p97_cumulative_5d_all.nc'], 'nc_var': 'Precipitations', 'var': 'acc_pr_d5_q97', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/acc/p_d5/pr_p99_cumulative_5d_all.nc'], 'nc_var': 'Precipitations', 'var': 'acc_pr_d5_q99', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/acc/p_d5/pr_p5_cumulative_5d_all.nc'], 'nc_var': 'Precipitations', 'var': 'acc_pr_d5_q5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/acc/p_d5/pr_p3_cumulative_5d_all.nc'], 'nc_var': 'Precipitations', 'var': 'acc_pr_d5_q3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/acc/p_d5/pr_p1_cumulative_5d_all.nc'], 'nc_var': 'Precipitations', 'var': 'acc_pr_d5_q1', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/epm/acc/p_d5/pr_p10_cumulative_5d_all.nc'], 'nc_var': 'Precipitations', 'var': 'acc_pr_d5_q10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
]
zarr_path = 'nc/epm.zarr'
ncs2zarr(netcdfs, zarr_path, beginning=True)

# 37 minutos con max/min; nczarrgenerator_all
# 64 minutos con max/min; nczarrgenerator