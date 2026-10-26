# Scanners ProRealTime — Documento de referencia

**Plataforma:** ProRealTime / ProScreener  
**Uso:** recordatorio de qué hace cada scanner, para qué sirve, cuándo usarlo y cómo consolidarlos.  
**Cómo usar este documento:** pégalo al inicio de un chat nuevo y pide revisar un scanner concreto por su nombre. Cada sección es autocontenida.

---

## Índice

1. [ATR Trailing Vervoort](#1-atr-trailing-vervoort)
2. [Bearish Engulfing + Trend Power](#2-bearish-engulfing--trend-power)
3. [Death Cross SMA20/SMA50](#3-death-cross-sma2050)
4. [Day Trading filter (liquidez + volatilidad)](#4-day-trading-filter)
5. [PRTBands](#5-prtbands)
6. [Nivel 1: Reversal Alert](#6-nivel-1-reversal-alert)
7. [Nivel 2: Trend Change Confirmation](#7-nivel-2-trend-change-confirmation)
8. [Nivel 3: Quality Score Composite](#8-nivel-3-quality-score-composite)
9. [Tabla de consolidación](#9-tabla-de-consolidación)
10. [Flujo de trabajo: Cómo usar la Trilogía (Niveles 1, 2 y 3)](#10-flujo-de-trabajo-cómo-usar-la-trilogía)
11. [Revisión rápida de giro al alza (Scanners clásicos)](#11-revisión-rápida-de-giro-al-alza)
12. [Próximos pasos](#12-próximos-pasos)
13. [Outlier Screener](#13-outlier-screener)

---

## 1. ATR Trailing Vervoort

**Archivo original:** `REM ==============================================.txt` (v1.1, 2026-10-18)  
**Dirección:** Long  
**Timeframe:** Multi-timeframe (semanal + diario)  
**Estilo:** Conservador, tendencia con pullback y ruptura  
**Complejidad:** Alta

### Objetivo
Radar de tendencia long con dos capas: un “muro” semanal (línea Vervoort con trinquete) y una línea diaria equivalente. Combina filtro de tendencia semanal con tres puertas de entrada en diario.

### Lógica resumida
- **Bloque semanal:** calcula `lineW` con trinquete ATR. El desfase `wo` depende de `semanaCerrada` (0 el sábado, 1 entre semana).
- **Señal 1 — Giro semanal (puerta B):** el cuerpo de la vela semanal supera el muro y el cierre previo estaba por debajo.
- **Señal 4 — Pérdida del muro (salida):** el cierre semanal cae bajo el muro habiendo estado por encima. Marca salida del radar.
- **Bloque diario:** calcula `lineD` con el mismo esquema, usando `multD` (2.0 acciones / 2.5 ETF).
- **Señal 2 — Pullback (puerta A):** precio sobre el muro semanal y cerca de MA10, MA20 o `lineD` (distancia ≤ ATR diario).
- **Señal 3 — Ruptura momentum (puerta C):** ruptura del máximo de 20 barras, vela de fuerza y volumen por encima de la media, con precio sobre el muro semanal.

### Parámetros clave
| Parámetro | Valor | Función |
|---|---|---|
| `isETF` | 0/1 | Selecciona multiplicador ATR diario |
| `semanaCerrada` | 0/1 | Desfase semanal (sábado vs entre semana) |
| `atrPer` | 14 | Periodo ATR |
| `multW` | 1.5 | Multiplicador ATR semanal |
| `multETF` / `multStock` | 2.5 / 2.0 | Multiplicador ATR diario |
| `maPer1` / `maPer2` | 10 / 20 | Medias del pullback |
| `boPer` | 20 | Periodo de ruptura |
| `volPer` | 20 | Media de volumen |
| `hsPer` | 252 | Ventana 52 semanas |

### Salida
- **`Senal`**: código combinable. `1` = giro semanal, `2` = pullback, `3` = ruptura, `4` = pérdida de muro. Ejemplo `23` = pullback + ruptura.
- **`Dist52W`**: distancia porcentual al máximo de 52 semanas.
- **`Stop`**: `close - multD * atrD`.

### Fortalezas
- Filtro semanal que evita operar contra la tendencia mayor.
- Tres puertas complementarias: giro, pullback, ruptura.
- Stop dinámico basado en ATR.

### Limitaciones
- Depende del timeframe de la interfaz (Diario).
- Puede dar señales tardías en giros bruscos.
- No incluye filtro de liquidez propio.

### Cuándo usarlo
- Para entradas long conservadoras con confirmación semanal.
- Cuando prefieres pullbacks o rupturas con stop ATR claro.

### Cuándo NO usarlo
- Para intradía puro.
- Para cortos.

---

## 2. Bearish Engulfing + Trend Power

**Dirección:** Short / salida  
**Timeframe:** Diario  
**Estilo:** Giro bajista tras avance  
**Complejidad:** Baja

### Objetivo
Detectar valores que forman una vela de envolvente bajista (bearish engulfing) tras un avance alcista previo, y clasificarlos por la fuerza de ese avance normalizada por volatilidad.

### Lógica resumida
- `LowPoint = LOWEST[8](LOW)` — mínimo de las últimas 8 velas.
- `Advance = CLOSE - LowPoint` — avance desde ese mínimo.
- `Norm = SUMMATION[3](TR) - HIGHEST[3](TR) - LOWEST[3](TR)` — TR intermedio de 3 velas.
- **Filtro engulfing:** `CLOSE[1] > OPEN[1] AND OPEN > CLOSE[1] AND CLOSE < OPEN[1]`.
- **Salida:** `Trend Power = Advance / Norm`.

### Limitaciones
- Definición de engulfing estricta.
- Solo detecta la barra actual.
- No confirma giro por sí solo.

---

## 3. Death Cross SMA20/50

**Dirección:** Short  
**Timeframe:** Diario  
**Estilo:** Cambio de tendencia por cruce de medias  
**Complejidad:** Baja

### Objetivo
Detectar el cruce bajista de SMA20 por debajo de SMA50 en la barra actual (“death cross”) y medir la velocidad del cruce.

### Lógica resumida
- `ma20 = AVERAGE[20](close)`, `ma50 = AVERAGE[50](close)`.
- `speed = MOMENTUM(ma20-ma50) * 100 / CLOSE`.
- `IF ma20 CROSSES UNDER ma50 THEN SCREENER(speed AS "Speed")`.

### Limitaciones
- Solo detecta el cruce en la barra actual.
- Medias simples retrasadas, propensas a falsos positivos.
- `MOMENTUM` sin periodo explícito puede dar error según versión.

---

## 4. Day Trading filter

**Dirección:** Neutro (utilidad)  
**Timeframe:** Diario (crítico)  
**Estilo:** Pre-filtro de liquidez y volatilidad  
**Complejidad:** Baja

### Objetivo
Pre-seleccionar valores con liquidez mínima, precio mínimo y movimiento absoluto relevante. **No es señal de compra/venta: es filtro para pegar dentro de otros scanners.**

### Lógica resumida
- `MinDailyCapital = 100000000` — facturación mínima (volumen × precio).
- `MinPrice = 0.5` — evita penny stocks.
- Condición: `(volume[2]*DClose(2) > MinDailyCapital OR volume[1]*DClose[1] > MinDailyCapital OR volume*DClose(0) > MinDailyCapital) AND close > MinPrice`.

### Limitaciones
- **Debe ejecutarse en Diario.**
- No mide volumen relativo.
- `ABS` incluye ganancias y pérdidas.

---

## 5. PRTBands

**Archivo original:** `bandsUp = PRTBandsUp.txt`  
**Dirección:** Long  
**Timeframe:** Diario  
**Estilo:** Momentum agresivo, 3 setups de ignición  

### Objetivo
Detectar valores en uptrend con uno de tres setups: nuevo uptrend, cruce de línea corta sobre media, o rebote desde la banda inferior.

### Lógica resumida
- **Señal 1 — `signalUpTrend`:** `upTrendLength` entre 1 y 3 (nuevo uptrend).
- **Señal 2 — `signalShortAboveMedium`:** `shortTerm > mediumTerm` en uptrend.
- **Señal 3 — `signalShortLineBounce`:** `shortTerm` gira al alza tras mínimo.
- **Salida:** `SCREENER[conditionCapital AND conditionShortLineGoingUp AND signal](upTrendLength)`.

### Limitaciones
- `minCapital = 5000` no filtra nada (subir a 100.000).
- Depende del indicador PRTBands (no estándar).

---

## 6. Nivel 1: Reversal Alert

**Dirección:** Long / Short (táctico)  
**Timeframe:** Diario  
**Estilo:** Aviso temprano de giro  
**Complejidad:** Media

### Objetivo
Detectar giros de precio a corto plazo (1 a 5 días) mediante 5 capas de momentum y acción de precio. Generador de watchlist tácticas.

### Capas
1. Divergencia RSI.
2. MACD Histograma girando.
3. RSI cruzando 30/70.
4. Estocástico cruzando desde 20/80.
5. Vela de reversión con volumen (1.5x).

### Salida (`Senal`)
`Dir*10 + Score`. 
- `13` = Bull con 3 capas alineadas.
- `22` = Bear con 2 capas alineadas.
Score máximo = 5.

### Uso
Filtrar los que tengan Score 3 o más (`13`, `14`, `23`). Son avisos tempranos; el contexto del gráfico es vital.

---

## 7. Nivel 2: Trend Change Confirmation

**Dirección:** Long / Short (estructural)  
**Timeframe:** Diario (con confirmación semanal)  
**Estilo:** Confirmación de cambio de tendencia  
**Complejidad:** Alta

### Objetivo
Confirmar cambios de tendencia reales combinando estructura de precio (BOS) y timeframes superiores.

### Capas
1. ADX cayendo (agotamiento).
2. BOS (ruptura de máximo/mínimo de 20).
3. Fallo de ruptura.
4. Alineación semanal (Vervoort).
5. Pendiente EMA200.

### Salida (`Senal`)
`Dir*10 + Fase`.
- `13` = Bull Confirmado (Fase 3).
- `22` = Bear PrimerAviso (Fase 2).
Fases: 1 (Agotamiento), 2 (PrimerAviso), 3 (Confirmado), 4 (Fallido).

### Uso
Buscar `13` o `23` (Confirmado) para mayor fiabilidad. Ignorar `14`/`24` (Fallido).

---

## 8. Nivel 3: Quality Score Composite

**Dirección:** Long / Short (máxima confluencia)  
**Timeframe:** Diario  
**Estilo:** Integrador final  
**Complejidad:** Muy Alta

### Objetivo
Fusionar el Nivel 1 (alertas tempranas) y el Nivel 2 (estructura) en un único score de 0 a 10. Busca el "Santo Grial": un valor que avisa de giro y estructuralmente confirma.

### Capas
Suma las 10 capas (5 del N1 + 5 del N2).

### Salida (`Senal`)
`Dir*10 + Tier`.
- `11` / `21` = Aviso (Score 4-5).
- `12` / `22` = Buena (Score 6-7).
- `13` / `23` = **Excelente (Score 8-10)**.

### Uso
Máxima prioridad en la watchlist. Un `13` significa que todas las capas de momentum y estructura están alineadas.

---

## 9. Tabla de consolidación

| Scanner | Tarea | Dirección | ¿Se solapa con? | Recomendación |
|---|---|---|---|---|
| **ATR Trailing Vervoort** | Radar tendencia long, conservador | Long | PRTBands / Nivel 2 | Conservar si prefieres entradas en pullback/ruptura |
| **PRTBands** | Radar momentum long, agresivo | Long | ATR Trailing / Nivel 1 | Conservar si prefieres entradas más frecuentes |
| **Bearish Engulfing** | Giro bajista por patrón | Short | Death Cross / Nivel 1 | Conservar si operas cortos por patrón |
| **Death Cross SMA20/50** | Cambio tendencia bajista | Short | Bearish Engulfing / Nivel 2 | Conservar si operas cortos por tendencia |
| **Day Trading filter** | Pre-filtro liquidez | Neutro | Ninguno | **No borrar**: utilidad para pegar en otros |
| **Nivel 1 (Reversal Alert)** | Aviso temprano de giro | Ambos | PRTBands | **Conservar**: alimenta la watchlist del N3 |
| **Nivel 2 (Trend Change)** | Confirmación estructural | Ambos | ATR Trailing | **Conservar**: valida la estructura del N3 |
| **Nivel 3 (Quality Score)** | Integrador de alta convicción | Ambos | Todos | **Conservar**: es el disparador final |

---

## 10. Flujo de trabajo: Cómo usar la Trilogía

La mejor forma de operar con los Niveles 1, 2 y 3 no es usarlos por separado, sino como un **embudo de filtrado**. Aquí tienes el flujo recomendado:

### Paso 1: Filtrado Base (Liquidez)
- **Herramienta:** Day Trading filter.
- **Acción:** Ejecútalo primero para eliminar penny stocks y valores con volumen insuficiente. No quieres operar nada que no tenga liquidez.

### Paso 2: El Radar (Nivel 1)
- **Herramienta:** Reversal Alert (Nivel 1).
- **Acción:** Ejecútalo sobre tu lista filtrada. Busca valores con `Senal 13` o `Senal 23`.
- **Resultado:** Obtienes una *watchlist* de valores que están mostrando signos de agotamiento o giro. **No compres aquí.** Muchos fallarán.

### Paso 3: La Confirmación (Nivel 2)
- **Herramienta:** Trend Change Confirmation (Nivel 2).
- **Acción:** Ejecútalo. Si un valor de tu watchlist del Paso 2 aparece aquí con `Senal 13` o `Senal 23` (Fase Confirmado), la probabilidad de giro real aumenta drásticamente. Ha roto estructura y el semanal lo apoya.

### Paso 4: El Disparo (Nivel 3)
- **Herramienta:** Quality Score Composite (Nivel 3).
- **Acción:** Ejecútalo a diario. Si un valor aparece con `Senal 13` (Tier 3 - Excelente), tienes luz verde.
- **Resultado:** Es una señal de máxima convicción. El Nivel 1 avisó y el Nivel 2 confirmó, todo en el mismo día.

### Paso 5: Gestión (Gráfico)
- **Acción:** Abre el gráfico del valor.
- **Stop:** Colócalo por debajo del mínimo de la vela de ruptura (BOS) o del mínimo de las últimas 3-5 velas.
- **Target:** Busca la resistencia más cercana (máximo de 52 semanas, o utiliza la columna `Dist52W` del ATR Trailing).

---

## 11. Revisión rápida de giro al alza (Scanners clásicos)

**Pregunta típica:** “Quiero revisar un giro al alza: una vela que ya ha cruzado y cerrado sobre una media. ¿Qué scanner uso?”

### Respuesta corta (Usando los clásicos)
Usa **PRTBands** para la detección rápida y **ATR Trailing Vervoort** para el contexto semanal.

- **PRTBands `Senal 1` o `2`**: Vela que cruza y cierra sobre una banda/media, o media corta cruza sobre media larga.
- **ATR Trailing `wkBull = 1`**: Confirma que el contexto semanal es alcista.
- **ATR Trailing `Senal 4`**: Si aparece, descarta el long (ha perdido el muro).

### Respuesta corta (Usando la Trilogía)
Si quieres una respuesta más moderna y fiable, sigue el flujo de la sección 10:
1. **Nivel 1** (Aviso).
2. **Nivel 2** (Confirmación estructural).
3. **Nivel 3** (`Senal 13` - Excelente).

### Qué comprobar manualmente en el gráfico
Para cada valor que salga, revisa:
- **Volumen del cruce:** Un cruce sin volumen es sospechoso.
- **RSI:** Evita comprar sobrecomprado (>70) en un giro.
- **Resistencia cercana:** Un giro justo debajo de resistencia mayor no sirve.
- **Stop natural:** El mínimo de la vela de reversión.

---

## 12. Próximos pasos

Cuando abras un chat nuevo, puedes usar este documento así:
1. **Pega este `.md` al inicio** y di: “Tengo estos scanners. Quiero revisar [nombre].”
2. **Pide ajustes**: “Quiero modificar el Nivel 3 para que el score mínimo sea 5.”
3. **Pide backtest o validación**: “¿Cómo puedo validar el Nivel 2 en mi universo?”
4. **Pide un giro al alza**: “Tengo un valor que ha cruzado SMA50 al alza. ¿Qué secuencia de la trilogía uso?”

### Pendientes sugeridos
- [ ] Validar en backtest qué Tier del Nivel 3 funciona mejor (Tier 2 vs Tier 3).
- [ ] Integrar el Day Trading filter mejorado dentro del Nivel 1, 2 y 3.
- [ ] Verificar sintaxis de `ADX` y `ExponentialAverage` en tu versión de PRT (ya aplicado en los scripts, pero verificar en actualizaciones).
- [ ] Probar el Nivel 3 en distintos marcos temporales (Semanal).

---

## 13. Outlier Screener

**Archivo fuente:** `screeners/scanner-ovtlier/scanner-ovtlier.prs` (version vigente: v5)  
**Direccion:** Long  
**Timeframe:** Diario  
**Estilo:** Continuacion de tendencia con momentum y liquidez  
**Complejidad:** Media  
**Guia detallada:** `docs/indicators/outlier-screener.md`

### Objetivo

Detectar valores en tendencia alcista confirmada con momentum sano y liquidez suficiente, ordenados por rendimiento de 5 dias. No busca giros: busca continuacion de tendencia ya en marcha.

### Logica resumida (v5)

- **Tendencia corto:** EMA10 > EMA20 y Close > EMA50.
- **Tendencia largo:** Close > EMA200.
- **Pendiente:** EMA50 con pendiente positiva sobre 5 sesiones.
- **Calidad:** ADX(14) > 20.
- **Momentum:** RSI(14) > 58 y Close > Close[5].
- **Liquidez:** VolumeMA20 > 500.000 y DollarVolume > 5.000.000.
- **Anti-sobre-extension:** distancia a EMA50 < 20%.

### Evolucion de versiones

| Version | Cambios clave |
|---|---|
| v1 | Base: EMA10>EMA20, Close>EMA50, RSI>55, Close>10 |
| v2 | + Volumen 1M, + Close>Close[5], + Vol Ratio |
| v3 | + EMA200, RSI>58, + Ret 20d, + ATR% (regresion volumen a 100k) |
| v4 | Corrige volumen a 500k, fix ATR(Close), + Dollar Volume, RS->Ret |
| v5 | + ADX>20, + pendiente EMA50, + Dist EMA50<20% (vigente) |

### Columnas de salida

`Mom 5d %`, `RSI`, `ADX`, `Ret 20d %`, `ATR %`, `Vol Ratio`, `Dist EMA50 %`. Ordenacion recomendada: `Mom 5d %` descendente.

### Fortalezas

- Combina tendencia multi-plazo (EMA50 + EMA200) con calidad (ADX) y liquidez monetaria.
- Filtro anti-sobre-extension evita entradas en climas de agotamiento.
- Columna ATR% util para position sizing directo desde el screener.

### Limitaciones

- No detecta giros: si el valor acaba de cambiar de tendencia, no aparecera.
- ADX > 20 es permisivo: en fases laterales puede colar valores con tendencia debil.
- Dist EMA50 < 20% puede excluir breakouts muy fuertes.
- Depende del timeframe diario: no usar en intradia sin recalibrar.

### Cuando usarlo

- Para construir watchlist long diaria de continuacion de tendencia.
- Como primer filtro antes de analisis grafico manual.
- En mercados alcistas o neutros con amplitud razonable.

### Cuando NO usarlo

- En mercados claramente bajistas (pocos resultados y de baja calidad).
- Para buscar suelos o giros: usa la Trilogia (Niveles 1-3).
- Para cortos.

*Documento generado como referencia personal. Cada sección es autocontenida para facilitar la revisión individual en chats futuros.*