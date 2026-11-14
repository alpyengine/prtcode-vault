<!-- RESULTADOS_backtest-condicionado · v1.0 · 2026-11-14 -->

# Resultados — Backtest condicionado por estado técnico

**Pregunta:** ¿qué puerta funciona mejor en cada estado técnico del valor?

**Motor:** el de la Ronda 2 (`tools/motor-puertas/motor_puertas.py` v1.0), sin cambios en las puertas ni en las salidas. **Universo:** las 40 acciones de la Ronda 2, `esETF = 0`. 10.000 $ por operación, sin comisiones. T1 = 2010-2022 · T2 = 2023 – 9-nov-2026 (último dato). Una operación pertenece al tramo en el que entra.

**Salidas:** a) la elegida (A: cierre bajo la línea ATR diaria · B, C, D: vela entera bajo la EMA50) · b) stop fijo 2,5 × ATR(14), mitad a +2R, resto a +3R.

## Paso 0. Regresión

Sin clasificar por estado, el número de operaciones y el ratio de cada puerta, salida y tramo (24 casos) son **idénticos** a los de la Ronda 2. Se sigue adelante.

## Paso 1. Clasificación

Estado del valor al cierre del día de la señal (el día anterior a la entrada). Máximo de 52 semanas = máximo de los High de las últimas 252 sesiones, incluido el día de la señal. EMA200 y EMA50 sobre el cierre diario.

| Estado | Condiciones |
|---|---|
| E1 retroceso en tendencia | cierre > EMA200 · cierre entre 0 % y +10 % sobre la EMA50 · cierre entre 3 % y 15 % bajo el máximo de 52 semanas |
| E2 pre-rotura | cierre > EMA50 y > EMA200 · a menos del 3 % del máximo de 52 semanas |
| E3 castigado | más de un 25 % bajo el máximo de 52 semanas · cierre entre 0 % y −15 % respecto a la EMA200 |
| E0 | ninguno de los anteriores |

**Comprobación:** 5.863 operaciones (4 puertas × 2 salidas). Ninguna cae en más de un estado. En las 24 combinaciones de puerta, salida y tramo, la suma de E1 + E2 + E3 + E0 da el total de la Ronda 2.

**Aviso:** los datos empiezan en junio de 2009. En 110 operaciones de principios de 2010, el máximo de 52 semanas se calcula con menos de 252 sesiones, y la EMA200 todavía está arrancando.

## Paso 2. Tablas por puerta, estado, salida y tramo

«Mejor valor» = % de la ganancia neta que aporta el valor con más ganancia (vacío si la ganancia neta es ≤ 0; «>100 %» si el resto del grupo pierde dinero).

### Puerta A retroceso

