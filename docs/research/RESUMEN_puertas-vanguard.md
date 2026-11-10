<!-- RESUMEN_puertas-vanguard · v1.1 · 2026-11-10 -->

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
| A retroceso | 4 de 5 | 1 de 6 | 2 de 5 | 2 de 6 |
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
- **Cuatro diferencias:** D en IBB, IVV y PAVE (PRT dio 18, 30 y 13 operaciones; Python 27, 50 y 24) y A en IBB (33 contra 36).
- Los PDF de D en IBB, IVV y PAVE son dudosos: en PRT salían menos operaciones con `emaSube = 0` que con `emaSube = 1`, cosa que no puede pasar. Pendiente de control en PRT.

## Pendiente

1. Repetir en PRT la D (`esETF = 1`, `emaSube = 0`, `salida = 2`) en IBB, IVV y PAVE. Python espera 27, 50 y 24 operaciones.
2. Ampliar la lista de valores (test 2) con más ETF y acciones.
3. Implementar la salida de sistema en PRT (hoy solo está en Python).
