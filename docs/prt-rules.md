<!-- prt-rules.md · v1.4 · 18-oct-2026 · La Granja -->

# PRT Rules — errores y reglas reales de ProRealTime

Reglas aprendidas al compilar y probar scripts en ProRealTime.
Complementa la skill `prt-script`. No repite el manual: solo lo que falló, sorprendió o no está claro en él.

Leer antes de escribir o depurar cualquier `.prt`, `.pts` o `.prs`.

---

## Cómo añadir una regla

Una regla por línea, con este formato:

`[MÓDULO] Regla corta. — Origen: script/versión · fecha · ✅ confirmada | ⚠️ por confirmar`

- **MÓDULO**: GEN, IND, ORD, SCR, MTF.
- **✅ confirmada**: probada en la plataforma (compila o falla de verdad).
- **⚠️ por confirmar**: sale del manual o de una sospecha, aún sin probar.

---

## 1. General ProBuilder (GEN)

- [GEN] Toda variable calculada debe usarse después. Si no, da "Syntax error: This variable is not used in the code". Para dejar código preparado, comenta también sus cálculos (y sus parámetros), no solo la línea de salida. — Origen: scanner-atr-trailing v1.0 · 18-oct-2026 · ✅ confirmada (ProScreener)

## 2. Indicador (IND)

_(vacío)_

## 3. ProBacktest / ProOrder (ORD)

- [ORD] `DEFPARAM CumulateOrders = False` obligatorio. — Origen: manual · ⚠️ por confirmar

## 4. ProScreener (SCR)

- [SCR] `DEFPARAM` da error de compilación. — Origen: manual · ⚠️ por confirmar
- [SCR] Historial máximo: 256 velas (1024 Premium) del timeframe elegido. — Origen: manual · ⚠️ por confirmar
- [SCR] Resultados visibles: 50 (100 Premium). — Origen: manual · ⚠️ por confirmar
- [SCR] Columnas: 3 o 6 según licencia. Solo con una única instrucción `SCREENER`. — Origen: test-columnas v1 · 18-oct-2026 · ✅ confirmada (licencia gratuita = 3)
- [SCR] Comentarios: el manual ProScreener v6.1.0 usa `//` en sus propios ejemplos. `REM` sigue siendo la opción segura. — Origen: manual v6.1.0 · ⚠️ por confirmar
- [SCR] `PERCENTFORMAT` multiplica por 100. Pasar la fracción (0,05), no el porcentaje (5). — Origen: manual v6.1.0, p. 9 · ⚠️ por confirmar
- [SCR] La columna de orden se elige en la interfaz entre las columnas del `SCREENER`. — Origen: manual v6.1.0, p. 8-9 · ⚠️ por confirmar

## 5. Multi-timeframe (MTF)

- [MTF] `TIMEFRAME(weekly, UPDATEONCLOSE)` calcula solo al cierre de la vela superior. Documentado en ProBuilder; el manual ProScreener no lo menciona. — Origen: manual ProBuilder v6.1.0, p. 42 · ⚠️ por confirmar en ProScreener

## 6. Plataforma y licencia

| Dato | Valor |
|---|---|
| Licencia | Gratuita (PRT desktop, sin suscripción) — v13.0 · build 29-sep-2026 |
| Columnas ProScreener | 3 ✅ (test 18-oct-2026). Posible paso a 6 con licencia profesional — pendiente |
| Resultados / historial | Se asume 50 resultados · 256 velas (no Premium) |
| ¿Exige la app abierta? | _por indicar_ |

## 7. Errores de compilación conocidos

| Mensaje de error | Causa | Solución | Script · fecha |
|---|---|---|---|
| `Syntax error: This variable is not used in the code: td9, distwall, rsid` | Variables calculadas solo para la línea `SCREENER` de 6 columnas, que estaba comentada | Comentar sus cálculos con `REM [6COL]` | scanner-atr-trailing v1.0 · 18-oct-2026 |

## 8. Pendiente de verificar

- _(dudas abiertas que aún no se han probado)_

---

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| v1 | 18-oct-2026 | Esqueleto inicial |
| v1.4 | 18-oct-2026 | Error confirmado: variable calculada y no usada |
| v1.3 | 18-oct-2026 | Confirmado: 3 columnas en licencia gratuita |
| v1.2 | 18-oct-2026 | Datos de licencia: gratuita, v13.0 |
| v1.1 | 18-oct-2026 | Reglas SCR/MTF del manual v6.1.0 (`//`, `PERCENTFORMAT`, orden, `UPDATEONCLOSE`) |
