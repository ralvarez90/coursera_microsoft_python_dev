"""
_11_indexing.py

La funcionalidad de pandas incluye un sistema de indexación, que permite localizar y recuperar datos dentro
de DataFrames utilizando muchos métodos.

La indexación de Pandas es el sistema de catalogación de DataFrames, que le permite localizar con rapidez
y precisión los datos que necesita.

Una indexación eficiente ahorra tiempo y permite complejas manipulaciones y transformaciones de datos. Al
proporcionar acceso directo a subconjuntos específicos de datos, la indexación le permite cortar, dividir
y remodelar sus DataFrames para extraer información significativa y tomar decisiones informadas.


"""
from pprint import pprint

import pandas as pd

from utils import UtilConsole, StringFormatter

lesson_content: str = '''
MÉTODOS DE INDEXACIÓN

Dos de los métodos de indexación más comunes en pandas son:
- método .loc
- método .iloc

Método loc
El método .loc está basado en etiquetas, lo que significa que utiliza etiquetas de 
fila y columna para acceder a los datos.

Método iloc
El método .loc está basado en índices, lo que significa que se utilizan índices de
filas y columnas para acceder a los datos.

Indexación Booleana
La indexación booleana es una de las técnicas más potentes en Pandas. Consiste en 
filtrar datos de un DataFrame o Serie utilizando una "máscara" de valores verdaderos 
o falsos (True/False).

En lugar de seleccionar filas por su nombre o posición, las seleccionas porque cumplen
una condición lógica.
 
La indexación booleana es increíblemente potente porque permite combinar varias condiciones 
mediante operadores lógicos como & (y), | (o) y ~ (no).

Métodos .at y .iat
Su único propósito es acceder o modificar un único valor (un escalar) en una celda 
específica.

Indexación Multilevel (Indexación Jerárquica)
La indexación multilevel (también conocida como Hierarchical Indexing o MultiIndex) es una 
de las funciones más avanzadas de Pandas. Te permite trabajar con datos de dimensiones 
superiores (3D, 4D, etc.) dentro de una estructura bidimensional (un DataFrame) mediante 
el uso de varios "niveles" de índices en una fila o columna.

Método query
El método .query() de Pandas es una forma elegante y extremadamente legible de filtrar 
datos utilizando una cadena de texto (string) con una sintaxis muy similar a la de 
SQL o al lenguaje natural.

Es la alternativa "limpia" a la indexación booleana tradicional, ideal para cuando 
tienes condiciones largas y complejas que de otro modo llenarían tu código de corchetes 
y paréntesis.

Gestión de Valores Faltantes
Gestione los datos que faltan: Los valores perdidos (NaN) pueden crear problemas en tus 
operaciones de indexación. Utilice métodos como .fillna() o .dropna() para manejarlos 
adecuadamente, garantizando la precisión y fiabilidad de su análisis. El tratamiento 
adecuado de los datos que faltan es crucial para evitar errores inesperados y garantizar la 
validez de sus resultados.
'''

# Console.show_lesson(lesson_content)

# Get data dictionary
data = {
    'Product': ['Monitor', 'Teclado', 'Ratón', 'Laptop', 'Cable HDMI'],
    'Price': [250, 45, 25, 1200, 150],
    'Stock': [10, 50, 100, 5, 200],
}

# Create a dataframe from a dictionary
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

# Show Original DataFrame
print(StringFormatter.make_title('DataFrame Original'))
print(df, end='\n' * 2)

# Show an example with loc
print(StringFormatter.make_title('Example With "loc" Method'))
print(f'df.loc["b", "Price"]: ${df.loc['b', 'Price']:,.2f}\n')

# Inclusive slicing: from 'b' to 'd'
print(f'df.loc["b":"d"]:\n {df.loc['b':'d']}\n')

# Show an example with iloc
print(StringFormatter.make_title('Example with "iloc" Method'))
ilocRange = df.iloc[1, 1]
print(f'1. Price of keyboard: {ilocRange}\n')

# Use boolean indexing
print(StringFormatter.make_title('Example with "Boolean Indexing"'))
result = df[df['Price'] > 100]
print(f'df[df["Price"] > 100]:\n{result}')

# End application
UtilConsole.system_pause()
