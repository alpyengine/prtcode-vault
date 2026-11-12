<!-- RESUMEN_puertas-vanguard · v2.2 · 2026-11-12 -->

# Resumen — Puertas Vanguard (matriz homogénea)

Ratio ganancia/pérdida con 10.000 $ fijos por operación, en dos tramos: **T1** 2010-2022 y **T2** 2023-nov 2026. Cada celda: `T1 · T2`. Detalle completo en `RESULTADOS_matriz-homogenea.md`.

**Aviso:** T2 tiene pocas operaciones (de 1 a 13 por valor). Léelo como una comprobación, no como un resultado.

## Salida a) — la elegida en cada backtest

| Puerta | Salida | VGT | VHT | IBB | IVV | PAVE | JPM | KO | CAT | MSFT | AAPL | AMGN |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A retroceso | 3 · línea ATR diaria | 3,9 · 1,2 | 0,7 · 2,3 | 1,4 · 2,8 | 2,6 · 2,5 | 1,1 · 2,2 | 2,9 · 0,9 | 0,6 · 0,6 | 1,5 · 0,2 | 2,1 · 3,8 | 1,1 · 0,1 | 0,6 · 1,6 |
| B giro semanal | 4 · bajo EMA50 | 2,0 · 14,3 | 1,8 · 3,7 | 0,8 · 14,4 | 1,1 · 15,0 | 0,6 · 3,8 | 3,1 · 1,6 | 0,9 · 4,1 | 1,1 · 7,0 | 3,1 · 4,7 | 4,0 · 3,1 | 0,5 · 2,3 |
| C rotura | 4 · bajo EMA50 | 1,5 · 7,6 | 2,1 · 1,0 | 5,0 · ∞ | 2,0 · 3,9 | 6,4 · 0,1 | 9,3 · 17,8 | 1,5 · ∞ | 8,3 · 12,7 | 2,5 · ∞ | 4,4 · 0,3 | 1,4 · 0,2 |
| D cruce de medias | 4 · bajo EMA50 | 2,4 · 1,9 | 3,8 · 1,0 | 4,3 · 0,9 | 1,3 · 2,2 | 2,7 · 2,6 | 1,6 · ∞ | 0,6 · 1,2 | 6,6 · 0,9 | 1,6 · 0,3 | 5,5 · 0,0 | 0,4 · ∞ |

## Salida b) — sistema: stop 2,5 ATR, objetivo 3R, mitad a +2R

| Puerta | Salida | VGT | VHT | IBB | IVV | PAVE | JPM | KO | CAT | MSFT | AAPL | AMGN |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A retroceso | sistema | 2,9 · 0,7 | 0,9 · 1,5 | 1,4 · 1,0 | 3,6 · 0,6 | 3,4 · 1,6 | 1,1 · 1,1 | 0,7 · 0,2 | 1,3 · 0,9 | 4,3 · 4,3 | 0,9 · ∞ | 0,4 · 7,0 |
| B giro semanal | sistema | 2,1 · 9,4 | 1,3 · 2,3 | 1,2 · 6,5 | 1,7 · 7,7 | 3,6 · 2,6 | 1,7 · 1,1 | 2,8 · 2,4 | 2,1 · 1,7 | 1,7 · 1,1 | 2,3 · 6,1 | 0,9 · 1,4 |
| C rotura | sistema | 1,6 · 1,7 | 1,9 · 1,6 | 5,4 · 1,2 | 1,1 · 3,8 | 0,0 · 0,5 | 4,2 · 3,4 | 0,9 · 2,4 | 1,5 · 0,9 | 1,2 · ∞ | 2,3 · 3,6 | 5,4 · 0,0 |
| D cruce de medias | sistema | 1,9 · 2,7 | 2,1 · 2,9 | 3,7 · 1,8 | 1,3 · 4,2 | 1,6 · 3,7 | 1,3 · ∞ | 0,3 · 0,5 | 1,6 · 1,3 | 1,4 · 2,5 | 3,5 · 4,1 | 0,6 · ∞ |

ETF: VGT, VHT, IBB, IVV, PAVE. Acciones: JPM, KO, CAT, MSFT, AAPL, AMGN.

## Cuántos valores ganan en los dos tramos (ratio > 1 en T1 y en T2)

| Puerta | Salida a) ETF | Salida a) acciones | Salida b) ETF | Salida b) acciones |
|---|---|---|---|---|
| A retroceso | 4 de 5 | 1 de 6 | 1 de 5 | 2 de 6 |
| B giro semanal | 3 de 5 | 4 de 6 | 5 de 5 | 5 de 6 |
| C rotura | 4 de 5 | 4 de 6 | 4 de 5 | 3 de 6 |
| D cruce de medias | 4 de 5 | 1 de 6 | 5 de 5 | 4 de 6 |

## Lectura

