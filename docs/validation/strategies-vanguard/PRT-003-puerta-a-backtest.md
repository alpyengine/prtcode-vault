<!-- PRT-003 · v1.0 · 2026-11-09 -->

# PRT-003 — Validación puerta-a-backtest v1

- **Script:** `strategies/strategies-vanguard/puerta-a-backtest.pts` (v1)
- **Módulo:** ProBacktest · gráfico diario
- **Señal:** igual que el scanner puerta A v1.1
- **Estado:** APROBADA para ETF. En acciones, pendiente.

## Nivel 1 — Compilación

| Resultado | Fecha | Nota |
|---|---|---|
| ✅ | 2026-11-09 | Compila y corre en PRT |

## Nivel 2 — Funcional

| Ticker | Corre | Nota |
|---|---|---|
| VGT, VHT, IBB, IVV, PAVE | ✅ | Salidas 2, 3 y 4 (VGT y VHT); salida 3 (resto) |
| JPM, KO, CAT | ✅ | `esETF = 0`, salida 3 |

## Nivel 3 — Visual

✅ Panel de posiciones: un bloque por operación, sin solapes.

## Nivel 4 — Regresión

✅ Misma lógica de filtro semanal que la puerta D v2.

## Nivel 5 — Rendimiento

✅ Un solo bloque semanal.

## Resultado

- ETF, salida 3: ratio mayor que 1 en 4 de 5 (1,42 a 2,06). VGT 0,86.
- Acciones, salida 3: JPM 1,08, KO 0,58, CAT 0,32. No valida.
- Scanner A se queda en v1.1.

Resultados: `docs/research/RESULTADOS_puerta-a-backtest.md`.

## Límites conocidos

1. 1 acción por operación.
2. Sin comisiones ni deslizamiento.
3. En acciones la salida 3 es demasiado ajustada. Falta probar salidas 2 y 4.
