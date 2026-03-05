"""
_10_dataframes.py

Son estructura de datos bidimensional que almacena y organiza datos en filas
y columnas.

Un DataFrame proporciona una forma estructurada e intuitiva de administrar
y manipular su información.

Como cualquier estructura de datos, los DataFrames tienen definidas determinado
tipo de operaciones como:
- Indexing
- Slicing
- Filtering

Es una estructura de datos bidimensional que almacena y organiza datos en filas
y columnas.

Cada columna representa una variable o característica específica, mientras que
cada fila corresponde a una observación o puntos de datos individuales.

En esencia un DataFrame consta de 3 componentes clave:
- Data (values)
- Index (índices)
- Columns (columnas)

1. Data (datos- valores)
Son la información real almacenada dentro del DataFrame. Pueden ser datos numéricos,
textuales, booleanos, o combinaciones de diversos tipos.

2. Index (índice)
Es una estructura independiente que identifica de forma exclusiva cada fila (renglón)
dentro de un DataFrame, lo que permite operaciones eficientes basadas en filas.

3. Columns (columnas)
Las columnas representan las diferentes variables o características dentro de un
conjunto de datos. Cada columna tiene un nombre y tipo de dato a almacenar
asociado.

---------------------------------------------------------------------------------

TIPOS DE OPERACIONES

1. Indexación
Operación que permite acceder a elementos específicos dentro de un DataFrame. Se
puede indexar por medio de etiquetas de filas (row labels), con los métodos loc y
iloc. Esto brinda un control preciso sobre las partes de sus datos con las que desea
trabajar.

2. Slicing
Es similar a la indexación, con la diferencia que este permite seleccionar un rango de
filas o columnas a la vez. Esto es extremadamente útil cuando desea extraer un
subconjunto de sus datos para su análisis o visualización.

3. Filtering
El filtrado le permite seleccionar filas en función de condiciones o criterios
específicos
"""
