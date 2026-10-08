---
name: fisica
description: Protocolo para resolver problemas de física de cualquier área (mecánica, dinámica, estática, energía, fluidos, termodinámica, electricidad, magnetismo, circuitos, ondas, óptica, física moderna) evitando errores de lectura, de modelo y de cuenta, y cerrando siempre con una lista compacta de las suposiciones usadas para que el usuario detecte rápido si alguna es falsa. Usar SIEMPRE que el usuario pida resolver, plantear, revisar o verificar un ejercicio o problema de física, con o sin imagen, aunque no lo pida explícitamente, y cuando invoque /fisica. Incluye el protocolo para leer figuras (poleas, planos, circuitos, diagramas). Usar también cuando el usuario cuestione una resolución de física anterior ("¿estás seguro?", "eso no da", "¿estás viendo bien el dibujo?").
---

# Física: resolver sin errores ocultos

## La idea central

La mayoría de los errores en problemas de física no son de cálculo: son **supuestos silenciosos**. Un dibujo leído según el caso típico del libro, un signo de referencia que nunca se declaró, un "sin rozamiento" que el enunciado no decía, un ángulo medido desde la vertical cuando se tomó desde la horizontal. Las cuentas que siguen pueden ser impecables y el resultado igual estar mal, y como el supuesto quedó disperso dentro del texto, el usuario no tiene forma rápida de encontrarlo.

Por eso este protocolo tiene dos objetivos:

1. **Reducir errores:** leer el problema completo con cuidado antes de plantear.
2. **Hacer visibles los errores que igual ocurran:** todo supuesto queda listado al final en un bloque corto, ordenado por riesgo, donde el usuario lo puede verificar en segundos.

## Protocolo

### 1. Leer el enunciado y extraer datos

Antes de plantear, identificá:

- **Qué se pide exactamente**, incluido el sentido de una relación (m_A/m_B no es m_B/m_A) y las unidades esperadas.
- **Cada dato con su unidad.** Convertí todo a un sistema coherente (normalmente SI) y anotá las conversiones.
- **Condiciones escritas en el texto:** "parte del reposo", "velocidad constante", "equilibrio", "sin rozamiento", "masa despreciable", "instantes después".
- **Condiciones implícitas que tendrías que agregar.** Estas son las que después van al bloque de suposiciones como interpretaciones propias.

### 2. Si hay figura: ampliar y describir antes de resolver

Las figuras de los libros suelen ser chicas, y los detalles decisivos ocupan pocos píxeles. Si la figura ocupa menos de ~600 px de ancho o tiene detalles finos, ampliala antes de interpretarla:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/ampliar.py imagen.png
python3 ${CLAUDE_SKILL_DIR}/scripts/ampliar.py imagen.png --crop x0 y0 x1 y1   # zona específica
```

(Si `${CLAUDE_SKILL_DIR}` no está definido, el script está en `scripts/ampliar.py` junto a este SKILL.md.) Mirá el resultado con `view`. Si alguna zona sigue ambigua (un nudo, un nodo de un circuito, el extremo de una cuerda), hacé un segundo recorte.

Después escribí una sección **"Lectura de la figura"** que describa elemento por elemento lo que se ve:

- **Mecánica:** cada cuerda (dónde empieza, por dónde pasa, dónde termina; "rodea la polea" vs. "está atada al eje"), cada polea (fija o móvil), de qué cuelga o sobre qué apoya cada cuerpo, ángulos y desde dónde se miden.
- **Circuitos:** cada nodo, qué elementos están en serie y cuáles en paralelo, polaridad de las fuentes, sentido de corrientes marcadas, dónde se conectan los instrumentos.
- **Óptica:** posición del objeto, tipo de lente o espejo, distancias y desde dónde se miden.
- **Gráficos:** qué magnitud va en cada eje, unidades, escala, si el origen está en cero.

Si un detalle no se ve con claridad, **no lo completes con el caso típico**: declarálo como supuesto. Un supuesto declarado se corrige en segundos; uno oculto arruina la resolución entera.

Caso real que motivó esto: en un sistema con dos poleas, la cuerda de A estaba atada al **eje** de la polea inferior, y por esa polea pasaba otra cuerda con B en un extremo y el otro atado al piso. Leída sin ampliar, se interpretó como una polea móvil clásica sosteniendo a B. Resultado: 5/8 en lugar de 5/2, presentado con total seguridad.

### 3. Elegir el modelo y las convenciones, y declararlos

- **Sistema de referencia y signos:** ejes, sentido positivo, origen. Mantenelos en toda la resolución.
- **Idealizaciones:** cuerdas inextensibles y sin masa, poleas ideales, partícula puntual, sin resistencia del aire, gas ideal, cables sin resistencia, etc. Usá solo las que el enunciado da o que son estándar en el contexto, y listalas.
- **Valores convencionales:** g = 9,8 o 10 m/s², sen 37° = 3/5 y sen 53° = 4/5, constantes redondeadas. Usá lo que indique el enunciado o el curso; si no lo indica, aclaralo.

Para trampas típicas por área, consultá `references/errores-comunes.md` cuando el problema sea de un área donde no tengas claro qué puede salir mal.

### 4. Plantear y resolver

- Diagrama de cuerpo libre de cada cuerpo (y de cada polea móvil), o el equivalente del área: balance de energía, Kirchhoff por malla y nodo, marcha de rayos.
- Trabajá en forma literal (con letras) lo más posible y reemplazá números al final. Así se ven las dependencias y es más fácil revisar.
- Cuando en medio de la resolución uses un supuesto, marcalo con su número entre corchetes, por ejemplo **[S2]**, para que el usuario conecte la ecuación con el bloque final.

### 5. Verificar antes de entregar

Hacé al menos dos de estos chequeos y mostrá el resultado en una línea cada uno:

- **Unidades:** el resultado tiene las dimensiones correctas.
- **Orden de magnitud:** el número es razonable (una persona no pesa 3 t, un auto no frena en 0,01 m).
- **Casos límite:** qué pasa si θ → 0°, θ → 90°, m → 0, μ → 0. El resultado tiene que comportarse como dicta la intuición.
- **Recorrido numérico:** un valor concreto pasado por todas las ecuaciones de nuevo.
- **Sentido físico:** qué cuerpo debería ser más pesado, hacia dónde debería moverse el sistema, si una energía o tiempo salió negativo.

## Formato de respuesta

```
## Lectura del problema
[datos con unidades, qué se pide; si hay figura, su descripción elemento por elemento]

