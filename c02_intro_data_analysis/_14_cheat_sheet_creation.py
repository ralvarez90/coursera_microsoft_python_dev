"""
_14_cheat_sheet_creation.py

CREACIÓN DE DATAFRAMES

Pandas ofrece diversas formas de crear DataFrames, acomodando varias
fuentes de datos. Estas fuentes pueden provenir de diccionarios, listas
de listas y Archivos CSV.

Empleamos la función pd.read_csv para leer datos a partir de un archivo
CSV y obtener un dataframe.

Pandas también ofrece funciones como read_excel, read_json y read_sql para
importar datos de otros formatos populares.
"""

from pprint import pprint

import pandas as pd

from utils import StringFormatter

# Raw dictionary data
dataDict = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 28],
}

# Generate dataframe from data dict
print(StringFormatter.make_title('pd.DataFrame(dataDict)'))
dataDF = pd.DataFrame(dataDict)
pprint(dataDF)

# Raw data list
dataList = [
    ['Alice', 25],
    ['Bob', 30],
    ['Charlie', 28],
]

# Generate dataframe from data list
print(StringFormatter.make_title('pd.DataFrame(dataList)'))
dataDF = pd.DataFrame(dataList, columns=['Name', 'Age'])
pprint(dataDF)
