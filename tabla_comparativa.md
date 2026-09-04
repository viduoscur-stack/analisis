# Experimento de 3 condiciones — Tabla comparativa por test

| test | accuracy false | accuracy true | accuracy omitido | lat false (ms) | lat true (ms) | lat omitido (ms) | tokens ocultos true | tokens ocultos omitido | veredicto |
|---|---|---|---|---|---|---|---|---|---|
| T101 | 100% | 100% | 100% | 20481 | 36994 | 39408 | 5 | 1654 | NO necesita (desperdicia tiempo) |
| T105 | 100% | 100% | 100% | 6111 | 16945 | 14175 | 5 | 715 | NO necesita (desperdicia tiempo) |


## Respuestas A-G (con evidencia de esta corrida)

**A. % de los 2 tests medibles que mejora con think=true vs think=false:** 0.0% (0/2)

**B. Tests que NECESITAN razonamiento** (accuracy sube ≥40 puntos porcentuales): ninguno con ese umbral

**C. Tests que NO necesitan razonamiento** (accuracy similar, pero más lento con think=true): T101, T105

**D. Costo promedio de latencia de think=true vs think=false** (todos los tests): 13674 ms adicionales en promedio

**E. Con think omitido**: 100.0% de las generaciones mostraron generación oculta significativa (>20 tokens de diferencia) sin exponerla en el campo 'thinking'

**F. Tests con el mismo patrón cualitativo que T004** (false falla, true/omitido aciertan): ver columna 'veredicto' de la tabla, categoría 'NECESITA razonamiento'

**G. Categorías identificadas**: 0 tests necesitan razonamiento, 2 no lo necesitan (pierden tiempo con think=true), 0 ambiguos o sin check automático (requieren revisión humana)