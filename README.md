<!-- README.md · v1.7 · 2026-10-18 -->

# prtcode-vault

Scripts de ProRealTime (ProBuilder, ProBacktest/ProOrder y ProScreener) de "La Granja".
Sigue las mismas convenciones que `pinescripts-vault`.

## Estructura

```
indicators/<nombre>/<nombre>.prt        Indicadores ProBuilder
strategies/<nombre>/<nombre>.pts        Estrategias ProBacktest / ProOrder
screeners/<nombre>/<nombre>.prs         Screeners ProScreener
docs/indicators/<nombre>.md             Ficha / especificación de cada script
docs/decisions/ADR-XXXX-<tema>.md       Decisiones de diseño
docs/validation/<nombre>/PRT-XXX.md     Fichas de validación
```

ProRealTime no impone extensión: el código se pega en la plataforma. Las extensiones `.prt`, `.pts` y `.prs` solo sirven para distinguir el tipo en Git.

## Scripts

| Script | Tipo | Versión | Estado |
|---|---|---|---|
| [scanner-atr-trailing](docs/indicators/scanner-atr-trailing.md) | ProScreener | v1.2 | En validación |
| [atr-trailing-vervoort](docs/indicators/atr-trailing-vervoort.md) | Indicador | v1.5 | En validación |

## Convenciones

- Ramas en kebab-case, sin prefijo (por ejemplo, `scanner-atr-trailing`).
- Conventional Commits en inglés.
- Tags por script: `<nombre>-prt/vX.Y.Z`.
- A `main` solo llega código con su ficha PRT cerrada.

## Licencia

MIT.
