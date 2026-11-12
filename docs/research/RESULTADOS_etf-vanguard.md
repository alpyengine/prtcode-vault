<!-- RESULTADOS_etf-vanguard · v1.0 · 2026-11-10 -->

# Resultados — Puertas A, B, C y D en los ETF de Vanguard

**Motor:** el mismo de la ronda 2 (Python, réplica de los `.pts`). 10.000 $ por operación, sin comisiones ni diferencial. `esETF = 1`. Datos de Twelve Data hasta el 9-nov-2026.

**Tramos:** T1 = 2010-2022 · T2 = 2023 – 9-nov-2026. Una operación pertenece al tramo en el que entra.

**Salidas:**
- **a)** la elegida: A = cierre bajo la línea ATR diaria · B, C, D = vela entera bajo la EMA50.
- **b)** stop fijo: 2,5 × ATR(14) del día de la señal, mitad a +2R y resto a +3R.

## 1. Universo: 55 ETF de Vanguard

Los 9 que ya tenía de la ronda 2 más 46 nuevos. Agrupados por tipo, porque la renta fija y la renta variable no se pueden mezclar.

| Grupo | ETF |
|---|---|
| Renta variable EE.UU. (17) | VTI VOO VV VO VB VUG VOE VOT VBR VBK VXF VIOO VOOG VOOV VYM VIG VTV |
| Sectores EE.UU. (11) | VGT VHT VFH VAW VDC VCR VDE VIS VNQ VOX VPU |
| Internacional (11) | VEA VWO VEU VSS VGK VPL VYMI VIGI VT VNQI VXUS |
| Renta fija (16) | BND BNDX BSV BIV BLV VCIT VCSH VCLT VGIT VGSH VGLT VMBS VTIP VTEB EDV VTC |

- Twelve Data tiene los 55. No falta ninguno.
- **Historial corto** (menos operaciones en T1): VOO, VIOO, VOOG y VOOV desde sep-2010 · VNQI desde nov-2010 · VXUS desde ene-2011 · VTIP desde oct-2012 · BNDX desde jun-2013 · VTEB desde ago-2015 · VYMI y VIGI desde mar-2016 · VTC desde nov-2017.
- **No es una lista oficial.** Son los ETF de Vanguard que conozco con cotización en EE. UU.; si falta alguno, dímelo. Quedan fuera los ETF de Vanguard que cotizan en Europa (UCITS).
- **Dato corregido:** Twelve Data devolvía VIOO sin ajustar por el split 2:1 del 7-mar-2023 (el precio caía de 186 a 92 de un día para otro). Dividí entre 2 los precios anteriores y multipliqué por 2 el volumen. Revisé todos los valores descargados en las dos rondas y es el único caso.
- **Mucho solapamiento:** VTI, VOO, VV, VOOG y VOOV son casi el mismo mercado. Que «cumplan 9 de 17» no significa 9 resultados independientes.

## 2. Criterio por grupo de ETF (todas las operaciones sumadas)

Regla de la ronda 2: ratio > 1,5 en conjunto, > 1 en T1 y en T2, y al menos 30 operaciones por tramo. Salida a) y salida b) (stop fijo).

### Renta variable EE.UU. (amplia y estilo) (17 ETF)

