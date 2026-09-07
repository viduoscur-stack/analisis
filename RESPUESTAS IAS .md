ESTA ES LA RESPUEsta del panel que dirias para la discusion y encender la pradera xD para mejorar la respuesta : 



🗨️ ChatGPT (pegado):
Sí. Y después de revisar el estado actual de OpenSKP, mi conclusión es bastante clara:

No abandonaría OpenSKP ahora. Pero tampoco construiría ORA SKP Viewer suponiendo que buildScene() es una fuente de verdad geométrica.

Lo convertiría en un pipeline tolerante a fallos, donde el parser es una etapa potencialmente imperfecta y ORA valida, aísla, puntúa y degrada la geometría antes de entregársela a Three.js.

Además, hay un dato importante que cambia ligeramente el diagnóstico: OpenSKP ya evolucionó bastante respecto a la situación que describes. La documentación actual declara soporte VFF y MFC, parsing streaming/low-memory, observabilidad, y reporta pruebas sobre un archivo de hasta 620 MB y más de 1.300 tests. Eso no elimina tus bugs, pero sí significa que merece la pena investigar si tus dos casos están relacionados con una zona concreta aún no cubierta por el corpus de pruebas.

Mi arquitectura recomendada para ORA SKP Viewer

Yo lo plantearía así:

                    ┌──────────────────────┐
                    │      archivo .SKP    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     OpenSKP           │
                    │ parser / scene build  │
                    └──────────┬───────────┘
                               │
                     puede contener errores
                               │
                               ▼
              ┌─────────────────────────────────┐
              │       ORA VALIDATION LAYER       │
              │                                 │
              │  • bounds                        │
              │  • escala                        │
              │  • NaN / Infinity                │
              │  • índices                       │
              │  • área de triángulos            │
              │  • normales                      │
              │  • degenerados                   │
              │  • outliers                      │
              │  • transforms                    │
              │  • duplicación / instancing      │
              └───────────────┬─────────────────┘
                              │
                  ┌───────────┴────────────┐
                  │                        │
             HEALTHY                    SUSPECT
                  │                        │
                  ▼                        ▼
          ┌───────────────┐       ┌────────────────┐
          │ Three.js      │       │ quarantine     │
          │ render        │       │ / diagnostic   │
          └───────────────┘       └────────────────┘

La clave es que OpenSKP no debe ser quien decida que algo es válido.

1. ¿Cómo detectar corrupción silenciosa?

Aquí creo que hay una distinción importantísima:

No intentes determinar si una geometría es "correcta".

Eso es imposible en el caso general.

Un parser no sabe si una cocina de 3.80 m debería medir 3.80 m o 380 m.

Lo que sí puede determinar es:

"Esta geometría es estadísticamente incompatible con el resto de la escena."

Y eso sí es muy potente.

2. Primera defensa: validación matemática absoluta

Antes de cualquier heurística, cada primitive debería pasar por validaciones duras.

Por ejemplo:

Positions

Rechazar inmediatamente:

NaN
Infinity
- Infinity

y valores absurdos.

Por ejemplo:

abs(x) > MAX_COORD
abs(y) > MAX_COORD
abs(z) > MAX_COORD

No usaría un MAX_COORD demasiado pequeño porque un modelo arquitectónico puede tener coordenadas grandes dependiendo del origen.

Pero sí establecería algo como:

MAX_COORD = 1e7

o una cifra equivalente según las unidades internas que estés usando.

3. Validación de índices

Para cada triángulo:

i0
i1
i2

debe cumplirse:

0 <= i < vertexCount

Si aparece:

vertex 4812

pero solo existen:

4812 vertices

entonces el último índice válido es:

4811

Eso es corrupción inequívoca.

4. Triángulos degenerados

Calcula:

cross(B-A, C-A)

y su magnitud.

Si:

area ≈ 0

es un triángulo degenerado.

Pero no lo trataría automáticamente como corrupción.

SketchUp puede producir geometría degenerada por distintas razones.

Lo que interesa es:

degenerateRatio =
degenerateTriangles / totalTriangles

Por ejemplo:

0.02%   → OK
1%      → warning
20%     → sospechoso
80%     → probablemente roto

Los umbrales deben calibrarse con modelos reales.

5. El detector que probablemente te habría encontrado tu bisagra corrupta

Aquí está una de las partes más importantes.

No compares únicamente:

primitive A
primitive B
primitive C
primitive D

por cantidad de vértices.

Construye para cada primitive un descriptor:

PrimitiveHealth {

    vertexCount
    triangleCount

    minX
    maxX
    minY
    maxY
    minZ
    maxZ

    sizeX
    sizeY
    sizeZ

    diagonal

    center

    surfaceArea

    volumeApprox

    centroid

    materialCount

    degenerateRatio

    invalidIndexCount

    normalErrorRatio
}

Entonces puedes detectar:

Component 1
size = 0.18 m

Component 2
size = 0.19 m

Component 3
size = 0.17 m

Component 4
size = 9.82 m   ← 🚨

Eso no demuestra matemáticamente que Component 4 esté mal.

Pero sí genera:

ANOMALY SCORE = 0.97
6. Pero cuidado: no hagas "outlier detection" global ingenuo

Esto es muy importante para arquitectura.

Imagina una casa:

puerta        0.90 m
silla         0.50 m
cocina        3.20 m
muro          8.00 m
terreno      25.00 m

Si utilizas:

"el objeto más grande es corrupto"

vas a romper modelos perfectamente válidos.

Por eso usaría varios niveles de comparación.

Nivel 1 — dentro de una definición

Si tienes:

4 instancias de la misma bisagra

y:

3 ≈ 0.18 m
1 ≈ 9 m

la anomalía es extremadamente fuerte.

Porque son la misma definición.

Este es probablemente tu detector más poderoso.

7. Instancias repetidas = tu mejor sistema de validación

SketchUp tiene precisamente una estructura de componentes/instancias.

OpenSKP expone esa jerarquía.

Supongamos:

Definition:
    KitchenHandle

Instances:
    #1
    #2
    #3
    #4

Si las cuatro deberían compartir geometría:

G
G
G
G

pero después de buildScene() obtienes:

G
G
G
G × 50

tienes una señal brutalmente fuerte.

Porque puedes comparar la geometría antes de aplicar transforms.

Esto es mucho mejor que analizar solamente el bounding box mundial.

8. Separaría "Definition Space" de "World Space"

Esta decisión arquitectónica te va a ahorrar muchos problemas.

Nunca trabajaría únicamente con:

world-space vertices

Mantendría:

DefinitionGeometry
        +
InstanceTransform
        =
WorldGeometry

Así:

Chair
 ├── definition geometry
 │
 ├── instance #1 → transform A
 ├── instance #2 → transform B
 └── instance #3 → transform C

Si la definición mide:

0.80 × 0.80 × 1.00

y una instancia termina midiendo:

40 × 40 × 50

puedes determinar si:

el transform es realmente enorme;
la definición está corrupta;
hubo un problema al aplicar el transform.

Es muchísimo más diagnosticable.

9. Segundo nivel de validación: transformaciones

Una corrupción de escala puede venir no de los vértices sino de una matriz.

Para cada transform:

M =
[ ... ]

extraería:

scaleX
scaleY
scaleZ
determinant
rotation
translation

Y comprobaría:

finite(M)

y:

scaleX > 0
scaleY > 0
scaleZ > 0

Además:

scaleX ≈ scaleY ≈ scaleZ

no siempre debe ser cierto, porque SketchUp permite transformaciones no uniformes.

Pero una diferencia absurda sí merece una bandera.

10. Normales: útiles, pero NO como detector principal

Tu pregunta menciona:

manifold/normales

Sí, pero yo no pondría el foco ahí.

Para un viewer arquitectónico:

non-manifold

no significa necesariamente:

corrupto

Puedes tener:

geometría abierta;
caras coplanares;
componentes superpuestos;
hojas;
telas;
planos;
geometría auxiliar;
objetos importados;
elementos 2D.

Todo perfectamente válido para SketchUp.

Las normales sirven mejor para detectar:

NaN
Infinity
longitud ≈ 0
normal incompatible con triángulo

pero no para decir:

"esta pieza está mal".

11. Yo crearía un "Geometry Health Score"

Esto sería muy ORA.

Por primitive:

GeometryHealth {

    structural: 0..1
    numerical: 0..1
    topological: 0..1
    statistical: 0..1
    instanceConsistency: 0..1

    confidence: 0..1
}

Ejemplo:

KitchenHandle #1

numerical            1.00
structural           1.00
topological           .99
statistical           .98
instanceConsistency  1.00

HEALTH = 0.994

Mientras:

KitchenHandle #4

numerical            1.00
structural           1.00
topological           .97
statistical           .02
instanceConsistency   .03

HEALTH = .40

No lo eliminas.

Lo marcas:

SUSPECT
12. Y aquí viene una decisión de diseño muy importante
Nunca ocultes automáticamente una geometría sospechosa.

Porque podrías ocultar justamente una pieza legítima.

En lugar de:

corrupt → delete

haz:

corrupt/suspect
      ↓
quarantine
      ↓
renderable = false
      +
diagnostic metadata

Y el usuario puede hacer:

Mostrar geometría sospechosa
13. ¿Qué hacer con la cámara?

Este es un problema que tú ya encontraste.

Tu cámara hace:

sceneBoundingBox
        ↓
fitCamera()

y una pieza corrupta de 50× hace:

sceneBoundingBox × 50

Resultado:

modelo real → microscópico

Yo separaría:

renderBounds
diagnosticBounds
renderBounds

Solo:

HEALTH >= threshold
diagnosticBounds

Incluye:

TODO

Entonces:

fit camera
     ↓
renderBounds

pero:

diagnostics
     ↓
diagnosticBounds

Así puedes mostrar:

⚠️ 1 geometría sospechosa fuera del encuadre principal.

14. Incluso iría un paso más allá

Si tienes:

healthy bounds
suspect bounds

puedes dibujar el sospechoso con:

wireframe

y una etiqueta:

⚠ GEOMETRY ANOMALY
Component #4

Eso convertiría ORA SKP Viewer en algo más que un visor.

Sería también:

un detector de problemas de importación SKP.

Y eso es bastante valioso.

15. ¿Qué hacer cuando OpenSKP lanza una excepción?

Aquí hay dos casos completamente diferentes.

Caso A
parser throws
Caso B
parser succeeds
but geometry is wrong

El caso B es mucho más peligroso.

Por eso tu arquitectura debe considerar:

Exception ≠ corruption detected
Success ≠ geometry valid

Esta frase debería prácticamente convertirse en principio de diseño de ORA.

16. Aislar por componente

Aquí hay una limitación importante.

Si llamas:

SkpFile.fromBuffer(buffer).buildScene()

y el parser falla en medio del proceso, quizá no puedas recuperar limpiamente las primitivas posteriores.

No intentes solucionar esto exclusivamente desde Three.js.

La solución correcta es hacer que la frontera de aislamiento esté lo más cerca posible del parser.

Idealmente:

SKP
 │
 ├── definition A → parse → OK
 ├── definition B → parse → OK
 ├── definition C → parse → ERROR
 ├── definition D → parse → OK
 └── definition E → parse → OK

Eso requiere soporte del parser.

Y aquí yo abriría un issue/PR en OpenSKP con tus archivos mínimos reproducibles.

17. Tu bug F901 es especialmente interesante

Tu error:

record=17/26
tag=F901

es mucho más útil que simplemente:

Array buffer allocation failed

porque ya tienes:

record
tag
stage

Eso demuestra que la capa de observabilidad del parser está ayudando. OpenSKP precisamente documenta errores estructurados con ubicación/progreso.

Yo no parchearía todavía EdgeFlagStore basándome solamente en el síntoma.

Primero haría:

archivo bueno
archivo malo
       ↓
extraer model.dat
       ↓
TLV diff
       ↓
F901
       ↓
payload
       ↓
campos que alimentan EdgeFlagStore

Y buscaría:

¿el ID realmente está corrupto?

o:

¿EdgeFlagStore interpreta correctamente un ID válido?

Son dos problemas completamente diferentes.

18. Hay una prueba extremadamente importante que yo haría

Tienes:

Archivo A
bisagra simple
Archivo B
bisagra detallada
Archivo C
adorno curvo

Haz una matriz:

Característica	A	B	C
curvas	?	?	✓
smooth edges	?	?	✓
múltiples materiales		✓	
componentes	✓	✓	
texturas		✓	
edge flags		?	?
F901			✓

Entonces busca la característica común que aparece justo antes del fallo.

No asumiría todavía:

"curvas = problema".

Podría ser:

curvas + smooth

o:

curvas + edge flags

o:

curvas + determinados records
19. Tu bug silencioso puede convertirse en un regression test excelente

Ese archivo de 192 KB es oro.

No lo descartes.

Debe convertirse en:

tests/regression/

hinge_192kb.skp
ornament_4mb.skp

y el test debería verificar cosas como:

definition count
instance count
vertex ranges
triangle ranges
bounding boxes
material count

Por ejemplo:

Expected:

definition #3:
bbox ≈ 0.12 × 0.03 × 0.04

No necesariamente tienes que comparar todos los vértices bit por bit.

Puedes comparar invariantes geométricas.

20. Incluso puedes generar un "golden fingerprint"

Por componente:

vertexCount
triangleCount
bbox
surfaceArea
centroid
material IDs

→ hash.

Algo conceptual como:

SHA256(
  vertexCount +
  triangleCount +
  bbox +
  area +
  centroid +
  materials
)

Entonces una nueva versión de OpenSKP:

v0.3.0

se prueba contra:

v0.3.1

y ORA puede detectar:

