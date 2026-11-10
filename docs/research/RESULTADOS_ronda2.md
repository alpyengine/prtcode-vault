<!-- RESULTADOS_ronda2 · v1.0 · 2026-11-10 -->

# Resultados — Ronda 2 (puertas A, B, C y D)

**Motor:** el mismo motor Python de la matriz homogénea (réplica de los `.pts`), ampliado con las salidas c) y d). 10.000 $ fijos por operación, sin comisiones. Compra a la apertura del día siguiente a la señal. Datos de Twelve Data hasta el 9-nov-2026.

**Tramos:** T1 = 2010-2022 · T2 = 2023 – 9-nov-2026. Una operación pertenece al tramo en el que entra. Las abiertas se valoran al último cierre.

**Salidas:**
- **a)** la elegida: A = cierre bajo la línea ATR diaria · B, C, D = vela entera bajo la EMA50.
- **b)** stop fijo: 2,5 × ATR(14) del día de la señal. Mitad a +2R, resto a +3R.
- **c)** V1: como b), pero al vender la mitad a +2R el stop sube al precio de entrada (rige desde el día siguiente).
- **d)** V2: como b), pero el stop sigue la línea ATR diaria (×2,5 en ETF, ×2 en acciones) y solo puede subir.
- Si en un día se tocan stop y objetivo, cuenta el stop. Los huecos se ejecutan a la apertura.

## 1. Regresión (punto 0)

Repetidos 3 casos de la matriz anterior con el motor nuevo: B en VGT, C en JPM, D en VHT, con salidas a) y b) y en T1 y T2.

**Resultado: 12 de 12 filas idénticas** (operaciones, % ganadoras, medias, ratio, peor operación y tiempo en mercado, a 9 decimales). No hubo que parar.

## 2. Universo

- **20 ETF:** VGT VHT IBB IVV PAVE VFH VAW VXUS VYM VDC SCHD VIG VTV XLE XLF XLK XLP XLU QQQ IWM. `esETF = 1`.
- **40 acciones** (`esETF = 0`): XOM, AAPL, MSFT, WMT, GE, GOOGL, CVX, JNJ, WFC, IBM, PG, JPM, T, KO, PFE, C, BAC, CSCO, ORCL, INTC, PEP, VZ, MRK, HD, AMZN, CMCSA, MCD, ABT, SLB, COP, QCOM, UNH, DIS, AMGN, MMM, UPS, OXY, HPQ, CAT, BRK.B.
- **Twelve Data tiene los 60 valores.** No falta ninguno.
- **Historial corto:** VXUS empieza el 28-ene-2011 y SCHD el 20-oct-2011. Tienen menos operaciones en T1; su tiempo en mercado se mide sobre sus sesiones.
- **Aviso sobre la lista de acciones:** la elegí de memoria como las mayores de EE. UU. por capitalización en 2010. No la he contrastado con un listado oficial. Incluye las que han ido mal (GE, C, BAC, INTC, HPQ, PFE).
- **Sesgo de supervivencia:** Twelve Data solo ofrece valores que cotizan hoy. No hay empresas quebradas ni excluidas del mercado.
- Los precios salen ajustados por splits (sin saltos artificiales). Los mayores movimientos diarios son reales (por ejemplo, petróleo en marzo de 2020).

## 3. Tablas por grupo, puerta, salida y tramo

Todas las operaciones del grupo sumadas. 10.000 $ por operación, sin comisiones. «Todo» = T1 + T2 (2010 – 9-nov-2026). Tiempo en mercado = media por valor. «Mejor valor» = % de la ganancia neta del grupo que aporta el valor con más ganancia (vacío si la ganancia neta del grupo es ≤ 0).

### ETF (20) · puerta A retroceso

