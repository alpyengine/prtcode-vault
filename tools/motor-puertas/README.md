<!-- README motor-puertas · v1.1 · 2026-11-13 -->

# Motor de puertas (Python) · v1.1

Réplica en Python de los backtests de ProRealTime de las puertas A, B, C y D. Es el motor de la Ronda 2 y de la prueba de ETF de Vanguard. Solo usa la librería estándar de Python 3.

Validación: coincide con los informes de ProRealTime (ver `docs/research/RESUMEN_puertas-vanguard.md`). Antes de guardarlo aquí se comparó con los resultados de la Ronda 2: 1.440 filas idénticas.

## Ficheros

| Fichero | Qué hace |
|---|---|
| `motor_puertas.py` | Indicadores, señales, salidas, simulación y métricas |
| `ejecutar.py` | Pasa las puertas por una lista de tickers e imprime los resultados |
| `senales_hoy.py` | Dice qué tickers dan señal en una fecha, con cierre, ATR14 y stop |
| `test/` | Un CSV de prueba (VGT) y las salidas esperadas |

Versiones: paquete v1.1 · `motor_puertas.py` v1.0 · `ejecutar.py` v1.0 · `senales_hoy.py` v1.0. La v1.1 añade `senales_hoy.py` y `test/`; las señales y las salidas no cambian.

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

## Señales de hoy

```
python3 senales_hoy.py --datos /ruta/a/csv --etf VGT VHT --acciones JPM
python3 senales_hoy.py --datos /ruta/a/csv --etf VGT --fecha 2026-04-17 --csv hoy.csv
```

- `--fecha`: por defecto, la última sesión de cada CSV. Solo usa los datos hasta esa fecha.
- Salida, una línea por ticker y puerta con señal: `ticker;puerta;fecha;cierre;ATR14;stop`, con stop = cierre − 2,5 × ATR14.
- Si no hay ninguna señal, escribe `Sin senales en la fecha indicada.`
- **Puerta B:** solo se evalúa si la fecha es la última sesión de su semana. Si es la última fila del CSV, solo cuenta si es viernes. La señal sale al cierre de la semana. En el backtest la misma señal aparece el primer día de la semana siguiente y la compra es el día después; si compras el lunes, entras un día antes que en el backtest.
- Las señales de A, C y D son las del cierre de esa fecha. El backtest compra en la apertura siguiente.

**Comprobado contra el backtest** (3 casos de la Ronda 2, salida a):

| Caso | Operaciones del backtest | Señal encontrada por `senales_hoy.py` | Barrido día a día 2025-2026 |
|---|---|---|---|
| B en VGT | 29 | 29 de 29 | Mismas fechas (2) |
| C en JPM | 13 | 13 de 13 | Mismas fechas (2) |
| D en VHT | 39 | 39 de 39 | Mismas fechas (4) |

`senales_hoy.py` puede dar señales que el backtest no usa porque ya está comprado. Es lo esperado: el backtest no acumula posiciones.

## Historia mínima

Sesiones de historia que necesita cada puerta para que sus señales sean idénticas a las calculadas con toda la historia. Medido con 6 valores (VGT, VHT, IVV, JPM, KO, MSFT) y 5 fechas de inicio distintas; se toma el peor caso.

| Puerta | Sesiones medidas (peor caso) | Recomendado |
|---|---|---|
| A retroceso | 262 | 500 (2 años) |
| B giro semanal | 300 | 500 (2 años) |
| C rotura | 246 | 500 (2 años) |
| D cruce de medias | 288 | 500 (2 años) |

- C y D usan la MM50 semanal. No pueden dar ninguna señal hasta tener unas 52 semanas cerradas (unas 255 sesiones). La cifra medida de C (246) es algo menor porque en esos días tampoco había señal con la historia completa.
- Con menos de unas 300 sesiones, las líneas ATR y las medias todavía no coinciden con las de la historia completa.

## Test

Desde `tools/motor-puertas`:

```
diff <(python3 ejecutar.py --datos test --etf VGT) test/esperado_ejecutar.txt && diff <(python3 senales_hoy.py --datos test --etf VGT --fecha 2026-04-17) test/esperado_senales_hoy.txt && echo TEST OK
```

Si todo está bien, solo escribe `TEST OK`. El 17-abr-2026 VGT da señal de las puertas B y C.

## Límites

- 10.000 $ por operación, sin comisiones ni deslizamiento.
- Las operaciones abiertas se valoran al último cierre.
- No incluye las salidas c) y d) ni las salidas 1, 2 y 5 de los `.pts`.