REGRESSION
Component X changed unexpectedly

Esto es exactamente el tipo de protección que necesitas si dependes de un parser reverse-engineered.

21. Para modelos arquitectónicos grandes: no empezaría por LOD

Aquí discrepo ligeramente con la intuición habitual.

Para ORA SKP Viewer, el orden sería:

1. Correctness
parse
validate
isolate
2. Memory
workers
transferables
disposal
3. Rendering
GPU buffers
instancing
frustum culling
4. LOD

solo cuando realmente haga falta.

22. Web Worker: sí, absolutamente

No pondría:

SKP parsing
+
buildScene
+
geometry conversion

en el hilo principal.

Arquitectura:

MAIN THREAD
│
├── UI
├── Three.js
├── OrbitControls
└── camera
       │
       │ postMessage
       ▼
WORKER
│
├── OpenSKP
├── parse
├── validation
├── scene preparation
└── transferable buffers
       │
       ▼
MAIN THREAD

El navegador no debería congelarse mientras OpenSKP procesa una casa.

23. Y usaría Transferable ArrayBuffers

No hagas:

worker → huge JS object → main thread

porque puedes acabar copiando cantidades enormes de memoria.

Prefiero:

Float32Array positions
Float32Array normals
Float32Array uvs
Uint32Array indices

y transferir los ArrayBuffer.

Conceptualmente:

postMessage(data, [
    positions.buffer,
    normals.buffer,
    uvs.buffer,
    indices.buffer
]);

La geometría pasa de:

Worker

a:

GPU preparation

sin copias innecesarias.

24. No crees un Three.js Mesh por cada pequeña primitiva

Este es otro posible cuello de botella.

Un modelo arquitectónico puede tener:

50,000 primitives

aunque tenga una cantidad razonable de polígonos.

Tener:

50,000 THREE.Mesh

es mucho peor que tener:

menos objetos
+
buffers grandes

Agrupa por:

material
+
visibility
+
render characteristics

cuando sea posible.

25. Instancing: sí, pero solamente para geometría realmente repetida

SketchUp es particularmente interesante porque tiene:

Component Definition
        ↓
Instance

Entonces:

500 sillas

pueden ser:

1 geometry
+
500 transforms

y no:

500 geometries

Ahí THREE.InstancedMesh tiene muchísimo sentido.

Pero no convertiría indiscriminadamente todo a InstancedMesh.

Úsalo cuando:

same geometry
different transform
26. La memoria es probablemente tu verdadero enemigo

Una cosa importante:

SKP size ≠ GPU geometry size

Un:

200 MB .skp

puede terminar ocupando mucho más después de:

decompression
+
parser structures
+
scene
+
positions
+
normals
+
UV
+
indices
+
Three.js buffers
+
textures

Puedes terminar fácilmente multiplicando el tamaño.

Por eso necesitas medir:

SKP bytes
↓
ZIP/model.dat
↓
parsed representation
↓
scene
↓
GPU buffers
↓
textures

y mostrarlo incluso internamente como:

Memory profiler

SKP              186 MB
Parser            420 MB
Scene             610 MB
Geometry          280 MB
Textures          190 MB
GPU estimate      350 MB
27. No confiaría en "archivo máximo X MB"

No existe un límite útil del tipo:

"Chrome aguanta 500 MB."

Depende de:

RAM del equipo;
navegador;
arquitectura;
GPU;
cantidad de objetos;
texturas;
buffers;
tamaño de JavaScript heap;
WebGL;
fragmentación.

Por eso ORA debería calcular un:

complexity profile

antes de intentar renderizar.

Por ejemplo:

Vertices:       8.2 M
Triangles:      4.6 M
Primitives:     12,480
Instances:      2,130
Textures:       840 MB

y decidir:

NORMAL
HEAVY
EXTREME
28. Para "EXTREME", carga progresiva

Yo sí implementaría:

Parse
 ↓
metadata
 ↓
definitions
 ↓
priority geometry
 ↓
visible geometry
 ↓
remaining geometry

Pero hay una dificultad:

OpenSKP actualmente documenta streaming/low-memory parsing, pero eso no significa automáticamente que su buildScene() sea un renderer progresivo listo para tu UX.

Probablemente tendrás que construir tú la capa de scheduling.

29. Priorización espacial

En vez de:

load everything

puedes cargar:

camera
  ↓
frustum
  ↓
nearby geometry
  ↓
important geometry

Pero para un modelo SKP local, hay una complicación:

primero necesitas saber dónde está la geometría.

Por eso una estrategia razonable sería:

Fase 1
parse metadata
Fase 2
definition bounding boxes
Fase 3
instance transforms
Fase 4
spatial index
Fase 5
load/render geometry
30. ¿LOD?

Sí, pero no intentaría generar LOD durante el primer parse.

Podrías tener:

LOD 0 = bounding box / proxy
LOD 1 = simplified
LOD 2 = full geometry

Pero para ORA 1.0 yo priorizaría:

culling
+
instancing
+
frustum
+
memory management

antes que un sistema sofisticado de LOD.

31. ¿Migrar a otro parser?
Mi respuesta: todavía NO.

Porque tienes una situación muy particular.

OpenSKP tiene:

MIT;
TypeScript/JS;
navegador;
sin SketchUp;
sin SDK;
VFF;
legacy;
componentes;
materiales;
texturas;
scene baking;
observabilidad;
tests;
múltiples implementaciones.

Encontrar otro parser que te dé todo eso no es trivial.

32. Pero tampoco apostaría toda ORA a OpenSKP

Aquí está mi posición exacta:

OpenSKP = backend primario

pero:

ORA = capa de resiliencia independiente.

Así:

ORA SKP Viewer
        │
        ▼
┌────────────────────┐
│ SKP Adapter         │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ OpenSKP             │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ ORA Geometry        │
│ Validation          │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ ORA Scene Model     │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Three.js            │
└────────────────────┘

Así puedes cambiar mañana:

OpenSKP

por:

Parser B

sin reescribir:

camera
UI
selection
tree
materials
diagnostics
performance
33. ¿Y el SDK oficial de Trimble?

Aquí hay que separar dos cosas.

Trimble sí ofrece un SketchUp Desktop SDK para leer y escribir archivos SKP desde aplicaciones propias.

Pero eso no significa que sea la solución perfecta para tu requisito:

"un solo HTML, navegador, sin SketchUp instalado."

El SDK oficial te lleva hacia:

native application

y no hacia:

100% browser / standalone HTML

Por tanto, para tu producto actual, no lo veo como reemplazo directo.

34. Donde sí veo muchísimo valor al SDK oficial

Como oracle de validación.

Esto es muy diferente.

Podrías tener un entorno de desarrollo:

                 mismo SKP
                    │
          ┌─────────┴─────────┐
          │                   │
      OpenSKP             Trimble SDK
          │                   │
          ▼                   ▼
       Geometry           Geometry
          │                   │
          └─────────┬─────────┘
                    ▼
               Comparator

Entonces puedes descubrir:

OpenSKP bbox ≠ SDK bbox
OpenSKP face count ≠ SDK face count
OpenSKP instance transform ≠ SDK

Eso sería oro para desarrollar el parser.

No necesitas distribuir el SDK con ORA.

Lo usas como referencia de laboratorio.

35. Y aquí aparece una estrategia todavía mejor

Construiría un corpus propio:

ORA-SKP-Corpus/

con:

01_simple/
02_components/
03_curves/
04_smooth_edges/
05_textures/
06_non_uniform_scale/
07_nested_components/
08_dynamic_components/
09_large_architecture/
10_imported_geometry/
11_legacy/
12_corrupted_or_edge_cases/

Y cada archivo tendría:

model.skp
expected.json

con invariantes.

36. Tu objetivo no debería ser "OpenSKP no tenga bugs"

Eso es imposible.

Tu objetivo debería ser:

"ORA no puede ser destruido por un bug de OpenSKP."

Esa es una diferencia arquitectónica enorme.

37. ¿Cuándo sí abandonaría OpenSKP?

Yo definiría criterios objetivos.

🔴 Migraría si ocurre alguno de estos:

1. Corrupción silenciosa recurrente

Por ejemplo:

> 1% de archivos reales

produce geometría incorrecta.

2. Bugs que afectan estructuras fundamentales

Por ejemplo:

component hierarchy
transforms
faces
curves
materials

de forma generalizada.

3. No existe forma razonable de aislar errores

Si un único componente corrupto obliga a perder:

todo el modelo

y la arquitectura del parser no permite recuperación.

4. Cada nueva familia de SKP genera regresiones

Ejemplo:

fix curves
→ rompe components

fix components
→ rompe materials

fix materials
→ rompe legacy

Eso indica deuda arquitectónica seria.

5. No puedes construir un corpus reproducible

Si los bugs dependen de:

"este archivo raro"

pero no pueden convertirse en tests automatizados.

38. ¿Cuándo seguiría apostando fuerte por OpenSKP?

Si ocurre esto:

Bug encontrado
↓
mínimo reproducible
↓
causa localizada
↓
fix
↓
regression test
↓
no regresión

Eso es exactamente lo que quieres de una dependencia joven.

Los bugs no son necesariamente la señal mala.

La señal mala sería:

bugs imposibles de reproducir, imposibles de aislar y que vuelven a aparecer.

39. Hay otra señal que yo vigilaría especialmente

OpenSKP tiene actualmente cinco implementaciones independientes del formato y documentación que indica que se comparan sobre los mismos archivos.

Eso abre una posibilidad muy interesante para ti.

Si tienes:

TypeScript
Python
C++
.NET
Dart

puedes probar un archivo problemático en más de una implementación.

Si:

TS → corrupto
Python → correcto
C++ → correcto

tienes una pista potentísima:

probablemente es un bug específico del port TypeScript.

Si:

TS → corrupto
Python → corrupto
C++ → corrupto

entonces probablemente:

la especificación reverse-engineered

tiene un gap.

Esto es muchísimo más informativo que simplemente probar otra versión de Three.js.

40. Para tu caso F901 yo haría exactamente esto

Mi investigación sería:

ornament_4mb.skp
        │
        ├── TS
        ├── Python
        ├── C++
        ├── .NET
        └── Dart

y registrar:

parse OK?
F901?
vertex count?
edge count?
bbox?
scene build?

Luego:

hinge_192kb.skp

igual.

Si los resultados difieren entre ports:

no es un problema de tu visor.

Eso te ahorra muchísimo tiempo.

41. Mi arquitectura final para ORA SKP Viewer

Yo la dejaría así:

                    .SKP
                      │
                      ▼
              ┌───────────────┐
              │ File Analyzer  │
              └───────┬───────┘
                      │
                      ▼
               Web Worker
                      │
                      ▼
              ┌───────────────┐
              │   OpenSKP     │
              └───────┬───────┘
                      │
             ┌────────┴────────┐
             │                 │
          SUCCESS             ERROR
             │                 │
             ▼                 ▼
       Geometry data       isolate/error
             │
             ▼
      ┌────────────────┐
      │ ORA Validator  │
      └───────┬────────┘
              │
       ┌──────┴──────┐
       │             │
    HEALTHY       SUSPECT
       │             │
       ▼             ▼
    render        quarantine
       │             │
       └──────┬──────┘
              ▼
        Scene Manager
              │
      ┌───────┼────────┐
      │       │        │
   culling instancing LOD
      │       │        │
      └───────┼────────┘
              ▼
           Three.js
              │
              ▼
       OrbitControls
42. Y añadiría un "ORA Diagnostic Mode"

Esto me parece especialmente interesante para tu proyecto.

Un botón:

🧪 Diagnóstico

que muestre:

FILE
SKP 2025
Size: 192 KB

PARSER
OpenSKP 0.3.x
Parse: 31 ms
Scene: 18 ms

GEOMETRY
Vertices: 4,812
Triangles: 2,744
Primitives: 4

HEALTH
█████████░ 94%

WARNINGS
⚠ Component #4 bbox anomaly
⚠ 0.03% degenerate triangles

CAMERA
Render bounds: 0.82 m
Diagnostic bounds: 41.7 m

Y:

[Mostrar sospechosos]
[Recalcular cámara sin sospechosos]
[Exportar diagnóstico]

Eso te permitiría desarrollar ORA contra los propios problemas de OpenSKP, en vez de sufrirlos.

Mi veredicto para tus 5 preguntas
Pregunta	Mi decisión
1. Corrupción silenciosa	Validación matemática + invariantes + outliers + consistencia de instancias
2. Un componente no debe matar todo	Aislamiento por definición/instancia + quarantine + bounds separados
3. Archivos grandes	Worker + TransferableArrayBuffer + instancing + culling + memory budget; LOD después
4. Abandonar OpenSKP	No todavía. Mantenerlo detrás de un adapter
5. Parsers reverse-engineered	Tratar parser como fuente no confiable + corpus + golden fingerprints + regression tests
Y mi recomendación más importante

No invertiría ahora semanas en intentar "arreglar OpenSKP completo".

Haría primero estas 4 piezas de ORA:

1. ORA Geometry Validator
2. ORA Component Isolation
3. ORA Diagnostic/Health System
4. ORA Memory/Worker Pipeline

Después atacaría F901.

Porque si mañana encuentras:

F901

y lo arreglas, pero pasado mañana aparece:

F734

en otro modelo arquitectónico, ya tendrás una arquitectura que no se cae.

Y eso es exactamente lo que necesitas si ORA va a pasar de "visor que funciona con bisagras" a visor capaz de abrir modelos arquitectónicos reales de cientos de MB y millones de triángulos.

OpenSKP, por cierto, actualmente documenta explícitamente una arquitectura de parse() separada de buildScene() precisamente por razones de memoria, y declara streaming/low-memory parsing; yo aprovecharía esa separación en ORA en vez de tratar buildScene() como una caja negra única.

