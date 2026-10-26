# ADR-0003: Diseño del scanner Reversal Alert (Nivel 1)

**Fecha:** 2026-10-26
**Estado:** Aceptado
**Contexto:** Necesidad de un scanner de aviso temprano de giros de precio (1-5 días), complementario al Nivel 2.

## Decisión

Implementar un scanner táctico de 5 capas, con scoring de 0 a 5, y salida combinada `Dir*10 + Score`. Salida limitada a 3 columnas (`Senal`, `BullSc`, `BearSc`).

## Capas elegidas

- **A1 (Divergencia RSI):** Detección temprana de agotamiento.
- **B1 (MACD Histograma):** Cambio de momentum. Se renombró la variable a `macdMain` para evitar conflicto con la palabra reservada `MACDline` de PRT.
- **B2 (RSI cruce de 30/70):** Confirmación clásica.
- **B3 (Estocástico):** Confirmación de giro. Se aplicó la sintaxis `Stochastic[N,K](close)` de PRT.
- **C3 (Vela + Volumen):** Confirmación de acción de precio.

## Alternativas rechazadas

- **Usar solo RSI:** Puede quedarse sobrevendido durante semanas.
- **Usar solo patrones de velas:** Fallan sin contexto.
- **Incluir la EMA200:** Demasiado lenta para alertas de 1-5 días.

## Consecuencias

- Alta tasa de falsos positivos (radar de alertas).
- Requiere interpretación visual del gráfico.
- Restricción estricta de ProRealTime sobre nombres de variables reservadas y sintaxis de funciones.