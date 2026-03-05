"""
_15_cheat_sheet_inspection.py

INSPECCIÓN DE DATAFRAMES

Una vez que tienes tu dataframe creado y listo, pandas proporciona un conjunto de
funciones para explorar y entender su estructura y contenido:

df.head():
Muestra las primeras filas (por defecto 5) para una rápida visión general de la
naturaleza de los datos, incluyendo nombres de columnas, tipos de datos y
una muestra de valores. Es como echar un vistazo al principio de un conjunto de
datos para hacerse una idea de lo que contiene.

df.tail():
De forma similar, muestra las últimas filas (por defecto 5), ayudando a identificar
patrones o anomalías hacia el final. Esto puede ser útil para detectar valores
inesperados o tendencias que requieran una mayor investigación.

df.shape:
Devuelve una tupla que representa las dimensiones del DataFrame (número de filas
y columnas). Esto es crucial para comprender la escala de sus datos y planificar
su estrategia de análisis en consecuencia.

df.info():
Genera un resumen conciso del DataFrame, que incluye los nombres de las columnas,
los tipos de datos (esencial para saber cómo trabajar con cada columna) y la
presencia de valores perdidos. Este resumen proporciona una rápida comprobación
de la salud de sus datos, destacando las áreas potenciales de limpieza o
preprocesamiento.

df.describe(): Calcula las estadísticas descriptivas de las columnas numéricas, ofreciendo
información sobre la distribución de los datos y las tendencias centrales. Esto incluye
métricas como el recuento, la media, la desviación estándar, el mínimo, el máximo y los
cuartiles, que le ayudan a comprender las características de sus datos numéricos.
"""