Si quieres llevar esto a implementación, el siguiente paso que haría es diseñar el ORA Geometry Validation Layer completo —con las métricas exactas, fórmulas de anomaly score, thresholds, estructura JSON de diagnóstico y estrategia para que Three.js nunca encuadre un outlier corrupto— antes de tocar más el parser.

---

🗨️ Claude (pegado):
Buena pregunta, y el enfoque de "necesito una estrategia general, no parches por archivo" es el correcto dado el estado de la librería. Voy por partes.

1. Detectar corrupción silenciosa sin conocer la forma "correcta"

No hay bala de plata, pero hay una batería de heurísticas baratas que juntas dan buena cobertura, exactamente el patrón que ya viste en tu Bug 2 (una pieza ~50x más grande que las otras):

Outliers de bounding box entre primitivas del mismo modelo/componente. Calcula el bbox de cada primitiva/componente y compara volumen, diagonal y centroide contra la mediana (no el promedio — un outlier extremo distorsiona el promedio) de todas las primitivas hermanas. Si una está a >3-5 desviaciones típicas (o simplemente >10x el tamaño mediano), márcala como sospechosa. Esto es exactamente lo que te habría atrapado en Bug 2 automáticamente.
Densidad de vértices por unidad de volumen. Una geometría "sana" tiene una relación razonablemente estable entre número de triángulos y volumen del bbox (para el tipo de objeto). Un salto brusco de 50x en volumen con el mismo conteo de triángulos que sus hermanos es una señal fortísima de escala/desplazamiento corrupto, independiente del bbox absoluto.
Chequeo de manifold / normales consistentes. Cuenta edges no compartidos (edges que pertenecen a un solo triángulo en vez de dos) — un modelo bien formado de superficies cerradas debería tener muy pocos o ninguno. Un salto en ese conteo entre componentes "similares" es señal de parseo roto, no solo de geometría abierta legítima (que también existe en arquitectura, ojo).
Rango de coordenadas fuera de la envolvente del resto del archivo. Si el 95% de los vértices de la escena caen dentro de un rango razonable y un componente tiene vértices en coordenadas absurdas (orden de magnitud distinto), es la señal más barata y más confiable de todas — literalmente lo que te está pasando.
Determinismo por reparseo. Si tienes margen, parsear el mismo archivo dos veces y comparar hash de posiciones/índices te detecta corrupción no determinística (útil si sospechas de un bug de estado compartido tipo el EdgeFlagStore).

En la práctica: calculas 2-3 de estas métricas por primitiva, las comparas contra la distribución del resto del modelo (mediana + MAD, no media + desviación estándar, porque es más robusto a outliers), y cualquier primitiva que se salga del rango esperado se marca como "sospechosa" para el punto 2.

2. Aislar fallos por componente sin arruinar todo el render

Este es el punto de mayor apalancamiento porque te protege de bugs que ni siquiera conoces todavía:

Parsear y triangular por componente/entidad de forma aislada, con try/catch alrededor de cada uno. Si un componente revienta (como tu Bug 1), captura el error, loguéalo con su id, y sigue con el resto — nunca dejes que una excepción en una entidad tire todo el parseo del archivo.
Separar "cálculo de cámara" de "qué se renderiza". Excluye del bounding box de encuadre cualquier primitiva marcada como sospechosa por las heurísticas del punto 1, pero sigue renderizándola (quizás con un material distintivo tipo rojo semitransparente o wireframe) para que el usuario vea "aquí hay algo raro" en vez de que desaparezca silenciosamente. Esto es clave: nunca ocultes el problema, hazlo visible pero no dejes que rompa la vista general.
Presupuesto de bbox robusto: en vez de min/max crudo de todos los vértices, usa percentiles (ej. percentil 1-99) para el encuadre de cámara por defecto, y muestra un botón "encuadre completo" aparte que sí use el bbox real. Esto amortigua automáticamente el efecto de un outlier corrupto sin necesidad de que la heurística sea perfecta.
Un log/panel de diagnóstico visible en el visor (no solo consola) que liste: componentes cargados, componentes fallados con su tag/id, componentes marcados como sospechosos. Para tu caso de uso (biblioteca personal de modelos reales, no solo demos) esto es casi tan importante como el render mismo — te permite confiar en lo que ves.
3. Rendimiento para modelos arquitectónicos completos

Con órdenes de magnitud más polígonos (casas/cocinas/interiores completos), en un solo HTML sin backend:

Web Worker para el parseo, siempre. SkpFile.fromBuffer sobre un archivo grande va a bloquear el hilo principal el tiempo suficiente para que el navegador se sienta colgado. Estructura el worker para que emita progreso por componente/entidad (mensaje postMessage por cada N% o cada componente terminado), así puedes mostrar una barra de carga real y no un spinner ciego.
Streaming/carga progresiva por componente, no por el archivo completo. Si OpenSKP te da acceso a la estructura antes de triangular todo, parsea y sube a GPU componente por componente, renderizando incrementalmente. El usuario ve el modelo "aparecer" en vez de esperar el 100%.
Instancing en Three.js para geometría repetida — típico en arquitectura: mismo mueble, misma silla, mismo módulo de cocina repetido N veces. InstancedMesh te ahorra un multiplicador enorme de memoria GPU si detectas geometría idéntica (hash de vertex buffer) reutilizada en distintas transformaciones.
LOD real es más difícil sin acceso a los datos fuente de SketchUp (los LOD de SketchUp no existen como tal, es geometría plana triangulada), así que lo más realista es simplificación post-hoc (decimación de mallas, ej. algoritmo de Quadric Error Metrics) aplicada bajo demanda para componentes lejanos de la cámara o para una vista "preview rápido" antes de cargar el detalle completo.
Límites de memoria en navegador: en la práctica, WebGL/Three.js empieza a sufrir con >5-10M triángulos activos en escena dependiendo del hardware, y el propio ArrayBuffer de JS tiene límites duros (~2GB en la mayoría de navegadores para un solo buffer). Para modelos arquitectónicos reales grandes, vas a necesitar descartar/mergear geometría redundante y comprimir posiciones (ej. cuantización a Uint16 en vez de Float32 cuando la precisión lo permita) antes de subir a GPU.
Frustum culling + occlusion culling básico de Three.js ayuda mucho en interiores (cuartos no visibles no se renderizan), pero solo si tu escena está organizada jerárquicamente por espacio/habitación y no como una sopa plana de triángulos.
4. ¿Seguir parchando OpenSKP, migrar, o híbrido?

Dado que en dos archivos mínimos ya aparecieron un fallo duro y una corrupción silenciosa, la señal es clara: la robustez estructural (no solo la cobertura de casos) todavía es inmadura. Esto no descalifica la librería — es normal en un parser de 2.5 meses para un formato binario propietario sin especificación oficial — pero sí cambia tu estrategia de "confiar y usar" a "usar y verificar activamente", que es justo lo que ya estás haciendo con tus heurísticas de detección.

Señales concretas que yo usaría para decidir si seguir, migrar o ir híbrido:

¿Los bugs están en el "camino feliz" o en casos extremos? Curvas orgánicas y componentes anidados con materiales/texturas son el caso común en modelos arquitectónicos reales (muebles curvos, detalles decorativos), no casos raros. Si tus próximos 5-10 archivos reales siguen produciendo bugs nuevos a este ritmo, es señal de que el parser todavía no cubre el espacio de formatos que tú necesitas.
Velocidad de respuesta del mantenedor. Repórtalos como issues bien documentados (ya tienes el detalle técnico, ej. el análisis del EdgeFlagStore) y mide: ¿responde en días? ¿acepta PRs? Un solo mantenedor activo y receptivo puede ser mejor que una librería más vieja pero abandonada — pero si no hay respuesta en unas semanas, es una señal de riesgo real para un proyecto donde dependes de corrección de datos, no solo de features.
Enfoque híbrido pragmático (el que yo recomendaría empezar): sigue usando OpenSKP como parser base (te ahorra meses de ingeniería inversa), pero trata su output como no confiable por default — corre las heurísticas de validación (punto 1) sobre cada escena parseada antes de renderizar, y para archivos que fallan/corrompen, considera hacer fallback a exportar/pre-procesar desde SketchUp mismo (si el usuario lo tiene) usando el SDK oficial de Trimble como ruta de verificación cruzada offline, no como dependencia runtime — así mantienes tu requisito de "no necesita SketchUp instalado" para el caso común, pero tienes una forma de generar "ground truth" para debuggear y eventualmente contribuir fixes upstream a OpenSKP.
El SDK oficial de Trimble corriendo local sería la opción más robusta en fidelidad, pero rompe tu requisito duro de "no SketchUp/SDK propietario instalado" y probablemente no corre en un solo archivo HTML cliente — solo tendría sentido como herramienta de desarrollo/verificación tuya, no como parte del producto final.
Migrar a otro parser de terceros hoy probablemente no resuelve nada — cualquier parser de ingeniería inversa de un formato binario propietario sin spec pública va a tener su propio set de bugs de fidelidad. El problema no es "OpenSKP específicamente", es la naturaleza del problema (punto 5).
5. Patrones para visores resilientes contra parsers de ingeniería inversa

Esto es realmente el principio unificador de todo lo anterior — trátalo como defensive rendering, análogo a defensive programming:

Nunca confíes en que "parseó sin excepción" = "parseó correcto". Como ya viste, son dos fallos completamente distintos y necesitas defensas para ambos por separado.
Aislamiento por unidad mínima (componente/entidad), nunca "todo o nada" a nivel archivo.
Degradación visible, no degradación silenciosa. Cuando algo es dudoso, muéstralo marcado, no lo ocultes ni lo dejes romper el resto.
Métricas de "salud" del parseo expuestas al usuario, no solo logueadas: % de componentes cargados limpio, cuántos marcados sospechosos, cuántos fallidos. Para un visor que vas a usar con modelos reales de forma recurrente, esto construye confianza calibrada en vez de confianza ciega.
Suite de regresión con archivos reales variados, no solo los de prueba mínimos. Cada archivo real que uses se convierte en caso de test — guarda snapshots de las métricas (vértices, triángulos, bbox por componente) de parseos que sabes que salieron bien, y compara contra eso en cada actualización de OpenSKP o de tu propio código.
Versiona el parser como dependencia de alto riesgo. Pinea la versión exacta de OpenSKP que usas, no sigas latest automáticamente — un parser tan joven puede introducir regresiones tan fácilmente como fixes.

En resumen: tu instinto de pedir "estrategia general" es el correcto, y la buena noticia es que las tres defensas (heurísticas de outlier, aislamiento por componente, exposición visible de dudas) son relativamente baratas de implementar comparadas con reescribir un parser de SKP desde cero — y te van a servir sin importar qué decidas en el punto 4.

---

🗨️ DeepSeek (pegado):
Abordemos tus preguntas de una manera estructurada y práctica. Has descrito con precisión los desafíos de trabajar con un formato propietario reconstruido por ingeniería inversa. La clave no es solo parchear, sino construir un sistema robusto por diseño que asuma que el parser puede fallar.

1. Detección de Corrupción Silenciosa
Es el desafío más complejo porque no hay un "dato correcto" con qué comparar. La estrategia debe ser heurística y por capas, sin depender de un único método mágico.

Outliers por Bounding Box (La primera línea de defensa): Como ya intuyes, es muy efectiva. Calcula el bounding box de cada primitiva o componente de forma aislada. Si el volumen de uno es, por ejemplo, > 3 desviaciones estándar del promedio de todos los volúmenes, es un fuerte candidato a estar corrupto. También puedes fijarte en la relación de aspecto del bounding box (ej., un componente 50 veces más largo que ancho podría ser un error).

Análisis de la Relación Vértices/Triángulos: Una primitiva con un número desproporcionado de vértices para sus triángulos (o viceversa) es sospechosa. Por ejemplo, una geometría enorme con solo 3 triángulos es un claro indicio de que los datos de posición están corruptos.

Validación de la Malla (Normales y Manifold): Es una técnica más pesada, pero muy robusta. Puedes comprobar si la mayoría de las normales de una malla apuntan en direcciones coherentes. Si una primitiva tiene normales con una varianza extremadamente alta, probablemente su geometría esté mal. También puedes verificar si la malla es "manifold" (cada arista es compartida por exactamente dos caras). La mayoría de los modelos 3D válidos lo son, y una desviación grande puede ser síntoma de corrupción.

En la práctica: Implementa estas heurísticas como una capa de validación post-parseo. Si una primitiva falla una o más de estas pruebas, márcala como "sospechosa" en lugar de descartarla de inmediato, para no perder datos que podrían ser válidos pero atípicos.

2. Aislamiento de Errores y "Fail-Soft"
Este es un principio de diseño fundamental. El objetivo es que un componente corrupto no pueda arruinar la experiencia del usuario con el resto del modelo.

Aislar por Primitiva/Componente: El parser debe devolverte una lista de entidades (mallas, componentes). En lugar de intentar renderizarlas todas juntas de una vez, procesa y renderiza cada una de forma independiente.

Bulkhead Pattern (Compartimentación): Envuelve el proceso de creación de cada malla Three.js en un try...catch. Si una malla en particular falla al crearse (por datos corruptos), atrapas el error, registras el incidente y continúas con la siguiente malla. El resto del modelo se visualizará sin problemas.

Cálculo de Cámara Robusto: Para el OrbitControls, no calcules el bounding box sobre toda la escena. Hazlo solo sobre las entidades que hayan pasado tus controles de validación (ver punto 1) y se hayan creado exitosamente. Esto evita que una pieza corrupta desplace la cámara y "oculte" el modelo real.

