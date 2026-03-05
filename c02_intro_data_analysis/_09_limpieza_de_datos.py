"""
_09_limpieza_de_datos.py

LIMPIEZA DE DATOS

Los datos en bruto rara vez son perfectos; a menudo están desordenados, incompletos y
plagados de incoherencias. La limpieza de datos, también conocida como "data wrangling" o
"data munging", es el proceso crítico de transformar estos datos en bruto en un formato
limpio, estructurado y utilizable.

Esta transformación también implica garantizar que el conjunto de datos tenga encabezados
claros, coherentes e informativos para cada columna, lo que facilita la comprensión del
significado de los datos.

Este proceso es la base sobre la que se construyen todos los análisis, modelos y
toma de decisiones posteriores. Datos limpios garantizan la precisión de sus análisis,
la fiabilidad de sus modelos y la solidez de sus conclusiones.

1. Valores Perdidos
Los valores que faltan son como las piezas que faltan en un rompecabezas: crean lagunas
que impiden obtener una imagen completa. Pueden deberse a diversas causas, como errores
en la introducción de datos, fallos en los equipos o la falta de disponibilidad de
determinada información. Si no se abordan, los valores que faltan pueden sesgar el análisis
y llevar a conclusiones inexactas.

2. Valores Atípicos
Los valores atípicos son puntos de datos que se desvían significativamente del resto
del conjunto de datos. Aunque a veces los valores atípicos pueden representar
auténticas anomalías o fenómenos interesantes, también pueden distorsionar
las medidas estadísticas y dar lugar a resultados engañosos.

3. Inconsistencias
Datos incoherentes crean confusión y dificultan el progreso. Las incoherencias pueden deberse
a diversas causas, como errores en la introducción de datos, cambios en los métodos de
recopilación de datos o fusión de datos de distintas fuentes. Pueden dar lugar a errores en
el análisis y socavar la fiabilidad de las conclusiones.

Los encabezados incoherentes son un tipo común de incoherencia. Por ejemplo, diferentes
conjuntos de datos pueden utilizar nombres ligeramente diferentes para la misma columna
(por ejemplo, "ID de cliente" frente a "ID_cliente"), o tener variaciones en las
mayúsculas o el espaciado. Estas incoherencias pueden dificultar la combinación o el análisis
de datos procedentes de distintas fuentes.

-------------------------------------------------------------------------------------------------
"""
from utils import UtilConsole