| Puerta | Salida | Ops T1 | Ops T2 | % gan. | Ratio todo | Ratio T1 | Ratio T2 | Media/op | Peor op. | Tiempo | Mejor ETF | Estado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A retroceso | a) línea ATR | 322 | 132 | 47 % | 1,06 | 0,81 | 2,00 | 0,07 % | -8,0 % | 10 % | VOOG 92 % | **NO CUMPLE** |
|  | b) stop fijo | 255 | 101 | 44 % | 1,80 | 1,67 | 2,15 | 1,36 % | -7,4 % | 24 % | VOE 14 % | **CUMPLE** |
| B giro semanal | a) EMA50 | 393 | 103 | 42 % | 1,65 | 1,09 | 6,20 | 0,97 % | -7,0 % | 30 % | VUG 15 % | **CUMPLE** |
|  | b) stop fijo | 348 | 93 | 45 % | 2,22 | 1,74 | 5,57 | 2,14 % | -7,5 % | 37 % | VUG 13 % | **CUMPLE** |
| C rotura | a) EMA50 | 221 | 83 | 48 % | 1,60 | 1,72 | 1,34 | 0,98 % | -9,9 % | 23 % | VXF 16 % | **CUMPLE** |
|  | b) stop fijo | 250 | 88 | 43 % | 1,58 | 1,75 | 1,21 | 0,92 % | -5,2 % | 21 % | VUG 22 % | **CUMPLE** |
| D cruce de medias | a) EMA50 | 635 | 163 | 37 % | 1,46 | 1,50 | 1,33 | 0,57 % | -8,9 % | 39 % | VTI 12 % | **NO CUMPLE** |
|  | b) stop fijo | 366 | 122 | 46 % | 1,70 | 1,69 | 1,75 | 1,35 % | -8,1 % | 38 % | VOOG 13 % | **CUMPLE** |

### Sectores EE.UU. (11 ETF)

| Puerta | Salida | Ops T1 | Ops T2 | % gan. | Ratio todo | Ratio T1 | Ratio T2 | Media/op | Peor op. | Tiempo | Mejor ETF | Estado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A retroceso | a) línea ATR | 219 | 73 | 38 % | 0,97 | 0,79 | 1,54 | -0,03 % | -7,6 % | 9 % | — | **NO CUMPLE** |
|  | b) stop fijo | 161 | 58 | 38 % | 1,35 | 1,40 | 1,22 | 0,74 % | -8,4 % | 19 % | VAW 29 % | **NO CUMPLE** |
| B giro semanal | a) EMA50 | 253 | 62 | 38 % | 1,44 | 1,16 | 2,76 | 0,75 % | -8,0 % | 26 % | VGT 43 % | **NO CUMPLE** |
|  | b) stop fijo | 228 | 53 | 39 % | 1,72 | 1,54 | 2,85 | 1,61 % | -7,4 % | 32 % | VGT 23 % | **CUMPLE** |
| C rotura | a) EMA50 | 136 | 50 | 38 % | 1,02 | 1,06 | 0,92 | 0,05 % | -14,3 % | 18 % | VGT (ganancia neta casi nula) | **NO CUMPLE** |
|  | b) stop fijo | 151 | 54 | 36 % | 1,20 | 1,18 | 1,27 | 0,43 % | -10,7 % | 16 % | VGT 50 % | **NO CUMPLE** |
| D cruce de medias | a) EMA50 | 362 | 119 | 38 % | 1,36 | 1,53 | 1,00 | 0,52 % | -8,8 % | 33 % | VGT 40 % | **NO CUMPLE** |
|  | b) stop fijo | 248 | 74 | 41 % | 1,48 | 1,55 | 1,27 | 1,05 % | -9,1 % | 34 % | VGT 27 % | **NO CUMPLE** |

### Internacional (11 ETF)

| Puerta | Salida | Ops T1 | Ops T2 | % gan. | Ratio todo | Ratio T1 | Ratio T2 | Media/op | Peor op. | Tiempo | Mejor ETF | Estado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A retroceso | a) línea ATR | 116 | 48 | 32 % | 0,49 | 0,42 | 0,77 | -0,63 % | -5,9 % | 4 % | — | **NO CUMPLE** |
|  | b) stop fijo | 108 | 47 | 27 % | 0,63 | 0,51 | 1,00 | -0,85 % | -8,1 % | 11 % | — | **NO CUMPLE** |
| B giro semanal | a) EMA50 | 192 | 73 | 38 % | 1,44 | 1,11 | 2,68 | 0,63 % | -6,5 % | 25 % | VNQI 22 % | **NO CUMPLE** |
|  | b) stop fijo | 180 | 56 | 36 % | 1,33 | 1,05 | 2,86 | 0,68 % | -6,4 % | 30 % | VYMI 31 % | **NO CUMPLE** |
| C rotura | a) EMA50 | 120 | 67 | 35 % | 0,87 | 1,26 | 0,35 | -0,27 % | -13,7 % | 19 % | — | **NO CUMPLE** |
|  | b) stop fijo | 141 | 73 | 34 % | 0,96 | 1,20 | 0,61 | -0,07 % | -6,0 % | 16 % | — | **NO CUMPLE** |
| D cruce de medias | a) EMA50 | 266 | 145 | 29 % | 0,91 | 0,96 | 0,81 | -0,13 % | -9,8 % | 25 % | — | **NO CUMPLE** |
|  | b) stop fijo | 187 | 84 | 35 % | 0,95 | 0,88 | 1,11 | -0,11 % | -7,8 % | 27 % | — | **NO CUMPLE** |

