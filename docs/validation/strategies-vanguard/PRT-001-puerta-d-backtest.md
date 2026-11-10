<!-- PRT-001 · v1.0 · 2026-11-08 -->

# PRT-001 — Validación puerta-d-backtest v1

- **Script:** `strategies/strategies-vanguard/puerta-d-backtest.pts` (v1)
- **Módulo:** ProBacktest · gráfico diario
- **Señal:** igual que el scanner puerta D v1.3 (solo EMA50, ventana de 3 sesiones)
- **Estado:** APROBADA como herramienta de estudio, con los límites de abajo

## Nivel 1 — Compilación

| Resultado | Fecha | Nota |
|---|---|---|
| ✅ | 2026-11-07 | Compila y corre en PRT (licencia completa) |

## Nivel 2 — Funcional

| Ticker | Corre | Nota |
|---|---|---|
| VGT | ✅ | 50 operaciones (2010-2026) |
| IBB | ✅ | 37 operaciones |
| IVV | ✅ | 52 operaciones |
| PAVE | ✅ | 21 operaciones (desde 2017) |
| VHT | ✅ | 45 operaciones |

Las entradas caen donde da la señal del scanner. Comprobado en el gráfico de VGT.

## Límites conocidos (a resolver en v2)

1. El filtro semanal está aproximado con la media de 250 sesiones diarias. Es más flojo que el del scanner.
2. La salida a 20 sesiones es solo de referencia y corta las subidas.
3. La señal acepta cruzar una EMA50 que todavía baja.

Resultados: `docs/research/RESULTADOS_puerta-d-backtest.md`.
