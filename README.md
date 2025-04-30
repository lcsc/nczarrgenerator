## Execution

For example, to generate the SEDI zarr from the NetCDF file `SEDI.nc`, you can follow these steps:

1. Create a working directory:

    ```bash
    $ mkdir ~/sedi
    $ cd ~/sedi
    ```

2. Create and activate a virtual environment to install the module and its dependencies:

    ```bash
    $ python3 -m venv sedi
    $ source sedi/bin/activate
    ```

3. Install nczarrgenerator:

    ```bash
    (sedi) $ pip install \
        --index-url https://pypi:Preterito43@mirror.lcsc.csic.es/repository/pypi-lcsc/simple/ \
        --extra-index-url https://pypi.org/simple \
      nczarrgenerator
    ```

4. Create the script `sedi.py` to generate the SEDI zarr with the following content:

    ```python
    import warnings
    from nczarrgenerator import ncs2zarr

    warnings.filterwarnings('ignore')

    nc_paths = [
        {'path': ['nc/sedi/SEDI.nc'], 'nc_var': 'SEDI', 'var': 'SEDI', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (9, 90, 180)},
    ]
    zarr_path = 'nc/sedi.zarr'
    ncs2zarr(nc_paths, zarr_path, beginning=True)
    ```

5. Place the SEDI NetCDF file in the location parameterized in the script, i.e., `~/sedi/nc/sedi/SEDI.nc`.
6. Run the script:

    ```bash
    (sedi) $ python sedi.py
    ```

If everything went as expected, you will find the zarr at the path `~/sedi/nc/sedi.zarr`.

SEDI does not have multiple portions, but if there were any, they would simply be listed in the `nc_paths.path` parameter. For example, for the FRI viewer:

```python
nc_paths = [
    {'path': ['nc/fri/fwi12_ERA5-Land_pen.nc', 'nc/fri/fwi12_ERA5-Land_can.nc'], 'nc_var': 'fwi12', 'var': 'fwi12', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (349, 16, 28)},
    {'path': ['nc/fri/percentiles/fwi12_pen.nc', 'nc/fri/percentiles/fwi12_can.nc'], 'nc_var': 'fwi12_percentiles', 'var': 'fwi12_p', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': False, 'chunk_shape': (4, 16, 28)},
]
zarr_path = 'nc/fri.zarr'
ncs2zarr(nc_paths, zarr_path, beginning=True)
```