| Estado | Salida | Tramo | Ops | % gan. | Gan. media | Pérd. media | Ratio | Media/op | Peor op. | Mejor valor |
|---|---|---|---|---|---|---|---|---|---|---|
| E1 retroceso en tendencia | a) elegida | T1 | 379 | 42 % | 4,0 % | -2,3 % | 1,26 | 0,34 % | -17,1 % | HPQ 48 % |
|  |  | T2 | 156 | 39 % | 4,6 % | -2,4 % | 1,25 | 0,37 % | -9,5 % | OXY 80 % |
|  |  | Todo | 535 | 41 % | 4,2 % | -2,3 % | 1,26 | 0,35 % | -17,1 % | HPQ 35 % |
|  | b) stop fijo | T1 | 292 | 41 % | 9,9 % | -5,0 % | 1,39 | 1,15 % | -15,2 % | MSFT 20 % |
|  |  | T2 | 114 | 44 % | 11,3 % | -5,4 % | 1,65 | 1,96 % | -9,3 % | INTC 23 % |
|  |  | Todo | 406 | 42 % | 10,3 % | -5,1 % | 1,47 | 1,38 % | -15,2 % | MSFT 15 % |
| E2 pre-rotura | a) elegida | T1 | 363 | 37 % | 3,9 % | -2,1 % | 1,14 | 0,18 % | -8,5 % | ABT 43 % |
|  |  | T2 | 64 | 52 % | 5,0 % | -2,9 % | 1,83 | 1,17 % | -7,6 % | GE 56 % |
|  |  | Todo | 427 | 40 % | 4,1 % | -2,2 % | 1,25 | 0,33 % | -8,5 % | GE 28 % |
|  | b) stop fijo | T1 | 253 | 36 % | 8,4 % | -4,1 % | 1,15 | 0,39 % | -11,7 % | HD 37 % |
|  |  | T2 | 48 | 35 % | 8,8 % | -4,5 % | 1,08 | 0,24 % | -7,7 % | GE >100 % |
|  |  | Todo | 301 | 36 % | 8,4 % | -4,2 % | 1,14 | 0,36 % | -11,7 % | HD 35 % |
| E3 castigado | a) elegida | T1 | 20 | 40 % | 4,9 % | -3,4 % | 0,95 | -0,11 % | -7,4 % | — |
|  |  | T2 | 16 | 62 % | 4,6 % | -4,8 % | 1,60 | 1,09 % | -7,5 % | COP 90 % |
|  |  | Todo | 36 | 50 % | 4,7 % | -3,9 % | 1,22 | 0,42 % | -7,5 % | HPQ >100 % |
|  | b) stop fijo | T1 | 19 | 26 % | 18,6 % | -8,4 % | 0,79 | -1,28 % | -15,1 % | — |
|  |  | T2 | 12 | 50 % | 17,5 % | -7,6 % | 2,31 | 4,96 % | -10,0 % | QCOM 46 % |
|  |  | Todo | 31 | 35 % | 18,0 % | -8,1 % | 1,22 | 1,14 % | -15,1 % | HPQ >100 % |
| E0 ninguno | a) elegida | T1 | 103 | 32 % | 6,9 % | -3,5 % | 0,95 | -0,11 % | -11,6 % | — |
|  |  | T2 | 48 | 52 % | 5,3 % | -2,8 % | 2,01 | 1,38 % | -10,1 % | GOOGL 85 % |
|  |  | Todo | 151 | 38 % | 6,2 % | -3,3 % | 1,18 | 0,37 % | -11,6 % | QCOM >100 % |
|  | b) stop fijo | T1 | 96 | 29 % | 14,6 % | -6,4 % | 0,93 | -0,32 % | -16,3 % | — |
|  |  | T2 | 41 | 24 % | 12,6 % | -6,9 % | 0,59 | -2,16 % | -19,4 % | — |
|  |  | Todo | 137 | 28 % | 14,1 % | -6,6 % | 0,82 | -0,87 % | -19,4 % | — |

### Puerta B giro semanal

