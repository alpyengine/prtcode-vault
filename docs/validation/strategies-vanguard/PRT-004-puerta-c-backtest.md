<!-- PRT-004 · v1.0 · 2026-11-10 -->

# PRT-004 — Validación puerta-c-backtest v1.1

- **Script:** `strategies/strategies-vanguard/puerta-c-backtest.pts` (v1.1)
- **Módulo:** ProBacktest · gráfico diario
- **Señal:** igual que el scanner puerta C v1.1
- **Estado:** APROBADA para ETF. En acciones, pendiente.

## Nivel 1 — Compilación

| Resultado | Fecha | Nota |
|---|---|---|
| ✅ | 2026-11-10 | Compila y corre en PRT |

## Nivel 2 — Funcional

| Ticker | Corre | Nota |
|---|---|---|
| VGT, VHT | ✅ | Salidas 2, 3 y 4 |
| IBB, IVV, PAVE | ✅ | Salidas 3 y 4 |

## Nivel 3 — Visual

✅ Panel de posiciones: un bloque por operación, sin solapes.

## Nivel 4 — Regresión

✅ Mismo filtro semanal y mismas salidas que la puerta A.

## Nivel 5 — Rendimiento

✅ Un solo bloque semanal.

## Resultado

- Salida 4: ratio mayor que 1,7 en 4 de 5 ETF (1,75 a 4,44).
- PAVE falla (0,40) con solo 8 operaciones.
- Scanner C se queda en v1.1.

Resultados: `docs/research/RESULTADOS_puerta-c-backtest.md`.

## Límites conocidos

1. 1 acción por operación.
2. Sin comisiones ni deslizamiento.
3. Muestras de 8 a 32 operaciones.
4. Acciones (`esETF = 0`) sin probar.
