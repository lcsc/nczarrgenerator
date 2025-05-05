## Build and deploy to Nexus

To build and deploy the package to Nexus, you can follow these steps:
1. Create a working directory:

    ```bash
    $ cd ~/git
    ```

2. Create and activate a virtual environment to install the module and its dependencies:

    ```bash
    $ python3 -m venv nczarrgenerator
    $ source nczarrgenerator/bin/activate
    ```

3. Install the dependencies:

    ```bash
    (nczarrgenerator) $ pip install setuptools wheel twine
    ```

4. Download the repository:

    ```bash
    $ git clone git@github.com:lcsc/nczarrgenerator.git
    ```

5. Bump the version in `setup.py`:

    ```python
    version = '1.1.0'
    ```

6. Build the package:

    ```bash
    $ python setup.py sdist bdist_wheel
    ```

7. Deploy the package to Nexus:

    ```bash
    $ twine upload --repository-url https://mirror.lcsc.csic.es/repository/pypi-lcsc/ -u pypi -p passwd dist/*1.1.0*
    ```

8. If you want to deploy the package to Nexus with a different version, you can change the version in `setup.py` and repeat steps 5 and 6.

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
        --index-url https://pypi:passwd@mirror.lcsc.csic.es/repository/pypi-lcsc/simple/ \
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