Transparencia y Feedback: Si una entidad se descarta o se marca como sospechosa, es buena práctica mostrarlo. Podrías ponerla en un color de advertencia (ej., rojo semitransparente) o simplemente notificarlo en una consola o panel de estado para el usuario.

3. Rendimiento para Archivos de Gran Tamaño
Para modelos de arquitectura, el rendimiento es crítico. El navegador y Three.js tienen límites, pero con una buena estrategia se pueden manejar modelos muy grandes.

Offload con Web Workers: El parseo de un archivo SKP es una tarea intensiva de CPU que debe ejecutarse en un Web Worker. Esto evita que el hilo principal (UI) se congele. El worker parsea el archivo y devuelve la escena ya triangulada (o, idealmente, en trozos) al hilo principal.

Carga Progresiva/Streaming: Si el parser o el formato lo permiten, procesa el archivo por partes. Three.js no soporta carga "chunked" de forma nativa, pero puedes simularlo. Por ejemplo, el worker puede ir enviando lotes de mallas al hilo principal para que se vayan añadiendo a la escena de forma incremental, mejorando la percepción de velocidad.

Instancing en Three.js: Para objetos repetidos (ej., miles de sillas, ventanas), usa InstancedMesh. Esto reduce drásticamente el número de llamadas a la GPU. Puedes detectar geometrías duplicadas (mismo número de vértices y estructura) y agruparlas en una sola instancia.

Level of Detail (LOD): Para modelos extremadamente grandes, genera versiones simplificadas de la geometría (usando, por ejemplo, SimplifyModifier de Three.js). El THREE.LOD puede entonces mostrar la versión de baja resolución para objetos lejanos y la de alta resolución para los cercanos.

Límites de Memoria: El navegador es el principal limitante. Monitorea el uso de memoria y, si es necesario, implementa un sistema de "carga bajo demanda" (paginación) donde solo se cargan en GPU los objetos dentro del frustum de la cámara.

4. ¿Parchar OpenSKP o Migrar? Señales para Decidir
Tu preocupación es válida. Un proyecto de 2.5 meses con bugs reales en archivos pequeños es una señal de alerta, pero no es una sentencia.

Señales para Seguir con OpenSKP (y contribuir):

Actividad y Compromiso: El proyecto tiene un mantenedor activo y una comunidad que reporta issues.

Tu Caso de Uso: Eres un usuario real con casos de prueba complejos. Tus reportes de bugs son oro puro para el proyecto. Al contribuir con tus archivos problemáticos (de forma anónima si es necesario) y, si puedes, con parches, estarás ayudando a madurar la librería.

Filosofía del Proyecto: OpenSKP ya está en su segunda versión y tiene un enfoque multi-lenguaje, lo que sugiere un diseño pensado para ser robusto.

Señales para Migrar (o considerar un híbrido):

Estancamiento: Si el mantenedor no responde a tus issues o los bugs críticos no se arreglan en un tiempo razonable (ej., 1-2 meses).

Complejidad de tus Modelos: Si descubres que el parser falla de forma sistemática e irreparable con la mayoría de tus archivos grandes, puede que la ingeniería inversa del formato para ese tipo de geometría (curvas complejas) sea simplemente incorrecta.

El SDK Oficial de Trimble: La opción "híbrida" más realista no es un "parser alternativo", sino usar el SDK oficial de Trimble en un servicio backend (ej., un microservicio en Node.js o un script en Python). Este SDK es la fuente de la verdad y parseará cualquier archivo SKP correctamente. Tu frontend se comunicaría con este backend para obtener la geometría ya triangulada. La desventaja es la dependencia de un servicio y la infraestructura asociada.

Mi recomendación: Opta por un enfoque híbrido por ahora. Sigue usando OpenSKP en el frontend (es la solución más limpia para un visor 100% cliente), pero invierte tiempo en contribuir activamente al proyecto. Reporta los bugs con los archivos que los causan, y si puedes, ofrece parches. Este esfuerzo no solo te beneficia a ti, sino a toda la comunidad. Si la situación no mejora, el plan B (backend con SDK oficial) siempre estará ahí.

5. Patrones para Visores con Parsers de Ingeniería Inversa
Esta es la lección más importante. Asume que el parser es una caja negra imperfecta.

Diseño "Anti-Frágil": Tu visor debe ser resiliente. No des por sentado que los datos del parser son correctos. Implementa capas de validación (como las del punto 1) que actúen como un cortafuegos.

Logging y Telemetría: Cada vez que una validación falle o se descarte una entidad, regístralo. Esto te dará un historial de los problemas y te ayudará a priorizar qué arreglar en el parser.

Pruebas con Archivos Reales: Tu suite de pruebas no puede ser solo "cubos de prueba". Debe incluir una batería de archivos SKP reales, de diferentes versiones y complejidades, que representen tu caso de uso.

Transparencia con el Usuario: Si un modelo no se renderiza correctamente, es mejor ser honesto. Un mensaje como "Parte de la geometría no pudo ser procesada debido a limitaciones del parser" es mucho mejor que un modelo invisible o corrupto sin explicación.

Conclusión
Estás en el camino correcto. Los problemas que has encontrado son los esperados al trabajar con tecnología de vanguardia. La solución no es un único parche mágico, sino una estrategia de capas: un parser (OpenSKP) que mejora con tus contribuciones, una capa de validación robusta que detecta y aísla errores, y un motor de renderizado (Three.js) optimizado para rendimiento. Este enfoque te permitirá construir un visor que, aunque no sea perfecto, será lo suficientemente robusto para tus necesidades reales.

---

🗨️ Kimi (pegado):
Buen documento: el diagnóstico es correcto y las preguntas están bien separadas. Voy punto por punto, con algunos hallazgos concretos sobre OpenSKP que cambian parcialmente el panorama.
Hallazgo previo que afecta tu Bug 1
Antes de diseñar defensas, vale la pena verificar contra qué versión estás corriendo. El changelog muestra que 1.1.0 salió el 2026-08-20 con reescrituras importantes, y el README actual documenta explícitamente dos cosas relevantes para tus bugs: parseo streaming con memoria pico acotada por el registro más grande (no por el archivo completo) , y un sistema de observabilidad opt-in con errores estructurados que llevan ubicación (record 17/26, tag F901) . Tu EdgeFlagStore que reasigna buffers crecientes suena a código pre-streaming; si el adorno de 4.2MB te explota en un Array buffer allocation failed interno, lo primero es reproducir contra la última versión antes de asumir que el bug es tuyo que descubrir. Reporta el archivo al upstream: tiene historial de aceptar test files y fixes (los créditos del README listan colaboradores que arreglaron exactamente este tipo de cosas) .
Dicho esto, tu estrategia general es la correcta: no parches por archivo. Las respuestas:
1. Detección genérica de corrupción silenciosa
La regla de oro: un visor no puede saber qué forma "correcta" tiene el modelo, pero sí puede verificar invariantes. Sin conocer la geometría esperada, tienes cuatro capas de defensa, de más barata a más cara:
a) Chequeos numéricos baratos (por vértice/primitiva). Nada de esto requiere conocer el modelo: coordenadas finitas (rechazar NaN/Inf, que además rompen el bounding box y el render), triángulos no degenerados (área > ε), normales unitarias válidas, y magnitud absoluta: SketchUp trabaja en pulgadas internamente , así que un edificio real vive en el rango de 10³–10⁵ pulgadas. Un vértice a 10⁹ pulgadas de distancia es corrupción con ~certeza estadística, no un rascacielos. Esto solo habría atrapado tu Bug 2 si el desplazamiento era enorme, pero es gratis.
b) Outliers estadísticos sobre la escena completa. Calcula el bounding box por primitiva, toma el logaritmo de la diagonal, y marca outliers con z-score robusto (mediana + MAD), no con IQR simple: con 4 primitivas el IQR es inestable, con 400 es fino. Un criterio pragmático: una primitiva cuya diagonal supera k × mediana (k≈10) o cuyo centro está a más de k × mediana_diagonal del centro mediano, se marca sospechosa. Para tu caso concreto de instancias de la misma definición, hay un invariante mucho más fuerte que la estadística: todas las instancias de un componente comparten definición, luego deben tener exactamente el mismo tamaño de bounding box (el tamaño local) y solo difieren en transformación. Una bisagra de 4 componentes donde 3 miden lo mismo y 1 es 50× mayor no es un outlier estadístico, es una violación de invariante estructural — detectable con 100% de confianza, sin heurísticas. Esta es la señal más confiable que tienes y debería ser el centro de tu validador.
c) Consistencia de conteos. El archivo crudo sabe cuántos vértices/car tiene cada definición (los registros TLV lo dicen). Si buildScene() entrega una primitiva con conteos incoherentes con la definición que dice representar, hay corrupción en la resolución del grafo de escena, no en la geometría. Barato de chequear y atraparía bugs en la fase de scene baking separada de la de parseo.
d) Manifold/normales: úsalos como señal, no como veredicto. No lo recomiendo como chequeo duro: los modelos de SketchUp reales están llenos de caras sueltas, sólidos no-manifold e inversiones a propósito (caras traseras pintadas distinto). Un chequeo de manifold que rechaze geometría rechazará modelos legítimos. En cambio, úsalo suave: fracción de normales invertidas respecto al centro de la primitiva ≫50% sugiere una transformación con determinante negativo mal aplicada — otra huella típica de bugs de instancing.
2. Que un fallo no arruine todo el modelo
Tres decisiones independientes:
Parseo con fronteras por definición. OpenSKP ya separa parse() (por definición, liviano) de buildScene() (resolución del grafo, opt-in) . Aprovéchalo: parsea definición por definición con try/catch individual. Si la definición 17/26 falla, conservas 25 y muestras el modelo incompleto con un aviso "N definiciones no pudieron parsearse". Para buildScene(), haz lo mismo por rama del grafo de instancias: un subárbol corrupto no debería tumbar a sus hermanos.
Cámara desacoplada de la validez. Esta es la pieza que te rompió la vista en el Bug 2 y merece diseño explícito: el framing de cámara nunca debe calcularse sobre datos sin validar. Patrón: calcula el bbox sobre primitivas validadas (o sobre el bbox recortado — descarta outliers antes de la mediana). Las primitivas sospechosas se renderizan igual (quizá resaltadas con un tinte rojo translúcido), pero no votan en el encuadre. Así el modelo real siempre es visible y la pieza corrupta aparece como mancha señalada en lugar de vacío. Añade un panel de diagnóstico colapsable ("3 primitivas marcadas — ver") que haga zoom a cada una al hacer clic: convierte un bug silencioso en una feature de QA.
Presupuesto de errores. En vez de booleano "éxito/fracaso", el pipeline devuelve { scene, issues: [{severity, primitiveId, kind, detail}] }. Toda degradación pasa por ahí. Esto además te da, gratis, telemetría para decidir la pregunta 4 con datos.
3. Rendimiento en órdenes de magnitud mayores
Prioridades en orden de impacto/esfuerzo para Three.js en navegador:
Instancing real. Los componentes de SketchUp son instancias por naturaleza; si OpenSKP te da el árbol de escena, usa InstancedMesh por (definición × material) en lugar de una malla por instancia. Una cocina con 200 sillas iguales deja de ser 200 geometrías. Es la ganancia más grande y la más barata.
Parseo y baking en Web Worker, con Transferable (ArrayBuffers) hacia el hilo principal. El parseo TLV y el bake son puros CPU; el hilo principal solo debería ensamblar BufferGeometry y subir a GPU. Con esto, archivos de decenas de MB dejan de congelar la UI.
Primera pintura progresiva. Renderiza lo que tengas al llegar (el 60% del modelo visible ya sirve para orbitar), y sigues agregando primitivas en frames sucesivos. El usuario percibe "carga rápida" aunque el bake total tarde.
Materiales y texturas. Aquí suele estar la mitad de la memoria: las texturas embebidas en .skp vienen como PNG/JPEG sin control de tamaño. Downscale a un máximo (p. ej. 1024²) y considera atlas por material. Los materiales sin textura se mergean en geometría estática por material para reducir draw calls.
Límites realistas. Con índices Uint32 y una copia en JS + una en GPU, un modelo de ~5M triángulos ≈ 300–400MB solo de geometría, sin contar texturas — cómodo en desktop, riesgoso en móvil. Puntos de control: performance.memory en Chromium, y un modo "ligero" que simplifique mallas (meshopt simplifier, o meshopt/draco si algún día relajas el "sin conversión"). LOD agresivo solo si tu caso de uso incluye orbitar modelos de +10M triángulos; para visualización arquitectónica estándar, instancing + merging + texturas controladas alcanzan.
4. ¿Parchar, migrar o híbrido?
Tu restricción "un solo HTML, sin backend, sin SketchUp instalado" elimina el SDK oficial como opción principal (es C++, requiere binarios nativos, y rompe el modelo de distribución). Además, OpenSKP ya corre en producción en proyectos de terceros , lo que sugiere que tus dos bugs pueden ser de versiones tempranas o de una superficie aún no ejercitada. Mi recomendación: híbrido con criterio de salida definido, no migración preventiva.
Señales concretas para decidir, en orden:
Tasa de corrupción silenciosa sobre tu corpus real. Arma un corpus de 30–50 .skp de tu biblioteca (los más viejos, los más grandes, los con curvas, los con texturas) y mide: ¿qué % parsea limpio? ¿qué % falla con excepción? ¿qué % pasa tu validador de la pregunta 1? La corrupción silenciosa es el peor escenario porque degrada confianza sin avisar; si supera ~2–3% de tu corpus y el upstream no responde en semanas, ahí sí evalúas alternativas (p. ej., wasm de otro parser, o un conversor offline vía SDK para precachear GLB — aunque eso viola tu "sin conversión", sería fallback, no pipeline principal).
Latencia del upstream. Abre los dos issues con archivos de reproducción mínimos. Si responden con fix en releases, el riesgo de mantenedor único está mitigado. Tu licencia MIT y su estructura por paquetes te permiten incluso parcharte un fork local sin drama.
Costo de tu capa de defensa. Si con la capa de validación/aislamiento de las preguntas 1–2 logras que el 100% de tu corpus sea visualizable (aunque 1 de 50 piezas salga marcada), el producto cumple su promesa. Un visor con "pieza sospechosa resaltada" es mejor producto que uno que a veces no abre.
5. Patrones para visores resilientes sobre parsers de ingeniería inversa
Lo que describen (assimp sobre formatos CAD, los visores de PDF, los lectores de Office de los 90) converge en el mismo patrón, que te recomiendo adoptar como arquitectura explícita de tres capas:
Capa 1 — Parser (OpenSKP). La tratas como no confiable. Cero lógica de producto aquí, cero decisiones de cámara. Configuras su observabilidad para capturar todo.
Capa 2 — Sanitizador/validador (tuyo, la pieza que falta). Todo lo de la pregunta 1: invariantes numéricos, invariantes estructurales (instancias del mismo componente), outlier detection, conteos cruzados. Transforma "salida del parser" en "geometría con nivel de confianza". Esta capa es además portable: si mañana migras de parser, la conservas entera.
Capa 3 — Escena y UX (Three.js). Solo consume geometría validada, renderiza todo (lo dudoso marcado, no oculto), cámara sobre bbox robusto, panel de diagnóstico, degradación gradual.
Y dos prácticas de proceso que valen más que cualquier código: (a) corpus dorado con tests de regresión — cada bug real que encuentres (tus dos actuales incluidos) se convierte en fixture permanente con snapshot de conteos/bboxes, de modo que un upgrade de OpenSKP nunca te reintroduce un bug viejo silenciosamente; y (b) testing diferencial cuando puedas: para los archivos donde tengas acceso a SketchUp (en otra máquina, una vez), exporta una referencia (GLB/OBJ desde SketchUp Pro, que soporta interchange export ) y compara bboxes/conteos automáticamente. No necesitas hacerlo en el pipeline del usuario — basta como validación offline de tu corpus.
Prioridad sugerida
Verificar/reproducir tus dos bugs contra OpenSKP 1.1.0 y reportarlos upstream con archivos mínimos (podrían estar ya arreglados).
Construir la capa 2 (validador) con el invariante "instancias de la misma definición miden igual" como primer chequeo — resuelve el Bug 2 con detección perfecta.
Cámara sobre bbox robusto + renderizado de sospechosos marcados — neutraliza el daño del Bug 2 aunque reaparezca otro similar.
Corpus de 30+ archivos reales con métricas de corrupción — esto te da la evidencia para la decisión de la pregunta 4.
Worker + instancing + presupuesto de texturas — escala.
Panel de diagnóstico — convierte la fragilidad inherente del formato en una feature visible del producto.

