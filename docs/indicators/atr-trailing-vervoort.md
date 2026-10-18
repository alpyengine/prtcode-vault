<!-- atr-trailing-vervoort.md · v1.1 · 2026-10-18 -->

# ATR Trailing Vervoort (indicador) — ficha / especificación

| Campo | Valor |
|---|---|
| Plataforma | ProRealTime · Indicador (ProBuilder) |
| Fichero | `indicators/atr-trailing-vervoort/atr-trailing-vervoort.prt` |
| Versión | v1.1 |
| Estado | En validación → `docs/validation/atr-trailing-vervoort/PRT-001.md` |
| Tag | `atr-trailing-vervoort-prt/v1.1.0` |

## Propósito

Ver en el gráfico la misma lógica que `scanner-atr-trailing`:
- Línea diaria Vervoort (naranja).
- Muro semanal Vervoort ×1,5 (rojo).
- Código de señal (1-4) escrito encima de la vela.

Sirve para validar el screener en instrumentos que ProScreener no devuelve con la licencia gratuita (ETF, Nasdaq), y como herramienta de análisis.

## Uso

1. Gráfico **diario**.
2. `isETF = 1` en ETF, `0` en acciones.
3. `semanaCerrada = 1` el sábado.

## Relación con el screener

- El bloque de cálculo es una copia del screener v1.2. ProBuilder no tiene librerías, así que hay que mantener los dos a mano.
- No calcula las columnas del screener (Dist52W, Stop): ProRealTime da error si una variable se calcula y no se usa.

## Limitación

En el historial, las señales semanales (1 y 4) pueden aparecer a mitad de semana, porque el muro se recalcula con la vela semanal en curso. Lo fiable es la última vela con la semana cerrada.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| v1.0 | 2026-10-18 | Primera versión, lógica del screener v1.1 |
| v1.1 | 2026-10-18 | Señal 1 con confirmación la semana siguiente (ADR-0002) |
