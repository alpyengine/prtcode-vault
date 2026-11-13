"""Motor de puertas Vanguard - v1.0 (13-nov-2026)

Replica en Python de los backtests de ProRealTime de las puertas A, B, C y D
(puerta-*-backtest.pts) y de dos salidas:
  a) la salida elegida de cada puerta (A: cierre bajo la linea ATR diaria;
     B, C y D: vela entera bajo la EMA50)
  b) stop fijo: 2,5 x ATR(14) del dia de la senal, mitad a +2R, resto a +3R

Es el motor usado en la Ronda 2 y en la prueba de ETF de Vanguard.
Validado contra informes de ProRealTime (ver RESUMEN_puertas-vanguard.md).

Solo usa la libreria estandar de Python 3.
"""
import datetime as dt
import os

__version__ = '1.0'


# ---------------------------------------------------------------- datos
def cargar(ruta_csv, desde=None):
    """Lee un CSV 'fecha;open;high;low;close;volume', sin cabecera, fechas
    YYYY-MM-DD en orden ascendente. Devuelve listas d, o, h, l, c, v."""
    filas = [x.strip().split(';') for x in open(ruta_csv) if x.strip()]
    if filas and not filas[0][0][:1].isdigit():      # admite cabecera
        filas = filas[1:]
    if desde:
        filas = [f for f in filas if f[0] >= desde]
    filas.sort(key=lambda f: f[0])
    d = [f[0][:10] for f in filas]
    o, h, l, c, v = ([float(f[k]) for f in filas] for k in (1, 2, 3, 4, 5))
    return d, o, h, l, c, v


# ---------------------------------------------------------------- indicadores
def ema(c, n):
    a = 2.0 / (n + 1)
    e = [c[0]]
    for x in c[1:]:
        e.append(e[-1] + a * (x - e[-1]))
    return e


def sma(c, n):
    out = [0.0] * len(c)
    s = 0.0
    for i, x in enumerate(c):
        s += x
        if i >= n:
            s -= c[i - n]
        out[i] = s / n if i >= n - 1 else 0.0
    return out


def atr(h, l, c, n=14):
    """ATR de Wilder."""
    tr = [h[0] - l[0]] + [max(h[i] - l[i], abs(h[i] - c[i - 1]), abs(l[i] - c[i - 1])) for i in range(1, len(c))]
    a = [0.0] * len(c)
    if len(c) >= n:
        a[n - 1] = sum(tr[:n]) / n
        for i in range(n, len(c)):
            a[i] = (a[i - 1] * (n - 1) + tr[i]) / n
    return a


def linea_atr(h, l, c, m, n=14):
    """Linea Vervoort de ATR x m con trinquete (igual que en los .pts)."""
    a = atr(h, l, c, n)
    ln = [c[0]]
    for i in range(1, len(c)):
        p = ln[-1]
        if c[i] > p and c[i - 1] > p:
            ln.append(max(p, c[i] - m * a[i]))
        elif c[i] < p and c[i - 1] < p:
            ln.append(min(p, c[i] + m * a[i]))
        elif c[i] > p:
            ln.append(c[i] - m * a[i])
        else:
            ln.append(c[i] + m * a[i])
    return ln


def _lunes(s):
    x = dt.date.fromisoformat(s)
    return (x - dt.timedelta(days=x.weekday())).isoformat()


def semanal(d, o, h, l, c):
    W = {}
    for i in range(len(d)):
        k = _lunes(d[i])
        if k not in W:
            W[k] = [o[i], h[i], l[i], c[i]]
        else:
            w = W[k]
            w[1] = max(w[1], h[i]); w[2] = min(w[2], l[i]); w[3] = c[i]
    ks = sorted(W)
    return ks, [[W[k][j] for k in ks] for j in range(4)]


