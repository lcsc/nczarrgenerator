# nczarrgenerator

A Python package that converts one or more NetCDF files into a single [Zarr](https://zarr.dev) store enriched with the metadata required to serve gridded climate data directly from static file storage to web-based viewers. It is the Zarr counterpart of the [`ncartifactgenerator`](https://github.com/lcsc/ncartifactgenerator) R package: both implement the same server-side preprocessing workflow, and the browser-side library [`AnemUI`](https://github.com/lcsc/AnemUI) can consume either backend.


## Purpose

Web viewers of gridded climate data need two very different query patterns to be fast: retrieving the full time series of a single pixel, and retrieving the full spatial map of a single date. `nczarrgenerator` prepares a Zarr store so that a browser (or any HTTP client) can resolve both query types with plain HTTP requests against static files, without a GeoServer or OGC endpoint.

Beyond the raw data conversion, the package adds the metadata a viewer needs at startup:

- Per-variable min/max value arrays over time (for colour-scale rendering of each date).
- Global min/max attributes per variable (`minVal`, `maxVal`).
- Display metadata per variable (`varTitle`, `legendTitle`, `projection`).
- Geographic centre (`center_lat`, `center_lon`) and an approximate web-map `zoom` level at the root group.
- The list of available `variables` and the `creation_date` at the root group.
- Consolidated Zarr metadata, so a client can discover the whole store with a single request.

It also handles common preprocessing needs of operational datasets: merging several spatial portions (e.g. mainland + islands grids) into one regular grid, sorting coordinates in ascending order, renaming variables and dimensions to a uniform scheme (`time`, `y`, `x`), and incrementally appending or updating time steps of an existing store.


## Requirements

- **Python ≥ 3.11**
- Dependencies (installed automatically): `xarray`, `zarr`, `numpy`, `pyproj`, `netCDF4`, `dask`

Input files must be NetCDF files with a 3-dimensional variable (time × latitude × longitude, in any dimension order and with any dimension names).


## Installation

```sh
# From GitHub
pip install git+https://github.com/lcsc/nczarrgenerator.git

# Or from a local clone
git clone https://github.com/lcsc/nczarrgenerator.git
pip install ./nczarrgenerator
```

Using a virtual environment is recommended:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install git+https://github.com/lcsc/nczarrgenerator.git
```


## Usage

The package exposes a single entry point, `ncs2zarr(nc_paths, zarr_path, beginning=False, zarr_version=2)`:

| Parameter | Type | Description |
|---|---|---|
| `nc_paths` | list of dict | One dictionary per output variable (see keys below) |
| `zarr_path` | str | Path of the output Zarr store |
| `beginning` | bool | `True` creates the store from scratch (overwriting it if it exists); `False` appends/updates time steps of an existing store. Default `False` |
| `zarr_version` | int | Zarr format version, `2` or `3`. Default `2` |

Each dictionary in `nc_paths` accepts the following keys:

| Key | Type | Default | Description |
|---|---|---|---|
| `path` | list of str | required | Paths to the NetCDF file(s) for this variable. If several are given, they are treated as spatial portions of the same grid and merged (see below) |
| `nc_var` | str | required | Name of the variable inside the NetCDF file(s) |
| `var` | str | required | Name to use for the variable (and its group) in the Zarr store |
| `time_dim` | str | `'time'` | Name of the time dimension in the NetCDF file |
| `ver_dim` | str | `'lat'` | Name of the vertical (latitude/y) dimension |
| `hor_dim` | str | `'lon'` | Name of the horizontal (longitude/x) dimension |
| `nc_projection` | str | `'EPSG:4326'` | CRS of the input coordinates, as an EPSG code string |
| `calc_min_max` | bool | `True` | Compute per-date min/max arrays and global `minVal`/`maxVal` attributes |
| `include_center_calc` | bool | `False` | Include this variable's extent in the computation of the store-level centre and zoom |
| `chunk_shape` | tuple of int | `(16, 128, 128)` | Zarr chunk shape as (time, latitude, longitude) |

### Creating a store

To generate a Zarr store from a single NetCDF file, save the following script (e.g. as `convert.py`), adjusting paths and parameters to your data:

```python
import warnings
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

nc_paths = [
    {'path': ['nc/sedi/SEDI.nc'], 'nc_var': 'SEDI', 'var': 'SEDI',
     'time_dim': 'time', 'ver_dim': 'lat', 'hor_dim': 'lon',
     'nc_projection': 'EPSG:4326', 'calc_min_max': True,
     'include_center_calc': True, 'chunk_shape': (9, 90, 180)},
]
ncs2zarr(nc_paths, 'nc/sedi.zarr', beginning=True)
```

and run it:

```sh
python convert.py
```

The Zarr store is written to `nc/sedi.zarr`.

### Multiple variables and spatial portions

A single call can process several variables (one dictionary each), and each variable may come from several NetCDF files covering different parts of the domain (e.g. a peninsular grid and an islands grid). The portions are reindexed onto a common regular grid — built from the union of their extents at the finest resolution found — using nearest-neighbour matching, and merged:

```python
nc_paths = [
    {'path': ['nc/fri/fwi12_ERA5-Land_pen.nc', 'nc/fri/fwi12_ERA5-Land_can.nc'],
     'nc_var': 'fwi12', 'var': 'fwi12',
     'nc_projection': 'EPSG:4326', 'calc_min_max': True,
     'include_center_calc': True, 'chunk_shape': (349, 16, 28)},
    {'path': ['nc/fri/percentiles/fwi12_pen.nc', 'nc/fri/percentiles/fwi12_can.nc'],
     'nc_var': 'fwi12_percentiles', 'var': 'fwi12_p',
     'nc_projection': 'EPSG:4326', 'calc_min_max': True,
     'include_center_calc': False, 'chunk_shape': (4, 16, 28)},
]
ncs2zarr(nc_paths, 'nc/fri.zarr', beginning=True)
```

### Updating an existing store

Operational datasets grow over time. With `beginning=False` (the default), `ncs2zarr` opens the existing store and processes the input time steps one by one: dates already present in the store are overwritten in place, and new dates are appended, keeping the per-date and global min/max metadata up to date. This makes periodic (e.g. daily) updates cheap — only the new NetCDF needs to be processed:

```python
nc_paths = [
    {'path': ['nc/sedi/SEDI_latest.nc'], 'nc_var': 'SEDI', 'var': 'SEDI',
     'nc_projection': 'EPSG:4326', 'include_center_calc': True,
     'chunk_shape': (9, 90, 180)},
]
ncs2zarr(nc_paths, 'nc/sedi.zarr', beginning=False)
```

### Choosing a chunk shape

`chunk_shape` controls the trade-off between the two query patterns: larger time chunks favour pixel time-series queries, larger spatial chunks favour date-map queries. As a starting point, pick chunks whose compressed size stays in the hundreds of kilobytes; for example, for a `2592 × 834 × 1115` (time × lat × lon) dataset we use `(41, 105, 140)`. The first element of `chunk_shape` also determines the size of the temporal batches in which the input is processed, so it bounds memory usage during conversion.


## Output structure

For the single-variable example above, the resulting store looks like this:

```
sedi.zarr/
├── .zattrs               ← variables, creation_date, center_lat, center_lon, zoom
├── .zmetadata            ← consolidated metadata (single-request discovery)
└── SEDI/                 ← one group per variable
    ├── .zattrs           ← varTitle, legendTitle, projection, minVal, maxVal
    ├── SEDI/             ← data array (time × y × x), chunked as requested
    ├── SEDI_min/         ← per-date minimum (length T, single chunk)
    ├── SEDI_max/         ← per-date maximum (length T, single chunk)
    ├── time/             ← time coordinate (single chunk)
    ├── y/                ← vertical coordinate
    └── x/                ← horizontal coordinate
```

Dimension names are normalised to `time`, `y`, `x` regardless of the names used in the input files. `varTitle` and `legendTitle` are taken from the `long_name` and `short_name` attributes of the NetCDF variable when present. The time coordinate is stored as a single chunk so a client can fetch the full time axis in one request.


## Repository structure

```
nczarrgenerator/
├── nczarrgenerator/          ← package source (ncs2zarr and helpers)
├── test/                     ← example and test scripts used during development
├── VisorServiciosClimaticos/ ← real-world generation scripts (PTI+ Clima viewers)
├── Visores-LCSC/             ← real-world generation scripts (LCSC viewers)
├── Visores-Clices/           ← real-world generation scripts (CLICES viewers)
├── setup.py                  ← package metadata and dependencies
└── pyproject.toml            ← build system configuration
```

The three `Visores*` directories contain the actual scripts used to generate the Zarr stores behind the operational climate service viewers of our group; they are good references for realistic parameter choices.


## Development

```sh
git clone https://github.com/lcsc/nczarrgenerator.git
cd nczarrgenerator
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
```

To build distributable packages:

```sh
pip install build
python -m build
```


## Related projects

- [`ncartifactgenerator`](https://github.com/lcsc/ncartifactgenerator) — the NetCDF (dual-chunked + binary index) backend of the same workflow, in R.
- [`AnemUI`](https://github.com/lcsc/AnemUI) — the browser-side TypeScript library that consumes either backend.


## License

GPL (≥ 3) — see [LICENSE](LICENSE).


## Author

Eduardo Moreno-Lamana (IPE-CSIC)
