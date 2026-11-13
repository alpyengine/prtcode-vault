"""Senales de hoy - v1.0 (13-nov-2026)

Dice que tickers dan senal de las puertas A, B, C o D en una fecha, usando solo
los datos hasta esa fecha (sin mirar el futuro). Usa las mismas funciones de
senal que motor_puertas.py; no las modifica.

Salida: ticker;puerta;fecha;cierre;ATR14;stop   (stop = cierre - 2,5 x ATR14)

Puerta B: solo se evalua si la fecha es la ultima sesion de su semana. La senal
se da al cierre de esa semana. (En el backtest, la misma senal aparece el primer
dia de la semana siguiente y la compra es al dia siguiente de ese dia.)

Ejemplo:
  python3 senales_hoy.py --datos datos/ --etf VGT VHT --acciones JPM
  python3 senales_hoy.py --datos datos/ --etf VGT --fecha 2026-10-27 --csv hoy.csv
"""
import argparse
import datetime as dt
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motor_puertas import Valor, cargar, semanal, linea_atr, ruta_ticker, SENAL

VERSION = '1.0'
CABECERA = 'ticker;puerta;fecha;cierre;ATR14;stop'


def _semana(fecha):
    return dt.date.fromisoformat(fecha).isocalendar()[:2]


def ultima_de_semana(fechas, i):
    """True si la sesion i es la ultima de su semana. Si es la ultima fila del
    CSV, solo se acepta si es viernes (la semana no se da por cerrada antes)."""
    if i + 1 < len(fechas):
        return _semana(fechas[i + 1]) != _semana(fechas[i])
    return dt.date.fromisoformat(fechas[i]).weekday() == 4


def senal_B_cierre_semana(V):
    """Condicion de la puerta B con la semana que termina en la ultima fila de V.
    Misma regla que Valor.senal_B (ADR-0002), pero con la semana actual ya cerrada:
    B = cond(semana actual) y no cond(semana anterior)."""
    ks, (wo, wh, wl, wc) = semanal(V.d, V.o, V.h, V.l, V.c)
    ln = linea_atr(wh, wl, wc, 1.5)

    def cond(w):
        if w - 2 < 0 or ln[w - 2] == 0:
            return False
        return (wc[w - 2] <= ln[w - 2] and wc[w - 1] > ln[w - 1] and wc[w] > ln[w]
                and min(wo[w], wc[w]) > ln[w - 2])
    k = len(ks) - 1
    return cond(k) and not cond(k - 1)


def valor_hasta(ruta, es_etf, fecha):
    """Carga el ticker solo con las sesiones <= fecha (copia temporal del CSV)."""
    d, o, h, l, c, v = cargar(ruta)
    n = sum(1 for x in d if x <= fecha)
    if n == 0:
        return None
    with tempfile.NamedTemporaryFile('w', suffix='.csv', delete=False) as fh:
        for i in range(n):
            fh.write(f'{d[i]};{o[i]};{h[i]};{l[i]};{c[i]};{v[i]}\n')
        tmp = fh.name
    try:
        return Valor(tmp, es_etf)
    finally:
        os.remove(tmp)


def senales(ruta, es_etf, fecha=None, puertas='ABCD'):
    """Devuelve (fecha usada, lista de filas [puerta, cierre, atr, stop]) o (None, aviso)."""
    d = cargar(ruta)[0]
    if not d:
        return None, 'CSV vacio'
    fecha = fecha or d[-1]
    if fecha not in d:
        return None, f'sin sesion el {fecha}'
    V = valor_hasta(ruta, es_etf, fecha)
    i = V.n - 1
    out = []
    for p in puertas:
        if p == 'B':
            if not ultima_de_semana(d, d.index(fecha)):
                continue
            ok = senal_B_cierre_semana(V)
        else:
            ok = getattr(V, SENAL[p])()[i]
        if ok:
            c, a = V.c[i], V.atrD[i]
            out.append([p, c, a, c - 2.5 * a])
    return fecha, out


def main():
    ap = argparse.ArgumentParser(description=f'Senales de hoy v{VERSION}')
    ap.add_argument('--datos', required=True, help='carpeta con un CSV por ticker (TICKER.csv)')
    ap.add_argument('--etf', nargs='*', default=[], help='tickers ETF (esETF = 1)')
    ap.add_argument('--acciones', nargs='*', default=[], help='tickers de acciones (esETF = 0)')
    ap.add_argument('--fecha', help='YYYY-MM-DD; por defecto la ultima sesion de cada CSV')
    ap.add_argument('--puertas', default='ABCD')
    ap.add_argument('--csv', help='guardar las senales en este CSV')
    a = ap.parse_args()

    filas = []
    for tks, es_etf in ((a.etf, 1), (a.acciones, 0)):
        for t in tks:
            ruta = ruta_ticker(a.datos, t)
            if not os.path.exists(ruta):
                print(f'AVISO: falta {ruta}; se omite {t}')
                continue
            fecha, res = senales(ruta, es_etf, a.fecha, a.puertas)
            if fecha is None:
                print(f'AVISO: {t}: {res}')
                continue
            for p, c, atr14, stop in res:
                filas.append(f'{t};{p};{fecha};{c:.2f};{atr14:.2f};{stop:.2f}')

    if filas:
        print(CABECERA)
        print('\n'.join(filas))
    else:
        print('Sin senales en la fecha indicada.')
    if a.csv:
        with open(a.csv, 'w') as fh:
            fh.write(CABECERA + '\n' + ''.join(f + '\n' for f in filas))
        print(f'Guardado: {a.csv}')


if __name__ == '__main__':
    main()
