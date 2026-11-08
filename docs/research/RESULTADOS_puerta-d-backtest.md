<!-- RESULTADOS_puerta-d-backtest · v1.0 · 2026-11-08 -->

# Resultados — Backtest puerta D

## v1 (2026-11-07)

**Configuración:** señal del scanner puerta D v1.3. Compra a la apertura del día siguiente y venta a las 20 sesiones. Filtro de tendencia aproximado (MM250 diaria). 1 acción por operación. Periodo desde 2010 (PAVE desde 2017) hasta el 6-nov-2026.

| ETF | Operaciones | Ganadoras | Ratio ganancia/pérdida | Peor operación |
|---|---|---|---|---|
| VGT | 50 | 72 % | 1,53 | −13,87 $ |
| IBB | 37 | 57 % | 1,22 | — |
| IVV | 52 | 58 % | 2,30 | — |
| PAVE | 21 | 76 % | 2,54 | — |
| VHT | 45 | 64 % | 0,94 | — |

Unas 3 operaciones al año por ETF. Los importes en $ no se usan para comparar: es 1 acción por operación.

### Observaciones

- La salida a 20 sesiones corta subidas buenas. No sirve para decidir.
- Hay entradas con la EMA50 todavía bajando (rebotes en bajista).
- VHT pierde (ratio < 1).

### Prueba previa fuera de PRT (12 meses, 10 ETF Vanguard, salida a 20 sesiones)

| Entrada | Señales | Ganan | Media |
|---|---|---|---|
| v1.3 actual | 43 | 63 % | +1,1 % |
| + EMA50 subiendo | 32 | 63 % | +1,2 % |
| + EMA20 > EMA50 | 29 | 52 % | −0,2 % |

### Siguiente paso (v2)

1. Filtro semanal real con `TIMEFRAME(weekly)`.
2. Interruptor "EMA50 subiendo".
3. Salidas a elegir: 20 sesiones / vela entera bajo la EMA50 / cierre semanal bajo la línea ATR ×2.
