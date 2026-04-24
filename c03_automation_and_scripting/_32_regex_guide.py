"""
GUÍA DE REGEX

Son secuencias de caracteres que define un patrón de búsqueda. Permiten
1. Buscar información específica
2. Validar Datos
3. Limpiar y transformar datos
4. Sustitución de texto

Carácteres Literales
Son las forma más sencilla de patrones. Coinciden exactamente con ellos
mismos. Por ejemplo, la expresión regular cat coincidiría con la cadena
"cat", pero no con "Cat" o "catalog".

Metacharacters
Son caracteres especiales que tienen un significado más allá de su interpretación literal.
Algunos metacharacters comunes son:

. (punto): Matches any single character except a newline.

* (asterisco): Coincide con cero o más apariciones del elemento precedente.

+ (más): Coincide con uno o más elementos del elemento anterior.

? (signo de interrogación): Coincide con cero o una ocurrencia del elemento precedente.

[] (clase de caracteres): Coincide con cualquier carácter entre paréntesis. Por ejemplo,
[aeiou] coincide con cualquier vocal.

^ (signo de intercalación): Cuando se utiliza dentro de una clase de caracteres, niega
la clase. Por ejemplo, [^aeiou] coincide con cualquier carácter que no sea una vocal.

Cuantificadores: Especifican el número de veces que debe aparecer un elemento. Los
cuantificadores más comunes son *, + y ?, como ya se ha mencionado. También puede
utilizar las llaves {} para especificar un rango más preciso. Por ejemplo, a{2,4}
coincide con "aa", "aaa" o "aaaa".

Anclas
Las anclas coinciden con el inicio (^) o el final ($) de una cadena. Si se
utilizan con el indicador re.MULTILINE, también coinciden con el principio o el final
de cada línea de una cadena multilínea. Las anclas más comunes son:
^ (signo de intercalación): Coincide con el inicio de una línea.
$ (símbolo del dólar): Coincide con el final de una línea.

Grupos
Grupos: Permiten tratar varios caracteres como una sola unidad. Puede utilizar
paréntesis () para crear grupos. Por ejemplo, (ab)+ coincide con una o más
repeticiones de "ab".

------------------------------------------------------------------------------------------------------------------------
Una vez que haya extraído los datos utilizando expresiones regulares u otras
técnicas, a menudo necesitará limpiarlos y transformarlos antes de analizarlos.
Entre las tareas más comunes se incluyen:
1. Quitar Duplicados
2. Rellanar valores que faltan
3. Normalizar formatos
"""
import re


def extractEmails(txt: str) -> list[str]:
    pattern: str = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, txt)


text = 'Please contact me at john.doe@example.com or jane.doe@company.org for more information.'
emails = extractEmails(text)
if emails:
    for email in emails:
        print(email)
else:
    print(f'Emails not found!')