| Salida | Tramo | Ops | % gan. | Gan. media | Pérd. media | Ratio | Media/op | Peor op. | Tiempo | Valores con ops | Mejor valor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| a) línea ATR diaria | T1 | 385 | 41 % | 3,2 % | -1,9 % | 1,15 | 0,17 % | -7,6 % | 10 % | 20 |  |
|  | T2 | 134 | 49 % | 4,0 % | -2,4 % | 1,66 | 0,79 % | -9,7 % | 14 % | 20 |  |
|  | Todo | 519 | 43 % | 3,4 % | -2,0 % | 1,29 | 0,33 % | -9,7 % | 11 % | 20 | XLE 41 % |
| b) stop fijo | T1 | 304 | 41 % | 7,7 % | -3,2 % | 1,68 | 1,28 % | -9,2 % | 20 % | 20 |  |
|  | T2 | 114 | 39 % | 7,7 % | -3,8 % | 1,31 | 0,72 % | -9,2 % | 27 % | 20 |  |
|  | Todo | 418 | 41 % | 7,7 % | -3,4 % | 1,56 | 1,13 % | -9,2 % | 22 % | 20 | XLU 12 % |
| c) V1 stop a entrada | T1 | 308 | 42 % | 7,4 % | -3,2 % | 1,63 | 1,19 % | -9,2 % | 20 % | 20 |  |
|  | T2 | 114 | 39 % | 7,4 % | -3,8 % | 1,26 | 0,60 % | -9,2 % | 25 % | 20 |  |
|  | Todo | 422 | 41 % | 7,4 % | -3,4 % | 1,51 | 1,03 % | -9,2 % | 21 % | 20 | XLU 13 % |
| d) V2 stop línea ATR | T1 | 411 | 26 % | 3,8 % | -1,7 % | 1,21 | 0,17 % | -5,4 % | 7 % | 20 |  |
|  | T2 | 148 | 25 % | 4,2 % | -1,7 % | 1,40 | 0,30 % | -4,8 % | 9 % | 20 |  |
|  | Todo | 559 | 25 % | 3,9 % | -1,7 % | 1,26 | 0,21 % | -5,4 % | 8 % | 20 | XLU 36 % |

### ETF (20) · puerta B giro semanal

| Salida | Tramo | Ops | % gan. | Gan. media | Pérd. media | Ratio | Media/op | Peor op. | Tiempo | Valores con ops | Mejor valor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| a) EMA50 | T1 | 446 | 39 % | 5,0 % | -2,7 % | 1,18 | 0,30 % | -10,5 % | 25 % | 20 |  |
|  | T2 | 114 | 51 % | 9,7 % | -2,6 % | 3,79 | 3,62 % | -8,2 % | 31 % | 20 |  |
|  | Todo | 560 | 41 % | 6,1 % | -2,7 % | 1,63 | 0,98 % | -10,5 % | 27 % | 20 | VGT 18 % |
| b) stop fijo | T1 | 392 | 40 % | 10,1 % | -3,6 % | 1,84 | 1,82 % | -7,8 % | 34 % | 20 |  |
|  | T2 | 100 | 58 % | 8,9 % | -3,2 % | 3,80 | 3,79 % | -6,2 % | 37 % | 20 |  |
|  | Todo | 492 | 43 % | 9,7 % | -3,5 % | 2,11 | 2,22 % | -7,8 % | 35 % | 20 | VGT 9 % |
| c) V1 stop a entrada | T1 | 402 | 40 % | 9,7 % | -3,6 % | 1,78 | 1,68 % | -7,8 % | 33 % | 20 |  |
|  | T2 | 104 | 57 % | 8,6 % | -3,2 % | 3,49 | 3,48 % | -6,2 % | 34 % | 20 |  |
|  | Todo | 506 | 43 % | 9,4 % | -3,5 % | 2,02 | 2,05 % | -7,8 % | 34 % | 20 | VGT 11 % |
| d) V2 stop línea ATR | T1 | 450 | 41 % | 3,5 % | -1,8 % | 1,42 | 0,43 % | -6,6 % | 13 % | 20 |  |
|  | T2 | 117 | 40 % | 6,4 % | -1,6 % | 2,88 | 1,68 % | -4,1 % | 12 % | 20 |  |
|  | Todo | 567 | 41 % | 4,1 % | -1,8 % | 1,69 | 0,69 % | -6,6 % | 12 % | 20 | VGT 17 % |

### ETF (20) · puerta C rotura

