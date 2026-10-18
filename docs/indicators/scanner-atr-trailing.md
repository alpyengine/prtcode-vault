<!-- scanner-atr-trailing.md · v1.2 · 2026-10-18 -->

# Scanner ATR Trailing (Vervoort) — ficha / especificación

| Campo | Valor |
|---|---|
| Plataforma | ProRealTime · ProScreener |
| Fichero | `screeners/scanner-atr-trailing/scanner-atr-trailing.prs` |
| Versión | v1.2 |
| Estado | Validado (PRT-001 cerrada 2026-10-18) |
| Decisiones | `docs/decisions/ADR-0001-scanner-atr-trailing-diseno.md` · `ADR-0002-senal1-confirmacion.md` |
| Tag | `scanner-atr-trailing-prt/v1.2.0` |

## Propósito

Revisar cada sábado la watchlist de valores estudiados y marcar los que dan una de las 4 señales del método ATR trailing de Vervoort. El código no lleva tickers: corre sobre la lista que se elija en la interfaz.

## Uso

1. Periodo de la interfaz: **Diario**.
2. Dos copias guardadas en ProRealTime: `scanner-atr-trailing ETF` (`isETF = 1`) sobre la lista de ETF, y `scanner-atr-trailing ACC` (`isETF = 0`) sobre la de acciones.
3. Sábado: `semanaCerrada = 1`. Entre semana: `semanaCerrada = 0`.
4. Orden: columna `Dist52W`, valores más bajos primero (lo más cerca del máximo arriba).

## Método base

- Línea ATR trailing de Vervoort con trinquete (memoria): sube como soporte, baja como resistencia y cambia de lado en el cruce.
- ATR 14, suavizado Wilder (`AverageTrueRange`).
- Semanal ×1,5: es "el muro".
- Diaria: ×2,5 para ETF y ×2,0 para acciones.

## Parámetros

| Variable | Valor | Uso |
|---|---|---|
| `isETF` | 1 / 0 | Elige el múltiplo diario |
| `semanaCerrada` | 1 / 0 | 1 = sábado; 0 = usa la última semana cerrada |
| `atrPer` | 14 | Periodo del ATR |
| `multW` | 1,5 | Múltiplo semanal |
| `multETF` / `multStock` | 2,5 / 2,0 | Múltiplo diario |
| `maPer1` / `maPer2` | 10 / 20 | Medias del pullback |
| `boPer` | 20 | Máximo de N días para la ruptura |
| `volPer` | 20 | Media de volumen |
| `hsPer` | 252 | Máximo de 52 semanas en barras diarias |
| `rsiPer` | 14 | RSI diario |
| `tdLook` | 3 | Ventana del TD Buy Setup 9 (días) |

ProScreener no tiene parámetros en la interfaz: se editan en el propio código.

## Señales

| Código | Nombre | Condición |
|---|---|---|
| 1 | Giro semanal confirmado (puerta B) | Hace 2 semanas, cierre en el muro o por debajo; la semana pasada, cruce al alza; esta semana sigue por encima **y su cuerpo** (`min(open, close)`) **supera el muro antiguo**. Llega una semana después del cruce (ADR-0002) |
| 2 | Pullback en tendencia (puerta A) | Muro en soporte, cierre diario por encima del muro y cierre a ≤1 ATR diario de MM10, MM20 o la línea diaria |
| 3 | Ruptura momentum (puerta C) | Cierre > máximo de 20 días previo, cierre > apertura, cierre > máximo de ayer, volumen > media de 20 y muro en soporte |
| 4 | Pérdida del muro (salida) | Semana cerrada por debajo de la línea semanal y la anterior en la línea o por encima |

Columna `Senal`: un dígito por señal activa, en orden. Ejemplo: `23` = pullback y ruptura a la vez. Las señales 1 y 4 no pueden coincidir; tampoco la 4 con la 2 o la 3.

TD Buy Setup 9: 9 cierres seguidos por debajo del cierre de 4 barras antes, completado en los últimos `tdLook` días. Es informativo y solo se muestra en la versión de 6 columnas.

## Columnas de salida

| Versión | Columnas |
|---|---|
| 3 columnas (licencia gratuita) | `Senal`, `Dist52W` %, `Stop` |
| 6 columnas (licencia completa) | `Senal`, `Dist52W` %, `Stop`, `DistMuro` %, `RSI14`, `TD9` |

- Ticker y último precio los pone la tabla de ProScreener.
- `Stop` = cierre − múltiplo diario × ATR14 diario.
- ATR14 no lleva columna propia. Se deduce del stop: ATR = (cierre − Stop) / múltiplo.
- Los porcentajes se calculan como fracción, porque `PERCENTFORMAT` multiplica por 100.

## Límites

| Límite | Valor |
|---|---|
| Historial | 256 velas por timeframe (1024 en Premium) |
| Barras necesarias | 252 diarias para el máximo de 52 semanas; la línea semanal se estabiliza en unas 30 semanas |
| Resultados visibles | 50 (100 en Premium) |
| Columnas | 3 (gratuita, confirmado) / 6 (completa) |
| App abierta | Pendiente de confirmar |

## Pruebas de referencia (semana cerrada el 16-oct-2026)

Calculadas fuera de ProRealTime con datos semanales ajustados (Twelve Data). Pueden variar unos céntimos por la forma de arrancar el ATR, pero la señal debe coincidir.

| Ticker | Línea semanal | Rol | Dist. muro | Señal semanal esperada |
|---|---|---|---|---|
| VGT | 127,34 | Resistencia | −6,7 % | **4** (pérdida del muro) |
| SCHD | 33,10 | Soporte | +3,8 % | ninguna (cruzó esta semana; 1 posible el 24-oct) |
| VDC | 226,39 | Soporte | +4,9 % | ninguna (cruzó esta semana; 1 posible el 24-oct) |
| KO | 88,79 | Soporte | +5,8 % | ninguna (cruzó esta semana; 1 posible el 24-oct) |
| JPM | 354,02 | Resistencia | −4,0 % | ninguna |
| XOM | 165,81 | Soporte | +7,9 % | ninguna |

Histórico de la señal 1 (regla D) para comprobar con el indicador: VGT 13-abr-2026, KO 26-ene y 18-may-2026, XOM 27-jul-2026.

**Limitación de datos:** con la licencia gratuita, ProScreener solo devuelve acciones de NYSE (ver `docs/prt-rules.md`). VGT, SCHD y VDC se validan con el indicador.

Las señales diarias (2 y 3) se comprueban en el gráfico durante la validación.

## Fuera de alcance (fase 2)

- Líneas del indicador DOC (línea de corrección).
- Versión TradingView, que iría por bloques de unos 40 símbolos.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| v1.0 | 2026-10-18 | Primera versión: 4 señales, 3 columnas, línea de 6 preparada |
| v1.1 | 2026-10-18 | Cálculos de la versión 6 col comentados (`REM [6COL]`): PRT no admite variables sin usar |
| v1.2 | 2026-10-18 | Señal 1 = confirmación la semana siguiente al cruce, con el cuerpo sobre el muro antiguo (ADR-0002) |