### Renta fija (16 ETF)

| Puerta | Salida | Ops T1 | Ops T2 | % gan. | Ratio todo | Ratio T1 | Ratio T2 | Media/op | Peor op. | Tiempo | Mejor ETF | Estado |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A retroceso | a) línea ATR | 253 | 62 | 37 % | 0,88 | 1,26 | 0,16 | -0,04 % | -5,2 % | 6 % | — | **NO CUMPLE** |
|  | b) stop fijo | 188 | 55 | 33 % | 0,93 | 1,26 | 0,33 | -0,06 % | -6,4 % | 18 % | — | **NO CUMPLE** |
| B giro semanal | a) EMA50 | 238 | 78 | 38 % | 1,45 | 1,81 | 0,55 | 0,29 % | -6,0 % | 17 % | VGLT 32 % | **NO CUMPLE** |
|  | b) stop fijo | 217 | 66 | 44 % | 1,34 | 1,51 | 0,76 | 0,31 % | -10,0 % | 31 % | VGLT 39 % | **NO CUMPLE** |
| C rotura | a) EMA50 | 84 | 29 | 42 % | 0,94 | 1,06 | 0,27 | -0,07 % | -16,1 % | 9 % | — | **MUESTRA INSUFICIENTE** |
|  | b) stop fijo | 105 | 31 | 49 % | 1,76 | 2,05 | 0,67 | 0,56 % | -9,9 % | 6 % | EDV 50 % | **NO CUMPLE** |
| D cruce de medias | a) EMA50 | 258 | 90 | 26 % | 1,14 | 1,21 | 0,78 | 0,08 % | -8,0 % | 14 % | EDV (ganancia neta casi nula) | **NO CUMPLE** |
|  | b) stop fijo | 186 | 54 | 34 % | 0,97 | 0,98 | 0,90 | -0,03 % | -14,0 % | 17 % | — | **NO CUMPLE** |

## 3. Resultado por ETF (salida a)

Ratio total · T1 · T2 y operaciones totales. ✓ = ratio total > 1,5 y > 1 en T1 y en T2. Con pocas operaciones por ETF, el ✓ es solo orientativo. Entre paréntesis, operaciones.

### Renta variable EE.UU. (amplia y estilo)

