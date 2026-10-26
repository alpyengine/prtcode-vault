
# Scanner: Reversal Alert (Nivel 1)

**Versión:** 1.1 (Final compilada)
**Plataforma:** ProRealTime — ProScreener
**Periodo:** Diario
**Fichero:** `scanner-reversal-alert.prt`
**ADR:** `ADR-0003-scanner-reversal-alert.md`

---

## 1. Objetivo

Detectar **avisos tempranos de giro** en el precio a corto plazo (1 a 5 días). Es un generador de *watchlist* tácticas.

---

## 2. Capas de confirmación (0 a 5 puntos)

| Capa | Nombre | Qué mide | Cuándo suma |
|---|---|---|---|
| **A1** | Divergencia RSI | Precio hace nuevo mínimo pero RSI sube | `close <= lowest[20]` y `RSI > RSI[5]` (Bull) |
| **B1** | MACD girando | Histograma cruza el cero o gira | `hist[1] < 0` y `hist > hist[1]` (Bull) |
| **B2** | RSI nivel clave | Salida de zona de sobreventa/sobrecompra | `RSI CROSSES OVER 30` (Bull) |
| **B3** | Estocástico | Cruce desde zona extrema | `Stochastic CROSSES OVER 20` desde < 20 (Bull) |
| **C3** | Vela + Volumen | Vela de fuerza con volumen 1.5x superior | `close > open`, `close > high[1]`, `vol > media*1.5` |

---

## 3. Cómo leer la columna `Senal`

El código combina la **dirección** (decenas) y el **Score** (unidades):
- `12` = Bull (1) con Score 2.
- `13` = Bull (1) con Score 3.
- `22` = Bear (2) con Score 2.
- `24` = Bear (2) con Score 4.

**Cuanto mayor sea el número de unidades, más capas se han alineado y más fuerte es el aviso.**

---

## 4. Cómo utilizarlo

1. **Filtra el ruido:** Busca valores con `Senal` que terminen en 3, 4 o 5 (ej. `13`, `14`).
2. **Contexto:** Un `Senal 13` en un soporte semanal es una oportunidad. En tierra de nadie es ruido.
3. **Stop:** Usa el mínimo de la vela de reversión como stop.
4. **Combínalo con el Nivel 2:** Si el Nivel 1 avisa y el Nivel 2 confirma, tienes una entrada de alta probabilidad.

---

## 5. Limitaciones y notas de implementación

- **Es ruidoso por diseño:** Alerta de giros, no de tendencias.
- **Variables reservadas:** PRT tiene `MACDline` como palabra reservada, por lo que en este script usamos `macdMain`.
- **Sintaxis Estocástico:** Se debe usar `Stochastic[N,K](close)` con paréntesis, de lo contrario da error de compilación (línea 38).
- **Límite de 3 columnas:** No muestra qué capa exacta disparó la señal. Hay que deducirlo por el score.