| Salida | Tramo | Ops | % gan. | Gan. media | Pérd. media | Ratio | Media/op | Peor op. | Tiempo | Valores con ops | Mejor valor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| a) EMA50 | T1 | 242 | 44 % | 5,8 % | -3,2 % | 1,41 | 0,74 % | -8,4 % | 19 % | 20 |  |
|  | T2 | 84 | 43 % | 4,3 % | -2,7 % | 1,18 | 0,28 % | -7,7 % | 19 % | 19 |  |
|  | Todo | 326 | 44 % | 5,4 % | -3,1 % | 1,36 | 0,62 % | -8,4 % | 19 % | 20 | VGT 29 % |
| b) stop fijo | T1 | 268 | 40 % | 6,6 % | -3,0 % | 1,45 | 0,81 % | -8,2 % | 16 % | 20 |  |
|  | T2 | 93 | 40 % | 6,5 % | -3,4 % | 1,25 | 0,51 % | -5,4 % | 20 % | 19 |  |
|  | Todo | 361 | 40 % | 6,6 % | -3,1 % | 1,39 | 0,73 % | -8,2 % | 17 % | 20 | IBB 28 % |
| c) V1 stop a entrada | T1 | 269 | 39 % | 6,4 % | -3,0 % | 1,40 | 0,73 % | -8,2 % | 15 % | 20 |  |
|  | T2 | 93 | 40 % | 6,4 % | -3,4 % | 1,23 | 0,48 % | -5,4 % | 18 % | 19 |  |
|  | Todo | 362 | 40 % | 6,4 % | -3,1 % | 1,35 | 0,66 % | -8,2 % | 16 % | 20 | IBB 27 % |
| d) V2 stop línea ATR | T1 | 306 | 41 % | 3,0 % | -2,0 % | 1,06 | 0,07 % | -5,9 % | 8 % | 20 |  |
|  | T2 | 107 | 41 % | 3,1 % | -1,9 % | 1,14 | 0,15 % | -4,2 % | 9 % | 19 |  |
|  | Todo | 413 | 41 % | 3,1 % | -2,0 % | 1,08 | 0,09 % | -5,9 % | 8 % | 20 | VGT 109 % |

### ETF (20) · puerta D cruce de medias

| Salida | Tramo | Ops | % gan. | Gan. media | Pérd. media | Ratio | Media/op | Peor op. | Tiempo | Valores con ops | Mejor valor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| a) EMA50 | T1 | 641 | 37 % | 5,2 % | -2,1 % | 1,50 | 0,65 % | -10,4 % | 34 % | 20 |  |
|  | T2 | 206 | 33 % | 6,2 % | -2,4 % | 1,22 | 0,36 % | -8,9 % | 31 % | 20 |  |
|  | Todo | 847 | 36 % | 5,5 % | -2,2 % | 1,42 | 0,58 % | -10,4 % | 34 % | 20 | XLK 21 % |
| b) stop fijo | T1 | 416 | 45 % | 7,7 % | -3,7 % | 1,69 | 1,39 % | -8,9 % | 35 % | 20 |  |
|  | T2 | 138 | 45 % | 7,2 % | -3,8 % | 1,54 | 1,14 % | -8,0 % | 35 % | 20 |  |
|  | Todo | 554 | 45 % | 7,5 % | -3,7 % | 1,65 | 1,33 % | -8,9 % | 35 % | 20 | VGT 12 % |
| c) V1 stop a entrada | T1 | 427 | 45 % | 7,5 % | -3,7 % | 1,71 | 1,42 % | -8,9 % | 34 % | 20 |  |
|  | T2 | 144 | 46 % | 7,2 % | -3,8 % | 1,58 | 1,21 % | -8,0 % | 31 % | 20 |  |
|  | Todo | 571 | 46 % | 7,4 % | -3,7 % | 1,67 | 1,37 % | -8,9 % | 34 % | 20 | IBB 13 % |
| d) V2 stop línea ATR | T1 | 771 | 26 % | 3,7 % | -1,8 % | 1,54 | 0,33 % | -7,2 % | 14 % | 20 |  |
|  | T2 | 243 | 26 % | 4,2 % | -2,2 % | 1,28 | 0,24 % | -5,1 % | 14 % | 20 |  |
|  | Todo | 1014 | 26 % | 3,8 % | -1,9 % | 1,46 | 0,31 % | -7,2 % | 14 % | 20 | XLK 22 % |

### Acciones (40) · puerta A retroceso