| Estado | Salida | Tramo | Ops | % gan. | Gan. media | Pérd. media | Ratio | Media/op | Peor op. | Mejor valor |
|---|---|---|---|---|---|---|---|---|---|---|
| E1 retroceso en tendencia | a) elegida | T1 | 305 | 36 % | 8,6 % | -4,2 % | 1,18 | 0,48 % | -14,3 % | HPQ 42 % |
|  |  | T2 | 94 | 47 % | 11,3 % | -4,1 % | 2,40 | 3,09 % | -15,8 % | WMT 25 % |
|  |  | Todo | 399 | 39 % | 9,4 % | -4,2 % | 1,43 | 1,10 % | -15,8 % | WMT 16 % |
|  | b) stop fijo | T1 | 276 | 36 % | 10,8 % | -4,7 % | 1,30 | 0,90 % | -12,9 % | UNH 30 % |
|  |  | T2 | 84 | 42 % | 11,2 % | -5,1 % | 1,56 | 1,68 % | -12,4 % | MMM 23 % |
|  |  | Todo | 360 | 38 % | 10,9 % | -4,8 % | 1,36 | 1,09 % | -12,9 % | ABT 17 % |
| E2 pre-rotura | a) elegida | T1 | 237 | 37 % | 9,0 % | -3,8 % | 1,39 | 0,93 % | -16,2 % | OXY 30 % |
|  |  | T2 | 55 | 49 % | 13,6 % | -5,6 % | 2,33 | 3,81 % | -20,8 % | GE 64 % |
|  |  | Todo | 292 | 39 % | 10,1 % | -4,1 % | 1,59 | 1,47 % | -20,8 % | GE 31 % |
|  | b) stop fijo | T1 | 204 | 38 % | 8,6 % | -4,4 % | 1,17 | 0,48 % | -11,1 % | CMCSA 68 % |
|  |  | T2 | 51 | 45 % | 10,9 % | -5,8 % | 1,53 | 1,71 % | -18,7 % | CSCO 25 % |
|  |  | Todo | 255 | 39 % | 9,1 % | -4,7 % | 1,25 | 0,73 % | -18,7 % | CMCSA 36 % |
| E3 castigado | a) elegida | T1 | 36 | 47 % | 18,3 % | -4,3 % | 3,79 | 6,36 % | -11,1 % | GE 31 % |
|  |  | T2 | 15 | 40 % | 11,9 % | -6,2 % | 1,27 | 1,02 % | -16,3 % | BAC >100 % |
|  |  | Todo | 51 | 45 % | 16,6 % | -4,9 % | 2,77 | 4,79 % | -16,3 % | GE 29 % |
|  | b) stop fijo | T1 | 35 | 46 % | 18,9 % | -7,6 % | 2,10 | 4,52 % | -16,7 % | OXY 21 % |
|  |  | T2 | 15 | 40 % | 21,6 % | -9,3 % | 1,55 | 3,07 % | -18,1 % | ORCL 77 % |
|  |  | Todo | 50 | 44 % | 19,6 % | -8,1 % | 1,90 | 4,08 % | -18,1 % | ORCL 17 % |
| E0 ninguno | a) elegida | T1 | 193 | 33 % | 12,0 % | -3,6 % | 1,62 | 1,51 % | -16,0 % | QCOM 29 % |
|  |  | T2 | 59 | 53 % | 15,3 % | -5,0 % | 3,39 | 5,68 % | -19,9 % | C 33 % |
|  |  | Todo | 252 | 37 % | 13,1 % | -3,8 % | 2,03 | 2,49 % | -19,9 % | C 22 % |
|  | b) stop fijo | T1 | 189 | 44 % | 16,6 % | -6,6 % | 2,00 | 3,69 % | -24,1 % | DIS 12 % |
|  |  | T2 | 56 | 54 % | 14,7 % | -6,7 % | 2,53 | 4,77 % | -12,8 % | INTC 29 % |
|  |  | Todo | 245 | 47 % | 16,1 % | -6,7 % | 2,11 | 3,94 % | -24,1 % | CAT 9 % |

### Puerta C rotura

