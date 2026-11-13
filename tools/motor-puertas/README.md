<!-- README motor-puertas · v1.0 · 2026-11-13 -->

# Motor de puertas (Python)

Réplica en Python de los backtests de ProRealTime de las puertas A, B, C y D. Es el motor de la Ronda 2 y de la prueba de ETF de Vanguard. Solo usa la librería estándar de Python 3.

Validación: coincide con los informes de ProRealTime (ver `docs/research/RESUMEN_puertas-vanguard.md`). Antes de guardarlo aquí se comparó con los resultados de la Ronda 2: 1.440 filas idénticas.

## Ficheros

| Fichero | Qué hace |
|---|---|
| `motor_puertas.py` | Indicadores, señales, salidas, simulación y métricas |
| `ejecutar.py` | Pasa las puertas por una lista de tickers e imprime los resultados |

## Funciones de cada puerta (en la clase `Valor`)

| Puerta | Función | Qué detecta |
|---|---|---|
| A retroceso | `senal_A()` | Muro semanal + vela de fuerza + toque de la EMA20 o de la línea ATR diaria |
| B giro semanal | `senal_B()` | Giro de la línea ATR semanal ×1,5 con la regla del cuerpo (ADR-0002). Una sola vez |
| C rotura | `senal_C()` | Filtro + vela de fuerza + vela entera sobre el máximo de 20 días + volumen sobre su media |
| D cruce de medias | `senal_D()` | Filtro + cruce al alza de la EMA50 en los últimos 3 días + vela de fuerza sobre la EMA50 |

Filtros comunes: `tendW()` (muro semanal), `filtroMM()` (MM50 semanal subiendo) y `filtro()` (en acciones exige además el muro semanal).

## Salidas

- **a)** la elegida: A = cierre bajo la línea ATR diaria (`sal_linea`); B, C y D = vela entera bajo la EMA50 (`sal_ema50`). Se vende en la apertura siguiente.
- **b)** stop fijo: 2,5 × ATR(14) del día de la señal, mitad a +2R y resto a +3R. Si se tocan stop y objetivo el mismo día, cuenta el stop.

La simulación está en `operaciones(valor, puerta, salida, desde)`. Compra en la apertura del día siguiente a la señal.

## Datos de entrada

Un CSV por ticker, con el nombre `TICKER.csv` (por ejemplo `VGT.csv`):

```
2009-06-01;20.5;21.0;20.3;20.9;1250000
```

- Columnas: `fecha;open;high;low;close;volume`, separadas por `;`.
- Fecha `YYYY-MM-DD`, una fila por sesión diaria.
- Precios ajustados por splits. Revisa saltos raros (pasó con VIOO).
- Mejor con al menos 1 año de historia antes de la primera fecha que quieras medir (la MM50 semanal lo necesita).

## Cómo se ejecuta

```
cd tools/motor-puertas
python3 ejecutar.py --datos /ruta/a/csv --etf VGT VHT IVV --acciones JPM KO
```

| Opción | Uso |
|---|---|
| `--datos` | Carpeta con los CSV (obligatorio) |
| `--etf` | Tickers ETF (`esETF = 1`) |
| `--acciones` | Tickers de acciones (`esETF = 0`) |
| `--puertas` | Por defecto `ABCD`. Ejemplo: `--puertas B` |
| `--salidas` | Por defecto `ab`. Ejemplo: `--salidas a` |
| `--desde` | Primera fecha con señales. Por defecto `2010-01-01` |
| `--csv` | Guarda todas las filas en un CSV |

Sale una fila por ticker, puerta, salida y tramo (T1 = 2010-2022, T2 = 2023 en adelante, Todo). Al final van los totales por grupo, con todas las operaciones sumadas.

## Límites

- 10.000 $ por operación, sin comisiones ni deslizamiento.
- Las operaciones abiertas se valoran al último cierre.
- No incluye las salidas c) y d) ni las salidas 1, 2 y 5 de los `.pts`.
