"""
CASOS DE USO

1. Validaciones de entradas de usuario
Cuando se trata de interfaces de usuario y formulario web, garantizar la integridad de los datos
es primordial. Las expresiones regulares proporcionan un mecanismo robusto para validar la entrada
de datos del usuario, garantizando que se adhiere a formatos específicos.

2. Análisis de Fechas y Horas
Las representaciones textuales de fechas y horas pueden variar mucho, lo que dificulta su
procesamiento y análisis. El regex ofrece una solución al permitir extraer estos elementos
temporales del texto y convertirlos a un formato estandarizado. Esta estandarización
allana el camino para realizar comparaciones, cálculos y visualizaciones sin problemas,
lo que le permite obtener información significativa a partir de datos temporales.

3. Análisis de Sentimientos
En la era de las redes sociales y los comentarios en línea, medir el sentimiento del
público es una tarea valiosa. Las expresiones regulares pueden ayudar en este proceso
identificando palabras clave o frases en los datos de texto que indiquen un sentimiento
positivo o negativo. Al aplicar patrones regex a las publicaciones en redes sociales, a
las reseñas de productos o a los comentarios de los clientes, se puede obtener una
comprensión cuantitativa de la opinión pública, lo que ayuda en las estrategias de marketing,
el desarrollo de productos y la gestión de la reputación de la marca.
"""
import re


def validate_email(email: str) -> bool:
    pattern: str = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return bool(re.match(pattern, email))
