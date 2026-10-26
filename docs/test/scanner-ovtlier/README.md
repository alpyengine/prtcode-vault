# Test Outlier v6 vs v7a — Protocolo

**Inicio:** pendiente
**Fin previsto:** inicio + 21 dias naturales
**Universo:** multimercado
**Timeframe:** diario
**Ejecucion:** fin de sesion (mismo horario cada dia)

## Reglas

1. Ejecutar ambos screeners cada dia laborable sobre el mismo universo.
2. Registrar resultados en `log_diario.csv` el mismo dia.
3. Anotar el top 10 de cada version (o todos si hay menos).
4. Seguimiento a 5 sesiones en `seguimiento_senales.csv`.
5. No cambiar el codigo de v6 ni v7a durante el test.

## Criterios de decision (a las 3 semanas)

| Metrica | Peso | Umbral favorable a v7a |
|---|---|---|
| Solapamiento tickers | — | < 80% |
| Frecuencia media diaria | — | entre 2 y 15 resultados |
| Follow-through 5d >3% | 40% | > 55% de las senales |
| Falsos positivos (giro <1d) | 30% | < 20% de las senales |
| Calidad del top 5 | 30% | mejor retorno medio a 5d que v6 |

## Decision final

- v7a gana en >=2 de las 3 metricas con peso -> promocionar a v7
  (sobrescribir `scanner-ovtlier.prs`).
- Empate o v6 gana -> archivar v7a en `_archive/`.
