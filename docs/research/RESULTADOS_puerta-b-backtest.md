<!-- RESULTADOS_puerta-b-backtest · v1.2 · 2026-11-10 -->

# Resultados — Backtest puerta B

## v1 (2026-11-10)

**Configuración:** señal del scanner puerta B v1.1 (giro semanal con la regla del cuerpo sobre la línea antigua, ADR-0002). Compra a la apertura del primer día tras cerrar la semana de la señal, una sola vez. `esETF = 1`. 1 acción por operación. Periodo 2010 – 9-nov-2026.

### Matriz de salidas (VGT y VHT): ops / gan / ratio · tiempo en mercado

| salida | VGT | VHT |
|---|---|---|
| 3 (línea ATR diaria) | 28 / 50 % / 4,12 · 17 % | 28 / 39 % / 1,35 · 15 % |
| 4 (vela entera bajo EMA50) | 28 / 43 % / **4,44** · 34 % | 28 / 46 % / **1,99** · 32 % |
| 5 (cierre semanal bajo línea ATR x1,5) | 28 / 61 % / 4,34 · 59 % | 28 / 54 % / 1,84 · 56 % |

### Lectura

- La puerta B gana con las tres salidas en los dos ETF (ratio de 1,35 a 4,44).
- Unas 2 operaciones al año por ETF. Muestra aceptable (28 operaciones).
- Salida 4: mejor ratio en los dos ETF y tiempo comprado moderado (32-34 %).
- Salida 5: más % de ganadoras (54-61 %), pero casi siempre comprado (56-59 % del tiempo).
- Salida 3: sale pronto (15-17 % del tiempo). Peor en VHT (1,35).
- Comparación con otras puertas en VGT y VHT (ratio): D 1,98 / 2,13 · C (salida 4) 3,21 / 1,75 · A (salida 3) 0,86 / 1,42.

### Salida 4 en los 5 ETF (ops / gan / ratio · tiempo en mercado)

| ETF | Resultado |
|---|---|
| VGT | 28 / 43 % / 4,44 · 34 % |
| VHT | 28 / 46 % / 1,99 · 32 % |
| IBB | 25 / 44 % / 1,53 · 23 % |
| IVV | 29 / 41 % / 3,93 · 36 % |
| PAVE | 18 / 44 % / 1,71 · 26 % |

### Decisión (2026-11-10)

- **Salida elegida: 4** (vela entera bajo la EMA50). Ratio mayor que 1,5 en los 5 ETF (1,53 a 4,44).
- Es la única puerta que gana en los 5 ETF con una misma salida.
- Perfil tendencial: 41-46 % de ganadoras, pero las ganadoras pesan 2-4 veces más que las perdedoras.
- Muestra de 18 a 29 operaciones por ETF. Aceptable.
- **Scanner B se queda en v1.1.** `puerta-b-backtest.pts` se queda en v1 (`salida = 4` ya es el valor por defecto).
- Pendiente: probar en acciones con `esETF = 0`.