| Estado | Salida | Tramo | Ops | % gan. | Gan. media | Pérd. media | Ratio | Media/op | Peor op. | Mejor valor |
|---|---|---|---|---|---|---|---|---|---|---|
| E1 retroceso en tendencia | a) elegida | T1 | 47 | 38 % | 8,7 % | -4,8 % | 1,14 | 0,40 % | -11,2 % | AMZN >100 % |
|  |  | T2 | 23 | 39 % | 26,0 % | -4,9 % | 3,43 | 7,21 % | -9,8 % | CAT 73 % |
|  |  | Todo | 70 | 39 % | 14,5 % | -4,8 % | 1,89 | 2,64 % | -11,2 % | CAT 62 % |
|  | b) stop fijo | T1 | 46 | 43 % | 8,9 % | -5,0 % | 1,38 | 1,08 % | -6,9 % | UPS 40 % |
|  |  | T2 | 23 | 39 % | 9,7 % | -5,2 % | 1,21 | 0,67 % | -7,3 % | C >100 % |
|  |  | Todo | 69 | 42 % | 9,2 % | -5,0 % | 1,32 | 0,94 % | -7,3 % | UPS 30 % |
| E2 pre-rotura | a) elegida | T1 | 239 | 46 % | 9,8 % | -4,9 % | 1,71 | 1,86 % | -23,0 % | AAPL 27 % |
|  |  | T2 | 59 | 39 % | 7,8 % | -5,5 % | 0,91 | -0,29 % | -13,7 % | — |
|  |  | Todo | 298 | 45 % | 9,4 % | -5,0 % | 1,52 | 1,44 % | -23,0 % | AAPL 27 % |
|  | b) stop fijo | T1 | 277 | 42 % | 10,0 % | -4,5 % | 1,62 | 1,61 % | -12,4 % | AAPL 16 % |
|  |  | T2 | 68 | 40 % | 12,3 % | -5,6 % | 1,44 | 1,49 % | -9,0 % | INTC 38 % |
|  |  | Todo | 345 | 42 % | 10,4 % | -4,7 % | 1,57 | 1,58 % | -12,4 % | AAPL 15 % |
| E3 castigado | a) elegida | T1 | 0 | — | — | — | — | — | — | — |
|  |  | T2 | 0 | — | — | — | — | — | — | — |
|  |  | Todo | 0 | — | — | — | — | — | — | — |
|  | b) stop fijo | T1 | 0 | — | — | — | — | — | — | — |
|  |  | T2 | 0 | — | — | — | — | — | — | — |
|  |  | Todo | 0 | — | — | — | — | — | — | — |
| E0 ninguno | a) elegida | T1 | 14 | 71 % | 19,0 % | -5,0 % | 9,51 | 12,12 % | -7,5 % | QCOM 52 % |
|  |  | T2 | 11 | 55 % | 20,1 % | -8,8 % | 2,75 | 6,98 % | -21,4 % | INTC 49 % |
|  |  | Todo | 25 | 64 % | 19,4 % | -7,1 % | 4,87 | 9,86 % | -21,4 % | QCOM 38 % |
|  | b) stop fijo | T1 | 14 | 79 % | 12,5 % | -10,2 % | 4,48 | 7,63 % | -12,1 % | QCOM 33 % |
|  |  | T2 | 12 | 33 % | 18,8 % | -8,1 % | 1,16 | 0,87 % | -14,3 % | INTC >100 % |
|  |  | Todo | 26 | 58 % | 14,2 % | -8,7 % | 2,23 | 4,51 % | -14,3 % | INTC 40 % |

### Puerta D cruce de medias