| Salida | Tramo | Ops | % gan. | Gan. media | Pérd. media | Ratio | Media/op | Peor op. | Tiempo | Valores con ops | Mejor valor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| a) línea ATR diaria | T1 | 865 | 39 % | 4,3 % | -2,4 % | 1,15 | 0,21 % | -17,1 % | 9 % | 40 |  |
|  | T2 | 284 | 45 % | 4,9 % | -2,7 % | 1,53 | 0,76 % | -10,1 % | 8 % | 40 |  |
|  | Todo | 1149 | 40 % | 4,4 % | -2,4 % | 1,24 | 0,35 % | -17,1 % | 9 % | 40 | HPQ 23 % |
| b) stop fijo | T1 | 660 | 37 % | 10,1 % | -5,0 % | 1,18 | 0,57 % | -16,3 % | 21 % | 40 |  |
|  | T2 | 215 | 39 % | 11,4 % | -5,6 % | 1,28 | 0,96 % | -19,4 % | 20 % | 40 |  |
|  | Todo | 875 | 37 % | 10,4 % | -5,1 % | 1,21 | 0,67 % | -19,4 % | 20 % | 40 | MSFT 20 % |
| c) V1 stop a entrada | T1 | 663 | 37 % | 9,9 % | -5,0 % | 1,17 | 0,55 % | -16,3 % | 20 % | 40 |  |
|  | T2 | 218 | 39 % | 11,3 % | -5,6 % | 1,29 | 0,98 % | -19,4 % | 18 % | 40 |  |
|  | Todo | 881 | 38 % | 10,3 % | -5,1 % | 1,20 | 0,65 % | -19,4 % | 19 % | 40 | MSFT 20 % |
| d) V2 stop línea ATR | T1 | 942 | 24 % | 4,6 % | -2,1 % | 1,20 | 0,19 % | -15,2 % | 6 % | 40 |  |
|  | T2 | 306 | 19 % | 6,1 % | -2,1 % | 1,20 | 0,19 % | -7,9 % | 5 % | 40 |  |
|  | Todo | 1248 | 23 % | 4,9 % | -2,1 % | 1,20 | 0,19 % | -15,2 % | 6 % | 40 | MSFT 21 % |

### Acciones (40) · puerta B giro semanal

| Salida | Tramo | Ops | % gan. | Gan. media | Pérd. media | Ratio | Media/op | Peor op. | Tiempo | Valores con ops | Mejor valor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| a) EMA50 | T1 | 771 | 36 % | 10,1 % | -3,9 % | 1,46 | 1,15 % | -16,2 % | 23 % | 40 |  |
|  | T2 | 223 | 48 % | 13,1 % | -4,9 % | 2,52 | 3,81 % | -20,8 % | 26 % | 40 |  |
|  | Todo | 994 | 39 % | 10,9 % | -4,1 % | 1,70 | 1,75 % | -20,8 % | 24 % | 40 | GE 13 % |
| b) stop fijo | T1 | 704 | 39 % | 12,4 % | -5,2 % | 1,54 | 1,71 % | -24,1 % | 28 % | 40 |  |
|  | T2 | 206 | 46 % | 12,9 % | -6,0 % | 1,80 | 2,63 % | -18,7 % | 26 % | 39 |  |
|  | Todo | 910 | 41 % | 12,5 % | -5,4 % | 1,60 | 1,92 % | -24,1 % | 28 % | 40 | GOOGL 8 % |
| c) V1 stop a entrada | T1 | 713 | 39 % | 11,9 % | -5,2 % | 1,48 | 1,51 % | -24,1 % | 27 % | 40 |  |
|  | T2 | 217 | 46 % | 12,7 % | -6,0 % | 1,78 | 2,54 % | -18,7 % | 23 % | 40 |  |
|  | Todo | 930 | 41 % | 12,1 % | -5,4 % | 1,55 | 1,75 % | -24,1 % | 26 % | 40 | GOOGL 8 % |
| d) V2 stop línea ATR | T1 | 783 | 34 % | 4,4 % | -2,3 % | 1,10 | 0,14 % | -12,9 % | 8 % | 40 |  |
|  | T2 | 230 | 37 % | 7,3 % | -2,3 % | 2,19 | 1,46 % | -8,3 % | 6 % | 40 |  |
|  | Todo | 1013 | 35 % | 5,1 % | -2,3 % | 1,32 | 0,44 % | -12,9 % | 7 % | 40 | AAPL 20 % |

### Acciones (40) · puerta C rotura