# ---------------------------------------------------------------- valor
class Valor:
    """Datos de un ticker y todos los indicadores que usan las puertas.

    es_etf = 1 -> ETF (linea ATR diaria x2,5; filtro solo MM50 semanal)
    es_etf = 0 -> accion (linea diaria x2; el filtro exige ademas el muro semanal)
    Los valores semanales son siempre los de la ultima semana CERRADA."""

    def __init__(s, ruta_csv, es_etf, desde=None):
        s.d, s.o, s.h, s.l, s.c, s.v = cargar(ruta_csv, desde)
        n = s.n = len(s.d)
        ks, (wo, wh, wl, wc) = semanal(s.d, s.o, s.h, s.l, s.c)
        wi = {k: i for i, k in enumerate(ks)}
        lineW = linea_atr(wh, wl, wc, 1.5)
        mm = sma(wc, 50)
        k = [wi[_lunes(x)] for x in s.d]
        g = lambda arr, off: [arr[kk - off] if kk - off >= 0 else 0.0 for kk in k]
        s.wkClose, s.wkLine, s.wkMM, s.wkMMprev = g(wc, 1), g(lineW, 1), g(mm, 1), g(mm, 2)
        s.wkBodyLow = [min(wo[kk - 1], wc[kk - 1]) if kk >= 1 else 0.0 for kk in k]
        s.wkPrevClose, s.wkPrevLine = g(wc, 2), g(lineW, 2)
        s.wkOldClose, s.wkOldLine = g(wc, 3), g(lineW, 3)
        s.es_etf = es_etf
        s.multD = 2.5 if es_etf else 2.0
        s.atrD = atr(s.h, s.l, s.c)
        s.lvlD = [0.0] + linea_atr(s.h, s.l, s.c, s.multD)[:-1]   # lineD[1]
        s.e20, s.e50 = ema(s.c, 20), ema(s.c, 50)
        s.fuerza = [i > 0 and s.c[i] > s.o[i] and s.c[i] > s.h[i - 1] for i in range(n)]

    # --- filtros
    def tendW(s, i):
        """Muro semanal: cierre semanal y precio actual sobre la linea semanal x1,5."""
        return s.wkClose[i] > s.wkLine[i] and s.c[i] > s.wkLine[i]

    def filtroMM(s, i):
        """Cierre semanal sobre la MM50 semanal y MM50 subiendo."""
        return s.wkClose[i] > s.wkMM[i] and s.wkMM[i] > s.wkMMprev[i] and s.wkMMprev[i] > 0

    def filtro(s, i):
        return s.filtroMM(i) and (s.es_etf == 1 or s.tendW(i))

    # --- senales (lista de True/False, una por dia)
    def senal_A(s):
        """Retroceso: muro semanal + vela de fuerza + toque de EMA20 o de la linea ATR diaria."""
        out = [False] * s.n
        for i in range(2, s.n):
            tE = s.c[i - 1] > s.e20[i - 1] and s.l[i] <= s.e20[i] and s.c[i] > s.e20[i]
            lv = s.lvlD[i]
            tL = lv > 0 and s.c[i - 1] > lv and s.l[i] <= lv and s.c[i] > lv
            out[i] = s.tendW(i) and s.fuerza[i] and (tE or tL)
        return out

    def senal_B(s):
        """Giro semanal (ADR-0002): una sola vez, el primer dia de la semana siguiente."""
        sb = [s.wkOldLine[i] != 0 and s.wkOldClose[i] <= s.wkOldLine[i] and s.wkPrevClose[i] > s.wkPrevLine[i]
              and s.wkClose[i] > s.wkLine[i] and s.wkBodyLow[i] > s.wkOldLine[i] for i in range(s.n)]
        return [sb[i] and not (i > 0 and sb[i - 1]) for i in range(s.n)]

    def senal_C(s):
        """Rotura: filtro + vela de fuerza + vela entera sobre el maximo de 20 dias + volumen > media 20."""
        out = [False] * s.n
        va = sma(s.v, 20)
        for i in range(21, s.n):
            mx = max(s.h[i - 20:i])
            out[i] = s.filtro(i) and s.fuerza[i] and s.c[i] > mx and s.l[i] > mx and s.v[i] > va[i - 1]
        return out

    def senal_D(s):
        """Cruce de medias: cruce al alza de la EMA50 en los ultimos 3 dias + vela de fuerza
        entera sobre la EMA50, una vez por cruce."""
        out = [False] * s.n
        d50, hecho = 99, 0
        for i in range(s.n):
            if i > 0 and s.c[i] > s.e50[i] and s.c[i - 1] <= s.e50[i - 1]:
                d50, hecho = 0, 0
            else:
                d50 += 1
            ok = d50 < 3 and hecho == 0 and s.fuerza[i] and s.l[i] > s.e50[i]
            if ok:
                hecho = 1
            out[i] = s.filtro(i) and ok
        return out

    # --- salidas a) (evaluadas al cierre; se vende en la apertura siguiente)
    def sal_linea(s, i):
        return s.lvlD[i] > 0 and s.c[i] < s.lvlD[i]

    def sal_ema50(s, i):
        return s.h[i] < s.e50[i]


