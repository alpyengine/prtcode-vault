<!-- PRT-005 · v1.0 · 2026-11-10 -->

# PRT-005 — Validación puerta-b-backtest v1

- **Script:** `strategies/strategies-vanguard/puerta-b-backtest.pts` (v1)
- **Módulo:** ProBacktest · gráfico diario
- **Señal:** igual que el scanner puerta B v1.1 (regla ADR-0002)
- **Estado:** APROBADA para ETF. En acciones, pendiente.

## Nivel 1 — Compilación

| Resultado | Fecha | Nota |
|---|---|---|
| ✅ | 2026-11-10 | Compila y corre en PRT |

## Nivel 2 — Funcional

| Ticker | Corre | Nota |
|---|---|---|
| VGT, VHT | ✅ | Salidas 3, 4 y 5 |
| IBB, IVV, PAVE | ✅ | Salida 4 |

La señal semanal compra una sola vez (primer día tras cerrar la semana de la señal).

## Nivel 3 — Visual

✅ Panel de posiciones: un bloque por operación, sin solapes.

## Nivel 4 — Regresión

✅ Mismo filtro semanal y salidas 1 a 4 que las puertas A y C. La salida 5 es nueva.

## Nivel 5 — Rendimiento

✅ Un solo bloque semanal.

## Resultado

- Salida 4: ratio mayor que 1,5 en los 5 ETF (1,53 a 4,44).
- Scanner B se queda en v1.1.

Resultados: `docs/research/RESULTADOS_puerta-b-backtest.md`.

## Límites conocidos

1. 1 acción por operación.
2. Sin comisiones ni deslizamiento.
3. Muestras de 18 a 29 operaciones.
4. Acciones (`esETF = 0`) sin probar.