| Salida | Tramo | Ops | % gan. | Gan. media | Pérd. media | Ratio | Media/op | Peor op. | Tiempo | Valores con ops | Mejor valor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| a) EMA50 | T1 | 300 | 46 % | 10,3 % | -4,9 % | 1,80 | 2,11 % | -23,0 % | 13 % | 40 |  |
|  | T2 | 93 | 41 % | 14,1 % | -5,6 % | 1,73 | 2,42 % | -21,4 % | 12 % | 37 |  |
|  | Todo | 393 | 45 % | 11,1 % | -5,1 % | 1,78 | 2,19 % | -23,0 % | 13 % | 40 | CAT 26 % |
| b) stop fijo | T1 | 337 | 44 % | 10,0 % | -4,7 % | 1,68 | 1,78 % | -12,4 % | 11 % | 40 |  |
|  | T2 | 103 | 39 % | 12,4 % | -5,8 % | 1,35 | 1,24 % | -14,3 % | 11 % | 37 |  |
|  | Todo | 440 | 43 % | 10,5 % | -5,0 % | 1,58 | 1,66 % | -14,3 % | 11 % | 40 | INTC 13 % |
| c) V1 stop a entrada | T1 | 339 | 44 % | 9,6 % | -4,7 % | 1,64 | 1,65 % | -12,4 % | 10 % | 40 |  |
|  | T2 | 104 | 39 % | 11,6 % | -5,8 % | 1,29 | 1,03 % | -14,3 % | 10 % | 37 |  |
|  | Todo | 443 | 43 % | 10,0 % | -4,9 % | 1,54 | 1,51 % | -14,3 % | 10 % | 40 | INTC 14 % |
| d) V2 stop línea ATR | T1 | 379 | 41 % | 4,9 % | -2,5 % | 1,41 | 0,59 % | -10,2 % | 4 % | 40 |  |
|  | T2 | 117 | 42 % | 5,8 % | -3,4 % | 1,25 | 0,48 % | -9,5 % | 4 % | 37 |  |
|  | Todo | 496 | 42 % | 5,1 % | -2,7 % | 1,36 | 0,56 % | -10,2 % | 4 % | 40 | AAPL 18 % |

### Acciones (40) · puerta D cruce de medias

| Salida | Tramo | Ops | % gan. | Gan. media | Pérd. media | Ratio | Media/op | Peor op. | Tiempo | Valores con ops | Mejor valor |
|---|---|---|---|---|---|---|---|---|---|---|---|
| a) EMA50 | T1 | 502 | 37 % | 7,9 % | -2,9 % | 1,63 | 1,13 % | -12,7 % | 13 % | 40 |  |
|  | T2 | 115 | 39 % | 9,7 % | -3,8 % | 1,66 | 1,52 % | -15,5 % | 10 % | 38 |  |
|  | Todo | 617 | 38 % | 8,3 % | -3,1 % | 1,63 | 1,21 % | -15,5 % | 12 % | 40 | C 14 % |
| b) stop fijo | T1 | 393 | 41 % | 10,9 % | -4,7 % | 1,64 | 1,76 % | -13,3 % | 14 % | 40 |  |
|  | T2 | 92 | 52 % | 12,4 % | -5,2 % | 2,60 | 3,98 % | -9,8 % | 11 % | 38 |  |
|  | Todo | 485 | 44 % | 11,2 % | -4,8 % | 1,81 | 2,18 % | -13,3 % | 13 % | 40 | BAC 9 % |
| c) V1 stop a entrada | T1 | 401 | 42 % | 10,5 % | -4,7 % | 1,61 | 1,67 % | -13,3 % | 13 % | 40 |  |
|  | T2 | 95 | 54 % | 11,7 % | -5,2 % | 2,61 | 3,88 % | -9,8 % | 9 % | 38 |  |
|  | Todo | 496 | 44 % | 10,8 % | -4,8 % | 1,78 | 2,09 % | -13,3 % | 12 % | 40 | BAC 10 % |
| d) V2 stop línea ATR | T1 | 602 | 24 % | 5,0 % | -2,1 % | 1,71 | 0,51 % | -8,3 % | 4 % | 40 |  |
|  | T2 | 137 | 18 % | 5,6 % | -2,3 % | 1,14 | 0,12 % | -5,4 % | 2 % | 38 |  |
|  | Todo | 739 | 23 % | 5,1 % | -2,2 % | 1,59 | 0,44 % | -8,3 % | 3 % | 40 | COP 14 % |

## 4. Criterio de asignación de puerta a grupo

Regla: ratio > 1,5 en conjunto, > 1 en T1 y en T2 por separado, y al menos 30 operaciones por grupo y tramo. Se evalúa cada salida.

### ETF (20)

