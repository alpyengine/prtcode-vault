# Scanner: Reversal Alert (Nivel 1)

**Versión:** 1.0
**Plataforma:** ProRealTime — ProScreener
**Periodo:** Diario
**Fichero:** `scanner-reversal-alert.prt`
**ADR:** `ADR-0003-scanner-reversal-alert.md`

---

## 1. Objetivo

Detectar **avisos tempranos de giro** en el precio a corto plazo (1 a 5 días). Este scanner no busca confirmar un cambio de tendencia macro (eso lo hace el Nivel 2), sino detectar agotamientos y primeras reacciones. Es un generador de *watchlist* tácticas.

---

## 2. Capas de confirmación (0 a 5 puntos)

| Capa | Nombre | Qué mide | Cuándo suma |
|---|---|---|---|
| **A1** | Divergencia RSI | Precio hace nuevo mínimo/máximo pero el RSI no le acompaña | `close <= lowest[20]` y `RSI > RSI[5]` (Bull) |
| **B1** | MACD girando | El histograma cruza el cero o gira desde negativo | `hist[1] < 0` y `hist > hist[1]` (Bull) |
| **B2** | RSI nivel clave | Salida de zona de sobreventa/sobrecompra | `RSI CROSSES OVER 30` (Bull) |
| **B3** | Estocástico | Cruce desde zona extrema | `Stoch CROSSES OVER 20` desde < 20 (Bull) |
| **C3** | Vela + Volumen | Vela de fuerza con volumen 1.5x superior a la media | `close > open`, `close > high[1]`, `vol > media*1.5` |

---

## 3. Cómo leer la columna `Senal`

El código combina la **dirección** (decenas) y el **Score** (unidades):
- `12` = Bull (1) con Score 2.
- `13` = Bull (1) con Score 3.
- `22` = Bear (2) con Score 2.
- `24` = Bear (2) con Score 4.

**Cuanto mayor sea el número de unidades, más capas se han alineado y más fuerte es el aviso.** Un `14` es una señal de agotamiento muy potente.

---

## 4. Cómo utilizarlo

1. **Filtra el ruido:** Busca valores con `Senal` que terminen en 3, 4 o 5 (ej. `13`, `14`, `23`). Los que tienen score 2 (`12` o `22`) son muy tempranos y suelen fallar más.
2. **Contexto es rey:** Un `Senal 13` en un soporte semanal o en la EMA200 es una oportunidad excelente. Un `Senal 13` en tierra de nadie es ruido.
3. **Stop y Target:** Este scanner no calcula niveles. Usa el mínimo de la vela de reversion (o el mínimo de las últimas 3 velas) como stop.
4. **Combínalo con el Nivel 2:** Si el Nivel 1 te avisa (ej. `Senal 13`) y unos días después el Nivel 2 confirma (ej. `Senal 13` de Trend Change), tienes una entrada de alta probabilidad.

---

## 5. Limitaciones

- **Es ruidoso por diseño:** Alerta de giros, no de tendencias. Muchas señales fracasarán.
- **Divergencia RSI simple:** La capa A1 no busca divergencias complejas, solo que el precio haga un mínimo de 20 días mientras el RSI a 5 días esté subiendo.
- **Volumen relativo:** La capa C3 exige un pico de volumen (1.5x), lo cual es bueno, pero puede ignorar giros por absorción silenciosa.
- **Límite de 3 columnas:** No muestra qué capa exacta disparó la señal. Hay que deducirlo por el score.