---

🗨️ Grok (pegado):
Respuesta directa y práctica para un visor resiliente de .skp reales.
OpenSKP es actualmente la única librería open-source seria para parsear .skp sin el SDK de Trimble (ingeniería inversa de VFF 2021+ y MFC legacy). Tiene ~2.5 meses, un mantenedor principal y ya está en uso real, pero como todo parser de formato propietario reconstruido, tiene gaps de fidelidad. Los dos bugs que describes (crash en EdgeFlagStore por IDs mal leídos en geometría curva y corrupción silenciosa de transform/escala en un componente) son típicos de este tipo de trabajo.
1. Detección genérica de corrupción silenciosa
No existe una “verdad ground” del modelo, así que hay que usar heurísticas estadísticas + checks geométricos locales. Aplica después de buildScene() (o por definición/componente si puedes interceptar antes):

Outliers de bounding box / tamaño relativo (el más efectivo para tu bug 2):
Calcula el volumen o diagonal del AABB de cada primitiva/componente.
Usa mediana + MAD (median absolute deviation) o percentiles (P25–P75). Marca como sospechoso cualquier cosa > 8–20× la mediana o fuera de 3–5 MAD.
Compara también el centroide: si un componente está desplazado órdenes de magnitud respecto al resto del cluster principal, es corrupción de transform.
Para jerarquías: propaga la heurística por definición + instancias (un definition corrupto afecta todas sus instancias).

Checks geométricos locales (baratos y potentes):
Longitudes de arista: distribución de edge lengths; outliers extremos (aristas 100× más largas que la mediana) suelen indicar escala o coordenadas corruptas.
Aspect ratio de triángulos (área / perímetro² o longest/shortest edge). Triángulos degenerados o “slivers” masivos.
Normales: consistencia (ángulo entre normales de caras adyacentes) y orientaciones (winding). Muchos flips o normales caóticas = problema de triangulación/parsing.
Manifold / no-manifold: conteo de edges con >2 faces. No es perfecto (SketchUp no es estrictamente manifold), pero picos extremos son señal.
Densidad: vértices/triángulos por unidad de volumen. Una pieza con densidad absurda suele estar mal escalada.

Estadísticas globales de la escena:
Distribución de tamaños de componentes (histograma log).
Ratio total de vértices vs. bounding box de la escena.
Si el AABB global es dominado por 1–2 primitives → flag.


Implementa esto en un worker después del parse. Marca las primitives sospechosas (no las borres automáticamente) y expón un flag/UI para que el usuario pueda ocultarlas o inspeccionarlas. Es la misma filosofía que usan tools de validación de meshes (val3dity-style, checks de ruido/outliers en point clouds, etc.).
2. Aislamiento para que un fallo no mate todo el modelo
Trata el parse + buildScene como un pipeline por unidad (definition o primitiva):

Parsea el archivo completo si es posible, pero construye la escena de forma incremental / con try-catch por definition/instance.
Si una unidad falla (excepción o flag de corrupción), regístrala, omítela del grafo de render y sigue con el resto.
Cámara / framing: calcula el AABB solo sobre las primitives no-marcadas como outliers. Mantén las corruptas en la escena (quizá con material de error o wireframe rojo) pero exclúyelas del fit-to-view inicial. El usuario puede luego “Show outliers” o centrar en una pieza específica.
En Three.js: cada primitiva es un Mesh o Group independiente. Puedes añadir/quitar del scene graph sin reconstruir todo. Usa Box3 por grupo y un Box3 global limpio.

Esto convierte un fallo duro o silencioso en “modelo incompleto pero usable”.
3. Rendimiento para modelos arquitectónicos reales (órdenes de magnitud más grandes)
Límites realistas del navegador (Chrome/Firefox típicos 2026):

~1–4 GB de memoria JS práctica antes de OOM (varía por dispositivo).
Draw calls: ideal < 500–1000.
Triángulos: 1–5 M visibles con buen frustum culling + LOD se mantiene fluido; más requiere agresividad.

Estrategias prioritarias (en orden de impacto):

Web Workers + transferables:
Parse + triangulación + heurísticas de corrupción en un worker.
Transfiere ArrayBuffers de positions/normals/indices (zero-copy con postMessage(..., [buffers])).
Main thread solo crea BufferGeometry + materiales y añade a la escena. Evita el freeze de UI.

Instancing + BatchedMesh:
Componentes repetidos (puertas, ventanas, herrajes, etc.) → InstancedMesh o BatchedMesh (Three.js reciente).
Reduce draw calls drásticamente.

LOD / progressive:
Genera (o simplifica) versiones low/mid/high por definition.
Usa THREE.LOD o sistemas más avanzados (meshlets, progressive glTF-style).
Para archivos enormes: carga primero un “proxy” (bounding boxes o low-poly) y refine on-demand.

Frustum culling + octree/BVH (Three.js tiene MeshBVH o similar vía addons).
Streaming / carga por capas:
Si el formato lo permite (o si exportas intermedio a glTF), carga geometría por definition bajo demanda.
Texturas: KTX2 + basis, o lazy load.

Límites duros:
Cap de triángulos visibles o de memoria.
Opción de “simplified mode” que fusiona materials o reduce precisión de floats.


Para un modelo de casa completa (cientos de miles a millones de triángulos) con buen instancing + LOD + worker, es viable en desktop moderno. En móvil hay que ser mucho más agresivo.
4. ¿Seguir con OpenSKP, migrar o híbrido?
Señales claras para decidir:

Seguir parchando / contribuir a OpenSKP (recomendado a corto-medio plazo):
Es la única opción 100 % cliente, sin SketchUp, MIT, multi-lenguaje y ya con buildScene().
Reporta los bugs con archivos mínimos reproducibles (el crash de EdgeFlagStore y el componente escalado). El proyecto acepta contribuciones y tiene docs de formato.
Si el mantenedor responde y los fixes llegan rápido → quédate.
Añade tus propias capas de resiliencia (heurísticas + aislamiento) encima. Eso es más valioso que el parser perfecto.

Migrar / híbrido:
SDK oficial de Trimble: solo viable si puedes correr un proceso local (desktop app o backend). Rompe el requisito “100 % cliente / single HTML”.
Otros parsers: hay uno en Rust más limitado (solo ~2017). No hay alternativa madura equivalente.
Enfoque híbrido práctico: OpenSKP como primary path. Si detectas corrupción grave o crash, ofrece “Export to GLB via server” (si algún día tienes backend) o “Open in SketchUp Free” como fallback. O pre-procesa los archivos más problemáticos offline a glTF y guarda el .glb junto al .skp.


Señales de alerta roja para abandonar OpenSKP:

Bugs de corrupción silenciosa en >20–30 % de archivos reales de arquitectura.
Fallos sistemáticos en features comunes (curvas suaves, nested components profundos, texturas embebidas grandes).
Mantenedor desaparece o el proyecto se estanca.

Por ahora: contribuye los fixes + construye la capa de resiliencia. Es más barato y mantiene tu stack puro-cliente.
5. Patrones para visores resilientes contra parsers reverse-engineered

Nunca confíes en el parser al 100 %. Siempre valida post-parse (heurísticas de arriba).
Fail soft por unidad: try-catch + skip + log. Nunca dejes que un registro mate el proceso completo.
Observabilidad: loggea stage/tag/record del TLV (como ya te muestra el error), IDs de materiales, tamaños de buffers, etc. Facilita reportar bugs.
Modo degradado: si el parse es incompleto, muestra lo que hay + banner “Modelo parcialmente cargado – X componentes omitidos/sospechosos”.
Validación cruzada opcional: si el usuario tiene SketchUp, permite comparar bounding boxes o hash de geometría.
Tests con corpus real: mantén un set de archivos problemáticos (curvas, componentes anidados, texturas grandes, versiones viejas/nuevas) y corre las heurísticas en CI.
Separación parse vs. scene: parse() ligero + buildScene() opcional y robusto (exactamente lo que OpenSKP ya expone).
UI de depuración: wireframe, colorear por material/layer/componente, mostrar AABB de outliers, estadísticas de geometría.

Esto es el mismo enfoque que usan visores de formatos CAD/BIM propietarios o de meshes escaneados: asumir que el input puede estar “roto” y diseñar el pipeline para degradarse con gracia.
Resumen de plan de acción inmediato

Implementa worker + heurísticas de outlier AABB/edge-length/normales.
Framing solo sobre geometría limpia; outliers visibles pero no afectan cámara.
Reporta los dos bugs a OpenSKP con reproducers mínimos.
Añade instancing para components repetidos y empieza a pensar LOD simple.
Expón en la UI “estado de parse” (completo / parcial / con warnings).

Con eso tu visor pasa de “funciona con piezas de prueba” a “sobrevive a modelos arquitectónicos reales imperfectos”. Si quieres, puedo bajar al detalle de código (heurística de MAD en JS, patrón de worker + transferable, o cómo envolver buildScene por definition).

---

🗨️ Meta AI (pegado):
Visor resiliente de.skp sin SketchUp — estrategia para ORA

Tienes el diagnóstico correcto: un parser de 2.5 meses que funciona para una bisagra es un logro, pero dos fallos distintos (hard crash + corrupción silenciosa) en 2 archivos de <5MB es la señal de que el formato subyacente tiene ramas que OpenSKP aún no cubre. No es culpa de la librería — es lo normal en reverse engineering. La solución no es "parchar hasta que no falle", es diseñar el visor asumiendo que va a fallar.

Te propongo la arquitectura que usan visores de CAD/BIM resilientes.
1. Cómo detectar corrupción silenciosa sin ground truth

Tu bug 2 es clásico: parseó, pero una primitiva está 50x más grande. No puedes validar contra "lo correcto", validas contra estadística y física.

Pipeline de sanity por primitiva, después de buildScene():
JavaScript

function auditPrimitives(primitives) {
  // primitives = [{positions: Float32Array, indices, transform, name}]
  const boxes = primitives.map(p => computeAABB(p.positions, p.transform));
  const volumes = boxes.map(b => b.volume());
  const medianVol = median(volumes);

  return primitives.map((p,i) => {
    const b = boxes[i];
    const issues = [];
    if (!isFinite(b.min.x) || hasNaN(p.positions)) issues.push('nan');
    if (b.volume() > medianVol * 40 && volumes.length > 3) issues.push('outlier-volumen');
    if (b.diagonal() > 1e4) issues.push('escala-absurda'); // SketchUp en mm, 10m ya es raro para una bisagra
    if (isDegenerate(p)) issues.push('degenerada'); // >80% triángulos con área < 1e-8
    if (normalAnomaly(p)) issues.push('normales');
    return { primitive: p, box: b, issues, severity: issues.includes('nan')? 'fatal' : issues.length? 'sospechoso' : 'ok' }
  });
}