| ETF | Desde | A retroceso | B giro semanal | C rotura | D cruce de medias |
|---|---|---|---|---|---|
| VTI | 2009-06 | 1,5 · 1,6 · 1,3 (22) ✓ | 2,2 · 1,3 · 10,4 (31) ✓ | 2,7 · 2,6 · 3,4 (22) ✓ | 2,2 · 2,2 · 2,4 (45) ✓ |
| VOO | 2010-09 | 2,4 · 2,1 · 3,4 (24) ✓ | 2,7 · 1,4 · 14,9 (27) ✓ | 2,8 · 2,5 · 3,5 (17) ✓ | 1,9 · 1,7 · 2,7 (44) ✓ |
| VV | 2009-06 | 1,4 · 1,3 · 1,6 (24) | 2,0 · 1,0 · 13,4 (30) | 1,7 · 1,6 · 2,2 (22) ✓ | 1,6 · 1,4 · 2,1 (49) ✓ |
| VO | 2009-06 | 1,6 · 1,1 · 4,3 (25) ✓ | 2,1 · 1,6 · 6,4 (28) ✓ | 2,7 · 6,1 · 0,3 (13) | 1,8 · 1,9 · 1,4 (45) ✓ |
| VB | 2009-06 | 0,5 · 0,5 · 0,4 (35) | 1,4 · 1,2 · 2,9 (26) | 1,1 · 2,9 · 0,0 (15) | 0,9 · 1,1 · 0,4 (45) |
| VUG | 2009-06 | 2,1 · 2,0 · 2,5 (18) ✓ | 2,6 · 1,6 · 29,6 (29) ✓ | 2,7 · 2,2 · 6,8 (25) ✓ | 1,7 · 1,8 · 1,4 (54) ✓ |
| VOE | 2009-06 | 1,7 · 0,9 · 329,1 (29) | 1,5 · 1,0 · 3,7 (30) | 0,4 · 0,4 · 0,4 (18) | 1,2 · 1,2 · 1,5 (40) |
| VOT | 2009-06 | 1,0 · 0,5 · 9,5 (29) | 2,4 · 1,5 · 15,5 (29) ✓ | 1,2 · 1,0 · 2,0 (19) | 1,9 · 2,5 · 0,5 (48) |
| VBR | 2009-06 | 0,5 · 0,2 · 1,4 (38) | 1,0 · 1,0 · 0,8 (29) | 1,6 · 3,0 · 0,7 (14) | 0,7 · 0,7 · 0,6 (43) |
| VBK | 2009-06 | 0,5 · 0,3 · 1,3 (26) | 1,8 · 1,2 · ∞ (26) ✓ | 0,9 · 1,0 · 0,3 (18) | 1,3 · 1,9 · 0,4 (44) |
| VXF | 2009-06 | 0,7 · 0,6 · 1,0 (33) | 2,0 · 1,3 · 8,4 (25) ✓ | 2,8 · 4,1 · 1,3 (15) ✓ | 1,4 · 1,6 · 0,7 (45) |
| VIOO | 2010-09 | 0,7 · 0,4 · 1,8 (29) | 0,5 · 0,5 · 1,1 (30) | 1,6 · 3,6 · 0,0 (16) | 1,3 · 1,4 · 1,0 (48) |
| VOOG | 2010-09 | 1,9 · 2,2 · 1,5 (23) ✓ | 1,8 · 0,7 · 9,4 (28) | 2,4 · 1,3 · 5,7 (24) ✓ | 1,8 · 1,8 · 1,7 (51) ✓ |
| VOOV | 2010-09 | 1,1 · 0,9 · 1,8 (24) | 1,5 · 1,2 · 5,8 (32) ✓ | 1,0 · 0,4 · 2,3 (18) | 1,7 · 1,4 · 3,3 (47) ✓ |
| VYM | 2009-06 | 1,1 · 0,8 · 1,9 (22) | 0,7 · 0,7 · 0,5 (33) | 1,2 · 1,5 · 0,5 (15) | 1,0 · 0,8 · 2,7 (47) |
| VIG | 2009-06 | 1,1 · 0,7 · 2,9 (32) | 1,1 · 0,3 · 7,0 (29) | 0,6 · 0,5 · 1,4 (19) | 1,4 · 1,2 · 2,6 (51) |
| VTV | 2009-06 | 1,0 · 0,5 · 4,8 (21) | 1,6 · 1,2 · 4,0 (34) ✓ | 1,8 · 1,5 · 5,9 (14) ✓ | 1,3 · 1,0 · 3,2 (52) |

### Sectores EE.UU.

