from setuptools import setup, find_packages

setup(
    name='nczarrgenerator',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'xarray==2025.3.1',
        'zarr==2.18.7',
        'numpy==2.2.5',
        'pyproj==3.7.1',
        'netCDF4==1.7.2',
        'dask==2025.4.1'
    ],
    description='Convert multiple NetCDF files to a Zarr store with additional metadata and chunking',
    author='Eduardo Moreno',
    python_requires='>=3.6',
)