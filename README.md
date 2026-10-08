# Física sin errores ocultos — plugin para Claude

> **English summary:** A Claude plugin that solves physics problems in any area (mechanics, circuits, thermodynamics, optics…) while avoiding hidden-assumption errors. It enlarges and describes figures before solving, checks units and limiting cases, and always ends with a short, risk-ordered list of every assumption used, so you can spot a wrong one at a glance. Claude answers in your language.

Un plugin con una skill que hace que Claude resuelva problemas de física de **cualquier área** (mecánica, energía, fluidos, termodinámica, electricidad, circuitos, magnetismo, ondas, óptica, física moderna) con un protocolo pensado para evitar el error más común: **los supuestos silenciosos**.

## El problema que resuelve

La mayoría de los errores en problemas de física no son de cuenta. Son una figura mal leída, un signo de referencia que nunca se declaró, un "sin rozamiento" que el enunciado no decía. Las cuentas pueden estar perfectas y el resultado igual mal, y como el supuesto queda perdido en el medio del texto, encontrarlo cuesta.

Caso real que motivó esta skill: en un sistema de poleas, la cuerda de un bloque estaba atada al **eje** de la polea inferior, y por esa polea pasaba otra cuerda atada al piso. Leída sin ampliar la imagen, se interpretó como la polea móvil típica de los libros. Resultado: 5/8 en lugar de 5/2, presentado con total seguridad.

## Qué hace

1. **Lee el enunciado con cuidado:** qué se pide exactamente, datos con unidades, condiciones escritas e implícitas.
2. **Amplía la figura antes de interpretarla** (incluye un script) y la describe elemento por elemento: cada cuerda, polea, nodo, lente o eje, antes de plantear cualquier ecuación.
3. **Declara el modelo:** sistema de referencia, signos, idealizaciones y valores convencionales (g, sen 53° = 4/5, etc.).
4. **Resuelve marcando cada supuesto** en la ecuación donde se usa: [S1], [S2]…
5. **Verifica:** unidades, orden de magnitud, casos límite, sentido físico.
6. **Cierra siempre con un bloque de Suposiciones**, corto y ordenado por riesgo:

```
## Suposiciones
- S1 ⚠️ Interpretación: la cuerda de A termina en el eje de la polea inferior, no la rodea. Si la rodeara, cambia el factor 2 y el resultado sería 5/8.
- S2 ⚠️ Interpretación: el extremo derecho de la cuerda de B está fijo al piso. Si no, hay que replantear.
- S3 📐 Figura: el ángulo de 53° se mide entre el plano y la horizontal.
- S4 📄 Enunciado: sin rozamiento entre A y el plano; poleas de masa despreciable.
- S5 🔧 Convención: sen 53° = 4/5; cuerdas ideales.
```

| Etiqueta | Significado |
|---|---|
| ⚠️ Interpretación | Lo infirió Claude. **Es lo primero a revisar**, e indica qué cambia si es falsa. |
| 📐 Figura | Se lee con claridad en el dibujo. |
| 📄 Enunciado | Está escrito en el texto. |
| 🔧 Convención | Valor o idealización estándar. |

Además, si cuestionás el resultado, Claude revisa primero las suposiciones ⚠️ y la figura, pero **no cambia la respuesta solo por insistencia**: la cambia ante evidencia nueva e indica cuál suposición era la falsa.

## Instalación

**Desde el directorio de Claude** (cuando esté publicado): buscá "fisica" en Customize y agregalo.

**Manual en claude.ai:** descargá `fisica.zip` desde [Releases](https://github.com/Carlotess/fisica/releases), andá a **Customize > Skills**, tocá **+ > Create skill > Upload a skill** y subí el zip.

**Claude Code:**
```bash
git clone https://github.com/Carlotess/fisica.git
claude --plugin-dir ./fisica
# o solo la skill:
cp -r skills/fisica ~/.claude/skills/
```

**Otros agentes** (Cursor, Codex, Copilot, Gemini CLI…): la carpeta `skills/fisica` sigue el estándar abierto [Agent Skills](https://agentskills.io); copiala donde tu agente busca skills.

## Contenido

```
.claude-plugin/plugin.json        manifiesto del plugin
skills/fisica/SKILL.md            protocolo de resolución
skills/fisica/scripts/ampliar.py  amplía y recorta figuras (requiere Pillow)
skills/fisica/references/errores-comunes.md  trampas típicas por área
```

## Qué ejecuta y qué datos usa

- La skill es principalmente un conjunto de instrucciones (Markdown) que Claude sigue al resolver problemas de física.
- Incluye un único script, `skills/fisica/scripts/ampliar.py`, que Claude ejecuta localmente en su entorno de código para ampliar y recortar la imagen de un problema. Usa solo Python y la librería Pillow.
- El script no hace conexiones de red, no envía datos a ningún servicio externo y no lee archivos fuera de la imagen indicada. Solo guarda la imagen ampliada en el directorio de trabajo.
- No usa conectores, APIs ni credenciales.

## Limitaciones

- El protocolo reduce errores, pero no los elimina: la lectura de figuras de muy baja resolución puede seguir siendo ambigua. Por eso la skill marca esas interpretaciones con ⚠️ para que las revises.
- Por defecto usa convenciones habituales en cursos de física en español (por ejemplo sen 37° = 3/5, sen 53° = 4/5). Si tu curso usa otras, indicáselo a Claude.

## Contribuir

Si encontrás un problema donde la skill igual se equivoca, abrí un issue con el enunciado, la figura y qué suposición falló. Esos casos son los que más ayudan a mejorarla.

## Licencia

MIT
