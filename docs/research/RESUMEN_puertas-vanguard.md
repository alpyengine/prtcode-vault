<!-- RESUMEN_puertas-vanguard · v1.0 · 2026-11-10 -->

# Resumen — Puertas Vanguard en ETF

Ratio ganancia/pérdida con la mejor salida de cada puerta. 1 acción por operación. 2010 – 9-nov-2026.

| Puerta | Scanner | Salida | VGT | VHT | IBB | IVV | PAVE |
|---|---|---|---|---|---|---|---|
| A retroceso | v1.1 | 3 · línea ATR diaria | 0,86 | 1,42 | 1,65 | 2,06 | 1,76 |
| B giro semanal | v1.1 | 4 · bajo EMA50 | 4,44 | 1,99 | 1,53 | 3,93 | 1,71 |
| C rotura | v1.1 | 4 · bajo EMA50 | 3,21 | 1,75 | 4,44 | 2,66 | 0,40 |
| D cruce de medias | v1.3 | 2 · bajo EMA50 (ver nota) | 1,98 | 2,13 | 2,39 | 0,93 | 1,84 |

Nota D: en el backtest de D, la salida 2 es "vela entera bajo la EMA50". En los backtests de A, B y C esa misma salida es la número 4.

## Lectura

- **B** es la única que gana en los 5 ETF con una misma salida.
- **C** es la más fuerte donde acierta (VGT, IBB), pero falla en PAVE (8 operaciones).
- **A** es la más débil. Aporta en IVV y PAVE, donde C y D flojean.
- **D** falla en IVV (0,93).
- Las puertas se complementan según el ETF.

## Pendiente

1. Probar las cuatro puertas en acciones (`esETF = 0`). La A ya falló con salida 3 en JPM, KO y CAT.
2. Decidir cómo se usan juntas en el día a día.
