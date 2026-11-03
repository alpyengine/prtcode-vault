# Test Outlier v6 vs v7a — Protocolo

**Inicio:** 2026-11-03
**Fin previsto:** 2026-11-24 (inicio + 21 días naturales)
**Universo:** US NYSE Stocks
**Timeframe:** Diario
**Ejecución:** Fin de sesión (mismo horario cada día)
**Criterio del Screener:** Match ALL conditions (AND) — todas las condiciones a la vez.

## Configuración del Screener (Fija durante el test)
- **Columnas mostradas:** LAST (por defecto), Mom 5d %, ADX, RSI.
- **Ordenación:** Mom 5d % descendente.
- **Filtro SPY:** Manual. Si el SPY está por debajo de su EMA200, no se opera ese día (anotar en notas).

## Reglas
1. Ejecutar ambos screeners cada día laborable sobre el mismo universo.
2. Registrar resultados en `log_diario.csv` el mismo día.
3. Anotar el top 10 de cada versión (o todos si hay menos).
4. Seguimiento a 5 sesiones en `seguimiento_senales.csv`.
5. No cambiar el código de v6 ni v7a durante el test.

## Definiciones Operativas (No cambiar durante el test)
- **WIN a 5d:** Retorno > +3%.
- **FLAT a 5d:** Retorno entre -1% y +3%.
- **LOSS a 5d:** Retorno < -1%.
- **Falso positivo (giro <1d):** El cierre del día siguiente a la señal es inferior al precio de entrada.
- **Solapamiento:** Tickers comunes en el Top 10 de ambas versiones / Total Top 10 (se calcula diario y se promedia).
- **Calidad del top 5:** Retorno medio a 5d de los 5 primeros tickers de cada versión.

## Criterios de decisión (A las 3 semanas)

| Métrica | Peso | Umbral favorable a v7a |
|---|---|---|
| Solapamiento tickers | — | < 80% |
| Frecuencia media diaria | — | entre 2 y 15 resultados |
| Follow-through 5d >3% | 40% | > 55% de las señales |
| Falsos positivos (giro <1d) | 30% | < 20% de las señales |
| Calidad del top 5 | 30% | mejor retorno medio a 5d que v6 |

## Decisión final
- v7a gana en >=2 de las 3 métricas con peso -> promocionar a v7 (sobrescribir `scanner-ovtlier.prs`).
- Empate o v6 gana -> archivar v7a en `_archive/`.