- **Salida b) (sistema) con la puerta B y la D es la más estable:** ganan en los dos tramos en los 5 ETF.
- **Puerta B con sistema** también gana en 5 de 6 acciones. Es la combinación más robusta de toda la prueba.
- **Puerta C** con la salida a) gana en 4 de 5 ETF y en 4 de 6 acciones (JPM, KO, CAT y MSFT). Con el sistema, 4 de 5 ETF y 3 de 6 acciones.
- **Puerta A** con la salida a) gana en 4 de 5 ETF, pero en acciones solo en MSFT. Confirma lo visto antes: sirve para ETF, no para acciones.
- **Puerta D** con la salida a) falla en acciones (solo JPM). Con el sistema mejora (4 de 6).
- La salida de sistema (stop y objetivo) no es mejor siempre: baja a la A en T2 y a la C en acciones.

## Validación del motor Python

Comparado con 23 informes de PRT (1 acción por operación):

- Operaciones: 19 de 23 dentro de ±2. Ratio: 22 de 23 dentro del 25 %.
- Coincidencia exacta o casi exacta en la puerta B (5 ETF), la puerta C (4 de 5), la A en VGT, PAVE, JPM y CAT, y la D en VGT y VHT.
- **Control D v3 en PRT (10-nov):** IBB 28 operaciones (Python 27), IVV 50 (50), PAVE 24 (24). Ratios 1,98 / 1,94 / 2,15. Los PDF antiguos de D eran erróneos; el motor queda validado.
- **A en IBB:** la diferencia de 33 frente a 36 operaciones sigue sin explicar con el periodo completo. Control de A v1.1 en PRT (12-nov), desde 31-ene-2024: PRT 8 operaciones, Python 9. Las 5 pérdidas (−16,03 $), la mejor (+39,37 $) y la peor (−6,01 $) coinciden exactamente. La diferencia es una operación ganadora abierta que PRT no cuenta. Motor validado en ese periodo.

## Corrección (v2.0)

La puerta A con la salida b) en ETF gana en **1 de 5** valores (PAVE), no en 2. IBB en T2 sale con un ratio de 1,002, que cuenta como no ganador.

## Ronda 2 (10-nov-2026): 20 ETF y 40 acciones

Detalle completo en `RESULTADOS_ronda2.md`. Motor Python, 10.000 $ por operación, todas las operaciones sumadas por grupo. Regresión previa: 12 de 12 filas idénticas a la matriz anterior.

**Criterio** (ratio > 1,5 en conjunto y > 1 en T1 y T2, con ≥ 30 operaciones por grupo y tramo). Ninguna combinación tiene muestra insuficiente.

| Puerta | ETF con la salida elegida | Acciones con la salida elegida |
|---|---|---|
| A retroceso | NO CUMPLE (1,29) | NO CUMPLE (1,24) |
| B giro semanal | **CUMPLE** (1,63) | **CUMPLE** (1,70) |
| C rotura | NO CUMPLE (1,36) | **CUMPLE** (1,78) |
| D cruce de medias | NO CUMPLE (1,42) | **CUMPLE** (1,63) |

- **B es la más estable:** cumple en ETF y en acciones con las salidas a), b) y c).
- **D** cumple en acciones con las 4 salidas, y en ETF con b) y c).
- **A** solo cumple en ETF con las salidas b) y c).
- **C** no cumple en ETF con ninguna salida. En acciones depende de CAT (26 % de la ganancia).
- **Variantes de stop c) y d): no se adoptan.** Ninguna mejora el ratio de b) en los cuatro casos (ETF y acciones, T1 y T2).
- **Concentración:** A en ETF depende de XLE (41 %) y C en ETF de VGT (29 %).

## ETF de Vanguard (10-nov-2026): 55 ETF

Detalle en `RESULTADOS_etf-vanguard.md`. Salida a) y b), mismo criterio de la ronda 2, por grupos.

| Grupo | A | B | C | D |
|---|---|---|---|---|
| Renta variable EE.UU. (17) | b) cumple | **a) y b) cumplen** | a) y b) cumplen | b) cumple |
| Sectores EE.UU. (11) | no | b) cumple | no | no |
| Internacional (11) | no | no | no | no |
| Renta fija (16) | no | no | no | no |

- **El núcleo está en renta variable de EE. UU.** y la puerta B es la más sólida (cumple con las dos salidas).
- **Internacional y renta fija no cumplen con ninguna puerta.**
- Por ETF, cumplen con B 23 de 55, con D 14, con C 12 y con A 9. Hay mucho solapamiento entre ETF parecidos (VTI, VOO, VV), así que no son resultados independientes.
- VIOO venía sin ajustar por un split 2:1 (mar-2023). Corregido.

## Pendiente

1. Decidir si se lleva la salida de sistema (stop, objetivo y mitad a +2R) a los `.pts`. Decisión del 12-nov: **se deja fuera**. La ronda 2 no la favorece frente a la salida elegida.
2. La lista de 40 acciones se contrastó con Fortune 500 de 2009 (35 de 40 coinciden) y se deja como está.
