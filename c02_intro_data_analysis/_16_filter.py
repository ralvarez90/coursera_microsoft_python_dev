"""
_16_filter.py

FILTRO Y SELECCIÓN DE DATOS

Pandas tiene la capacidad de filtrar datos con precisión, lo que le permite centrar su
análisis en subconjuntos específicos de interés. Esta capacidad es fundamental para extraer
información significativa de conjuntos de datos grandes y complejos. Pandas proporciona una
sintaxis intuitiva para la selección de columnas.

1. Selección de Una Columna
La selección de una sola columna recupera una sola columna por su nombre utilizando corchetes.
El resultado es una Serie, un array unidimensional etiquetado capaz de contener cualquier tipo
de datos. Los objetos Series heredan muchas de las funcionalidades de DataFrame, permitiendo
una mayor manipulación y análisis de una sola columna.

2. Selección de varias columnas
La selección de varias columnas extrae varias columnas pasando una lista de nombres de
columnas entre corchetes dobles. El resultado es un nuevo DataFrame que contiene solo las
columnas seleccionadas, creando así un subconjunto específico de los datos originales. Esto
es útil cuando se quiere trabajar con un grupo específico de variables o características.

3. Función .loc y .iloc
df.loc[] emplea indexación basada en etiquetas, lo que le permite seleccionar filas
basándose en sus etiquetas de índice, que pueden ser cadenas, enteros o incluso fechas.
Esto resulta especialmente útil cuando el DataFrame tiene etiquetas de índice significativas
que desea utilizar para la selección. Se emplea iloc cuando se usa un índice entero.

4. Filtrado de Datos
El filtrado de datos se realiza con indexación booleana y sirve como una potente
herramienta para filtrar filas basándose en condiciones específicas. Consiste en
crear una máscara booleana (una serie de valores Verdadero/Falso) aplicando operadores
de comparación o condiciones lógicas a una o varias columnas. Esta máscara se utiliza
entonces para seleccionar solo las filas en las que la condición se evalúa como Verdadero,
filtrando eficazmente el DataFrame en función de sus criterios. Esto permite extraer
subconjuntos de datos que cumplen requisitos específicos, lo que facilita el análisis
específico.

5. Consulta de Datos (query)
La consulta de datos es para escenarios de filtrado más complejos que implican múltiples
condiciones o una lógica intrincada. El method query ofrece una sintaxis similar a SQL.
Esto mejora la legibilidad y la expresividad, ya que permite construir consultas que se
asemejan a expresiones de lenguaje natural, lo que hace que el código sea más intuitivo
y fácil de mantener. Resulta especialmente ventajoso cuando se trabaja con criterios de
filtrado complejos que serían engorrosos de expresar utilizando la indexación booleana
tradicional.
"""
from utils import UtilConsole

lessonExamples: str = """
1. Selección de una columna
df['Age']

2. Selección de varias columnas
df[['Name', 'Age']]

3. Uso de loc
df.loc[0]
df.loc['A']
df.iloc[2]

4. Filtrado de datos
df[df['Age'] > 25]

5. Filtrado por consulta (query)
df.query('Age > 25 and Name == "Bob"')
"""
print(lessonExamples)

# End application
UtilConsole.system_pause()
