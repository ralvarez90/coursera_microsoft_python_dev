"""
REGEX PARA LA EXTRACCIÓN DE DATOS

Se recomienda usar regex cuando, maneje texto desestructurado, requiera coincidir con
patrones específicos o trabajar con grandes conjuntos de datos.

Con expresiones regulares, puede crear patrones que coincidan con precisión con las
etiquetas y atributos HTML donde se encuentran los datos de los precios.
"""
import re

some_text: str = 'El gato negro y el gato blanco saltaron la valla.'

# 1. Búsqueda literal
cat_pattern: str = r'gato'
result: re.Match[str] | None = re.search(cat_pattern, some_text)
if result:
    print(result.group())

# 2. Uso de comodín, (representa cualquier carácter excepto el salto de línea)
cat_pattern: str = r'gato .'
result: list = re.findall(cat_pattern, some_text)
if result:
    print(result)


def validate_email(email: str) -> bool:
    pattern: str = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email.strip()))


def validate_phone(phone: str) -> bool:
    pattern: str = r'^\+?1?\d{9,15}$'
    return bool(re.match(pattern, phone))