| Puerta | Salida | Ratio todo | Ratio T1 | Ratio T2 | Ops T1 | Ops T2 | Estado |
|---|---|---|---|---|---|---|---|
| A retroceso | a) línea ATR diaria | 1,29 | 1,15 | 1,66 | 385 | 134 | **NO CUMPLE** |
|  | b) stop fijo | 1,56 | 1,68 | 1,31 | 304 | 114 | **CUMPLE** |
|  | c) V1 stop a entrada | 1,51 | 1,63 | 1,26 | 308 | 114 | **CUMPLE** |
|  | d) V2 stop línea ATR | 1,26 | 1,21 | 1,40 | 411 | 148 | **NO CUMPLE** |
| B giro semanal | a) EMA50 | 1,63 | 1,18 | 3,79 | 446 | 114 | **CUMPLE** |
|  | b) stop fijo | 2,11 | 1,84 | 3,80 | 392 | 100 | **CUMPLE** |
|  | c) V1 stop a entrada | 2,02 | 1,78 | 3,49 | 402 | 104 | **CUMPLE** |
|  | d) V2 stop línea ATR | 1,69 | 1,42 | 2,88 | 450 | 117 | **CUMPLE** |
| C rotura | a) EMA50 | 1,36 | 1,41 | 1,18 | 242 | 84 | **NO CUMPLE** |
|  | b) stop fijo | 1,39 | 1,45 | 1,25 | 268 | 93 | **NO CUMPLE** |
|  | c) V1 stop a entrada | 1,35 | 1,40 | 1,23 | 269 | 93 | **NO CUMPLE** |
|  | d) V2 stop línea ATR | 1,08 | 1,06 | 1,14 | 306 | 107 | **NO CUMPLE** |
| D cruce de medias | a) EMA50 | 1,42 | 1,50 | 1,22 | 641 | 206 | **NO CUMPLE** |
|  | b) stop fijo | 1,65 | 1,69 | 1,54 | 416 | 138 | **CUMPLE** |
|  | c) V1 stop a entrada | 1,67 | 1,71 | 1,58 | 427 | 144 | **CUMPLE** |
|  | d) V2 stop línea ATR | 1,46 | 1,54 | 1,28 | 771 | 243 | **NO CUMPLE** |

### Acciones (40)

| Puerta | Salida | Ratio todo | Ratio T1 | Ratio T2 | Ops T1 | Ops T2 | Estado |
|---|---|---|---|---|---|---|---|
| A retroceso | a) línea ATR diaria | 1,24 | 1,15 | 1,53 | 865 | 284 | **NO CUMPLE** |
|  | b) stop fijo | 1,21 | 1,18 | 1,28 | 660 | 215 | **NO CUMPLE** |
|  | c) V1 stop a entrada | 1,20 | 1,17 | 1,29 | 663 | 218 | **NO CUMPLE** |
|  | d) V2 stop línea ATR | 1,20 | 1,20 | 1,20 | 942 | 306 | **NO CUMPLE** |
| B giro semanal | a) EMA50 | 1,70 | 1,46 | 2,52 | 771 | 223 | **CUMPLE** |
|  | b) stop fijo | 1,60 | 1,54 | 1,80 | 704 | 206 | **CUMPLE** |
|  | c) V1 stop a entrada | 1,55 | 1,48 | 1,78 | 713 | 217 | **CUMPLE** |
|  | d) V2 stop línea ATR | 1,32 | 1,10 | 2,19 | 783 | 230 | **NO CUMPLE** |
| C rotura | a) EMA50 | 1,78 | 1,80 | 1,73 | 300 | 93 | **CUMPLE** |
|  | b) stop fijo | 1,58 | 1,68 | 1,35 | 337 | 103 | **CUMPLE** |
|  | c) V1 stop a entrada | 1,54 | 1,64 | 1,29 | 339 | 104 | **CUMPLE** |
|  | d) V2 stop línea ATR | 1,36 | 1,41 | 1,25 | 379 | 117 | **NO CUMPLE** |
| D cruce de medias | a) EMA50 | 1,63 | 1,63 | 1,66 | 502 | 115 | **CUMPLE** |
|  | b) stop fijo | 1,81 | 1,64 | 2,60 | 393 | 92 | **CUMPLE** |
|  | c) V1 stop a entrada | 1,78 | 1,61 | 2,61 | 401 | 95 | **CUMPLE** |
|  | d) V2 stop línea ATR | 1,59 | 1,71 | 1,14 | 602 | 137 | **CUMPLE** |

