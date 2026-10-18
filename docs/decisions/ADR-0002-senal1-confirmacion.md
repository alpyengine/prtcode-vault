<!-- ADR-0002 · v1.0 · 2026-10-18 -->

# ADR-0002 — Señal 1 (giro semanal): confirmación una semana después del cruce

- **Estado:** Aceptada
- **Fecha:** 2026-10-18
- **Afecta a:** `scanner-atr-trailing` v1.2 · `atr-trailing-vervoort` v1.1

## Contexto

La spec original pedía: "la semana cerró con cuerpo por encima de la línea ATR semanal ×1,5, y la semana anterior estaba por debajo". Falta decir con qué línea se compara el cuerpo.

En la línea Vervoort, al cruzar al alza la línea salta: deja de ser resistencia (muro antiguo) y pasa a soporte a 1,5 ATR por debajo del cierre (muro nuevo).

## Descubrimiento

Se probaron 4 reglas con datos semanales reales: 6 tickers (VGT, SCHD, VDC, KO, JPM y XOM), unas 50 semanas, 16 cruces al alza.

| Regla | Señales | Lectura |
|---|---|---|
| A. Cierre por encima del muro | 16 / 16 | No filtra |
| B. Cuerpo por encima del muro **nuevo** (v1.1) | 15 / 16 | Casi igual que A: el muro nuevo queda 1,5 ATR por debajo del cierre y la apertura casi siempre lo supera |
| C. Cuerpo por encima del muro **antiguo**, la misma semana | **0 / 16** | Señal muerta: la semana del cruce abre por debajo de la resistencia, porque el cruce ocurre durante esa semana. Solo saltaría con un salto de apertura |
| **D. Confirmación**: la semana **siguiente** al cruce sigue por encima y su cuerpo entero supera el muro antiguo | **8 / 16** | Filtra la mitad de los cruces y respeta la idea de ruptura clara |

Fechas en que salta la regla D: VGT 13-abr-2026 · SCHD 08-dic-2025 y 04-may-2026 · KO 26-ene-2026 y 18-may-2026 · JPM 15-dic-2025 y 13-abr-2026 · XOM 27-jul-2026 (semanas que empiezan ese lunes).

## Decisión

Se adopta la **regla D**. Con `wo` = desfase de `semanaCerrada`:

```
sig1 = close[wo+2] <= lineW[wo+2]          semana -2: por debajo del muro antiguo
   AND close[wo+1] >  lineW[wo+1]          semana -1: cruce al alza
   AND close[wo]   >  lineW[wo]            semana  0: sigue por encima
   AND MIN(open[wo], close[wo]) > lineW[wo+2]   cuerpo por encima del muro antiguo
```

## Consecuencias

- La señal 1 llega **una semana más tarde** que el cruce.
- Un cruce que se da la vuelta la semana siguiente ya no da señal (falso giro filtrado).
- La señal 4 (pérdida del muro) no cambia: se mantiene con el cierre de la semana del cruce.
- Hace falta una semana más de historial semanal (`[wo+2]`), algo irrelevante con 256 velas.
- Caso a vigilar: SCHD, VDC y KO cruzaron al alza la semana del 12-oct-2026. Darán señal 1 el 24-oct si esa semana su cuerpo queda por encima de 33,90 / 228,50 / 90,44.
