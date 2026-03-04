"""
1. Pandas
Una biblioteca potente y versátil para el análisis de datos en Python es pandas. Es una herramienta esencial
en el arsenal de cualquier científico de datos, equipado con una multitud de funciones para hacer frente a
diversos retos de limpieza de datos. En su núcleo, pandas proporciona estructuras de datos de alto rendimiento
como DataFrames, que ofrecen una forma cómoda e intuitiva de organizar y manipular datos tabulares.

Con pandas, puede filtrar, ordenar, agregar y transformar sus datos sin esfuerzo, lo que facilita su limpieza y
preparación para el análisis. Su sintaxis intuitiva y su amplia funcionalidad lo han convertido en una
herramienta de referencia para los científicos de datos.

2. Numpy
Numpy es una biblioteca fundamental para la computación numérica en Python. Proporciona un sólido soporte
para matrices y arrays, junto con una rica colección de funciones matemáticas optimizadas para
operaciones eficientes con matrices.

3. Scikit-Learn
Scikit-learn también ofrece un valioso conjunto de módulos de preprocesamiento diseñados específicamente
para la limpieza y transformación de datos. Estos módulos proporcionan una serie de funcionalidades,
incluyendo el escalado, la codificación y la imputación, que son pasos esenciales en la preparación
de sus datos para los modelos de aprendizaje automático. Las capacidades de preprocesamiento de Scikit-learn
complementan a Pandas y NumPy, creando un ecosistema completo para la gestión y el análisis de datos.
"""
import numpy as np
import pandas as pd

# Create data dict
data = {
    'price': [10, 150, np.nan, 200, np.nan, 180, 120],
}

# Create dataframe
df = pd.DataFrame(data)
print(df)

# Calculate median
median = df['price'].median()
df['price'].fillna(median, inplace=True)
print(df)