| ETF | Desde | A retroceso | B giro semanal | C rotura | D cruce de medias |
|---|---|---|---|---|---|
| VGT | 2009-06 | 1,8 · 3,9 · 1,2 (26) ✓ | 3,3 · 2,0 · 14,3 (29) ✓ | 2,3 · 1,5 · 7,6 (25) ✓ | 2,2 · 2,4 · 1,9 (52) ✓ |
| VHT | 2009-06 | 1,2 · 0,7 · 2,3 (28) | 2,1 · 1,8 · 3,7 (30) ✓ | 1,7 · 2,1 · 1,0 (20) ✓ | 2,8 · 3,8 · 1,0 (39) ✓ |
| VFH | 2009-06 | 0,5 · 0,1 · 5,3 (22) | 1,2 · 1,1 · 1,4 (33) | 1,3 · 2,1 · 0,5 (14) | 1,4 · 1,5 · 0,9 (43) |
| VAW | 2009-06 | 0,8 · 1,1 · 0,1 (30) | 0,7 · 0,7 · 0,6 (32) | 0,5 · 0,7 · 0,0 (19) | 0,6 · 0,6 · 0,7 (46) |
| VDC | 2009-06 | 1,2 · 0,9 · 2,7 (23) | 1,0 · 1,2 · 0,6 (26) | 0,2 · 0,3 · 0,0 (14) | 1,1 · 1,4 · 0,6 (52) |
| VCR | 2009-06 | 1,8 · 1,2 · 3,9 (24) ✓ | 1,5 · 1,3 · 2,0 (31) ✓ | 1,9 · 1,8 · 3,1 (21) ✓ | 1,9 · 2,2 · 1,2 (52) ✓ |
| VDE | 2009-06 | 0,9 · 0,9 · 1,0 (20) | 1,7 · 1,7 · 1,8 (26) ✓ | 0,7 · 0,7 · 0,7 (15) | 0,7 · 1,1 · 0,0 (34) |
| VIS | 2009-06 | 1,1 · 0,5 · 2,7 (19) | 1,5 · 0,9 · 4,0 (31) | 1,1 · 0,8 · 1,7 (19) | 1,5 · 1,4 · 1,7 (54) ✓ |
| VNQ | 2009-06 | 0,5 · 0,3 · 1,2 (43) | 0,5 · 0,5 · 0,3 (23) | 0,2 · 0,3 · 0,0 (11) | 0,4 · 0,4 · 0,3 (32) |
| VOX | 2009-06 | 0,9 · 1,0 · 0,5 (23) | 2,2 · 1,2 · 12,7 (27) ✓ | 1,0 · 1,3 · 0,0 (15) | 2,2 · 2,4 · 2,0 (38) ✓ |
| VPU | 2009-06 | 0,8 · 0,6 · 2,6 (34) | 0,9 · 0,7 · 1,5 (27) | 0,4 · 0,8 · 0,0 (13) | 0,8 · 1,6 · 0,1 (39) |

### Internacional

| ETF | Desde | A retroceso | B giro semanal | C rotura | D cruce de medias |
|---|---|---|---|---|---|
| VEA | 2009-06 | 0,2 · 0,3 · 0,0 (20) | 1,0 · 0,8 · 2,6 (27) | 0,9 · 2,0 · 0,2 (15) | 1,0 · 1,0 · 0,8 (37) |
| VWO | 2009-06 | 0,6 · 0,7 · 0,4 (17) | 1,3 · 1,0 · 3,7 (24) | 0,5 · 0,6 · 0,3 (21) | 0,9 · 1,4 · 0,2 (45) |
| VEU | 2009-06 | 0,1 · 0,1 · 0,0 (16) | 0,9 · 0,4 · 5,1 (26) | 0,5 · 0,5 · 0,4 (20) | 0,6 · 0,6 · 0,5 (41) |
| VSS | 2009-06 | 0,6 · 0,6 · 0,3 (12) | 1,4 · 1,2 · 1,9 (32) | 1,7 · 2,7 · 0,0 (14) | 0,7 · 1,0 · 0,3 (41) |
| VGK | 2009-06 | 1,0 · 1,0 · 1,2 (17) | 1,2 · 1,6 · 0,6 (24) | 0,9 · 2,4 · 0,0 (25) | 1,0 · 0,7 · 1,7 (45) |
| VPL | 2009-06 | 1,1 · 0,8 · 3,2 (13) | 1,7 · 0,8 · 8,8 (26) | 0,9 · 2,2 · 0,1 (16) | 0,8 · 0,7 · 1,0 (45) |
| VYMI | 2016-03 | 0,2 · 0,2 · 0,4 (9) | 2,0 · 2,4 · 1,8 (16) ✓ | 0,6 · 0,4 · 0,7 (13) | 1,6 · 0,4 · 2,8 (22) |
| VIGI | 2016-03 | 1,1 · 0,3 · 4,0 (10) | 1,8 · 1,8 · 1,9 (15) ✓ | 0,8 · 0,9 · 0,6 (14) | 0,5 · 0,5 · 0,4 (29) |
| VT | 2009-06 | 0,8 · 0,5 · 2,5 (24) | 1,3 · 0,6 · 8,4 (30) | 0,9 · 0,8 · 1,8 (23) | 2,0 · 2,1 · 1,5 (43) ✓ |
| VNQI | 2010-11 | 0,6 · 0,4 · 2,4 (13) | 2,6 · 3,8 · 1,2 (23) ✓ | 2,1 · 2,2 · 1,6 (8) ✓ | 0,5 · 0,5 · 0,5 (30) |
| VXUS | 2011-01 | 0,0 · 0,0 · 0,1 (13) | 1,6 · 1,0 · 4,3 (22) ✓ | 1,0 · 1,2 · 0,7 (18) | 0,8 · 1,1 · 0,4 (33) |

