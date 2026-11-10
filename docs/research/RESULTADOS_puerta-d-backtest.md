<!-- RESULTADOS_puerta-d-backtest · v1.5 · 2026-11-09 -->

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

## v2 (2026-11-08)

**Configuración:** filtro semanal real (`TIMEFRAME(weekly)`, última semana cerrada). `emaSube = 1` (EMA50 subiendo). `salida = 3` (cierre semanal bajo la línea ATR ×2). 1 acción por operación.

**Hallazgo:** `TIMEFRAME(weekly)` compila y funciona en ProBacktest.

| ETF | Operaciones | Ganadoras | Ratio | Tiempo en mercado |
|---|---|---|---|---|
| VGT | 28 | 46 % | 1,10 | 29 % |
| IBB | 16 | 44 % | 3,08 | 26 % |
| IVV | 27 | 41 % | 0,70 | 33 % |
| PAVE | 15 | 47 % | 1,24 | 16 % |
| VHT | 21 | 57 % | 2,29 | 32 % |

### Lectura

- Cambian tres cosas a la vez respecto a v1 (filtro, EMA50 subiendo y salida). No se puede saber cuál mejora o empeora.
- Menos operaciones y menos % de ganadoras: es normal con una salida de tendencia.
- IVV pasa a perder (ratio 0,70). VHT pasa a ganar (2,29).

### Pendiente

Matriz de 4 pruebas en VGT y VHT: emaSube 0/1 × salida 2/3.

### Matriz v2 (VGT y VHT)

| Prueba | emaSube | salida | VGT ops / gan / ratio | VHT ops / gan / ratio |
|---|---|---|---|---|
| A | 0 | 2 | 51 / 47 % / 1,98 | 38 / 47 % / 2,13 |
| B | 1 | 2 | 35 / 40 % / 1,27 | 26 / 54 % / 2,95 |
| C | 0 | 3 | 19 / 42 % / 0,94 | 18 / 50 % / 1,34 |
| D | 1 | 3 | 28 / 46 % / 1,10 | 21 / 57 % / 2,29 |

### Conclusión de la matriz (2026-11-09)

- **Salida:** la 2 (vela entera bajo la EMA50) gana a la 3 (ATR semanal ×2) en las 4 comparaciones. Se elige la salida 2.
- **EMA50 subiendo:** resultado mixto. En VGT empeora (1,98 → 1,27) y en VHT mejora (2,13 → 2,95). Sin decidir.
- Siguiente: pruebas A y B en IBB, IVV y PAVE para decidir EMA50 subiendo. Mientras, el scanner sigue en v1.3.

### Decisión EMA50 subiendo (salida 2) — IBB, IVV, PAVE

| Prueba | emaSube | IBB ops / gan / ratio | IVV ops / gan / ratio | PAVE ops / gan / ratio |
|---|---|---|---|---|
| A | 0 | 18 / 44 % / 2,39 | 30 / 33 % / 0,93 | 13 / 31 % / 1,84 |
| B | 1 | 21 / 57 % / 1,89 | 31 / 52 % / 0,73 | 12 / 75 % / 4,49 |

### Comparativa A vs B en los 5 ETF (salida 2)

| ETF | A ops / gan / ratio | B ops / gan / ratio | Mejor |
|---|---|---|---|
| VGT | 51 / 47 % / 1,98 | 35 / 40 % / 1,27 | A |
| VHT | 38 / 47 % / 2,13 | 26 / 54 % / 2,95 | B |
| IBB | 18 / 44 % / 2,39 | 21 / 57 % / 1,89 | A en ratio, B en % |
| IVV | 30 / 33 % / 0,93 | 31 / 52 % / 0,73 | A en ratio, B en % |
| PAVE | 13 / 31 % / 1,84 | 12 / 75 % / 4,49 | B |

### Decisión (2026-11-09)

- "EMA50 subiendo" sube el % de ganadoras en 4 de 5 ETF, pero el ratio solo mejora en 2 de 5. Sin ventaja clara.
- **No se añade al scanner. Se queda en v1.3.**
- Salida elegida: 2 (vela entera bajo la EMA50).
- IVV pierde o queda flojo en ambas pruebas. La puerta D encaja mal en ETF muy amplios.
- Dato a vigilar: IBB en A (18 ops) y B (21 ops). Con más filtro no debería haber más operaciones. Puede ser un efecto de la secuencia de operaciones, o que el PDF de A sea de otra prueba. Revisar si se quiere cerrar el dato.
