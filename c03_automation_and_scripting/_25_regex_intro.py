"""
EXPRESIONES REGULARES

Proporcionan una forma concisa y flexible de buscar, localizar y modificar texto basándose en
patrones específicos y no en secuencias de caracteres fijas. Piense en las expresiones regulares
como un lenguaje especializado para describir patrones dentro de un texto.

En esencia, las expresiones regulares son secuencias de caracteres que definen un patrón de
búsqueda. Estos patrones pueden ser tan simples como un solo carácter o tan complejos como
una combinación de caracteres, cuantificadores y símbolos especiales.

Las expresiones regulares son como un conjunto de instrucciones o un código que describe el patrón
del texto que está buscando.

Las regex se componen o se pueden componer de los siguientes elementos:

1. Caracteres
Son los elementos básicos, las letras, números o símbolos que componen el texto. Si busca la palabra
"gato", utilizará los caracteres "g", "a", "t" y "o".

2. Metacharacters
Son caracteres especiales que actúan como comodines o instrucciones. Por ejemplo, el
metacharacter punto (.) El punto (.) coincide con cualquier carácter excepto con una
nueva línea. Para incluir nuevas líneas, utilice la opción re.DOTALL de Python.

3. Cuantificadores
Indican cuántas veces debe aparecer un carácter o grupo de caracteres. El asterisk (*) significa
"cero o más veces". ab* coincide con a seguido de cero o más b, por lo que coincide con a, ab,
abb, etc., pero no coincide con a solo sin la b".

4. Clases de Caracteres
Permiten definir un conjunto de caracteres posibles. Por ejemplo, [aeiou] coincide con cualquier
vocal (a, e, i, o, u). También puede definir rangos entre paréntesis, como [a-z] para todas las
letras minúsculas, o negar el conjunto con [^aeiou] para que coincida con cualquier carácter que
no sea una vocal.

5. Anclas
Le ayudan a especificar la posición de la coincidencia. El signo de intercalación (^) coincide con el
principio de una línea y el signo de dólar ($) con el final.

------------------------------------------------------------------------------------------------------------------------

EJEMPLOS DE USO

1. Validación de correos
2. Extracción de números de teléfono
3. Análisis de logs
4. Limpieza de datos
"""
