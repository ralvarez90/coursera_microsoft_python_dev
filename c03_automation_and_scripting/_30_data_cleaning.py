"""
LIMPIEZA DE DATOS

La limpieza y transformación de datos es el proceso de arreglar o mejorar los datos en bruto
para hacerlos adecuados para el análisis.

1. Tratamiento de valores faltantes
El mejor enfoque para gestionar los valores perdidos depende del contexto específico y de la
naturaleza de los mismos.

Si los valores que faltan son pocos y están dispersos aleatoriamente por el conjunto de datos,
una solución razonable puede ser eliminar las filas o columnas correspondientes. Sin embargo,
si los datos que faltan son más sustanciales o tienen un patrón, puede plantearse la imputación.

Se trata de sustituir los valores que faltan por valores estimados basados en métodos estadísticos
como la imputación de la media, la mediana o la moda, o incluso técnicas más sofisticadas como la
imputación por regresión o los modelos de aprendizaje automático.

En algunos casos, frecuentemente cuando los valores que faltan tienen un significado en sí mismos
(como las no respuestas en una encuesta), puede ser mejor conservar los valores que faltan tal y
como están.

2. Quitar Duplicados
Los registros duplicados puedes distorsionar su análisis y llevar a conclusiones inexactas.
Identificar y eliminar estos duplicados es esencial para mantener la integridad de los datos.
La biblioteca Pandas de Python ofrece funciones prácticas como duplicated() y drop_duplicates()
que simplifican esta tarea, facilitando la localización y eliminación de entradas duplicadas.

3. Corrección de Datos Incoherentes
Los formatos y valores incoherentes de los datos pueden obstaculizar el análisis. Las fechas
pueden representarse en distintos formatos ('AAAA-MM-DD' o 'MM/DD/AAAA'), o las variables categóricas
pueden contener errores tipográficos o variaciones ortográficas. Estandarizar estos formatos y corregir
las incoherencias es crucial para garantizar un proceso de análisis preciso y sin problemas.

4. Valores Atípicos
Los valores atípicos, aquellos valores extremos que se desvían significativamente del resto
de los datos, pueden representar anomalías genuinas o errores. Técnicas como la puntuación Z o
el rango intercuartil (IQR) pueden ayudarle a identificar posibles valores atípicos.

Una vez identificados, puede eliminarlos, transformarlos mediante técnicas como la
winsorización o la limitación, o incluso conservarlos, en función del contexto de su
análisis y de sus objetivos específicos.

5. Conversión de Tipos de Datos
Los datos del mundo real a menudo llegan en una mezcla de tipos de datos (números,
texto, fechas, etc.). Convertir estos datos a los tipos adecuados es esencial. Es como asegurarse
de que todas las piezas de un puzzle encajan correctamente. Algunos algoritmos u operaciones solo
pueden funcionar con tipos de datos específicos, por lo que garantizar la coherencia es clave.

La biblioteca Pandas de Python viene al rescate en este caso, ofreciendo funciones como astype()
y to_numeric() que hacen que la conversión de tipos de datos sea pan comido.

6. Ingeniería de Características
Ingeniería de características es DONDE ocurre la magia Consiste en crear nuevas funciones o
transformar las existentes para descubrir patrones ocultos y mejorar el rendimiento de los
modelos de aprendizaje automático. Es como añadir el condimento perfecto a un plato
para realzar su sabor.

Una técnica común es la creación de "variables ficticias", que convierten datos categóricos
(como colores o categorías) en representaciones numéricas que los modelos de aprendizaje automático
pueden entender. Otro aspecto importante es el escalado y la normalización, que garantizan que
todas las características numéricas estén en igualdad de condiciones, evitando que una sola
característica domine el proceso de aprendizaje del modelo. La agregación también es útil,
ya que permite combinar datos de distintos niveles, como calcular medias diarias o mensuales a
partir de datos horarios.

7. Codificación de Datos
Muchos algoritmos de Aprendizaje automático prefieren trabajar con números en lugar de categorías.
La codificación de datos es el proceso de transformar variables categóricas en representaciones
numéricas que estos algoritmos puedan digerir. Es como traducir un idioma extranjero a una lengua
común que todos entiendan. Entre las técnicas de codificación más populares se encuentran la
codificación one-hot, la codificación de etiquetas y la codificación ordinal, cada una con sus
propios puntos fuertes y casos de uso.
"""
import pandas as pd


def drop_duplicates_example():
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Alice'],
        'age': [25, 30, 28, 25],
    }

    df = pd.DataFrame(data)
    print(f'df\n{df}\n')

    # Identify duplicates
    duplicated = df.duplicated()
    print(f'df.duplicated()\n{duplicated}\n')
    print(f'df[duplicated]\n{df[duplicated]}\n')

    # Drop duplicates
    df_clean = df.drop_duplicates()
    print(f'df_clean\n{df_clean}\n')


def inconsistent_data_example():
    data = {
        'date': ['2023-12-31', '12/30/2023', '2023-01-01', '01/02/2023'],
        'category': ['Electronics', 'electronics', 'ELECTRONICS', 'Electronic'],
    }

    df = pd.DataFrame(data)

    # Standardize date format
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d', errors='coerce')
    df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y', errors='coerce')
    df['date'] = df['date'].fillna(pd.to_datetime(df['date'], format='%Y-%m-%d'))

    # Standardize categorial values
    df['category'] = df['category'].str.lower()
    print(f'df\n{df}\n')


def outliers_example():
    pass


if __name__ == '__main__':
    drop_duplicates_example()
    print('-' * 64)

    inconsistent_data_example()
    print('-' * 64)

    outliers_example()
    print('-' * 64)
