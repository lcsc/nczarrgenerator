<!--
@name docker spei zarr
@title Docker para generación del zarr de spei
@version 1.0.0
@license GPL version 3 or newer

@author
Manuel Arretxea-Iriarte; Physics of climate and climate change, IGEO, CSIC <https://igeo.ucm-csic.es/>

@description
Docker para generación del zarr de spei

#####################################################################
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/> <http://www.gnu.org/licenses/gpl.txt/>.
#####################################################################
-->

# spei

Generation of the Zarr store behind the [SPEI Global Drought Monitor](https://spei.csic.es/)
viewer. spei is the first LCSC viewer to move from the NetCDF + `.bin` artifacts
(`ncartifactgenerator`) to Zarr.

## Files

- `spei.py` — creates the store, or appends the missing months to an existing one.

## Output

One group per SPEI time scale: `spei01`, `spei03`, `spei06`, `spei09`, `spei12`,
`spei24`, `spei36` and `spei48`. The names match the variable ids used by the viewer.

## Input

The `speiNN.nc` files of the full series, one per time scale:

- variable `spei` (time, lat, lon), float32, 921 × 180 × 360;
- 1° grid (lat -89.5..89.5, lon -179.5..179.5), EPSG:4326, `_FillValue` -1e20;
- time in `days since 1901-01-01 00:00:00` (1950-01 to 2026-09).

## Usage

Requires Python ≥ 3.11 and a virtual environment with `nczarrgenerator` ≥ 1.1.1
(earlier versions store the `<var>_min` and `<var>_max` arrays in several chunks):

```sh
python3 -m venv venv
venv/bin/pip install git+https://github.com/lcsc/nczarrgenerator.git
```

```sh
venv/bin/python spei.py <folder with the speiNN.nc files> <output zarr> [--completo]
```

- **If the store does not exist** (or with `--completo`), it is generated from scratch
  (921 months × 8 time scales).
- **If it exists**, the dates of each `speiNN.nc` are compared with those in the store,
  and only the missing months are appended. This is meant to run every month, after the
  NetCDF files are regenerated. The script stops without modifying the store if:
  - the time units of the `.nc` and the store differ;
  - the 8 time scales do not have the same new months.

  If there are no new months, nothing is done.

The viewer expects the store at the root of its domain (`<domain>/zarr`).

## Chunk shape

`(12, 30, 30)`: a map request downloads 72 chunks (~3.1 MB uncompressed) and a pixel
time series 77 chunks (~3.3 MB). Still to be compared with other shapes, such as
`(41, 90, 90)`.