## 5. Variantes de stop (c y d frente a b)

Regla: se adopta solo si el ratio mejora el de b) en ETF y en acciones, y en T1 y en T2 (los cuatro casos). Ratios b) → variante.

| Puerta | Variante | ETF T1 | ETF T2 | Acc. T1 | Acc. T2 | Decisión |
|---|---|---|---|---|---|---|
| A retroceso | c) V1 stop a entrada | 1,68 → 1,63 | 1,31 → 1,26 | 1,18 → 1,17 | 1,28 → 1,29 | **NO ADOPTAR** |
|  | d) V2 stop línea ATR | 1,68 → 1,21 | 1,31 → 1,40 | 1,18 → 1,20 | 1,28 → 1,20 | **NO ADOPTAR** |
| B giro semanal | c) V1 stop a entrada | 1,84 → 1,78 | 3,80 → 3,49 | 1,54 → 1,48 | 1,80 → 1,78 | **NO ADOPTAR** |
|  | d) V2 stop línea ATR | 1,84 → 1,42 | 3,80 → 2,88 | 1,54 → 1,10 | 1,80 → 2,19 | **NO ADOPTAR** |
| C rotura | c) V1 stop a entrada | 1,45 → 1,40 | 1,25 → 1,23 | 1,68 → 1,64 | 1,35 → 1,29 | **NO ADOPTAR** |
|  | d) V2 stop línea ATR | 1,45 → 1,06 | 1,25 → 1,14 | 1,68 → 1,41 | 1,35 → 1,25 | **NO ADOPTAR** |
| D cruce de medias | c) V1 stop a entrada | 1,69 → 1,71 | 1,54 → 1,58 | 1,64 → 1,61 | 2,60 → 2,61 | **NO ADOPTAR** |
|  | d) V2 stop línea ATR | 1,69 → 1,54 | 1,54 → 1,28 | 1,64 → 1,71 | 2,60 → 1,14 | **NO ADOPTAR** |

## 6. Concentración (salida a)

| Puerta | Grupo | Mejor valor | % de la ganancia neta | Valores con ops |
|---|---|---|---|---|
| A retroceso | ETF (20) | XLE | 41 % ⚠ | 20 |
| A retroceso | Acciones (40) | HPQ | 23 % | 40 |
| B giro semanal | ETF (20) | VGT | 18 % | 20 |
| B giro semanal | Acciones (40) | GE | 13 % | 40 |
| C rotura | ETF (20) | VGT | 29 % ⚠ | 20 |
| C rotura | Acciones (40) | CAT | 26 % ⚠ | 40 |
| D cruce de medias | ETF (20) | XLK | 21 % | 20 |
| D cruce de medias | Acciones (40) | C | 14 % | 40 |

## 7. Resumen del criterio

**Asignación de puerta a grupo (todas las combinaciones tienen ≥ 30 operaciones por tramo; ninguna es MUESTRA INSUFICIENTE):**

| Puerta | ETF | Acciones |
|---|---|---|
| A retroceso | a) NO · b) CUMPLE · c) CUMPLE · d) NO | NO en las 4 salidas |
| B giro semanal | CUMPLE en las 4 salidas | a), b), c) CUMPLE · d) NO |
| C rotura | NO en las 4 salidas | a), b), c) CUMPLE · d) NO |
| D cruce de medias | a) NO · b) CUMPLE · c) CUMPLE · d) NO | CUMPLE en las 4 salidas |

**Con la salida elegida a): CUMPLE** B en ETF y B, C y D en acciones. **NO CUMPLE** A (en ETF 1,29 y en acciones 1,24), C en ETF (1,36) y D en ETF (1,42).

**Variantes de stop:** ninguna se adopta. Ni c) ni d) mejoran el ratio de b) en los cuatro casos (ETF T1, ETF T2, acciones T1, acciones T2). c) queda casi igual que b) y d) empeora en la mayoría.

**Concentración:** C en acciones depende de CAT (26 % de la ganancia neta) y C en ETF de VGT (29 %). A en ETF depende de XLE (41 %).

## 8. Límites

- Resultados de Python. ProRealTime no se ha ejecutado para esta ronda, y la salida del sistema (b, c, d) no existe aún en los `.pts`.
- El tramo T2 es corto (2023-2026) y está dominado por un mercado alcista.
- Las 3 salidas de sistema usan el ATR(14) del día de la señal, con el mismo tamaño de riesgo en todos los valores.