12 líneas ocultas

Heurísticas que más señal dan en tu caso:

    Outlier relativo, no absoluto: En una casa, una pared puede ser 100x una bisagra, pero no 50x el resto de piezas de la misma definición. Compara dentro del mismo componentDefinition, no global. Usa MAD (median absolute deviation). Si vol > median + 6*MAD, marca.
    Centroide desplazado: Si el centroide de una primitiva está a > 10x la diagonal del AABB del 90% del resto, es casi seguro corrupción de transform.
    Densidad de vértices: vertices / volumen. La pieza corrupta suele tener densidad ridículamente baja.
    Check rápido de transform: SketchUp guarda matrix = T * R * S. Si determinant < 0 (espejo) + escala > 1000, sospechoso. Muchos bugs de parser vienen de leer mal un Double en la matriz.
    Normales: OpenSKP ya triangula, pero si todas las normales apuntan igual y el mesh es cerrado, o si length(normal) ~ 0, hay dato perdido.

Esto no corrige, solo etiqueta. Lo importante es qué haces con la etiqueta.
2. Que un componente roto no mate el resto

Hoy haces SkpFile.fromBuffer(...).buildScene() monolítico. Hay que romperlo en isla por isla.

a) Parse por definición, no por archivo:
JavaScript

// Pseudocódigo con API actual de OpenSKP
const file = SkpFile.fromBuffer(buf, { onRecordError: 'collect' }); // pide esta opción al mantenedor
const definitions = file.componentDefinitions; // array

for (const def of definitions) {
  try {
    const scenePart = file.buildScene({ only: def.id, safeMode: true });
    addToThreeJS(scenePart, { trusted: audit(def).severity === 'ok' });
  } catch (e) {
    logTelemetry({ def: def.name, error: e, record: e.recordTag });
    // sigue con el resto, no aborta
  }
}

8 líneas ocultas

Si buildScene() no permite only, monkey-patcheen EdgeFlagStore: envuelve la asignación en try/catch y si shift > 1e6, aborta esa definición y retorna null. Ya identificaste el bug — esa es la contención correcta. Ese es el PR que más valor tiene para upstream.

b) Framing de cámara resiliente:

Nunca calcules Box3.setFromObject(scene). Calcula dos cajas:

    trustedBox: unión de solo primitivas ok
    fullBox: unión de todo

Usa trustedBox para controls.fit(). Para las sospechosas, renderízalas igual pero con overlay: wireframe rojo + botón "aislar / ocultar". Así el usuario ve que algo existe, pero no arruina la vista.

    Patrón de visores pro: siempre orbita lo confiable, lista lo no confiable en un panel lateral.

3. Para modelos de 50M+ triángulos (casas reales)

En navegador tienes techo de ∼2-3GB de RAM por pestaña. Un SKP de 200MB descomprimido puede ser 1.5GB de buffers.

Stack que te falta hoy:

    Web Worker obligatorio: Mueve fromBuffer y buildScene a worker. El error Array buffer allocation failed que ves es OOM del main thread. En worker puedes atraparlo sin congelar UI.

JavaScript

worker.postMessage({ buf }, [buf]); // transferable

    No buildScene() directo a Three.js: OpenSKP te da positions/normals/uvs por primitiva. No crees una BufferGeometry por cada cara. Agrupa por material: mergeBufferGeometries por material dentro de cada definición. Reduces de 10k draw calls a 50.
    Instancing: Tu caso de 4 componentes es perfecto para InstancedMesh. Si una definición se repite 300 veces (ventanas), no dupliques buffers. Guarda 1 geometría + 300 matrices.
    Streaming / LOD pragmático: No puedes hacer LOD geométrico real sin simplificación (demasiado caro en JS). Haz esto:
        Fase 1: carga solo bounding boxes de componentes + conteo de triángulos. Render cajas.
        Fase 2: carga geometría por demanda según frustum + distancia. Lo más grande primero.
        Para arquitectura, un impostor de caja con el material es 95% útil para navegar.
    Límites explícitos: Antes de parsear, si arrayBuffer.byteLength > 100MB, activa modo low-memory: desactiva texturas, salta edges suaves, limita a maxTriangles = 2M y muestra aviso.

4. ¿Seguir con OpenSKP, migrar, o híbrido?

Señales para decidir, objetivas:

Sigue con OpenSKP si:

    Puedes contribuir el fix de EdgeFlagStore (es un chequeo de 5 líneas: if (shift > maxReasonable) throw CorruptRecord). El mantenedor está activo — PRs de julio/agosto 2026.
    El 80% de tus archivos reales son SketchUp 2021+ (formato que OpenSKP ya cubre bien).

Migra / híbrido si:

    Necesitas fidelidad de curvas suaves, soft/smooth edges y uv_transform exactos — que es justo donde falla. Esas son las partes menos documentadas del formato.
    Necesitas garantía legal para clientes.

Opciones reales:

    SDK oficial C de Trimble (SketchUp SDK): es gratis para lectura, pero no corre en navegador. No es MIT, no puedes hacerle bundle WASM sin licencia. Sirve como validador en servidor local: ORA podría tener un microservicio opcional en Rust/C++ que, si está disponible, convierte SKP->glTF con el SDK oficial. Si no está, usa OpenSKP. Así mantienes "100% cliente" como default, pero con salida de emergencia.
    No existe parser maduro alternativo: Assimp, etc. no leen SKP moderno.

Mi recomendación para ORA: enfoque híbrido defensivo.

    OpenSKP como motor principal (por licencia, tamaño y control), pero envuelto en una capa ORAParser tuya que implementa 1) auditoría 2) aislamiento por definición 3) fallback. Y en paralelo, mantén un conversor local opcional basado en SDK oficial para tus proyectos internos grandes.

Esto te deja seguir aportando a OpenSKP (te conviene que madure) sin bloquear tu suite.
5. Patrones de visores contra formatos reverse-engineered

    Nunca confíes en el parser: trátalo como un decodificador de red no confiable. Todo for que itera records debe tener try/catch por record.
    Golden files + fuzzing: Guarda esos 2 archivos que rompen como regression-bisagra-detallada.skp y regression-curva-f901.skp. Cada cambio en ORA corre audit sobre ellos. Incluso fuzzéa: cambia 1 byte aleatorio del SKP y verifica que no crashee el visor.
    Telemetría de parser: Loguea tag, record index, shift size cuando falle. Es lo que te permitió intuir el bug de F901. Con eso el fix upstream es trivial.
    Modo degradado visible: Todo visor serio de BIM tiene 3 estados por objeto: rendered | proxy-box | failed. Nunca failed = invisible.
    Separar parseo de baking: fromBuffer (bajo nivel) nunca debería tirar por geometría. El buildScene (alto nivel) sí puede decidir descartar. Pide esa separación al upstream.

Si quieres, te armo el esqueleto de ORAParser con worker + auditoría + framing resiliente en un HTML single-file como el que ya tienes, para que puedas dropear tus 2 archivos de prueba y ver las primitivas sospechosas marcadas en rojo.

¿Te sirve que lo deje listo con tu fix de material gris neutro ya integrado?

---

🗨️ Qwen (pegado):
Este es un desafío clásico y fascinante en el desarrollo de herramientas de arquitectura: construir robustez sobre cimientos de ingeniería inversa. El hecho de que ya tengas un prototipo funcional en 2.5 meses es un logro enorme.
A continuación, respondo a tus 5 preguntas con estrategias concretas, patrones de código y criterios de decisión para llevar ORA SKP Viewer a un nivel de producción con archivos reales.
1. Detección de corrupción SILENCIOSA (sin ground truth)
No puedes saber si una silla "debería" tener 4 patas, pero sí puedes detectar anomalías estadísticas y topológicas en los datos parseados. Implementa una capa de validación defensiva entre OpenSKP y Three.js:
Detección de Outliers por Transformación (El bug del 50x): Antes de crear la malla, calcula la escala implícita de la matriz de transformación 4x4 de cada componente/instancia. Calcula el determinante de la submatriz 3x3 superior izquierda (o la longitud de los vectores de escala).
Heurística: Calcula la mediana de la escala de todos los componentes. Si un componente tiene una escala > 10x la mediana (o un valor absoluto de traslación > 10,000 unidades, asumiendo mm), márcalo como sospechoso.
Validación de Geometría Degenerada: Itera sobre los triángulos (o una muestra aleatoria del 10% si son muchos). Calcula el área de cada triángulo (producto cruz de dos aristas). Si > 5% de los triángulos tienen área < 1e-6 o contienen coordenadas NaN/Infinity, la malla está corrupta.
Sanitización de Materiales: Ya hiciste esto con el color rojo. Extiéndelo: si un material tiene propiedades PBR con valores fuera de rango (ej. roughness < 0 o > 1, o texturas con dimensiones 0x0), reemplázalo por un material MeshStandardMaterial gris neutro por defecto.
javascript

123456789101112
2. Aislamiento de fallos y renderizado resiliente
Un parser no debe ser "todo o nada". Debes envolver el proceso en un patrón de circuito breaker a nivel de entidad:
Try-Catch por Componente/Entidad: No hagas un buildScene() monolítico. Itera sobre las entidades de nivel superior. Si el parseo de una entidad lanza una excepción, captúrala, registra un warning en consola (console.warn("Entidad X omitida por error de parseo", e)), y continúa con la siguiente.
Geometría de Fallback (Placeholder): Cuando detectes corrupción silenciosa o un fallo de parseo, no renderices nada vacío. Genera un BoxGeometry simple en la bounding box reportada (o una bounding box por defecto de 1x1x1) con un material de alambre rojo (wireframe: true). Esto le dice al usuario: "Aquí hay algo, pero no pudimos leerlo bien", sin arruinar el resto del modelo.
Cálculo de Cámara en Dos Pasos:
Calcula la Box3 de todas las entidades válidas.
Filtra las entidades cuya Box3 tenga un volumen > 50 veces la mediana de volúmenes (outliers).
Calcula el encuadre de la cámara (controls.fitToBox) usando solo el conjunto filtrado.
Opcional: Añade un botón en la UI "Restaurar cámara completa" que incluya los outliers por si el usuario quiere verlos.
3. Rendimiento para archivos arquitectónicos masivos
Un modelo de casa completo puede tener cientos de miles de polígonos y decenas de megabytes. El hilo principal se ahogará si no haces esto:
Web Workers + Transferable Objects: El parseo de binarios debe ocurrir en un Web Worker. Cuando el worker termine, no envíes el objeto JavaScript complejo de vuelta. Extrae los Float32Array (positions, normals, uvs) y Uint32Array (indices) y envíalos al hilo principal usando la API de Transferable. Esto hace la transferencia O(1) (cero copia de memoria).
javascript

12
Instancing Obligatorio: SketchUp se basa en componentes. Si un modelo tiene 500 sillas idénticas, no crees 500 THREE.Mesh. Usa THREE.InstancedMesh. OpenSKP ya te da las instancias; solo debes agruparlas por geometryHash o materialId y poblar la matriz de instancias. Esto reduce draw calls de miles a decenas.
Límites de Memoria del Navegador: Un ArrayBuffer único está limitado a ~2GB en la mayoría de los navegadores modernos, y el heap total a ~4GB. Para modelos gigantes, asegúrate de que OpenSKP no esté concatenando arrays innecesariamente. Usa vistas de memoria (DataView) sobre el buffer original siempre que sea posible en lugar de crear nuevos arrays.
Carga Progresiva (Chunking): Si el archivo es >20MB, procesa las entidades en lotes de 100. Usa setTimeout o requestIdleCallback entre lotes para ceder el control al hilo principal y evitar el aviso de "Página no responde".
4. ¿Parchar, Migrar o Híbrido? (Criterios de decisión)
Dado que es un proyecto de 2.5 meses con un solo mantenedor, la señal de alarma no es que existan bugs, sino la tasa de fallo en archivos reales.
Señales para ABANDONAR OpenSKP y migrar:
Más del 10% de tus archivos de prueba reales fallan de manera irrecuperable.
El mantenedor no responde a issues críticos en > 3 semanas.
El parser carga todo el archivo en memoria de una vez, haciendo imposible archivos >50MB sin rediseñar toda la librería.
Recomendación Estratégica: Fork + Capa de Robustez (Enfoque Híbrido Interno)
No esperes al mantenedor original. Haz un fork de OpenSKP en tu organización/proyecto.
Implementa el try-catch por entidad y la sanitización de matrices directamente en tu fork.
El bug de EdgeFlagStore (asignación de buffer absurda) es un clásico error de integer underflow o lectura de offset con signo incorrecto en ingeniería inversa. En tu fork, añade una guardia: if (shift < 0 || shift > MAX_REASONABLE_SHIFT) throw new Error("Offset corrupto detectado"). Esto convierte una corrupción silenciosa o un crash de memoria en un error manejable que puedes capturar y aislar.
Nota sobre el SDK oficial: El SDK de SketchUp (C++) no es fácilmente ejecutable "sin backend" en el navegador. Requeriría compilar a WebAssembly, lo cual es un proyecto de meses y sigue teniendo limitaciones de licencia para distribución. Quédate con el parser JS/TS, pero hazlo resiliente.
5. Mejores prácticas para visores de formatos reverse-engineered
Cuando trabajas con formatos propietarios sin documentación oficial, asume que los datos están hostilizados. Aplica estos patrones:
Defensive Parsing (Parseo Defensivo): Nunca confíes en un índice, longitud o offset leído del binario. Valida que offset + length < buffer.byteLength antes de cualquier DataView.getFloat32. Si no se cumple, lanza un error controlado, no dejes que el motor de JS intente leer memoria fuera de límites.
Fuzz Testing en CI: Crea un script que tome una carpeta con 50-100 archivos .skp diversos (curvos, anidados, vacíos, con texturas, versiones antiguas de SketchUp) y los ejecute contra tu parser en cada commit. Si un arreglo para un archivo rompe otro, lo sabrás inmediatamente.
Degradación Elegante (Graceful Degradation): El objetivo es visualizar, no editar.
¿Falla el decode de una textura JPEG embebida? → Usa un color sólido.
¿La matriz de transformación tiene un NaN? → Usa la matriz identidad.
¿Falta el array de normales? → Three.js puede calcularlas (computeVertexNormals), o usa un material flatShading.
Detección de Versión de Archivo: Los formatos binarios cambian entre SketchUp 2017, 2021, 2023, etc. Lee el header del archivo .skp inmediatamente. Si la versión no está explícitamente soportada por OpenSKP, muestra un aviso claro al usuario: "Versión SKP 2023 detectada. El renderizado puede ser imperfecto" antes de que siquiera intente parsear. Esto gestiona las expectativas y reduce reportes de bugs "falsos".
Próximos pasos accionables para tu prototipo:
Implementa la validación de matrices de transformación (escala/traslación) y filtra outliers antes de crear el BufferGeometry.
Envuelve el bucle de construcción de escena en un try-catch por entidad, generando un placeholder rojo para las fallidas.
Mueve la llamada a SkpFile.fromBuffer a un Web Worker y usa Transferable objects para los arrays tipados.
Haz un fork de OpenSKP y añade la guardia shift > MAX en el EdgeFlagStore para convertir el crash de memoria en un error capturables.
Estás construyendo algo muy valioso. La robustez en este tipo de herramientas no viene de un parser perfecto, sino de un pipeline de ingestión que sabe cómo caer de pie cuando el parser tropieza.

