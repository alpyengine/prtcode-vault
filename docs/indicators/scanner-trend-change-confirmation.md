# Scanner: Trend Change Confirmation (Nivel 2)

**Versión:** 1.0
**Plataforma:** ProRealTime — ProScreener
**Periodo:** Diario
**Fichero:** `scanner-trend-change-confirmation.prt`
**ADR:** `ADR-0002-scanner-trend-change-confirmation.md`

---

## 1. Objetivo

Detectar **cambios de tendencia con confirmación estructural y de timeframe superior**, no solo un cruce de medias o una vela de reversión aislada. El scanner responde a tres preguntas:

1. **¿La tendencia previa se está agotando?** (capa A2)
2. **¿El precio ha roto la estructura?** (capas C1 y C2)
3. **¿El timeframe superior lo confirma?** (capas D1 y D2)

En lugar de una señal binaria (sí/no), devuelve un **score 0–5 por dirección** y una **fase** que indica en qué punto del proceso está el giro.

---

## 2. Capas de confirmación

| Capa | Nombre | Qué mide | Cuándo suma |
|---|---|---|---|
| **A2** | ADX cayendo | Agotamiento de la tendencia previa | `ADX < ADX[5]` y `ADX < 25` |
| **C1** | BOS (Break of Structure) | Ruptura de máximo/mínimo de 20 barras | `close > highest[20](high[1])` (bull) o `close < lowest[20](low[1])` (bear) |
| **C2** | Fallo de ruptura | Trampa: rompe nivel y cierra de vuelta dentro | Nuevo mínimo de 20 + cierre alcista en mitad superior (bull) / espejo (bear) |
| **D1** | Alineación semanal | Muro Vervoort semanal alineado con la dirección | `close > lineW` y `close[1] > lineW[1]` (bull) / espejo (bear) |
| **D2** | Pendiente EMA200 | Tendencia de fondo alineada | `EMA200 > EMA200[10]` (bull) / espejo (bear) |

**Score máximo por dirección = 5.** A2 es dirección-agnóstico: suma a bull y a bear por igual, así que por sí sola no define dirección.

---

## 3. Fases

| Fase | Código | Significado | Qué hacer |
|---|---|---|---|
| **Agotamiento** | 1 | Solo A2 activo. La tendencia previa pierde fuerza, pero no hay estructura rota. | Watchlist. No actuar. |
| **PrimerAviso** | 2 | Estructura rota (C1 o C2) + **1** confirmación HTF (D1 o D2). | Entrada táctica con stop ajustado. Más riesgo. |
| **Confirmado** | 3 | Estructura rota + **2** confirmaciones HTF (D1 y D2). | Entrada con más convicción. Menos frecuencia, más calidad. |
| **Fallido** | 4 | Estructura rota **contra** ambas HTF (ni D1 ni D2 confirman). | No operar. Alta probabilidad de fakeout. |

---

## 4. Columna `Senal` (código combinado)

La columna `Senal` combina dirección y fase en un solo número:

- **Decenas** = dirección: `1` = Bull, `2` = Bear.
- **Unidades** = fase: `1` = Agotamiento, `2` = PrimerAviso, `3` = Confirmado, `4` = Fallido.

| Senal | Significado |
|---|---|
| **11** | Bull — Agotamiento |
| **12** | Bull — PrimerAviso |
| **13** | Bull — Confirmado |
| **14** | Bull — Fallido |
| **21** | Bear — Agotamiento |
| **22** | Bear — PrimerAviso |
| **23** | Bear — Confirmado |
| **24** | Bear — Fallido |

Ordena por `Senal` ascendente para agrupar por dirección y fase. O filtra `Senal = 13` para ver solo Bull Confirmado.

---

## 5. Columnas de salida

| Columna | Qué muestra | Cómo leerla |
|---|---|---|
| `Senal` | Código combinado dirección + fase | Ver tabla arriba |
| `BullSc` | Score bull (0–5) | Cuántas capas bull están activas |
| `BearSc` | Score bear (0–5) | Cuántas capas bear están activas |
| `A2_ADX` | 0/1 | 1 = ADX cayendo y débil |
| `C1_Bull` / `C1_Bear` | 0/1 | 1 = BOS en esa dirección |
| `C2_Bull` / `C2_Bear` | 0/1 | 1 = fallo de ruptura en esa dirección |
| `D1_WBull` / `D1_WBear` | 0/1 | 1 = semanal alineado |
| `D2_EMAup` / `D2_EMAdn` | 0/1 | 1 = EMA200 con pendiente a favor |
| `Stop` | Nivel de stop sugerido | `lowest[5](low) - 0.5*ATR` (bull) o `highest[5](high) + 0.5*ATR` (bear) |
| `Target` | Próxima resistencia/soporte | Máximo/mínimo de 50 barras |