### Renta fija

| ETF | Desde | A retroceso | B giro semanal | C rotura | D cruce de medias |
|---|---|---|---|---|---|
| BND | 2009-06 | 1,1 · 0,9 · ∞ (18) | 0,8 · 0,9 · 0,5 (24) | 0,5 · 0,5 · ∞ (6) | 0,1 · 0,1 · 0,0 (30) |
| BNDX | 2013-06 | 0,7 · 1,6 · 0,2 (14) | 0,7 · 1,3 · 0,0 (17) | 1,3 · 1,5 · 0,8 (6) | 0,0 · 0,0 · 0,0 (10) |
| BSV | 2009-06 | 0,2 · 0,2 · 0,0 (23) | 1,8 · 1,1 · 12,8 (19) ✓ | 1,1 · 1,2 · 1,0 (7) | 1,2 · 1,0 · 1,3 (20) |
| BIV | 2009-06 | 1,6 · 2,0 · 0,0 (20) | 1,8 · 2,1 · 0,3 (17) | 0,5 · 0,5 · 0,0 (8) | 0,6 · 0,7 · 0,0 (25) |
| BLV | 2009-06 | 0,8 · 1,2 · 0,2 (21) | 1,5 · 2,5 · 0,1 (21) | 0,6 · 0,6 · 0,0 (11) | 0,6 · 0,6 · ∞ (30) |
| VCIT | 2009-11 | 0,6 · 0,7 · 0,0 (23) | 1,0 · 0,8 · 2,8 (21) | 0,4 · 0,9 · 0,0 (10) | 0,7 · 0,8 · 0,6 (28) |
| VCSH | 2009-11 | 0,7 · 0,8 · 0,1 (28) | 1,9 · 2,1 · 1,1 (26) ✓ | 21,5 · 0,0 · ∞ (3) | 0,9 · 0,4 · 1,2 (22) |
| VCLT | 2009-11 | 1,3 · 1,5 · 0,3 (25) | 1,7 · 2,3 · 0,1 (21) | 0,3 · 0,3 · ∞ (8) | 0,6 · 0,5 · 2,1 (21) |
| VGIT | 2009-11 | 0,8 · 5,4 · 0,0 (18) | 0,9 · 1,0 · 0,7 (21) | 0,8 · 2,0 · 0,0 (10) | 1,3 · 1,4 · 0,1 (27) |
| VGSH | 2009-11 | 0,4 · 0,3 · 15,2 (26) | 0,7 · 0,6 · 0,8 (10) | 10,0 · 6,9 · ∞ (6) ✓ | 1,7 · 2,7 · 0,8 (24) |
| VGLT | 2010-01 | 1,2 · 1,7 · 0,0 (18) | 2,1 · 2,9 · 0,6 (26) | 2,5 · 2,5 · 0,0 (7) | 2,3 · 2,3 · ∞ (26) ✓ |
| VMBS | 2009-11 | 0,4 · 0,4 · 0,1 (37) | 3,3 · 3,7 · 2,7 (16) ✓ | 0,3 · 0,5 · 0,0 (6) | 0,9 · 1,1 · 0,0 (14) |
| VTIP | 2012-10 | 2,6 · 1,9 · 4,3 (17) ✓ | 0,7 · 0,7 · 0,3 (19) | 0,8 · 1,5 · 0,0 (5) | 1,1 · 0,5 · 2,7 (22) |
| VTEB | 2015-08 | 5,7 · 6,8 · 1,4 (6) ✓ | 1,6 · 1,6 · 1,8 (21) ✓ | 0,9 · 1,4 · 0,0 (8) | 0,3 · 0,3 · 0,3 (14) |
| EDV | 2009-06 | 0,7 · 2,0 · 0,0 (14) | 1,3 · 1,8 · 0,1 (26) | 1,7 · 1,7 · 0,0 (9) | 2,6 · 2,6 · 0,0 (22) |
| VTC | 2017-11 | 0,1 · 0,1 · 0,1 (7) | 3,5 · 5,5 · 2,1 (11) ✓ | 0,4 · 0,4 · 0,0 (3) | 0,3 · 0,0 · 0,5 (13) |

