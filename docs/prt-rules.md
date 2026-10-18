<!-- prt-rules.md · v1.8 · 18-oct-2026 · La Granja -->

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

- [IND] En un indicador sobre gráfico diario con datos de fin de día, `TIMEFRAME(weekly)` deja de actualizar la vela semanal en curso en las últimas sesiones. VGT, SNOW y XOM mostraban el viernes 16-oct el muro calculado con el cierre de martes o miércoles. El screener, con el mismo código, sí ve la semana completa (SNOW = señal 4). — Origen: atr-trailing-vervoort v1.1 · 18-oct-2026 · ✅ observado · ⚠️ causa por confirmar

- [IND] `DRAWTEXT` con `ANCHOR`: el texto con `|` dio `Unauthorized character: "a variable name"` (también llevaba `:`, `(`, `)`, `+`, `=` y parámetros de fuente). Con solo letras, números, comas, puntos y guiones compila. El punto de anclaje es el centro del texto. — Origen: atr-trailing-vervoort v1.4/v1.5 · 18-oct-2026 · ✅ confirmada
- [IND] Dos `COLORBETWEEN` en ramas distintas de un `IF` dejan bandas planas: la zona que no se llama mantiene sus últimos valores. Usar una sola llamada por vela con el color en variables. — Origen: atr-trailing-vervoort v1.5 · 18-oct-2026 · ✅ observado
- [IND] Las variables del indicador (ventana Variables) salen en la leyenda entre paréntesis, y su descripción en la pantalla de configuración. — Origen: atr-trailing-vervoort v1.2 · 18-oct-2026 · ✅ confirmada

## 3. ProBacktest / ProOrder (ORD)

- [ORD] `DEFPARAM CumulateOrders = False` obligatorio. — Origen: manual · ⚠️ por confirmar

## 4. ProScreener (SCR)

- [SCR] `DEFPARAM` da error de compilación. — Origen: manual · ⚠️ por confirmar
- [SCR] Historial máximo: 256 velas (1024 Premium) del timeframe elegido. — Origen: manual · ⚠️ por confirmar
- [SCR] Resultados visibles: el manual dice 50 (100 Premium), pero la licencia gratuita v13 muestra "up to 100 displayed". Historial: 256 velas. — Origen: debug v2 · 18-oct-2026 · ✅ observado
- [SCR] Columnas: 3 o 6 según licencia. Solo con una única instrucción `SCREENER`. — Origen: test-columnas v1 · 18-oct-2026 · ✅ confirmada (licencia gratuita = 3)
- [SCR] Comentarios: el manual ProScreener v6.1.0 usa `//` en sus propios ejemplos. `REM` sigue siendo la opción segura. — Origen: manual v6.1.0 · ⚠️ por confirmar
- [SCR] `PERCENTFORMAT` multiplica por 100. Pasar la fracción (0,05), no el porcentaje (5). — Origen: manual v6.1.0, p. 9 · ⚠️ por confirmar
- [SCR] Con licencia gratuita, ProScreener parece devolver solo acciones de NYSE. No salen ETF (VGT, SCHD, VDC) ni acciones de Nasdaq, ni con `SCREENER[close > 0]`, aunque el gráfico carga y se pueden añadir a listas. — Origen: test-datos v1 · 18-oct-2026 · ✅ observado (no 100 % seguro) · ⚠️ causa por confirmar con ProRealTime
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
| `Unauthorized character: "a variable name"` (línea con `DRAWTEXT`) | Símbolos en el texto (`\|` probable) | Solo letras, números, comas, puntos y guiones | atr-trailing-vervoort v1.4 · 18-oct-2026 |
| `Syntax error: This variable is not used in the code: td9, distwall, rsid` | Variables calculadas solo para la línea `SCREENER` de 6 columnas, que estaba comentada | Comentar sus cálculos con `REM [6COL]` | scanner-atr-trailing v1.0 · 18-oct-2026 |

## 8. Pendiente de verificar

- ¿Qué mercados cubre ProScreener con licencia gratuita? Observado: NYSE sí; Nasdaq y ETF no. Revisar con la licencia completa.

---

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| v1 | 18-oct-2026 | Esqueleto inicial |
| v1.8 | 18-oct-2026 | DRAWTEXT con símbolos falla; COLORBETWEEN una vez por vela; variables en leyenda |
| v1.7 | 18-oct-2026 | Indicador: semanal en curso desfasado; ProScreener muestra hasta 100 resultados |
| v1.6 | 18-oct-2026 | ProScreener gratuito: NYSE sí, Nasdaq y ETF no (observado) |
| v1.5 | 18-oct-2026 | ETF NYSE Arca no aparecen en ProScreener (licencia gratuita) |
| v1.4 | 18-oct-2026 | Error confirmado: variable calculada y no usada |
| v1.3 | 18-oct-2026 | Confirmado: 3 columnas en licencia gratuita |
| v1.2 | 18-oct-2026 | Datos de licencia: gratuita, v13.0 |
| v1.1 | 18-oct-2026 | Reglas SCR/MTF del manual v6.1.0 (`//`, `PERCENTFORMAT`, orden, `UPDATEONCLOSE`) |
