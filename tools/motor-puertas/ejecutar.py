"""Ejecutar motor de puertas - v1.0 (13-nov-2026)

Pasa las puertas A, B, C y D (salidas a y b) por una lista de tickers y
muestra las metricas por ticker y por grupo (todas las operaciones sumadas).

Ejemplo:
  python3 ejecutar.py --datos datos/ --etf VGT VHT IVV --acciones JPM KO
  python3 ejecutar.py --datos datos/ --etf VGT --puertas B --salidas a --csv salida.csv
"""
import argparse
import csv
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motor_puertas import Valor, operaciones, metricas, tramo, ruta_ticker, __version__

TRAMOS = {'T1': ('2010-01-01', '2022-12-31'), 'T2': ('2023-01-01', '2099-12-31'), 'Todo': ('2010-01-01', '2099-12-31')}


def pct(x):
    return f'{x * 100:6.1f}%'


def main():
    ap = argparse.ArgumentParser(description=f'Motor de puertas v{__version__}')
    ap.add_argument('--datos', required=True, help='carpeta con un CSV por ticker (TICKER.csv)')
    ap.add_argument('--etf', nargs='*', default=[], help='tickers ETF (esETF = 1)')
    ap.add_argument('--acciones', nargs='*', default=[], help='tickers de acciones (esETF = 0)')
    ap.add_argument('--puertas', default='ABCD')
    ap.add_argument('--salidas', default='ab')
    ap.add_argument('--desde', default='2010-01-01', help='primera fecha en la que se aceptan senales')
    ap.add_argument('--csv', help='guardar todas las filas en este CSV')
    a = ap.parse_args()

    grupos = [('ETF', a.etf, 1), ('Acciones', a.acciones, 0)]
    filas = []
    acum = {}
    for gname, tks, es_etf in grupos:
        for t in tks:
            ruta = ruta_ticker(a.datos, t)
            if not os.path.exists(ruta):
                print(f'AVISO: falta {ruta}; se omite {t}')
                continue
            V = Valor(ruta, es_etf)
            for p in a.puertas:
                for s in a.salidas:
                    T, enpos = operaciones(V, p, s, a.desde)
                    for tn, (d1, d2) in TRAMOS.items():
                        rets, tiempo = tramo(V, T, enpos, d1, d2)
                        m = metricas(rets, tiempo)
                        filas.append(dict(grupo=gname, ticker=t, puerta=p, salida=s, tramo=tn, **m))
                        k = (gname, p, s, tn)
                        acum.setdefault(k, ([], []))
                        acum[k][0].extend(rets); acum[k][1].append(tiempo)

    print(f'Motor de puertas v{__version__} - 10.000 $ por operacion, sin comisiones')
    print(f"{'grupo':9}{'ticker':8}{'pta':4}{'sal':4}{'tramo':6}{'ops':>5}{'%gan':>8}{'ratio':>7}{'media':>8}{'peor':>8}{'tiempo':>8}")
    for f in filas:
        print(f"{f['grupo']:9}{f['ticker']:8}{f['puerta']:4}{f['salida']:4}{f['tramo']:6}{f['ops']:5d}{pct(f['pct_gan']):>8}"
              f"{f['ratio']:7.2f}{pct(f['media']):>8}{pct(f['peor']):>8}{pct(f['tiempo']):>8}")
    print('\nPor grupo (todas las operaciones sumadas):')
    for (gname, p, s, tn), (rets, tims) in acum.items():
        m = metricas(rets, sum(tims) / len(tims))
        print(f"{gname:9}{'-':8}{p:4}{s:4}{tn:6}{m['ops']:5d}{pct(m['pct_gan']):>8}{m['ratio']:7.2f}"
              f"{pct(m['media']):>8}{pct(m['peor']):>8}{pct(m['tiempo']):>8}")

    if a.csv:
        with open(a.csv, 'w', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=list(filas[0].keys()), delimiter=';')
            w.writeheader(); w.writerows(filas)
        print(f'\nGuardado: {a.csv}')


if __name__ == '__main__':
    main()
