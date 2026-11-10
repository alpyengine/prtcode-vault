<!-- RESULTADOS_puerta-c-backtest · v1.3 · 2026-11-10 -->

# Resultados — Backtest puerta C

## v1 (2026-11-10)

**Configuración:** señal del scanner puerta C v1.1 (rotura del máximo de 20 días, vela entera y de fuerza, volumen sobre la media de ayer). Filtro semanal real (`TIMEFRAME(weekly)`). `esETF = 1`. Compra a la apertura del día siguiente. 1 acción por operación. Periodo 2010 – 9-nov-2026.

### Matriz de salidas (VGT y VHT)

| Prueba | salida | VGT ops / gan / ratio | VHT ops / gan / ratio |
|---|---|---|---|
| A | 2 (vela entera bajo EMA20) | 31 / 35 % / 1,97 | 24 / 46 % / 1,27 |
| B | 3 (cierre bajo línea ATR diaria) | 32 / 41 % / 1,66 | 23 / 48 % / 2,85 |
| C | 4 (vela entera bajo EMA50) | 26 / 31 % / 3,21 | 20 / 65 % / 1,75 |

### Comparación de salidas 3 y 4 en los 5 ETF (ops / gan / ratio)

| ETF | Salida 3 | Salida 4 | Puerta A (salida 3) |
|---|---|---|---|
| VGT | 32 / 41 % / 1,66 | 26 / 31 % / **3,21** | 0,86 |
| VHT | 23 / 48 % / **2,85** | 20 / 65 % / 1,75 | 1,42 |
| IBB | 17 / 53 % / 2,05 | 15 / 67 % / **4,44** | 1,65 |
| IVV | 24 / 50 % / 0,92 | 18 / 61 % / **2,66** | 2,06 |
| PAVE | 8 / 38 % / 0,58 | 8 / 25 % / 0,40 | 1,76 |

### Decisión (2026-11-10)

- **Salida elegida: 4** (vela entera bajo la EMA50). Ratio mayor que 1,7 en 4 de 5 ETF (1,75 a 4,44). Con la salida 3 eran 3 de 5.
- La salida 4 sube el % de ganadoras en IVV (50 → 61 %) e IBB (53 → 67 %). Pasa más tiempo comprado (22-28 % frente a 12-17 %).
- PAVE falla con las dos salidas (0,40 y 0,58), pero solo tiene 8 operaciones. Muestra demasiado corta.
- Las puertas A y C se complementan en PAVE, pero no en IVV: con la salida 4, la C también funciona en IVV (2,66).
- **Scanner C se queda en v1.1.** `salida = 4` por defecto en el backtest.
- Pendiente: probar en acciones con `esETF = 0`.
