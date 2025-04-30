## Execution

For example, to generate the MOPREDAS zarr from the NetCDF file `MOPREDAS_century.nc`, you can follow these steps:

1. Create a working directory:

    ```bash
    $ mkdir ~/mopredas
    $ cd ~/mopredas
    ```

2. Create and activate a virtual environment to install the module and its dependencies:

    ```bash
    $ python3 -m venv mopredas
    $ source mopredas/bin/activate
    ```

3. Install nczarrgenerator:

    ```bash
    (mopredas) $ pip install \
        --index-url https://pypi:Preterito43@mirror.lcsc.csic.es/repository/pypi-lcsc/simple/ \
        --extra-index-url https://pypi.org/simple \
      nczarrgenerator
    ```

4. Create the script `mopredas.py` to generate the MOPREDAS zarr with the following content:

    ```python
    import warnings
    from nczarrgenerator import ncs2zarr

    warnings.filterwarnings('ignore')

    netcdfs = [
        {'path': ['nc/mopredas/MOPREDAS_century.nc'], 'nc_var': 'p', 'var': 'pr', 'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon', 'nc_projection': 'EPSG:4326', 'calc_min_max': True, 'include_center_calc': True, 'chunk_shape': (20, 10, 16)},
    ]
    zarr_path = 'nc/mopredas.zarr'
    ncs2zarr(netcdfs, zarr_path, beginning=True)
    ```

5. Place the MOPREDAS NetCDF file in the location parameterized in the script, i.e., `~/mopredas/nc/mopredas/MOPREDAS_century.nc`.
6. Run the script:

    ```bash
    (mopredas) $ python mopredas.py
    ```

If everything went as expected, you will find the zarr at the path `~/mopredas/nc/mopredas.zarr`.