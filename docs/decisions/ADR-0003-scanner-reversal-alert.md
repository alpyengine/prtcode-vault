# ADR-0003: Diseño del scanner Reversal Alert (Nivel 1)

**Fecha:** 2026-10-26
**Estado:** Aceptado
**Contexto:** Necesidad de un scanner de aviso temprano de giros de precio (1-5 días), complementario al Nivel 2 (Trend Change Confirmation).

## Decisión

Implementar un scanner táctico de 5 capas, con scoring de 0 a 5, y salida combinada `Dir*10 + Score`. Salida limitada a 3 columnas (`Senal`, `BullSc`, `BearSc`).

## Capas elegidas

- **A1 (Divergencia RSI):** Detección temprana de agotamiento de impulso.
- **B1 (MACD Histograma):** Cambio de momentum a corto plazo.
- **B2 (RSI cruce de 30/70):** Confirmación clásica de salida de extremos.
- **B3 (Estocástico):** Confirmación de giro en el corto plazo.
- **C3 (Vela + Volumen):** Confirmación de acción de precio (vela de reversión con fuerza institucional).

## Alternativas rechazadas

- **Usar solo RSI:** El RSI puede quedarse sobrevendido durante semanas. Requiere cruces o divergencias.
- **Usar solo patrones de velas:** Las velas sin volumen ni contexto fallan mucho.
- **Incluir la EMA200:** La EMA200 es demasiado lenta para un scanner de alerta temprana (1-5 días), se reserva para el Nivel 2.

## Consecuencias

- Alta tasa de falsos positivos (es un radar de alertas, no de confirmaciones).
- Requiere interpretación visual del gráfico para descartar "tierra de nadie".
- Dependencia de la sintaxis de `Stochastic` y `MACDline` de PRT.