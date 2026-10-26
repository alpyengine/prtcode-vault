# Scanner: Trend Change Confirmation (Nivel 2)

**Versión:** 1.6 (Final compilada)
**Plataforma:** ProRealTime — ProScreener
**Periodo:** Diario
**Fichero:** `scanner-trend-change-confirmation.prt`
**ADR:** `ADR-0002-scanner-trend-change-confirmation.md`

---

## 1. Objetivo

Detectar **cambios de tendencia con confirmación estructural y de timeframe superior**. El scanner responde a tres preguntas:
1. ¿La tendencia previa se está agotando? (A2)
2. ¿El precio ha roto la estructura? (C1 y C2)
3. ¿El timeframe superior lo confirma? (D1 y D2)

Devuelve un **score 0–5 por dirección** y una **fase** que indica el punto del proceso.

---

## 2. Capas de confirmación

| Capa | Nombre | Qué mide | Cuándo suma |
|---|---|---|---|
| **A2** | ADX cayendo | Agotamiento de la tendencia previa | `ADX < ADX[5]` y `ADX < 25` |
| **C1** | BOS (Break of Structure) | Ruptura de máximo/mínimo de 20 barras | `close > highest[20](high[1])` (bull) |
| **C2** | Fallo de ruptura | Trampa: rompe nivel y cierra de vuelta dentro | Nuevo mínimo + cierre alcista en mitad superior (bull) |
| **D1** | Alineación semanal | Muro Vervoort semanal alineado | `close > lineW` y `close[1] > lineW[1]` (bull) |
| **D2** | Pendiente EMA200 | Tendencia de fondo alineada | `ExponentialAverage[200] > ExponentialAverage[200][10]` (bull) |

---

## 3. Fases y Código `Senal`

| Fase | Código | Significado | Qué hacer |
|---|---|---|---|
| **Agotamiento** | 1 | Solo A2. Tendencia débil, sin estructura rota. | Watchlist. No actuar. |
| **PrimerAviso** | 2 | Estructura rota + 1 confirmación HTF. | Entrada táctica. Más riesgo. |
| **Confirmado** | 3 | Estructura rota + 2 confirmaciones HTF. | Entrada con convicción. |
| **Fallido** | 4 | Estructura rota contra ambas HTF. | No operar. Fakeout probable. |

La columna **`Senal`** combina dirección (decenas) y fase (unidades):
- `13` = Bull Confirmado.
- `22` = Bear PrimerAviso.
- `14` = Bull Fallido.

---

## 4. Columnas de salida

Por límite de 3 columnas de la licencia:
- **`Senal`**: Dirección + Fase.
- **`BullSc`**: Score bull (0–5).
- **`BearSc`**: Score bear (0–5).

---

## 5. Notas de implementación y limitaciones de PRT

- **Filtro de mercado eliminado:** ProRealTime (versión estándar) no permite usar `EQUITYFRAME` para consultar índices de otras bolsas (ej. SPY en EE. UU. mientras escaneas Europa). Se ha eliminado para garantizar la compilación.
- **Sintaxis específica:** Se usa `ADX[N]` y `ExponentialAverage[N]` para que el compilador de ProRealTime lo acepte.
- **Variables no usadas:** El cálculo del ATR diario (`atrD`) se ha eliminado porque el `Stop` y `Target` no se muestran (límite de columnas). PRT lanza error si calculas una variable y no la usas.
- **Lag de la EMA200:** En PRT la EMA200 necesita muchas barras de historial. Puede que en valores con poco historial no calcule bien la pendiente (D2).

---

## 6. Cómo leer los resultados

1. **Filtra por fase:** `Senal = 13` o `23` (Confirmado) para mayor fiabilidad. `12` o `22` (PrimerAviso) para vigilar.
2. **Mira los scores:** `BullSc` alto (4 o 5) indica que casi todas las capas están alineadas.
3. **Revisa el gráfico:** Comprueba el volumen del BOS, el RSI y si hay resistencias mayores cerca.