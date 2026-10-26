# Outlier Screener — Guía de referencia

**Plataforma:** ProRealTime / ProScreener  
**Archivo fuente:** `screeners/scanner-ovtlier/scanner-ovtlier.prs`  
**Versión vigente:** v5  
**Dirección:** Long  
**Timeframe:** Diario  
**Estilo:** Continuación de tendencia con momentum sano y liquidez

---

## 1. Objetivo

Detectar valores en tendencia alcista confirmada con momentum sano y liquidez suficiente, ordenados por rendimiento de 5 días. No es un buscador de giros ni un detector de outliers estadísticos, a pesar del nombre: es un filtro de **continuación de tendencia**.

Uso típico: alimentar una watchlist diaria de candidatos long que ya están en movimiento, no que lo van a iniciar.

---

## 2. Evolución de versiones

| Versión | Cambios clave | Estado |
|---|---|---|
| v1 | Base: EMA10>EMA20, Close>EMA50, RSI>55, Close>10 | Base |
| v2 | + Volumen 1M, + Close>Close[5], + Vol Ratio | Superada |
| v3 | + EMA200, RSI>58, + Ret 20d, + ATR% (con regresión de volumen a 100k) | Superada |
| v4 | Corrige volumen a 500k, fix `ATR(Close)`, + Dollar Volume, renombra RS→Ret | Superada |
| v5 | + ADX>20, + pendiente EMA50>0, + Dist EMA50<20% | **Vigente** |

---

## 3. Filtros de la versión vigente (v5)

| Filtro | Condición | Para qué |
|---|---|---|
| Tendencia corto | EMA10 > EMA20 y Close > EMA50 | Alineación de medias a corto plazo |
| Tendencia largo | Close > EMA200 | No operar contra tendencia primaria |
| Pendiente EMA50 | `val50 > val50[5]` | Evita medias planas/bajistas |
| Calidad | ADX(14) > 20 | Tendencia con fuerza direccional real |
| Momentum RSI | RSI(14) > 58 | Momentum sano sin sobrecompra extrema |
| Precio mínimo | Close > 10 | Evita penny stocks |
| Volumen | Media 20d > 500.000 acciones | Liquidez en unidades |
| Liquidez monetaria | Media 20d × Close > 5.000.000 | Liquidez en dólares (más robusta) |
| Momentum precio | Close > Close[5] | Confirmación de impulso reciente |
| Anti-sobre-extensión | Dist EMA50 < 20% | Evita comprar ya muy estirado |

---

## 4. Columnas de salida

| Columna | Qué mide | Cómo interpretarla |
|---|---|---|
| **Mom 5d %** | Rendimiento de 5 sesiones | Criterio de clasificación recomendado (descendente). Valores >5% indican impulso fuerte. |
| **RSI** | RSI(14) | >58 es el mínimo del filtro. >70 es zona de sobrecompra; no es descarte automático pero conviene vigilar. |
| **ADX** | Fuerza de tendencia (14) | >20 en el filtro. >30 es tendencia fuerte; >40 es muy fuerte pero puede estar agotándose. |
| **Ret 20d %** | Retorno de 20 sesiones | Confirma tendencia mensual. Positivo y creciente = tendencia sana. |
| **ATR %** | ATR(14) como % del precio | Volatilidad normalizada. Usar para position sizing: a mayor ATR%, menor tamaño de posición. |
| **Vol Ratio** | Volumen actual / media 20d | >1 indica interés creciente. >2 puede ser catalizador (noticia, resultados). |
| **Dist EMA50 %** | Distancia % a la EMA50 | <20% por filtro. Valores cercanos a 0 indican entrada cerca de soporte dinámico. |

**Ordenación:** por defecto se ordena por `Mom 5d %` descendente al hacer clic en la cabecera. Los primeros resultados son los de mayor impulso reciente.

---

## 5. Cómo leer los resultados

**Resultado sano (día normal):** 10–40 valores. Si sale mucho más, el mercado está en un rally amplio (filtrar por `Dist EMA50 < 10%` para entradas más cercanas a soporte).

**Resultado con muchas señales sospechosas:** revisa el ADX. Si todos los valores tienen ADX entre 20 y 25, el mercado puede estar en una fase de tendencia débil. Considera subir `filtQuality` a 25.

**Resultado vacío:** poco habitual pero posible en correcciones fuertes o días de pánico. Ver sección 6.

---

## 6. Qué hacer si sale vacío

Orden de relajación recomendado (relajar **uno** a la vez, no todos):

1. `filtNotOver`: 20 → 25 (permite valores algo más estirados)
2. `filtQuality`: 20 → 15 (acepta tendencias más débiles)
3. `filtMoment`: 58 → 55 (vuelve al umbral de v1)

Si con los tres relajados sigue vacío, el mercado no está en condiciones para esta estrategia. No fuerces el screener: espera.

---

## 7. Flujo post-screener

Para cada valor del top 5–10 de la lista:

1. **Abrir gráfico diario.** Verificar visualmente la tendencia (no confiar solo en el filtro).
2. **Comprobar volumen del movimiento reciente.** Un Mom 5d % alto con Vol Ratio < 1 es sospechoso.
3. **Localizar soporte y resistencia.** La EMA50 y el mínimo de las últimas 3–5 velas son candidatos a stop.
4. **Calcular position sizing** con ATR%: riesgo por operación / (2 × ATR%) = % del capital.
5. **Stop:** mínimo de las últimas 3–5 velas o `Close - 2×ATR`.
6. **Target:** resistencia más cercana (máximos de 20 o 52 semanas).

---

## 8. Notas técnicas

- **ADX:** si tu versión de ProRealTime se queja de `ADX[14]`, prueba `ADX[14](Close)`. Funcionalmente equivalente en la práctica.
- **EMA200** en ProScreener calcula sobre 256 velas (1.024 en Premium). Con 256 velas, la EMA200 tiene solo ~56 velas de maduración real: es aceptable pero no óptima.
- **Dollar volume** es más robusto que el volumen en acciones para comparar valores de distinto precio. Si detectas falsos positivos de liquidez, sube el umbral a 10M o 20M.
- **Filtro top-down SPY:** no está en el código por problemas de cruce de exchanges en ProScreener. Se aplica manualmente fuera del screener (dashboard propio o TradingView). Si el SPY está por debajo de su EMA200, considera no operar este screener ese día.
- **`valSPY = 1`** aparece en v2 como código inerte; se eliminó en v4. No lo reintroduzcas sin implementar el filtro real.

---

*Guía autocontenida. Para el detalle de cada versión, ver `screeners/scanner-ovtlier/scanner-ovtlier.prs` en su historial git.*
