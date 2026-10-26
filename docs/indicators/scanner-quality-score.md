# Scanner: Quality Score Composite (Nivel 3)

**Versión:** 1.0
**Plataforma:** ProRealTime — ProScreener
**Periodo:** Diario
**Fichero:** `scanner-quality-score.prt`
**ADR:** `ADR-0004-scanner-quality-score.md`

---

## 1. Objetivo

Este es el scanner definitivo de la saga. Fusiona la **velocidad del Nivel 1** (alertas tempranas de reversión) con la **fiabilidad del Nivel 2** (cambios estructurales confirmados). 

Busca el "Santo Grial": un valor que ha dado señales de agotamiento (MACD, RSI, Volumen) **Y** que además ha roto estructura con confirmación semanal.

---

## 2. Sistema de Scoring (0 a 10)

Suma 10 capas en total:
- 5 capas del Nivel 1 (RSI Div, MACD Hist, RSI Cross, Stoch Cross, Vela+Vol).
- 5 capas del Nivel 2 (ADX, BOS, Failed BO, Vervoort, EMA200).

Se muestran los valores a partir de **4 puntos**.

---

## 3. Lectura de la columna `Senal` (El Tier)

La columna `Senal` combina dirección (decenas) y calidad (unidades). **La calidad (Tier) es lo más importante:**

- **`11` / `21` (Tier 1 - Aviso):** Score 4-5. El valor está despertando, pero aún es pronto. Útil para vigilar.
- **`12` / `22` (Tier 2 - Buena):** Score 6-7. Alta probabilidad de giro. Confluencia clara entre señal temprana y estructura.
- **`13` / `23` (Tier 3 - Excelente):** Score 8-10. **Máxima convicción.** Todas las capas (o casi todas) están alineadas. Son las señales que merecen el mayor tamaño de posición.

*Ejemplo:* `13` significa **Bull Excelente (Tier 3)**. `21` significa **Bear Aviso (Tier 1)**.

---

## 4. Cómo utilizarlo

1. **Filtra los excelentes:** Ordena o filtra por `Senal = 13` o `Senal = 23`. Son pocos al año, pero suelen ser los giros más rentables.
2. **Revisa el gráfico:** Un `Senal 13` justo en un soporte de 52 semanas (mira el `Dist52W` de otros scanners) es una entrada casi perfecta.
3. **Gestión de riesgo:** El stop debe ir por debajo del mínimo de la vela que rompió la estructura (el BOS del Nivel 2).

---

## 5. Limitaciones

- **Es restrictivo:** Un score de 8+ es difícil de ver. Puede haber semanas sin señales. Es normal.
- **Límite de 3 columnas:** No puedes ver cuál de las 10 capas falló. Confía en el Score Total (`BullSc` / `BearSc`).
- **Riesgo de sobreoptimización:** Al juntar 10 capas, en un mercado muy lateral pueden producirse "falsos positivos de confluencia".