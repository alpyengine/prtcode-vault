<!-- atr-trailing-vervoort.md · v1.2 · 2026-10-18 -->

# ATR Trailing Vervoort (indicador) — ficha / especificación

| Campo | Valor |
|---|---|
| Plataforma | ProRealTime · Indicador (ProBuilder) |
| Fichero | `indicators/atr-trailing-vervoort/atr-trailing-vervoort.prt` |
| Versión | v1.2 |
| Estado | En validación → `docs/validation/atr-trailing-vervoort/PRT-001.md` |
| Tag | `atr-trailing-vervoort-prt/v1.2.0` |

## Propósito

Ver en el gráfico la misma lógica que `scanner-atr-trailing`:
- Línea diaria Vervoort (naranja).
- Muro semanal Vervoort ×1,5 (rojo).
- Código de señal (1-4) escrito encima de la vela.

Sirve para validar el screener en instrumentos que ProScreener no devuelve con la licencia gratuita (ETF, Nasdaq), y como herramienta de análisis.

## Uso

1. Gráfico **diario**.
2. Crea las 4 variables en la ventana **Variables** del editor, en este orden. Salen en la leyenda entre paréntesis, por ejemplo `(14 2.5 1.5 1)`:

| Variable | Tipo | Valor por defecto | Uso |
|---|---|---|---|
| `atrPer` | Integer | 14 | Periodos del ATR, diario y semanal |
| `multD` | Decimal | 2.5 | Múltiplo diario: 2,5 ETF / 2,0 acción |
| `multW` | Decimal | 1.5 | Múltiplo semanal (el muro) |
| `semanaCerrada` | Integer | 1 | 1 = sábado / 0 = entre semana |

3. Las curvas se llaman "Diaria ATR x multD" (naranja) y "Semanal ATR x multW (muro)" (rojo).

## Vela semanal construida a mano (v1.2)

En el indicador, `TIMEFRAME(weekly)` dejaba de actualizar la semana en curso en las últimas sesiones (ver `docs/prt-rules.md`, regla IND). La v1.2 no usa `TIMEFRAME`: detecta el cambio de semana (`DayOfWeek` baja) y acumula apertura, máximo, mínimo y cierre semanales a partir de las velas diarias. El ATR semanal es Wilder, arrancado con la media simple de las primeras `atrPer` semanas.

Simulado con datos semanales reales: da los mismos muros que el cálculo de referencia (VGT 127,34 · SCHD 33,10 · VDC 226,39 · KO 88,79 · JPM 354,02 · XOM 165,81).

## Comparación con el "ATR Trailing Stop" de ProRealTime

- Semanal ×1,5: coincide en todo el historial. En la última semana, el de ProRealTime pinta todavía el muro anterior y enseña el nuevo como nivel horizontal discontinuo.
- Diario: coincide solo si `multD` es igual. El de ProRealTime estaba en ×2 y este en ×2,5 (ETF).

## Relación con el screener

- La lógica es la del screener v1.2. El screener sigue usando `TIMEFRAME(weekly)`, porque ahí sí ve la semana completa. ProBuilder no tiene librerías, así que hay que mantener los dos a mano.
- No calcula las columnas del screener (Dist52W, Stop): ProRealTime da error si una variable se calcula y no se usa.

## Limitación

En el historial, el muro y las señales semanales (1 y 4) se recalculan cada día con la semana en curso. Por eso pueden aparecer a mitad de semana. Lo que vale es el valor del último día de cada semana.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| v1.0 | 2026-10-18 | Primera versión, lógica del screener v1.1 |
| v1.1 | 2026-10-18 | Señal 1 con confirmación la semana siguiente (ADR-0002) |
| v1.2 | 2026-10-18 | Vela semanal construida con velas diarias; parámetros como variables visibles en la leyenda |