## Planteo y resolución
[ecuaciones y pasos, con [S1], [S2]... donde se usa cada supuesto]

## Resultado
[resultado destacado, con unidades y en el sentido pedido]

## Chequeo
[2 o más verificaciones, una línea cada una]

## Suposiciones
[bloque obligatorio, ver abajo]
```

Respondé en el idioma del usuario. En problemas muy simples podés condensar secciones, pero **el bloque de Suposiciones va siempre**.

## El bloque de Suposiciones

Es lo último de la respuesta, para que el usuario lo encuentre siempre en el mismo lugar. Su función es que pueda revisar de un vistazo todo lo que no se dedujo con certeza, así que tiene que ser corto y escaneable.

Reglas:

- **Una línea por suposición**, numerada como S1, S2… (los mismos números usados en la resolución).
- **Ordenadas de mayor a menor riesgo**: primero las interpretaciones propias de la figura o del texto, al final las idealizaciones estándar.
- **Cada una con su origen**, con una etiqueta al principio:
  - ⚠️ **Interpretación**: lo inferí yo, el enunciado no lo dice explícitamente o la figura es ambigua. Es lo primero a revisar.
  - 📐 **Figura**: se lee en el dibujo con claridad.
  - 📄 **Enunciado**: está escrito en el texto.
  - 🔧 **Convención**: valor o idealización estándar (g, aproximaciones trigonométricas, cuerda ideal).
- **Cada interpretación (⚠️) indica qué cambiaría si fuera falsa**, en pocas palabras. Eso le permite al usuario saber cuáles importan.
- Las convenciones estándar pueden agruparse en una sola línea al final, para no llenar la lista de obviedades.
- Si no hubo ninguna interpretación propia, decilo explícitamente: "Sin interpretaciones propias: todo surge del enunciado y la figura."

Ejemplo (problema de poleas con plano inclinado):

```
## Suposiciones
- S1 ⚠️ Interpretación: la cuerda de A termina en el eje de la polea inferior, no la rodea. Si la rodeara, cambia el factor 2 y el resultado sería 5/8.
- S2 ⚠️ Interpretación: el extremo derecho de la cuerda de B está fijo al piso (marca de ángulo recto). Si no, la polea inferior no queda en equilibrio y hay que replantear.
- S3 📐 Figura: el ángulo de 53° se mide entre el plano y la horizontal.
- S4 📄 Enunciado: sin rozamiento entre A y el plano; poleas de masa despreciable.
- S5 🔧 Convención: sen 53° = 4/5; cuerdas ideales (inextensibles, sin masa).
```

## Cuando el usuario cuestiona el resultado

Hay dos errores opuestos que evitar.

**Defender sin revisar.** Si el usuario pregunta "¿estás viendo bien el dibujo?" o plantea una objeción que no encaja con tu planteo, primero volvé a revisar las suposiciones marcadas con ⚠️ (y releé la figura ampliada si hay una) antes de defender la física. Una objeción que parece conceptualmente errónea puede estar señalando un supuesto equivocado.

**Cambiar por presión.** Si después de revisar todo se sostiene, mantené el resultado aunque el usuario insista ("¿estás seguro?", "ese no es el resultado del libro"). No inventes otra respuesta para complacer. En cambio:

- Explicá qué revisaste y por qué se sostiene.
- Separá la confianza en la física de la confianza en la lectura del problema.
- Si el libro da otro resultado, verificá primero si es el mismo expresado al revés o con otras unidades, y pedí el valor para identificar la diferencia. Muchas veces la diferencia apunta directo a una suposición del bloque (otro factor 2, seno por coseno, otro valor de g).

Cambiá la respuesta solo ante evidencia nueva: un detalle de la figura que no habías visto, un dato del enunciado, o un error concreto en el planteo. Cuando la cambies, actualizá el bloque de Suposiciones e indicá cuál era la falsa.
