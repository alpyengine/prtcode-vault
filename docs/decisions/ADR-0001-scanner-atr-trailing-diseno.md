<!-- ADR-0001 · v1.0 · 2026-10-18 -->

# ADR-0001 — Diseño del scanner ATR trailing (ProScreener)

- **Estado:** Aceptada
- **Fecha:** 2026-10-18
- **Script:** `screeners/scanner-atr-trailing/scanner-atr-trailing.prs`

## Contexto

ProScreener con licencia gratuita muestra 3 columnas (confirmado con test) y admite una sola instrucción `SCREENER` si hay varias columnas. La lista mezcla ETF y acciones, que usan múltiplos diarios distintos. El screener se corre los sábados, y a veces entre semana.

## Decisiones

1. **Un solo script para las 4 señales.** Una única instrucción `SCREENER` con filtro `sigCode > 0`.
2. **Código combinado en la columna Senal.** Un dígito por señal activa (por ejemplo, `23`). No se oculta ninguna señal.
3. **Dos listas, ETF y acciones.** El mismo código, cambiando `isETF` entre 1 y 0. ProScreener no distingue ETF de acción de forma fiable.
4. **Parámetro `semanaCerrada`.** 1 el sábado (vela semanal actual, ya cerrada). 0 entre semana (desfase de 1 en el bloque semanal, para usar la última semana cerrada). `UPDATEONCLOSE` no se usa porque el manual de ProScreener no lo documenta.
5. **3 columnas ahora y 6 preparadas.** 3 columnas: Senal, Dist52W, Stop. 6 columnas: + DistMuro, RSI14, TD9. La línea de 6 queda comentada con `REM`.
6. **ATR sin columna propia.** Se deduce del Stop, y así queda sitio para TD9 en la versión de 6.
7. **Trinquete Vervoort con 4 casos** (sigue alcista, sigue bajista, cruce al alza, cruce a la baja). Así la línea salta de lado en cada cruce y no se queda pegada al nivel antiguo.
8. **Solo `REM` en comentarios y solo ASCII en el código**, para evitar errores de compilación.

## Consecuencias

- Hay que correr el screener dos veces (ETF y acciones).
- Ordenar por señal y después por distancia no es posible a la vez: se ordena por `Dist52W` y la señal se lee en su columna.
- Pasar a 6 columnas es cambiar una línea.
