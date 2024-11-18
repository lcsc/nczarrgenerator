import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# [X] "Procesando: tmax_pen desde el fichero tmax_daily_grid_pen.nc"                time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: tmax_can desde el fichero tmax_daily_grid_can.nc"                time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: tmin_pen desde el fichero tmin_daily_grid_pen.nc"                time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: tmin_can desde el fichero tmin_daily_grid_can.nc"                time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: heat_wave_all desde el fichero heatwave_all.nc"                  time = 479; lat = 646 ; lon = 899 => 'chunk_shape': (16, 81, 113)
# [X] "Procesando: heat_wave_time_all desde el fichero heat_wave_duration_all.nc"   time = 479; lat = 646 ; lon = 899 => 'chunk_shape': (16, 81, 113)
# [X] "Procesando: cold_wave_all desde el fichero cold_wave_all.nc"                 time = 581; lat = 646 ; lon = 899 => 'chunk_shape': (16, 81, 113)
# [X] "Procesando: cold_wave_time_all desde el fichero cold_wave_duration_all.nc"   time = 581; lat = 646 ; lon = 899 => 'chunk_shape': (16, 81, 113)
# [X] "Procesando: tmax_q95_pen desde el fichero tmp_clim_q95_pen.nc"               time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: tmax_q95_can desde el fichero tmp_clim_q95_can.nc"               time = 12; lat = 71 ; lon = 189
# [X] "Procesando: tmax_q90_pen desde el fichero tmp_clim_q90_pen.nc"               time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: tmax_q90_can desde el fichero tmp_clim_q90_can.nc"               time = 12; lat = 71 ; lon = 189
# [X] "Procesando: tmax_q97_pen desde el fichero tmp_clim_q97_pen.nc"               time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: tmax_q97_can desde el fichero tmp_clim_q97_can.nc"               time = 12; lat = 71 ; lon = 189
# [X] "Procesando: tmax_q99_pen desde el fichero tmp_clim_q99_pen.nc"               time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: tmax_q99_can desde el fichero tmp_clim_q99_can.nc"               time = 12; lat = 71 ; lon = 189
# [X] "Procesando: tmax_q5_pen desde el fichero tmp_clim_q5_pen.nc"                 time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: tmax_q5_can desde el fichero tmp_clim_q5_can.nc"                 time = 12; lat = 71 ; lon = 189
# [X] "Procesando: tmax_q3_pen desde el fichero tmp_clim_q3_pen.nc"                 time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: tmax_q3_can desde el fichero tmp_clim_q3_can.nc"                 time = 12; lat = 71 ; lon = 189
# [X] "Procesando: tmax_q1_pen desde el fichero tmp_clim_q1_pen.nc"                 time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: tmax_q1_can desde el fichero tmp_clim_q1_can.nc"                 time = 12; lat = 71 ; lon = 189
# [X] "Procesando: tmax_q10_pen desde el fichero tmp_clim_q10_pen.nc"               time = 12; lat = 341 ; lon = 545 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: tmax_q10_can desde el fichero tmp_clim_q10_can.nc"               time = 12; lat = 71 ; lon = 189
# [X] "Procesando: acc/tmax_3_pen desde el fichero acc/tmax_cumulative_3_pen.nc"    time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: acc/tmax_3_can desde el fichero acc/tmax_cumulative_3_can.nc"    time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: acc/tmin_3_pen desde el fichero acc/tmin_cumulative_3_pen.nc"    time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: acc/tmin_3_can desde el fichero acc/tmin_cumulative_3_can.nc"    time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: acc/tmax_5_pen desde el fichero acc/tmax_cumulative_5_pen.nc"    time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: acc/tmax_5_can desde el fichero acc/tmax_cumulative_5_can.nc"    time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: acc/tmin_5_pen desde el fichero acc/tmin_cumulative_5_pen.nc"    time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: acc/tmin_5_can desde el fichero acc/tmin_cumulative_5_can.nc"    time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: acc/tmax_7_pen desde el fichero acc/tmax_cumulative_7_pen.nc"    time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: acc/tmax_7_can desde el fichero acc/tmax_cumulative_7_can.nc"    time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: acc/tmin_7_pen desde el fichero acc/tmin_cumulative_7_pen.nc"    time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: acc/tmin_7_can desde el fichero acc/tmin_cumulative_7_can.nc"    time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: acc/tmax_10_pen desde el fichero acc/tmax_cumulative_10_pen.nc"  time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: acc/tmax_10_can desde el fichero acc/tmax_cumulative_10_can.nc"  time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: acc/tmin_10_pen desde el fichero acc/tmin_cumulative_10_pen.nc"  time = 22645; lat = 341 ; lon = 545 => 'chunk_shape': (354, 81, 113)
# [X] "Procesando: acc/tmin_10_can desde el fichero acc/tmin_cumulative_10_can.nc"  time = 22645; lat = 71 ; lon = 189
# [X] "Procesando: acc/d5/tmin_q5_all desde el fichero percentiles/d5/tmin_p5_cumulative_5d_all.nc"     time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/tmin_q3_all desde el fichero percentiles/d5/tmin_p3_cumulative_5d_all.nc"     time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/tmin_q1_all desde el fichero percentiles/d5/tmin_p1_cumulative_5d_all.nc"     time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/tmin_q10_all desde el fichero percentiles/d5/tmin_p10_cumulative_5d_all.nc"   time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/tmax_q95_all desde el fichero percentiles/d5/tmax_p95_cumulative_5d_all.nc"   time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/tmax_q90_all desde el fichero percentiles/d5/tmax_p90_cumulative_5d_all.nc"   time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/tmax_q97_all desde el fichero percentiles/d5/tmax_p97_cumulative_5d_all.nc"   time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)
# [X] "Procesando: acc/d5/tmax_q99_all desde el fichero percentiles/d5/tmax_p99_cumulative_5d_all.nc"   time = 12; lat = 646 ; lon = 899 => 'chunk_shape': (12, 81, 113)