SENAL = {'A': 'senal_A', 'B': 'senal_B', 'C': 'senal_C', 'D': 'senal_D'}
SALIDA_A = {'A': 'sal_linea', 'B': 'sal_ema50', 'C': 'sal_ema50', 'D': 'sal_ema50'}


# ---------------------------------------------------------------- simulacion
def operaciones(V, puerta, salida='a', desde='2010-01-01'):
    """Simula una puerta sobre un Valor. Compra en la apertura siguiente a la senal.
    salida 'a' = salida elegida; 'b' = stop fijo (si se tocan stop y objetivo el
    mismo dia, cuenta el stop; los huecos se ejecutan a la apertura).
    Devuelve (lista de operaciones, lista de dias en posicion).
    Cada operacion: d0 entrada, d1 salida, ep precio de entrada, ret rentabilidad
    (0,05 = +5 %), abierta=True si sigue abierta (valorada al ultimo cierre)."""
    sig = getattr(V, SENAL[puerta])()
    ex = getattr(V, SALIDA_A[puerta])
    n = V.n
    T = []; pos = False; pend = None; tr = None
    enpos = [False] * n
    for i in range(n):
        if pend == 'buy':
            pos = True; pend = None
            ep = V.o[i]
            tr = dict(d0=V.d[i], ep=ep)
            if salida == 'b':
                R = 2.5 * V.atrD[i - 1]
                tr.update(stop=ep - R, t2=ep + 2 * R, t3=ep + 3 * R, half=False, rem=1.0, acc=0.0)
        elif pend == 'sell':
            tr.update(d1=V.d[i], ret=V.o[i] / tr['ep'] - 1)
            T.append(tr); pos = False; pend = None; tr = None
        if pos:
            enpos[i] = True
            if salida == 'b':
                o, h, l = V.o[i], V.h[i], V.l[i]
                fin = False
                if o <= tr['stop']:
                    tr['acc'] += tr['rem'] * (o / tr['ep'] - 1); fin = True
                elif l <= tr['stop']:
                    tr['acc'] += tr['rem'] * (tr['stop'] / tr['ep'] - 1); fin = True
                else:
                    if not tr['half'] and h >= tr['t2']:
                        p = max(o, tr['t2'])
                        tr['acc'] += 0.5 * (p / tr['ep'] - 1); tr['rem'] -= 0.5; tr['half'] = True
                    if h >= tr['t3']:
                        p = max(o, tr['t3'])
                        tr['acc'] += tr['rem'] * (p / tr['ep'] - 1); fin = True
                if fin:
                    tr.update(d1=V.d[i], ret=tr['acc'])
                    T.append(tr); pos = False; tr = None
                continue
        if V.d[i] < desde:
            continue
        if not pos and pend is None and sig[i] and i + 1 < n:
            pend = 'buy'
        elif pos and salida == 'a' and pend is None and ex(i):
            pend = 'sell'
    if pos and tr is not None:
        r = V.c[-1] / tr['ep'] - 1
        if salida == 'b':
            r = tr['acc'] + tr['rem'] * r
        tr.update(d1=V.d[-1], ret=r, abierta=True)
        T.append(tr)
    return T, enpos


def metricas(rets, tiempo=None):
    """Metricas de una lista de rentabilidades (10.000 $ fijos por operacion,
    sin comisiones). ratio = suma de ganancias / suma de perdidas."""
    n = len(rets)
    if n == 0:
        return dict(ops=0, pct_gan=0, gan_media=0, perd_media=0, ratio=0, media=0, peor=0, tiempo=tiempo)
    gp = [x for x in rets if x > 0]; lp = [x for x in rets if x < 0]
    return dict(ops=n, pct_gan=len(gp) / n,
                gan_media=sum(gp) / len(gp) if gp else 0, perd_media=sum(lp) / len(lp) if lp else 0,
                ratio=(sum(gp) / -sum(lp)) if lp else float('inf'),
                media=sum(rets) / n, peor=min(rets), tiempo=tiempo)


def tramo(V, T, enpos, desde, hasta):
    """Operaciones que ENTRAN en [desde, hasta] y fraccion de sesiones en posicion."""
    rets = [t['ret'] for t in T if desde <= t['d0'] <= hasta]
    idx = [i for i in range(V.n) if desde <= V.d[i] <= hasta]
    tiempo = sum(enpos[i] for i in idx) / len(idx) if idx else 0.0
    return rets, tiempo


def ruta_ticker(carpeta, ticker):
    return os.path.join(carpeta, ticker + '.csv')