---

## 6. Cómo leer los resultados

### Paso 1 — Filtra por fase

- **Solo `Senal` 13 o 23 (Confirmado)**: las más fiables. Menos frecuencia, más calidad.
- **`Senal` 12 o 22 (PrimerAviso)**: más tempranas, más riesgo. Úsalas para watchlist o entradas tácticas.
- **Ignora `Senal` 11 y 21 (Agotamiento)**: solo avisan de que algo se muere, no de que algo nace.
- **Ignora `Senal` 14 y 24 (Fallido)**: estructura rota contra HTF. Alta probabilidad de fakeout.

### Paso 2 — Mira qué capas confirmaron

Para cada valor, revisa las columnas `A2_ADX` a `D2_EMAdn`:

- **Bull Confirmado (13)**: esperado `C1_Bull = 1`, `D1_WBull = 1`, `D2_EMAup = 1`. Si además `C2_Bull = 1`, es un fallo de ruptura bear previo que se ha girado — muy potente.
- **Bull PrimerAviso (12)**: `C1_Bull = 1` pero solo una de `D1_WBull` o `D2_EMAup`. El semanal o el EMA200 aún no confirman. Más riesgo.
- **Bull Fallido (14)**: `C1_Bull = 1` pero `D1_WBull = 0` y `D2_EMAup = 0`. Está rompiendo contra todo. No operar.

### Paso 3 — Revisa el gráfico

Los scanners dan candidatos, no decisiones. Para cada valor con `Senal` 12 o 13, comprueba en gráfico:

| Qué | Por qué |
|---|---|
| **Volumen del BOS** | Un BOS sin volumen es sospechoso. Compara con la media de 20. |
| **Qué nivel se rompió** | ¿Máximo de 20 barras? ¿Máximo de 52 semanas? No es lo mismo. |
| **RSI** | Bull con RSI > 75 = sobrecompra, cuidado con la entrada. |
| **Distancia al Target** | Si el `Target` está muy cerca, el ratio riesgo/beneficio es malo. |
| **Stop vs Target** | Ratio mínimo recomendado: 1:2. Si `Stop` y `Target` están muy juntos, descarta. |
| **Contexto semanal** | Aunque `D1_WBull = 1`, revisa el gráfico semanal: ¿está en resistencia mayor? |

---

## 7. Cómo utilizarlo

### Flujo recomendado

1. **Ejecuta el scanner en Diario** sobre tu watchlist de ETF o acciones líquidas.
2. **Filtra por `Senal = 13`** (Bull Confirmado) o **`Senal = 23`** (Bear Confirmado) para la lista corta.
3. **Ordena por `BullSc` o `BearSc` descendente** para ver primero los que tienen más capas activas.
4. **Pasa los candidatos al gráfico** y aplica el checklist del paso 3.
5. **Usa `Stop` y `Target`** como referencia, no como niveles absolutos. Ajústalos a la estructura del gráfico.

### Combinación con otros scanners

- **Delante**: `Day Trading filter` mejorado como pre-filtro de liquidez.
- **Detrás**: `ATR Trailing Vervoort` para confirmar que el semanal no contradice (evita `Senal 4`).
- **En paralelo**: `PRTBands` para detectar entradas tácticas más tempranas en los valores que este scanner marca como `PrimerAviso`.

### Frecuencia esperada

- **`Senal` 13/23 (Confirmado)**: pocos valores al día. Calidad sobre cantidad.
- **`Senal` 12/22 (PrimerAviso)**: decenas de valores. Filtrar por liquidez y revisar.
- **`Senal` 11/21 (Agotamiento)**: muchos. Ignorar salvo que ya sigas el valor.

---

## 8. Parámetros

| Parámetro | Default | Función | Ajuste |
|---|---|---|---|
| `atrPer` | 14 | Periodo ATR | No tocar salvo estrategia específica |
| `adxPer` | 14 | Periodo ADX | No tocar |
| `emaPer` | 200 | Periodo EMA200 | 200 estándar; 150 para más reactivo |
| `bosLook` | 20 | Ventana de BOS | 20 = ~1 mes. 10 = más señales, más ruido |
| `failLook` | 20 | Ventana de fallo de ruptura | Igual que `bosLook` |
| `adxLook` | 5 | Ventana para "ADX cayendo" | 5 = última semana |
| `adxMax` | 25 | Umbral de ADX débil | 20 = más estricto, 30 = más laxo |
| `emaSlopeLook` | 10 | Ventana de pendiente EMA200 | 10 = 2 semanas |
| `multW` | 1.5 | Multiplicador ATR semanal | No tocar salvo estrategia |
| `minScore` | 3 | Score mínimo para mostrar | 3 = equilibrado, 4 = estricto |
| `minPrice` | 0.5 | Precio mínimo | Subir a 1.0 si operas solo large caps |
| `minAvgVol` | 100000 | Volumen medio mínimo | Subir a 500000 para más liquidez |