netcdfs = [
    {'path': ['nc/etm/tmin_daily_grid_pen.nc', 'nc/etm/tmin_daily_grid_can.nc'], 'nc_var': 'tmin', 'var': 'tmin', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/etm/tmax_daily_grid_pen.nc', 'nc/etm/tmax_daily_grid_can.nc'], 'nc_var': 'tmax', 'var': 'tmax', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/etm/heatwave_all.nc'], 'nc_var': 'Heatwaves (maximum temperature)', 'var': 'heat_wave', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (16, 81, 113)},
    {'path': ['nc/etm/heat_wave_duration_all.nc'], 'nc_var': 'hwd', 'var': 'heat_wave_time', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (16, 81, 113)},
    {'path': ['nc/etm/cold_wave_all.nc'], 'nc_var': 'Cold_waves (minimum temperature)', 'var': 'cold_wave', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (16, 81, 113)},
    {'path': ['nc/etm/cold_wave_duration_all.nc'], 'nc_var': 'cwd', 'var': 'cold_wave_time', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (16, 81, 113)},
    {'path': ['nc/etm/tmp_clim_q95_pen.nc', 'nc/etm/tmp_clim_q95_can.nc'], 'nc_var': 'tmp_q95', 'var': 'tmax_q95', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/tmp_clim_q90_pen.nc', 'nc/etm/tmp_clim_q90_can.nc'], 'nc_var': 'tmp_q90', 'var': 'tmax_q90', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/tmp_clim_q97_pen.nc', 'nc/etm/tmp_clim_q97_can.nc'], 'nc_var': 'tmp_q97', 'var': 'tmax_q97', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/tmp_clim_q99_pen.nc', 'nc/etm/tmp_clim_q99_can.nc'], 'nc_var': 'tmp_q99', 'var': 'tmax_q99', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/tmp_clim_q5_pen.nc', 'nc/etm/tmp_clim_q5_can.nc'], 'nc_var': 'tmp_q5', 'var': 'tmax_q5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/tmp_clim_q3_pen.nc', 'nc/etm/tmp_clim_q3_can.nc'], 'nc_var': 'tmp_q3', 'var': 'tmax_q3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/tmp_clim_q1_pen.nc', 'nc/etm/tmp_clim_q1_can.nc'], 'nc_var': 'tmp_q1', 'var': 'tmax_q1', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/tmp_clim_q10_pen.nc', 'nc/etm/tmp_clim_q10_can.nc'], 'nc_var': 'tmp_q10', 'var': 'tmax_q10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/acc/tmax_cumulative_3_pen.nc', 'nc/etm/acc/tmax_cumulative_3_can.nc'], 'nc_var': 'Maximum Temperature', 'var': 'acc_tmax_3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/etm/acc/tmin_cumulative_3_pen.nc', 'nc/etm/acc/tmin_cumulative_3_can.nc'], 'nc_var': 'Minimum Temperature', 'var': 'acc_tmin_3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/etm/acc/tmax_cumulative_5_pen.nc', 'nc/etm/acc/tmax_cumulative_5_can.nc'], 'nc_var': 'Maximum Temperature', 'var': 'acc_tmax_5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/etm/acc/tmin_cumulative_5_pen.nc', 'nc/etm/acc/tmin_cumulative_5_can.nc'], 'nc_var': 'Minimum Temperature', 'var': 'acc_tmin_5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/etm/acc/tmax_cumulative_7_pen.nc', 'nc/etm/acc/tmax_cumulative_7_can.nc'], 'nc_var': 'Maximum Temperature', 'var': 'acc_tmax_7', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/etm/acc/tmin_cumulative_7_pen.nc', 'nc/etm/acc/tmin_cumulative_7_can.nc'], 'nc_var': 'Minimum Temperature', 'var': 'acc_tmin_7', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/etm/acc/tmax_cumulative_10_pen.nc', 'nc/etm/acc/tmax_cumulative_10_can.nc'], 'nc_var': 'Maximum Temperature', 'var': 'acc_tmax_10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/etm/acc/tmin_cumulative_10_pen.nc', 'nc/etm/acc/tmin_cumulative_10_can.nc'], 'nc_var': 'Minimum Temperature', 'var': 'acc_tmin_10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (354, 81, 113)},
    {'path': ['nc/etm/percentiles/d5/tmin_p5_cumulative_5d_all.nc'], 'nc_var': 'Minimum Temperature', 'var': 'acc_d5_tmin_q5', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/percentiles/d5/tmin_p3_cumulative_5d_all.nc'], 'nc_var': 'Minimum Temperature', 'var': 'acc_d5_tmin_q3', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/percentiles/d5/tmin_p1_cumulative_5d_all.nc'], 'nc_var': 'Minimum Temperature', 'var': 'acc_d5_tmin_q1', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/percentiles/d5/tmin_p10_cumulative_5d_all.nc'], 'nc_var': 'Minimum Temperature', 'var': 'acc_d5_tmin_q10', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/percentiles/d5/tmax_p95_cumulative_5d_all.nc'], 'nc_var': 'Maximum Temperature', 'var': 'acc_d5_tmax_q95', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/percentiles/d5/tmax_p90_cumulative_5d_all.nc'], 'nc_var': 'Maximum Temperature', 'var': 'acc_d5_tmax_q90', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/percentiles/d5/tmax_p97_cumulative_5d_all.nc'], 'nc_var': 'Maximum Temperature', 'var': 'acc_d5_tmax_q97', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
    {'path': ['nc/etm/percentiles/d5/tmax_p99_cumulative_5d_all.nc'], 'nc_var': 'Maximum Temperature', 'var': 'acc_d5_tmax_q99', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (12, 81, 113)},
]
zarr_path = 'nc/etm.zarr'
ncs2zarr(netcdfs, zarr_path)

# 37 minutos con max/min