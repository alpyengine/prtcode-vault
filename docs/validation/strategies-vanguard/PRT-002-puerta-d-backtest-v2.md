<!-- PRT-002 · v1.0 · 2026-11-09 -->

# PRT-002 — Validación puerta-d-backtest v2

- **Script:** `strategies/strategies-vanguard/puerta-d-backtest.pts` (v2)
- **Módulo:** ProBacktest · gráfico diario
- **Señal:** igual que el scanner puerta D v1.3 (solo EMA50, ventana de 3 sesiones)
- **Estado:** APROBADA como herramienta de estudio

## Nivel 1 — Compilación

| Resultado | Fecha | Nota |
|---|---|---|
| ✅ | 2026-11-08 | Compila y corre en PRT. `TIMEFRAME(weekly)` funciona en ProBacktest. |

## Nivel 2 — Funcional

| Ticker | Corre | Nota |
|---|---|---|
| VGT, VHT, IBB, IVV, PAVE | ✅ | Matriz emaSube 0/1 y salida 2/3 ejecutada |

Filtro semanal real: última semana cerrada, sin mirar el futuro.

## Nivel 3 — Visual

✅ Entradas y salidas coinciden con las señales del scanner en el gráfico.

## Nivel 4 — Regresión

✅ Las señales de entrada son las de v1. Cambian solo el filtro semanal y las salidas.

## Nivel 5 — Rendimiento

✅ Un solo bloque semanal. Sin llamadas multi-timeframe repetidas.

## Resultado

- Salida elegida: 2 (vela entera bajo la EMA50).
- `emaSube`: sin ventaja clara. No pasa al scanner. Scanner en v1.3.

Resultados: `docs/research/RESULTADOS_puerta-d-backtest.md`.

## Límites conocidos

1. 1 acción por operación. El $ no sirve para comparar entre ETF.
2. Sin comisiones ni deslizamiento.
3. Muestra pequeña en algunos ETF (13-35 operaciones).
