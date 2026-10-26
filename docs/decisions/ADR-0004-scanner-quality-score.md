# ADR-0004: Diseño del scanner Quality Score Composite

**Fecha:** 2026-10-26
**Estado:** Aceptado
**Contexto:** Necesidad de unificar las alertas tempranas (Nivel 1) y las confirmaciones estructurales (Nivel 2) en un único sistema de ranking.

## Decisión

Implementar un scanner que suma 10 capas (5 del Nivel 1 + 5 del Nivel 2), generando un Score de 0 a 10. 
El resultado se clasifica en Tiers:
- Tier 3 (8-10): Excelente.
- Tier 2 (6-7): Buena.
- Tier 1 (4-5): Aviso.
Salida combinada `Dir*10 + Tier`.

## Justificación del orden de construcción

Se construyó en el orden 2 -> 1 -> 3. El Nivel 2 sentó las bases estructurales (BOS, Vervoort), el Nivel 1 añadió la capa de momentum (MACD, RSI) y el Nivel 3 es el integrador final. Construir el Nivel 3 primero habría carecido de componentes probados.

## Alternativas rechazadas

- **Suma simple sin Tiers:** Mostrar un Score del 0 al 10 es útil, pero agruparlo en Tiers (1, 2, 3) facilita la toma de decisiones rápida en la interfaz.
- **Requerir un mínimo de 1 capa de cada nivel:** Se rechazó porque hay giros válidos que no necesitan un BOS (ej. un failed breakout masivo) y otros que no necesitan un cruce de MACD. El Score global premia la confluencia sin ser excesivamente dogmático.

## Consecuencias

- El número de señales se reduce drásticamente (filtro de calidad).
- Requiere 18 variables calculadas simultáneamente (rendimiento óptimo en PRT).