| Estado | Salida | Tramo | Ops | % gan. | Gan. media | Pérd. media | Ratio | Media/op | Peor op. | Mejor valor |
|---|---|---|---|---|---|---|---|---|---|---|
| E1 retroceso en tendencia | a) elegida | T1 | 317 | 36 % | 8,2 % | -2,9 % | 1,58 | 1,08 % | -10,5 % | CAT 20 % |
|  |  | T2 | 98 | 40 % | 8,4 % | -3,8 % | 1,46 | 1,05 % | -15,5 % | WMT 38 % |
|  |  | Todo | 415 | 37 % | 8,2 % | -3,1 % | 1,55 | 1,07 % | -15,5 % | CAT 15 % |
|  | b) stop fijo | T1 | 256 | 41 % | 11,5 % | -5,0 % | 1,57 | 1,68 % | -13,3 % | BAC 14 % |
|  |  | T2 | 76 | 55 % | 12,2 % | -5,6 % | 2,71 | 4,26 % | -9,8 % | INTC 17 % |
|  |  | Todo | 332 | 44 % | 11,7 % | -5,1 % | 1,79 | 2,27 % | -13,3 % | BAC 13 % |
| E2 pre-rotura | a) elegida | T1 | 175 | 38 % | 7,6 % | -2,8 % | 1,68 | 1,18 % | -11,1 % | UNH 25 % |
|  |  | T2 | 13 | 23 % | 8,9 % | -2,8 % | 0,94 | -0,12 % | -10,5 % | — |
|  |  | Todo | 188 | 37 % | 7,6 % | -2,8 % | 1,62 | 1,09 % | -11,1 % | UNH 20 % |
|  | b) stop fijo | T1 | 128 | 41 % | 8,9 % | -4,0 % | 1,58 | 1,35 % | -8,3 % | ABT 18 % |
|  |  | T2 | 12 | 25 % | 7,4 % | -3,4 % | 0,73 | -0,67 % | -5,5 % | — |
|  |  | Todo | 140 | 40 % | 8,8 % | -3,9 % | 1,50 | 1,18 % | -8,3 % | ABT 19 % |
| E3 castigado | a) elegida | T1 | 0 | — | — | — | — | — | — | — |
|  |  | T2 | 0 | — | — | — | — | — | — | — |
|  |  | Todo | 0 | — | — | — | — | — | — | — |
|  | b) stop fijo | T1 | 0 | — | — | — | — | — | — | — |
|  |  | T2 | 0 | — | — | — | — | — | — | — |
|  |  | Todo | 0 | — | — | — | — | — | — | — |
| E0 ninguno | a) elegida | T1 | 10 | 60 % | 6,8 % | -4,8 % | 2,13 | 2,16 % | -12,7 % | OXY 49 % |
|  |  | T2 | 4 | 75 % | 27,6 % | -9,5 % | 8,68 | 18,29 % | -9,5 % | C 85 % |
|  |  | Todo | 14 | 64 % | 13,7 % | -5,7 % | 4,32 | 6,77 % | -12,7 % | C 74 % |
|  | b) stop fijo | T1 | 9 | 67 % | 18,5 % | -7,9 % | 4,68 | 9,68 % | -9,7 % | OXY 41 % |
|  |  | T2 | 4 | 75 % | 19,8 % | -9,0 % | 6,63 | 12,61 % | -9,0 % | INTC 53 % |
|  |  | Todo | 13 | 69 % | 18,9 % | -8,2 % | 5,22 | 10,59 % | -9,7 % | OXY 32 % |

## Paso 3. Criterio (fijado antes de ver los datos)

Una puerta se asigna a un estado si cumple las tres condiciones:
1. ratio > 1,5 en conjunto y > 1 en T1 y en T2;
2. al menos 30 operaciones en cada tramo;
3. ratio en ese estado ≥ ratio general de la puerta en la Ronda 2 (acciones, misma salida).

Con menos de 30 operaciones en un tramo: MUESTRA INSUFICIENTE.

| Puerta | Ratio general Ronda 2 · salida a) | Ratio general Ronda 2 · salida b) |
|---|---|---|
| A retroceso | 1,24 | 1,21 |
| B giro semanal | 1,70 | 1,60 |
| C rotura | 1,78 | 1,58 |
| D cruce de medias | 1,63 | 1,81 |

## Paso 4. Resumen: 4 puertas × 4 estados

Cada casilla: estado · ratio en conjunto (ops T1 / ops T2).

### Salida a) elegida

| Puerta | E1 retroceso | E2 pre-rotura | E3 castigado | E0 ninguno |
|---|---|---|---|---|
| A retroceso | **NO CUMPLE** · 1,26 (379/156) | **NO CUMPLE** · 1,25 (363/64) | **MUESTRA INSUFICIENTE** · 1,22 (20/16) | **NO CUMPLE** · 1,18 (103/48) |
| B giro semanal | **NO CUMPLE** · 1,43 (305/94) | **NO CUMPLE** · 1,59 (237/55) | **MUESTRA INSUFICIENTE** · 2,77 (36/15) | **CUMPLE** · 2,03 (193/59) |
| C rotura | **MUESTRA INSUFICIENTE** · 1,89 (47/23) | **NO CUMPLE** · 1,52 (239/59) | **MUESTRA INSUFICIENTE** · — (0/0) | **MUESTRA INSUFICIENTE** · 4,87 (14/11) |
| D cruce de medias | **NO CUMPLE** · 1,55 (317/98) | **MUESTRA INSUFICIENTE** · 1,62 (175/13) | **MUESTRA INSUFICIENTE** · — (0/0) | **MUESTRA INSUFICIENTE** · 4,32 (10/4) |