---

🗨️ GLM (pegado):
Antes de responder por pregunta, un cuadro que ordena todo: tus dos errores son de clases distintas , y eso ya sugiere la estrategia. El Bug 1 es un fallo de presupuesto (una asignación sin cota que revienta) — se puede neutralizar estructuralmente sin siquiera entender la causa raíz. El Bug 2 es un fallo de interpretación (un campo del formato leído con el diseño equivocado) — ese no se neutraliza, se diagnostica. La buena noticia del Bug 2: "50x más grande y desplazado" tiene una firma muy característica.

0. Diagnóstico rápido del Bug 2 (hazlo antes que nada)
Ese síntoma — geometría correcta en cantidad de vértices, pero escalada y desplazada — apunta casi siempre a la matriz de transformación de la instancia , no a la geometría local del componente. Un factor ~50.0 limpio no corresponde a ninguna conversión de unidades canónica (pulgada→metro es 39.37, cm→pulgada 2.54), lo que huele a un campo numérico mal interpretado (doble lectura como dos floats, offset de 4 bytes, orden de la matriz).

Experimento de 10 minutos que acota el bug: renderiza el componente corrupto en su espacio local , sin aplicar la transformación de instancia, y compara sus dimensiones con las de los otros 3. Si en local mide como los demás → la geometría parsea bien y el bug está en la lectura de la matriz (un solo punto de código, que afecta a todos los modelos con componentes instanciados, es decir, a casi todos los modelos reales). Inspecciona además los 16 valores de la matriz sospechosa: escalas ~50.0 o residuos tipo 1e-7 donde debería haber 1.0 son lectura corrupta; una matriz sana de SketchUp tiene un análisis plausible ( en Three.js te lo da).Matrix4.decompose()

1. Detectar corrupción silenciosa sin verdad fundamental
Construye una jerarquía de señales , de barata a cara, y clasifica cada primitiva/componente en tres niveles (sano / sospechoso / corrupto-casi-seguro). Nunca descartes en silencio — marca y notifica.

a) Invariantes de conteo. Un parser de formato binario debe verificar en cada registro que lo construido coincide con lo declarado (n caras, n aristas, n vértices). La divergencia de contenidos es la señal más temprana de desalineación de lectura, antes de que se produzca geometría visible.

b) Validez numérica. isFinite() sobre todos los vértices y transformaciones. Un solo NaN destruye las esferas delimitadoras, frustum culling y tu encuadre de cámara. Es gratis y obligatorio.

c) Plausibilidad intra-archivo con estadística robusta. No se comparan dimensiones absolutas entre componentes: en arquitectura una casa es legítimamente 5000x más grande que un tirador. Compara en log-escala con la mediana, que tolera hasta ~50% de componentes corruptos sin movimiento:

js

const d = primitives.map(p => Math.log10(p.bboxDiagonal)).sort((a,b)=>a-b);
const med = d[d.length >> 1];
const mad = 1.4826 * median(d.map(x => Math.abs(x - med)));
const flag = x => Math.abs(Math.log10(x.bboxDiagonal) - med) > 3 * mad; // + distancia del centroide
Agregue desplazamiento: centroide del componente a >10 medianas del centroide global es la segunda coordinada del valor atípico.

d) Comparación intradefinición — tu señal más fuerte. Si la misma definición de componente está instanciada varias veces y 9 instancias miden parecido y 1 no, el veredicto es inmediato, porque las instancias de una misma definición casi nunca varían 50x en un modelo real. Esto requiere que OpenSKP exponga la jerarquía definición/instancia (más sobre esto abajo).

e) Ground Truth embebido en el propio archivo. Este es el patrón subestimado: los formatos traen su propia imagen correcta. Dos fuentes concretas en .skp: las definiciones de componente serializan su cuadro delimitador (verifica si OpenSKP la exponen — si la geometría parseada difiere en órdenes de magnitud de la bbox declarada, veredicto sin estadística); y los .skp incorporan una miniatura de vista previa . Muestra la miniatura junto al render en un panel de diagnóstico: comparación visual humana trivial, y eventualmente automatizable (proyectar el modelo y comparar silueta con la miniatura con umbral laxo). Para una biblioteca personal, ese panel "esperado vs. obtenido" es oro.

f) Señales topológicas y geométricas internas. Fracción de triángulos degenerados (área ~0); consistencia normal-vs-cross-product (>95% de alineación esperada; desalineación masiva = índices corruptos); longitud mediana de arista de una primitiva 50x su propia mediana (índices apuntando a vértices lejanos); aristas con conteo de uso ≠ 1–2 (SketchUp trata las aristas como entidades de primera clase; conteos de 3+ o 0 tras el parseo indican geometría perdida). El chequeo estricto de manifold da falsos positivos en arquitectura (caras sueltas, componentes 2D), así que úsalo como estadística, no como regla.

2. Aislar fallos de un componente
Fail-soft en el walk, no global. Envuelve el procesamiento por registro de nivel superior , no alrededor de . Si el registro 17/26 revienta, salta al siguiente y sigue. Riesgo: el stream quedó desalineado y todo lo subsiguiente es basura — por eso necesitas resincronización (buscar el próximo tag/magic válido) y los validadores de la pregunta 1 como red de seguridad: si los siguientes N registros rompen invariantes, aborta. Para que esto funcione con monolítico tendrás que intervenir OpenSKP, pero ya tienes un fork de facto (tu fix del color sintetizado) — formalízalo.buildScene()buildScene()

Presupuesto de asignación — mata el Bug 1 estructuralmente. Regla dura: ninguna estructura interna del analizador reserva más que (k ~ 4–8 es generoso). El EdgeFlagStore pidiendo gigas para un .skp de 4.2MB viola un presupuesto trivial de detectar. Además, su diseño (buffer denso corrido por ) debería ser una estructura dispersa (Map o bitset paginado): los ids no tienen por qué ser densos. Con esto, tu adorno curvo parsea con degradación (posible pérdida de flags de suavizado → flat shading en curvas, visible pero no fatal) en vez de morir. El tag F901 con curva geométrica sugiere exactamente el registro de aristas suavizadas; registra en un log los tags que ves y los que ignoras te construye incrementalmente el mapa del formato — y te dice qué archivos de tu biblioteca usan territorio no cubierto.k · tamañoDelArchivoshift

Cámara robusta: la corrección de mayor ROI por líneas de código. Encuadra sobre estadísticas podadas, no sobre el bbox global: recorta por eje el 1–5% de puntos más lejanos (trimmed bbox), o encuadra solo sobre los componentes clasificados "sanos", dejando los sospechosos visibles pero fuera del cálculo — exactamente tu requisito de eliminar sin ocultar. Con fallback conservador si el filtro deja la escena vacía.

Estructura de escena: un grupo/mesh por componente, no una malla fusionada. Te da toggles, picks, crilling y la posibilidad de reemplazar individualmente una pieza cuando la repara. Si la geometría de un componente falla al construirse, deja un placeholder wireframe de su bbox declarado. Y un panel de diagnóstico visible (componente, dimensiones, estado, alternar) — la transparencia es la resiliencia más barata, y en una suite de arquitectura como ORA, la integridad de datos reportada explícitamente es una característica, no hay una solución alternativa.

3. Rendimiento para modelos arquitectónicos reales
Cifras de contexto: un interior completo va de 200k a 5M+ triángulos y 50–500MB de archivo. Techo práctico en pestaña de navegador de escritorio: ~2–4GB de montón; llamadas de sorteo <1000; 5–10M triángulos rinden bien en GPU integrada si las llamadas de sorteo son bajos.

Trabajador Web: obligatorio, no opcional. El paseo de 300MB en el hilo principal congela OrbitControls durante segundos y rompe tu promesa de "siempre orbitable". Worker dedicado, transferido (no copiado), postMessage por hito. Vigile el pico de memoria : el analizador construye estructuras intermedias (EdgeFlagStore incluido) que duplican o triplican la huella; convierte cada primitiva a typed arrays finales y suelta las intermedias en cuanto puedas.ArrayBuffer

Carga progresiva. Streaming de red no aplica (todo local), pero progresivo sí: el trabajador postea cada primitiva terminada; el hilo principal construye geometrías con presupuesto por frame (≤8ms) usando . El lienzo renderiza lo que ya hay mientras llega el resto.requestIdleCallback

La creación de instancias es LA optimización específica de SketchUp. SketchUp es una instancia por naturaleza: definición + N instancias con transformación. Una cocina repite el mismo tirador 40 veces. con la geometría de la definición y N matrices = 1 llamada de sorteo. Esto requiere que el parser exponga la jerarquía definición/instancia en vez de geometría horneada en el mundo — mismo requisito que la señal (d) de la pregunta 1 y que el diagnóstico del bug 2. Es el fork más valioso que puedes hacerle a OpenSKP: una sola exposición de datos desbloquea diagnóstico, memoria y rendimiento a la vez.InstancedMesh

Batching por material para lo no instanciable (el conteo de draw llama mata antes que el de triángulos). LOD: hazlo barato primero. En vez de simplificación de mallas (cara de computadora, con artefactos), aplica selección por tamaño en pantalla: ocultar componentes cuyo bbox proyectada <2px elimina tiradores cuando ves la casa entera, y es casi gratis. Simplificación real (meshoptimizer tiene compresor y simplificador) solo si medir lo exige. Texturas: dedupe por hash de bytes embebidos, (async) fuera del hilo principal; una 4K RGBA son 64MB de VRAM y los modelos reales reutilizan las mismas texturas.createImageBitmap

Matiz sobre la caché: un sidecar (geometría normalizada + manifiesto por hash de archivo) da reaperturas instantáneas. No es "convertir a otro formato" en el sentido que prohibiste — el .skp sigue siendo la fuente — pero es una decisión tuya de ponderar contra el espíritu del requisito.

4. ¿Parchar OpenSKP, migrar o híbrido?
El panorama real: no hay a dónde migrar . Assimp no lee .skp; el ecosistema de analizadores .skp puros en JS es prácticamente OpenSKP; pedir exportación a glTF viola tu requisito de no convertir. El SDK C oficial de Trimble es fidelidad ~perfecta pero: binario propietario con restricciones de redistribución, decenas de MB, requiere voltorio (WASM o binario local acompañante que rompe el espíritu de "un solo HTML, sin instalar nada"), y contradice el ADN MIT de tu proyecto. Así que la pregunta real es: fork formal + visor blindado, o rendirse al SDK . Y hay una decisión arquitectónica que hace la apuesta reversible: definir una interfaz ( ) y trata OpenSKP como backend intercambiable. Si mañana hay otro analizador, el visor no cambia.SkpBackendparse(buffer) → AsyncIterable<Primitiva> + warnings + jerarquía

Señales para decidir, en orden de peso:

Proporción de errores de código vs. de formato. Los primeros son baratos (tu EdgeFlagStore es uno: falta de cota); los segundos exigen RE nueva. Si tus fallos se concentran en 2–3 patrones, es parcheable; si cada archivo nuevo revela territorio desconocido del formato, el riesgo excede lo que un mantenedor absorba.
KPI mensual: % de tu biblioteca que parsea correctamente — "correctamente" con los validadores de la pregunta 1, no "sin excepción" (tu Bug 2 te enseñó exactamente por qué esa métrica miente). 95%+: viable. 70%: reconsiderar.
Cobertura de versiones del formato. Los .skp de épocas distintas (pre-2018, 2021+) difieren internamente. Inventario qué versiones tienes y cuáles cubren OpenSKP; tu corpus debe tener al menos un archivo por época.
Responsividad del mantenedor. Si acepta PRs puntualmente, contribuya (tu fix del color sintetizado es exactamente el tipo de aporte que un proyecto de 2.5 meses necesita); si no responde, fork formal con licencia MIT sin fricción.
El activo más valioso del proyecto a largo plazo no es el código: es el corpus dorado. Carpeta de .skp reales reproducibles, cada uno con un golden JSON (conteos por registro, vértices/triángulos por primitiva, bbox por componente, transformaciones serializadas), corrido en Node con CI en cada cambio del parser. Cada error arreglado queda congelado para siempre. Esa es la diferencia entre compartir y mantener.

