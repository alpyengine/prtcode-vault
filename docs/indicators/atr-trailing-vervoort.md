<!-- atr-trailing-vervoort.md · v1.6 · 2026-10-18 -->

# ATR Trailing Vervoort (indicador) — ficha / especificación

| Campo | Valor |
|---|---|
| Plataforma | ProRealTime · Indicador (ProBuilder) |
| Fichero | `indicators/atr-trailing-vervoort/atr-trailing-vervoort.prt` |
| Versión | v1.6 |
| Estado | En validación → `docs/validation/atr-trailing-vervoort/PRT-001.md` |
| Tag | `atr-trailing-vervoort-prt/v1.6.0` |

## Propósito

Ver en el gráfico la misma lógica que `scanner-atr-trailing`:
- Línea diaria Vervoort (naranja).
- Muro semanal Vervoort ×1,5 (rojo).
- Código de señal (1-4) escrito encima de la vela.

Sirve para validar el screener en instrumentos que ProScreener no devuelve con la licencia gratuita (ETF, Nasdaq), y como herramienta de análisis.

## Uso

1. Gráfico **diario**.
2. Crea las 5 variables en la ventana **Variables** del editor, en este orden. Salen en la leyenda entre paréntesis, por ejemplo `(14 2.5 1.5 1 0)`. La **descripción** es el texto que verás en la pantalla de configuración; sirve de recordatorio:

| Variable | Tipo | Valor | Descripción (copiar tal cual) |
|---|---|---|---|
| `atrPer` | Integer | 14 | ATR periodos, diario y semanal |
| `multD` | Decimal | 2.5 | Multiplo diario. 2.5 ETF, 2.0 accion |
| `multW` | Decimal | 1.5 | Multiplo semanal, el muro |
| `semanaCerrada` | Integer | 1 | 1 sabado, 0 entre semana |
| `verLeyenda` | Boolean | 0 | Leyenda. 1 giro, 2 pullback, 3 ruptura, 4 perdida muro |

3. La zona entre las dos líneas sale verde con el precio sobre el muro y roja con el precio debajo. Si tenías zonas en la pestaña **Color zones**, quítalas para no duplicar.
4. Las curvas se llaman "Diaria ATR x multD" (naranja) y "Semanal ATR x multW (muro)" (rojo).

## Vela semanal construida a mano (v1.2)

En el indicador, `TIMEFRAME(weekly)` dejaba de actualizar la semana en curso en las últimas sesiones (ver `docs/prt-rules.md`, regla IND). La v1.2 no usa `TIMEFRAME`: detecta el cambio de semana (`DayOfWeek` baja) y acumula apertura, máximo, mínimo y cierre semanales a partir de las velas diarias. El ATR semanal es Wilder, arrancado con la media simple de las primeras `atrPer` semanas.

Simulado con datos semanales reales: da los mismos muros que el cálculo de referencia (VGT 127,34 · SCHD 33,10 · VDC 226,39 · KO 88,79 · JPM 354,02 · XOM 165,81).

## Comparación con el "ATR Trailing Stop" de ProRealTime

- Semanal ×1,5: coincide en todo el historial. En la última semana, el de ProRealTime pinta todavía el muro anterior y enseña el nuevo como nivel horizontal discontinuo.
- Diario: coincide solo si `multD` es igual. El de ProRealTime estaba en ×2 y este en ×2,5 (ETF).

## Relación con el screener

- La lógica es la del screener v1.2. El screener sigue usando `TIMEFRAME(weekly)`, porque ahí sí ve la semana completa. ProBuilder no tiene librerías, así que hay que mantener los dos a mano.
- No calcula las columnas del screener (Dist52W, Stop): ProRealTime da error si una variable se calcula y no se usa.

## Qué significan los números azules

Encima de cada vela sale el código de las señales activas ese día: 1 giro semanal confirmado, 2 pullback, 3 ruptura, 4 pérdida del muro. Si hay varias, salen juntas (por ejemplo 23). Sin señal no sale nada: el 0 no se pinta, a propósito, para no llenar el gráfico.

El recordatorio está en la descripción de `verLeyenda`, en la configuración del indicador. Si la marcas, también sale en el gráfico, abajo a la izquierda.

Huecos sin números: el precio está por debajo del muro (2 y 3 exigen muro en soporte), o se ha alejado más de 1 ATR de la MM10, de la MM20 y de la línea diaria, y no hay ruptura.

Con `semanaCerrada = 0`, las señales semanales (1 y 4) se leen de la última semana cerrada. Por eso salen una semana más tarde: el 1 del 13-abr-2026 de VGT aparece en la semana del 20-abr (comprobado en ProRealTime).

## Limitación

En el historial, el muro y las señales semanales (1 y 4) se recalculan cada día con la semana en curso. Por eso pueden aparecer a mitad de semana. Lo que vale es el valor del último día de cada semana.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| v1.0 | 2026-10-18 | Primera versión, lógica del screener v1.1 |
| v1.1 | 2026-10-18 | Señal 1 con confirmación la semana siguiente (ADR-0002) |
| v1.2 | 2026-10-18 | Vela semanal construida con velas diarias; parámetros como variables visibles en la leyenda |
| v1.3 | 2026-10-18 | Zona coloreada entre las dos líneas con `COLORBETWEEN` |
| v1.4 | 2026-10-18 | Leyenda de señales fija en el gráfico (`DRAWTEXT` con `ANCHOR`). No compila |
| v1.5 | 2026-10-18 | Leyenda sin símbolos (`\|`, `:`, `(`, `)`, `+`, `=`) ni parámetros de fuente |
| v1.6 | 2026-10-18 | Una sola `COLORBETWEEN` por vela con color en variables (la v1.5 dejaba bandas planas). Leyenda opcional con la variable `verLeyenda` |
