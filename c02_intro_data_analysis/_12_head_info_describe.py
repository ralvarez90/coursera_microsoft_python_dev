"""
_12_head_info_describe.py

DIMENSIONALIDAD
En Pandas, la dimensionalidad se refiere a la estructura y los ejes sobre
los cuales se organizan los datos. Dependiendo de cuántos "niveles" de
información necesites cruzar, utilizarás una estructura u otra.

1D - Series
2D - DataFrames
ND - MultiIndex
----------------------------------------------------------------------------

Propiedad shape
Devuelve una tupla indicando las dimensiones de un conjunto de datos.

Method .head
Devuelve los primeros elementos de un conjunto de datos. Se emplea como herramienta
exploratoria.

Method .info
Su propósito es proporcionarte una "radiografía" instantánea del estado y la estructura
de tu DataFrame.

Method .describe
Cuando aplicas .describe() sobre un DataFrame, Pandas calcula automáticamente ocho
estadísticos para cada columna numérica:
- count: número de valores no nulos
- mean: promedio o media aritmética
- std: desviación estándar (qué tan dispersos están los datos)
- min: valor mínimo encontrado
- max: valor máximo encontrado
- 25%: Primer cuartil
- 50%: Segundo cuartil (mediana, valor central), indica qué tan dispersos están
       los datos con respecto a su media (promedio)
- 75% Tercer cuartil
"""
from pprint import pprint

import pandas as pd

from utils import StringFormatter

# CSV Filepath
IRIS_FILE_PATH: str = 'datacsv/iris.csv'
CARS_FILE_PATH: str = 'datacsv/cars.csv'

# Get dataframe from the csv
irisDataSet = pd.read_csv(IRIS_FILE_PATH)

# Head function example
print(StringFormatter.make_title('dataSet.head()'))
pprint(irisDataSet.head())
print()

# Info function example
print(StringFormatter.make_title('dataSet.info()'))
irisDataSet.info()
print()

# Describe function example
print(StringFormatter.make_title('dataSet.describe()'))
pprint(irisDataSet.describe())
print()

# Get dataframe from the cvs
carsDataSet = pd.read_csv(CARS_FILE_PATH)

# head function example
print(StringFormatter.make_title('carsDataSet.head()'))
pprint(carsDataSet.head())
print()

# Info function example
print(StringFormatter.make_title('carsDataSet.info()'))
carsDataSet.info()