---

## 9. Limitaciones

1. **ADX lagea.** La capa A2 detecta agotamiento cuando la tendencia previa ya lleva tiempo débil. No es una señal temprana.
2. **D2 (EMA200) lagea mucho.** En un giro bull, la EMA200 puede tardar semanas en girar. Por eso muchos Bull sólidos aparecerán como `PrimerAviso` (12) en lugar de `Confirmado` (13). Es correcto: el scanner te está diciendo que el HTF aún no confirma.
3. **C1 (BOS) es sensible a `bosLook`.** Con 20 barras detecta rupturas de ~1 mes. Con 10 detecta más pero con más ruido.
4. **C2 (fallo de ruptura) es raro.** Puede pasar días sin dispararse. Es normal.
5. **No detecta divergencias RSI.** Eso es A1, que está en el Nivel 1 (Reversal Alert), no en este scanner.
6. **Depende del indicador Vervoort semanal.** Si no lo tienes, `wkBull`/`wkBear` no funcionarán. Alternativa: sustituir por `close > EMA[30](close)` en semanal.
7. **La función ADX puede variar según versión de PRT.** Si da error, probar `ADX[adxPer]` o `ADX(adxPer)`.
8. **El scanner no backtestea.** Las fases son heurísticas basadas en diseño, no en validación estadística. Antes de operar, haz un backtest manual de 20–30 señales `Senal = 13`.

---

## 10. Ejemplos de lectura

### Ejemplo 1 — Bull Confirmado limpio

> **Salida:** Senal 13, BullSc 4, BearSc 1, A2_ADX 1, C1_Bull 1, C2_Bull 0, D1_WBull 1, D2_EMAup 1, Stop 48.20, Target 58.50.

**Lectura:** ADX cayendo (agotamiento previo), BOS al alza, semanal alineado, EMA200 girando. Score 4/5. Entrada con stop en 48.20 y target en 58.50. Ratio ~1:2.5. Revisar volumen del BOS y RSI antes de entrar.

### Ejemplo 2 — Bull PrimerAviso

> **Salida:** Senal 12, BullSc 3, BearSc 1, A2_ADX 1, C1_Bull 1, C2_Bull 0, D1_WBull 1, D2_EMAup 0, Stop 22.10, Target 26.80.

**Lectura:** BOS al alza y semanal alineado, pero EMA200 aún bajando. Es un giro temprano. Más riesgo. Esperar confirmación de EMA200 o reducir tamaño de posición.

### Ejemplo 3 — Bull Fallido

> **Salida:** Senal 14, BullSc 2, BearSc 3, A2_ADX 1, C1_Bull 1, C2_Bull 0, D1_WBull 0, D2_EMAup 0.

**Lectura:** BOS al alza pero semanal bajista y EMA200 bajando. Está rompiendo contra todo. Alta probabilidad de fakeout. No operar. Revisar de nuevo en 3–5 sesiones.

### Ejemplo 4 — Bear Confirmado

> **Salida:** Senal 23, BullSc 1, BearSc 4, A2_ADX 1, C1_Bear 1, C2_Bear 0, D1_WBear 1, D2_EMAdn 1, Stop 105.50, Target 92.00.

**Lectura:** Cambio de tendencia bajista confirmado. BOS a la baja, semanal bajista, EMA200 girando abajo. Para cortos o para salir de longs existentes.

---

## 11. Próximos pasos

- [ ] Validar en backtest manual 20–30 señales `Senal = 13` en tu universo.
- [ ] Ajustar `minScore` a 4 si hay demasiadas señales, a 2 si hay muy pocas.
- [ ] Probar sustituir ADX por otra medida de agotamiento si la función da problemas.
- [ ] Construir el Nivel 1 (Reversal Alert) para detectar giros más tempranos.
- [ ] Construir el Nivel 3 (Quality Score) que combine ambos.

---

*Documentación del scanner Trend Change Confirmation v1.0. Ver ADR-0002 para decisiones de diseño.*