lesson_content: str = '''
ESTRATEGIAS DE LIMPIEZA Y PREPARACIÓN DE DATOS

1. ELIMINAR VALORES FALTANTES
Aunque un enfoque sencillo para tratar los datos que faltan consiste en eliminar filas o 
columnas enteras que contienen estos vacíos, esta estrategia conlleva el riesgo significativo 
de descartar información valiosa. 

Esta pérdida puede ser especialmente perjudicial cuando los datos que faltan no son aleatorios, 
es decir, cuando existe una razón subyacente por la que faltan determinados valores. En tales casos, 
la eliminación de datos puede introducir un sesgo en el análisis, ya que los datos restantes pueden 
dejar de ser representativos del conjunto de datos original. En consecuencia, lo que parece una 
solución sencilla puede sesgar inadvertidamente los resultados y debilitar las conclusiones 
extraídas del análisis.

2. IMPUTAR VALORES PERDIDOS
El verbo imputar, que a menudo se confunde con "introducir", significa específicamente asignar o 
sustituir valores para los puntos de datos que faltan, un proceso al que se refiere el sustantivo 
imputación. En lugar de limitarse a "introducir" la información existente, la imputación 
implica el empleo de diversas técnicas, como la imputación de la media, la mediana o la moda, 
para rellenar estratégicamente estas lagunas y crear un conjunto de datos más completo para el 
análisis. 

Por tanto, mientras que "introducir" se refiere a introducir los datos recopilados, "imputar" 
e "imputación" describen el acto y los métodos utilizados para estimar y sustituir de forma 
inteligente los valores que faltan.

Otra estrategia consiste en imputar los valores que faltan utilizando métodos estadísticos. La 
imputación de la media, la mediana o la moda consiste en sustituir los valores que faltan por 
la media, la mediana o la moda de los datos disponibles, respectivamente. Este método es sencillo, 
pero puede no ser adecuado para todas las situaciones, especialmente si los valores que 
faltan no son aleatorios.

También pueden utilizarse técnicas más avanzadas, como la imputación por regresión o 
la imputación múltiple. La imputación por regresión consiste en predecir los valores que 
faltan basándose en otras variables del conjunto de datos, mientras que la imputación múltiple 
crea múltiples imputaciones plausibles para cada valor que falta, teniendo en cuenta la incertidumbre 
asociada al proceso de imputación. 

La elección del método depende de la naturaleza de los datos, del análisis específico que se 
vaya a realizar y del nivel de sofisticación requerido.

3. TRATAMIENTO DE VALORES ATÍPICOS
La forma adecuada de tratar los valores atípicos depende de su naturaleza y del contexto de su análisis.
Es crucial evaluar cuidadosamente los valores atípicos antes de decidir qué hacer, ya que pueden representar 
anomalías genuinas o información valiosa. En algunos casos, puede estar justificado eliminar los valores 
atípicos, sobre todo si se deben a errores o representan casos extremos e irrelevantes. 

Sin embargo, es esencial actuar con cautela al eliminar los valores atípicos, ya que a veces pueden 
proporcionar información valiosa o indicar patrones subyacentes en los datos.

También se pueden emplear técnicas como el "capping" para limitar los valores extremos a un umbral 
determinado y evitar que influyan indebidamente en el análisis. Otro enfoque consiste en utilizar 
métodos estadísticos robustos que sean menos sensibles a los valores atípicos, como la mediana y 
el rango intercuartílico. Además, en contextos de Aprendizaje automático, puede aprovechar 
algoritmos robustos como RobustScaler, que están diseñados para manejar los valores atípicos 
con eficacia. La elección de la técnica depende de las características específicas de sus datos y 
de los objetivos de su análisis.

4. RESOLVER INCOHERENCIAS
Para resolver las incoherencias es necesario examinar detenidamente los datos e identificar sus 
causas. Esto puede implicar la normalización de los formatos de datos, la corrección de errores 
o la conciliación de información contradictoria. Se pueden implementar reglas y comprobaciones 
de validación de datos para evitar que las incoherencias se cuelen en los datos. 

Para resolver las incoherencias es necesario examinar detenidamente los datos e identificar 
sus causas. Esto puede implicar la normalización de los formatos de datos, la corrección de errores 
o la conciliación de información contradictoria. Se pueden implementar reglas y comprobaciones de 
validación de datos para evitar que las incoherencias se cuelen en los datos. 

-----------------------------------------------------------------------------------------------------

ESCENARIOS REALES

1. Datos de compra de clientes con valores perdidos: Imagine que está analizando datos de 
compras de clientes, pero faltan las edades de algunos de ellos. Podría imputar las edades 
que faltan utilizando la edad media de los clientes con patrones de compra similares. 

Este enfoque aprovecha la información disponible para hacer conjeturas sobre los valores que 
faltan, preservando así la integridad de su análisis.

2. Datos de temperatura con valores atípicos: Supongamos que está analizando datos de 
temperatura y observa algunos valores extremadamente altos que parecen fuera de lugar. 
Estos valores podrían deberse a fallos o errores del sensor. Podría optar por eliminar 
estos valores atípicos o sustituirlos por valores más plausibles basados en puntos de 
datos circundantes o medias históricas. De este modo se asegura de que su análisis no 
esté sesgado por datos erróneos o irrelevantes.

3. Datos de empleados con incoherencias: Supongamos que está trabajando con datos de 
empleados y observa que algunos nombres de empleados se introducen en formatos diferentes 
(por ejemplo, "John Doe" frente a "Doe, John"). Tendría que estandarizar el formato para 
garantizar la coherencia. Esto podría implicar analizar los nombres y reorganizar 
los componentes en un formato coherente. Esto facilita la agrupación, el filtrado y 
el análisis de los datos en función de los nombres de los empleados.
'''
UtilConsole.show_lesson(lesson_content)
