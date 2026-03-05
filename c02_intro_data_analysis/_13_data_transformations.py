"""
_13_data_transformations.py

1. merge
En pandas, el merging es la operación que permite combinar dos DataFrames basándose
en columnas (o índices) comunes, de manera muy similar a cómo funciona un JOIN en
SQL. Es la herramienta principal cuando tienes datos relacionados en distintas
tablas y necesitas unirlos en una sola vista. El comportamiento del merge o unión
se define mediante el parámetro how.

2. concat
El concatenamiento en pandas es la operación de unir dos o más objetos (DataFrames o Series)
"pegándolos" a lo largo de un eje, ya sea de forma vertical (uno debajo del otro) o de forma
horizontal (uno al lado del otro).

Para esto, se utiliza la función principal pd.concat(). A diferencia del merge, que busca
coincidencias en los datos, el concatenamiento es más como armar un rompecabezas o
apilar piezas de Lego.

3. sorting
El ordenamiento en pandas es la operación de organizar las filas de un DataFrame o
los elementos de una Serie con base en un criterio específico, ya sea por sus valores
(contenido) o por sus etiquetas (índices).

Es una de las tareas más frecuentes en el análisis de datos para identificar rápidamente
valores máximos, mínimos o tendencias cronológicas. En pandas, las dos funciones principales
para esto son sort_values() y sort_index().

4. group_by
La agrupación en pandas mediante groupby es una de las herramientas más potentes para
el análisis de datos. Su función principal es permitirte examinar tus datos
por categorías, permitiéndote responder preguntas como:
- "¿Cuál es el promedio de ventas por tienda?"
- "¿Cuántos errores hay por cada lenguaje de programación?"

La función groupby sigue el principio de Split-Apply-Combine (Dividir-Aplicar-Combinar).

La estructura básica es: df.groupby('columna_categoria')['columna_a_calcular'].operacion()
Permite agrupar datos basados en columnas y realizar y obtener cálculos sobre ellos.

5. agg
La función .agg() (abreviatura de aggregate) en pandas es una de las herramientas más
potentes y flexibles para el análisis de datos. Su propósito principal es permitirte
aplicar una o más operaciones matemáticas sobre las columnas de un DataFrame,
ya sea de forma global o sobre datos agrupados.
"""
from pprint import pprint

import pandas as pd

from utils import StringFormatter

dfUsers = pd.DataFrame({
    'id': [1, 2, 3],
    'nombre': ['Hugo', 'Paco', 'Luis'],
})

dfLanguages = pd.DataFrame({
    'id': [1, 3, 4],
    'lenguaje': ['Python', 'Java', 'Dart'],
})

# Realizamos el merge por la columna id
print(StringFormatter.make_title('pd.merge(dfUsers, dfLanguages, on="id")'))
dfUserLangs = pd.merge(dfUsers, dfLanguages, on='id', how='inner')
pprint(dfUserLangs)

# Realizamos la concatenación (axis=0 by default), apila verticalmente
print(StringFormatter.make_title('pd.concat([dfUsers, dfLanguages], axis=0)'))
dfConcatUsersLangsVertical = pd.concat([dfUsers, dfLanguages], axis=0)
pprint(dfConcatUsersLangsVertical)

# Realizamos la concatenación (axis=1), apila horizontalmente
print(StringFormatter.make_title('pd.concat([dfUsers, dfLanguages], axis=1)'))
dfConcatUsersLangsHorizontal = pd.concat([dfUsers, dfLanguages], axis=1)
pprint(dfConcatUsersLangsHorizontal)

# Create a new data frame
dfProducts = df = pd.DataFrame({
    'Producto': ['Laptop', 'Mouse', 'Monitor', 'Teclado'],
    'Precio': [1200, 25, 300, 75],
    'Stock': [5, 50, 10, 50]
})

# Sort products by price
print(StringFormatter.make_title('pd.sort_values(by="Precio")'))
dfSortedByPrice = dfProducts.sort_values(by='Precio')
pprint(dfSortedByPrice)

# Sort products by price
print(StringFormatter.make_title('pd.sort_values(by="Precio")'))
dfSortedByPrice = dfProducts.sort_values(by='Precio', ascending=False)
pprint(dfSortedByPrice)

# Group by example
print(StringFormatter.make_title('df.groupby()'))
dfData = pd.DataFrame({
    'Language': ['Python', 'Swift', 'Python', 'Dart', 'Swift', 'Python'],
    'Lines': [150, 200, 300, 100, 250, 0],
    'Complexity': [5, 8, 7, 4, 9, 2],
})
pprint(dfData.groupby('Language')['Lines'].sum())
