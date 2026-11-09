<!-- RESULTADOS_puerta-a-backtest · v1.3 · 2026-11-09 -->

# Resultados — Backtest puerta A

## v1 (2026-11-09)

**Configuración:** señal del scanner puerta A v1.1. Filtro semanal real (`TIMEFRAME(weekly)`, última semana cerrada). `esETF = 1`. Compra a la apertura del día siguiente. 1 acción por operación. Periodo 2010 – 9-nov-2026.

### Matriz de salidas (VGT y VHT)

| Prueba | salida | VGT ops / gan / ratio | VHT ops / gan / ratio |
|---|---|---|---|
| A | 2 (vela entera bajo EMA20) | 24 / 38 % / 0,56 | 28 / 32 % / 1,50 |
| B | 3 (cierre bajo línea ATR diaria) | 25 / 52 % / 0,86 | 25 / 32 % / 1,42 |
| C | 4 (vela entera bajo EMA50) | 23 / 48 % / 0,82 | 24 / 25 % / 1,16 |

### Lectura (2026-11-09)

- VGT pierde con las 3 salidas (ratio 0,56 a 0,86).
- VHT gana con las 3 (1,16 a 1,50), pero solo 25-32 % de ganadoras. Gana por pocas operaciones grandes (la mejor: +35 $ frente a pérdida media de 2-3 $).
- Salida 3 (cierre bajo línea ATR diaria): la más equilibrada. Mejor % de ganadoras en VGT (52 %) y ratio 1,42 en VHT.
- Salida 2 (EMA20): peor en VGT (0,56).
- Salida 4 (EMA50, la de la puerta D): no mejora la A. Entra en un retroceso corto y la EMA50 queda lejos.
- Comparada con la D (VGT 1,98 / VHT 2,13 con salida 2), la puerta A es claramente más débil.

### Confirmación con salida 3 (IBB, IVV, PAVE)

| ETF | Operaciones | Ganadoras | Ratio |
|---|---|---|---|
| VGT | 25 | 52 % | 0,86 |
| VHT | 25 | 32 % | 1,42 |
| IBB | 33 | 33 % | 1,65 |
| IVV | 24 | 62 % | 2,06 |
| PAVE | 17 | 53 % | 1,76 |

### Decisión (2026-11-09)

- Con salida 3, la puerta A tiene ratio > 1 en 4 de 5 ETF (1,42 a 2,06). Solo VGT queda por debajo (0,86).
- IVV, que era el ETF flojo en la puerta D (0,93), es el mejor aquí (2,06). Las puertas A y D se complementan.
- Perfil: tendencial. Pocas ganadoras en IBB y VHT (32-33 %), pero ganan mucho más de lo que pierden.
- **Se mantiene el scanner A en v1.1.** Salida de trabajo: 3 (cierre bajo la línea ATR diaria).

### Prueba en acciones NYSE (`esETF = 0`, salida 3)

| Acción | Operaciones | Ganadoras | Ratio | Tiempo en mercado |
|---|---|---|---|---|
| JPM | 21 | 48 % | 1,08 | 5 % |
| KO | 37 | 35 % | 0,58 | 12 % |
| CAT | 22 | 27 % | 0,32 | 5 % |

### Decisión acciones (2026-11-09)

- En acciones la puerta A con salida 3 **no funciona**: 2 de 3 pierden y JPM apenas gana.
- Causa probable: en acciones la línea ATR diaria es x2 (más ajustada que x2,5 de ETF) y las acciones se mueven más. La salida corta las operaciones demasiado pronto (5 % del tiempo en mercado).
- La puerta A queda **validada solo para ETF**. En acciones, pendiente de probar otra salida (2 o 4).