### Salida b) stop fijo

| Puerta | E1 retroceso | E2 pre-rotura | E3 castigado | E0 ninguno |
|---|---|---|---|---|
| A retroceso | **NO CUMPLE** · 1,47 (292/114) | **NO CUMPLE** · 1,14 (253/48) | **MUESTRA INSUFICIENTE** · 1,22 (19/12) | **NO CUMPLE** · 0,82 (96/41) |
| B giro semanal | **NO CUMPLE** · 1,36 (276/84) | **NO CUMPLE** · 1,25 (204/51) | **MUESTRA INSUFICIENTE** · 1,90 (35/15) | **CUMPLE** · 2,11 (189/56) |
| C rotura | **MUESTRA INSUFICIENTE** · 1,32 (46/23) | **NO CUMPLE** · 1,57 (277/68) | **MUESTRA INSUFICIENTE** · — (0/0) | **MUESTRA INSUFICIENTE** · 2,23 (14/12) |
| D cruce de medias | **NO CUMPLE** · 1,79 (256/76) | **MUESTRA INSUFICIENTE** · 1,50 (128/12) | **MUESTRA INSUFICIENTE** · — (0/0) | **MUESTRA INSUFICIENTE** · 5,22 (9/4) |

**Recuento de las 32 casillas:** CUMPLE 2 · NO CUMPLE 14 · MUESTRA INSUFICIENTE 16.

**¿Cuántas cumplirían por azar?** Se repartieron al azar las etiquetas de estado entre las operaciones de cada puerta, salida y tramo (conservando cuántas hay de cada estado), y se aplicó el mismo criterio. Con 200 repeticiones:

| Salida | Cumplen de verdad | Media por azar | 95 % de las veces, por azar, como mucho |
|---|---|---|---|
| a) elegida | 1 | 2,7 | 4 |
| b) stop fijo | 1 | 2,7 | 4 |

## Lectura

- **Solo cumple una casilla en cada salida: puerta B en E0.** Es decir, B funciona mejor cuando el valor no está en ninguno de los tres estados definidos (ratio 2,03 con la salida a y 2,11 con la b, frente a 1,70 y 1,60 en general).
- **Eso no supera al azar.** Repartiendo los estados al azar salen de media unas 2,7 casillas que cumplen por salida, y hasta 4 en el 95 % de los casos. Una sola casilla real por salida está por debajo de lo esperado por suerte.
- **Conclusión: con estos datos, el estado técnico no ayuda a elegir puerta.** Ninguna puerta mejora claramente en E1, E2 o E3 respecto a su resultado general.
- **E3 (castigado) casi no tiene operaciones:** C y D no dan ninguna señal ahí (su filtro exige la MM50 semanal subiendo). A y B tienen menos de 30 operaciones en T2 (A también en T1).
- **C y D se concentran en E1 y E2.** D en E2 y C en E0 tienen muy pocas operaciones en T2.
- **Casos cerca del límite:** D con salida b) en E1 tiene ratio 1,79, justo por debajo de su ratio general (1,81). B con salida a) en E2 da 1,59, por debajo de 1,70.

## Límites

- **No incluye los filtros fundamentales de los screeners de IBKR** (margen, ventas, BPA, ROI, PER). Por eso VG4 no se puede probar.
- **Sesgo de supervivencia:** las 40 acciones cotizan hoy. Faltan las que quebraron o dejaron de cotizar.
- **Sin deslizamiento** y sin comisiones.
- El tramo T2 es corto (2023 – nov-2026).
- Primeros meses de 2010 con ventana de 52 semanas incompleta (110 operaciones).
