import os
import sys
import argparse
import tempfile
import warnings
import numpy as np
import xarray as xr
from nczarrgenerator import ncs2zarr

warnings.filterwarnings('ignore')

# Generación del zarr de spei (The zarr way), una variable por escala del mapa.
# Origen: serie completa de los speiNN.nc (la que se sirve en nc/full/).
# Destino: <carpeta del visor>/zarr. Ver README.md.
#
# Uso: python spei.py <carpeta de los speiNN.nc> <zarr de salida> [--completo]
# Si el zarr ya existe, solo añade los meses de los .nc que aún no tiene (actualización
# mensual, al final de la generación de los NetCDF); si no existe o con --completo, lo
# genera entero.
#
# Los speiNN.nc: variable 'spei' (time, lat, lon), float32, 921 x 180 x 360,
# rejilla de 1° (lat -89.5..89.5, lon -179.5..179.5), _FillValue -1e20,
# time en 'days since 1901-01-01 00:00:00' (de 1950-01 a 2026-09).

parser = argparse.ArgumentParser(description='Genera el zarr de spei a partir de los speiNN.nc')
parser.add_argument('nc_dir', help='carpeta de los speiNN.nc (serie completa)')
parser.add_argument('zarr_path', help='zarr de salida (junto al visor, p. ej. <visor>/zarr)')
parser.add_argument('--completo', action='store_true',
                    help='regenera el zarr entero aunque ya exista')
args = parser.parse_args()
NC_DIR = args.nc_dir
ZARR_PATH = args.zarr_path

# Escalas del selector "SPEI Time-scale" (SPEI_TIME_SCALES en spei/src/SpeiService.ts).
# El nombre de cada variable del zarr ('speiNN') es el varId que usa el visor (speiVarId).
TIME_SCALES = ['01', '03', '06', '09', '12', '24', '36', '48']

# Chunk (time, lat, lon). Un mapa lee un mes entero y un gráfico la serie de un píxel:
# con (12, 30, 30) cada mapa descarga 72 chunks (~3,1 MB sin comprimir, 12 meses de más)
# y cada serie 77 chunks (~3,3 MB). Por medir en local junto con otras opciones,
# por ejemplo (41, 90, 90) como en ETo: 8 chunks por mapa (~10,6 MB) y 23 por serie (~30 MB).
CHUNK_SHAPE = (12, 30, 30)

def nc_info(path, i, scale):
    return {
        'path': [path],
        'nc_var': 'spei',
        'var': f'spei{scale}',
        'time_dim': 'time',
        'ver_dim': 'lat',
        'hor_dim': 'lon',
        'nc_projection': 'EPSG:4326',
        'calc_min_max': True,
        'include_center_calc': i == 0,  # el centro del mapa basta calcularlo una vez
        'chunk_shape': CHUNK_SHAPE,
    }


if args.completo or not os.path.exists(ZARR_PATH):
    ncs2zarr([nc_info(os.path.join(NC_DIR, f'spei{s}.nc'), i, s) for i, s in enumerate(TIME_SCALES)],
             ZARR_PATH, beginning=True)
else:
    # El proceso mensual rehace los speiNN.nc con la serie completa: se pasan a
    # nczarrgenerator solo los meses que faltan en el zarr, porque los que ya están
    # los reescribiría uno a uno. Las fechas se comparan sin decodificar, así que
    # las unidades tienen que coincidir.
    with tempfile.TemporaryDirectory() as tmp:
        netcdfs, nuevos_por_escala = [], {}
        for i, scale in enumerate(TIME_SCALES):
            var = f'spei{scale}'
            ds = xr.open_dataset(os.path.join(NC_DIR, f'{var}.nc'), decode_times=False)
            zt = xr.open_zarr(ZARR_PATH, group=var, decode_times=False, consolidated=True)['time']
            if ds['time'].attrs.get('units') != zt.attrs.get('units'):
                sys.exit(f'{var}: unidades de tiempo distintas en el .nc '
                         f'({ds["time"].attrs.get("units")}) y en el zarr ({zt.attrs.get("units")})')
            nuevos = ds.isel(time=~np.isin(ds['time'].values, zt.values))
            nuevos_por_escala[var] = tuple(nuevos['time'].values)
            if nuevos.sizes['time']:  # netCDF4 no escribe un .nc sin fechas
                path = os.path.join(tmp, f'{var}.nc')
                nuevos.to_netcdf(path)
                netcdfs.append(nc_info(path, i, scale))
            ds.close()

        meses = set(nuevos_por_escala.values())
        if len(meses) > 1:
            # Se actualizan todas las escalas a la vez: ncs2zarr rehace la lista de
            # variables de la raíz con las que recibe
            sys.exit(f'Las escalas no tienen los mismos meses nuevos: {nuevos_por_escala}')
        if not next(iter(meses)):
            print('El zarr ya tiene todos los meses de los .nc; no hay nada que añadir.')
            sys.exit(0)
        print(f'Meses nuevos (days since 1901-01-01): {list(next(iter(meses)))}')
        ncs2zarr(netcdfs, ZARR_PATH, beginning=False)