5. Patrones conocidos de visores contra parsers de ingeniería inversa
Tu disciplina tiene un canon: los visores RAW de cámaras fotográficas (dcraw → LibRaw/rawspeed, darktable). Mismo problema exacto: formatos propietarios, decenas de variantes por fabricante y época, RE comunitaria, corrupción silenciosa constante. Lo que allí demostró funcionar:

Tabla de compatibilidad pública por variante de archivo: "soportado / parcial / degradado". Publica la tuya por versión de .skp.
Fail-soft por sección con la miniatura como último recurso renderizable — tu análogo es el thumbnail embebido.
Validadores de plausibilidad por encima del parser, siempre (exposiciones imposibles en RAW; escalas absurdas en SKP).
Presupuesto en toda asignación — la RE con fuzzing estructurado encuentra los crashes antes que tus archivos; en JS, tu versión es la cota , que habría atrapado el EdgeFlagStore solo.k·filesize
Capa de normalización explícita post-parseo. Tu fix del color sintetizado (255,84,84) es la instancia perfecta del patrón: no confies en que el parser reporte "sin material"; inferirlo y sanearlo en una etapa propia, auditable y con reglas documentadas (materiales sintetizados, unidades → metros, abrazadera de transformaciones, dedupe de texturas). Esa capa es tuya, no del analizador, y es donde vive tu diferenciación de fidelidad.sanitize(scene)
Fail-closed para lo crítico desconocido, fail-open para lo decorativo: decide por tag si omitirlo rompe geometría (aborta esa rama) o solo estilo (continúa y advierte).
Minivolcados: guarde el registro crudo de un componente corrupto para reproducir errores sin el archivo completo.
Qué haría la semana que viene, en orden de ROI
Experimento de espacio local del Bug 2 (10 min) — determina si es la matriz de instancia y acota el parche.
Cota de asignación + estructura dispersa en EdgeFlagStore — convierte el crash duro en degradación suave; El adorno curvo probablemente se renderice.
Encuadre robusto con trimmed bbox / exclusión de outliers (unas pocas líneas) — con ambos bugs vivos, tu visor ya se vuelve usable.
Panel de diagnóstico con la miniatura embebido — corrupción silenciosa → señal visible.
Corpus dorado + trabajador + interfazSkpBackend — la apuesta de fondo a dos meses.
La idea que atraviesa todo: no trates de que el parser no falle — trátalo como una fuente de datos no confiable y pon la confianza en capas tuyas que validan, aíslan y reportan. Es lo mismo que hiciste intuitivamente con el color sintetizado; ahora generalízalo a geometría, transformaciones y presupuesto de memoria.

---

Gemini:
Para blindar el visor ante corrupción silenciosa y caídas catastróficas, debes trasladar el parseo a un **Web Worker** y aplicar tolerancia a fallos por componente. Para evitar que una pieza desproporcionada arruine la vista, **desacopla el encuadre de la cámara del `Box3.union()` global**: calcula la caja contenedora representativa usando **estadística robusta (mediana y rango intercuartílico / IQR)** sobre los volúmenes y centros de cada componente, ignorando *outliers* estadísticos solo para la cámara y marcándolos en una lista de advertencias en la UI. A nivel de datos, la corrupción geométrica silenciosa suele ser un error de escala en la matriz de transformación; puedes detectarla comparando el determinante de la matriz local de cada instancia contra la mediana de sus hermanas. Para el fallo duro (Bug 1), debes modificar el parser para que envuelva la lectura de primitivas complejas en bloques defensivos que capturen buffers anómalos y simplemente descarten la arista o malla rota en lugar de propagar un `RangeError` que rompa toda la escena.

Estratégicamente, pretender que una librería por ingeniería inversa de apenas 2.5 meses procese modelos arquitectónicos reales sin romperse es inviable a corto plazo: la arquitectura depende críticamente de componentes anidados, planos de sección y curvas suaves que la librería aún no comprende. Si tu restricción de ser 100% en el navegador es innegociable, estás obligado a **hacer un fork de OpenSKP** para implementar defensas internas y optimizar la salida hacia **`InstancedMesh` en Three.js** (esencial para duplicados como ventanas o mobiliario, sin lo cual saturarás la memoria del navegador). No obstante, para un producto robusto, la mejor práctica es un enfoque de **degradación elegante**: parsear con OpenSKP en el cliente como primera opción rápida, pero admitir un puente local opcional (como un pequeño binario en Rust/C++ o Electron que use el SDK oficial de Trimble) como *fallback* garantizado cuando el parser de ingeniería inversa encuentre geometrías no soportadas.

---

NVIDIA NIM:
(sin respuesta: Client error '410 Gone' for url 'https://integrate.api.nvidia.com/v1/chat/completions'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/410)

---

Groq:
**1. Detección de corrupción silenciosa**  
- **Análisis de outliers**: compara bounding‑box de cada componente con la media/varianza de los demás; si la distancia supera 3 σ o el volumen es > 10 × el promedio, marca como sospechoso.  
- **Consistencia de índices**: verifica que los índices de vértices no referencien fuera del rango, que no haya triángulos degenerados (área ≈ 0) y que las normales no se crucen (normales opuestas en caras adyacentes).  
- **Propiedades topológicas**: cuenta vértices, aristas y caras; si el Euler‑characteristic difiere del esperado para un sólido (V – E + F ≈ 2) indica un fallo de parsing.  
- **Checksum de datos**: si el formato lo permite, valida un hash de cada sección (p. ej. SHA‑256 de los bytes de la geometría) contra el que se esperaba; cualquier discrepancia sugiere corrupción.

**2. Aislamiento de componentes defectuosos**  
- **Try/catch por componente**: encapsula la construcción de cada `Mesh` en un bloque que captura excepciones y, en caso de fallo, reemplaza el mesh por un placeholder (cubo rojo, “error”).  
- **Filtro de bounding‑box**: al calcular la cámara, excluye componentes marcados como outliers; usa el `Box3` de los demás meshes para la vista.  
- **Render de “fallback”**: si un componente está corrupto, muestra un icono o un texto “no se pudo cargar” en su lugar, manteniendo la interacción (orbit, zoom) sobre el resto.

**3. Rendimiento en modelos grandes**  
- **Carga progresiva**: lee el archivo en bloques con `ArrayBuffer.slice` y procesa cada bloque en un `WebWorker`; así el hilo principal sigue respondiendo.  
- **LOD y instancing**: genera versiones simplificadas (por ejemplo, decimación de meshes) y usa `THREE.InstancedMesh` para elementos repetidos (paredes, ventanas).  
- **Culling y frustum**: habilita `frustumCulled` y `renderOrder` para evitar renderizar geometría oculta.  
- **Memoria**: limita el número de vertices activos (p. ej. 2 M) y libera buffers de componentes ya renderizados con `dispose()`.

**4. Decisión de seguir o cambiar de librería**  
- **Frecuencia de bugs**: si aparecen más de 1 bug crítico por cada 10 MB de modelo, el riesgo de regresión es alto.  
- **Tiempo de respuesta**: si el mantenimiento consume > 30 % del tiempo total de desarrollo, vale la pena buscar una alternativa.  
- **Soporte y comunidad**: una librería con más colaboradores y documentación (p. ej. Trimble’s SDK, or `skp-parser` en Rust) reduce la carga de ingeniería inversa.  
- **Coste de migración**: si la nueva librería necesita un backend o dependencias no compatibles con tu stack, el beneficio debe superar el coste de re‑escritura.

**5. Patrones para visores resilientes**  
- **“Fail‑fast, continue”**: cada fase (parse, triangulación, material) debe devolver un objeto de estado (ok/errored) y el visor debe decidir qué mostrar.  
- **Validación continua**: integra pruebas unitarias con modelos de referencia (archivos de prueba con métricas conocidas) y CI que verifique que la salida no cambia inesperadamente.  
- **Fallback a formatos estándar**: si el parser falla, intenta convertir el `.skp` a `.glTF` con una herramienta externa (p. ej. `skp2gltf`) y usar ese como respaldo.  
- **Documentación de “gaps”**: publica una lista de casos conocidos (curvas de Bezier, componentes anidados, materiales sin nombre) para que los usuarios entiendan las limitaciones.  

Con estos mecanismos de detección, aislamiento y optimización, tu visor podrá manejar archivos reales y grandes sin depender de un parser perfecto, y tendrás criterios claros para decidir cuándo es tiempo de migrar.

---

gemma4:e2b:
El desafío que usted enfrenta es un ejemplo clásico de ingeniería de software aplicado a la ingeniería inversa de formatos propietarios: cómo construir un sistema robusto a partir de un código que es inherentemente imperfecto. La clave para la robustez no reside en la perfección del parser, sino en la capacidad del *visor* para gestionar la incertidumbre y aislar los fallos del *parser*.

Para abordar la **corrupción silenciosa y el aislamiento de errores**, se requiere un enfoque de validación de datos cruzada. En lugar de confiar únicamente en la estructura interna de un solo componente, implemente chequeos de consistencia geométrica y topológica entre primitivas adyacentes (por ejemplo, verificando la coherencia de los normales y la continuidad de los bordes) y utilice los *bounding boxes* de las primitivas como métrica de outliers. Esto permite que el render continúe con la mayor parte de la escena mientras se marcan las áreas sospechosas, en lugar de detenerse. Para el escalado a archivos masivos, la estrategia debe pivotar hacia el *streaming* de datos (carga progresiva), el uso de *Web Workers* para desahogar el trabajo pesado de parseo y cálculo de geometría, e implementar técnicas de optimización de renderizado como el *Level of Detail* (LOD) y el *instancing* de vértices en Three.js.

Finalmente, respecto a la estrategia de desarrollo, ante la aparición de fallos críticos como los que ha experimentado, la decisión se reduce a un equilibrio entre fidelidad y tiempo. Si bien parchear el código actual ofrece una solución inmediata, la estrategia más robusta a largo plazo es migrar hacia un enfoque híbrido: mantener el parser de ingeniería inversa como una base para la fidelidad del formato, pero explorar la integración de una capa de validación o un *fallback* utilizando el SDK oficial de Trimble (si es viable) para las partes críticas, o considerar un enfoque donde la integridad de la geometría sea el objetivo principal, no necesariamente la fidelidad exacta del formato propietario. Las mejores prácticas son siempre: validar la salida frente a un conjunto de datos conocidos, y diseñar el sistema para que el error se manifieste como una advertencia, no como una falla total.

---

gemma3:4b:
## Punto de Vista del Panel de IAs

Este es un problema técnico complejo con implicaciones importantes para el futuro de ORA SKP Viewer. Analizamos los hallazgos y ofrecemos las siguientes recomendaciones:

**1. Prioridad: Mitigar la Corrupción Silenciosa y Fallos de Memoria:** Los bugs 1 y 2 son, sin duda, la mayor preocupación. La corrupción silenciosa es particularmente peligrosa, ya que el usuario puede creer que el modelo se está cargando correctamente, cuando en realidad está dañado. La falla de memoria es un problema grave que debe abordarse inmediatamente.  Recomendamos investigar exhaustivamente `EdgeFlagStore` y sus mecanismos de asignación de memoria.  Implementar un sistema de validación de primitivas y geometría, incluyendo chequeos de "manifold" y anomalías de normales, es crucial para detectar la corrupción.

**2. Aislamiento de Primitivas y Renderizado Parcial:**  El aislamiento de primitivas es un enfoque sensato para evitar que un fallo arruine todo el modelo. Explorar la posibilidad de renderizar las partes funcionales del modelo, incluso si hay algunas partes corruptas, puede ofrecer una experiencia más útil al usuario.  Considerar mecanismos para excluir "outliers" del cálculo de la cámara sin ocultarlos completamente.

**3. Optimización de Rendimiento para Modelos Grandes:** Con la escala de archivos arquitectónicos, la optimización del rendimiento es esencial.  Implementar técnicas como la carga progresiva (streaming), Web Workers para la manipulación de la escena, LOD (Levels of Detail) y la instancing de Three.js es fundamental.  La gestión de la memoria en el navegador es clave y hay que establecer límites realistas.

**4. Estrategia de Desarrollo a Largo Plazo:** Dada la juventud de OpenSKP y la aparición temprana de bugs significativos, un enfoque híbrido podría ser la mejor opción.  Esto podría implicar:
    *   **Continuar el desarrollo de OpenSKP:** Aumentar los recursos (si es posible) para solucionar los problemas fundamentales en el parser, especialmente en el manejo de aristas curvas y la asignación de memoria.
    *   **Integrar un SDK alternativo:** Explorar el SDK oficial de Trimble para componentes críticos que son susceptibles a errores en la ingeniería inversa. Esto podría proporcionar mayor estabilidad y precisión.

**5. Resiliencia ante Parsers de Formato Propietario:**  Reconocer que un parser de formato propietario reconstruido por ingeniería inversa inevitablemente tendrá limitaciones.  Implementar mecanismos de "fallback" (respaldo) y validación robusta es vital.  Considerar la posibilidad de construir una capa de abstracción sobre el modelo reconstruido para facilitar futuras actualizaciones y correcciones.

**En resumen, la prioridad es mitigar los bugs existentes, seguido de la implementación de estrategias de optimización del rendimiento y resiliencia, mientras se evalúa la estrategia a largo plazo con un SDK alternativo, considerando la madurez del proyecto.**