## 4. Cuántos ETF cumplen por grupo (salida a)

| Grupo | Puerta A | Puerta B | Puerta C | Puerta D |
|---|---|---|---|---|
| Renta variable EE.UU. (amplia y estilo) | 5 de 17 | 9 de 17 | 7 de 17 | 7 de 17 |
| Sectores EE.UU. | 2 de 11 | 5 de 11 | 3 de 11 | 5 de 11 |
| Internacional | 0 de 11 | 4 de 11 | 1 de 11 | 1 de 11 |
| Renta fija | 2 de 16 | 5 de 16 | 1 de 16 | 1 de 16 |
| Total (55) | 9 de 55 | 23 de 55 | 12 de 55 | 14 de 55 |

## 5. Lectura

**Por grupo, con el criterio de la ronda 2** (≥ 30 operaciones por tramo, salvo donde se indica):

| Grupo | A retroceso | B giro semanal | C rotura | D cruce de medias |
|---|---|---|---|---|
| Renta variable EE.UU. | a) NO · b) CUMPLE | **a) y b) CUMPLE** | a) y b) CUMPLE | a) NO · b) CUMPLE |
| Sectores EE.UU. | NO | a) NO · b) CUMPLE | NO | NO |
| Internacional | NO | NO | NO | NO |
| Renta fija | NO | NO | NO (a: muestra insuficiente) | NO |

- **B es la puerta más sólida.** Cumple en renta variable de EE. UU. con las dos salidas (ratio 1,65 y 2,22) y con b) en sectores. De los 55 ETF, 23 cumplen individualmente con B, frente a 14 con D, 12 con C y 9 con A.
- **El núcleo está en renta variable de EE. UU.** (VTI, VOO, VUG y similares). Ahí cumplen B y C con la salida elegida.
- **Internacional y renta fija no funcionan con ninguna puerta.** La renta fija pierde en T2 (2023-2026) con casi todas. Para estos ETF no hay base para usar las puertas.
- **Sectores:** solo B con el stop fijo. Con la salida elegida, VGT aporta el 43 % de la ganancia de B y, sin VGT, el ratio de B en sectores baja de 1,44 a 1,27. Con el stop fijo b), sin VGT sigue en 1,61.
- **A en renta variable amplia** con la salida a) depende de VOOG (92 % de la ganancia). Con el stop fijo b) sí cumple (1,80), sin dependencia de un solo ETF (el mayor aporta el 14 %).
- **Muestra por ETF:** cada ETF tiene 10-60 operaciones. El ✓ por ETF es orientativo.

## 6. Límites

- Resultados de Python; ProRealTime no se ha ejecutado para esta ronda.
- Sin comisiones (como en tu broker), pero tampoco hay diferencial ni deslizamiento.
- El tramo T2 es corto (2023 – nov-2026).
- Elegir los ETF que mejor salen de esta tabla introduce sesgo de selección. Para decidir cuáles vigilar, lo prudente es usar los grupos, no los mejores individuales.
