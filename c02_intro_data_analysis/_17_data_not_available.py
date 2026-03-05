"""
_17_data_not_available.py

GESTIÓN DE DATOS NO DISPONIBLES

.isnull()
genera un DataFrame booleano que refleja el original, donde True indica un valor perdido y
False representa un valor no perdido. Esto proporciona una visión global del panorama de los
datos que faltan en su DataFrame, lo que le permite evaluar rápidamente el alcance de lo que
falta e identificar las columnas o filas que requieren atención.

df['Age'].isnull() aplica la misma lógica a una columna específica, devolviendo una serie
booleana que resalta los valores que faltan dentro de esa columna. Esto le permite centrar
su atención en variables específicas y evaluar si están completas, lo que es importante
para decidir las estrategias de imputación adecuadas.

.dropna()
Elimina las filas que contienen valores perdidos, reduciendo el DataFrame pero asegurando
la integridad de los datos. Este enfoque es adecuado cuando los valores que faltan son
relativamente escasos y su eliminación no afecta significativamente a la representatividad
de los datos. Sin embargo, es importante tener cuidado, ya que la eliminación de filas puede
provocar la pérdida de información valiosa si no se hace con criterio.

.fillna(value)
Sustituye los valores que faltan por un valor especificado (por ejemplo, 0), una técnica de
imputación sencilla adecuada para determinados casos. Esto puede ser útil cuando se tiene
una suposición razonable sobre el valor probable de los datos que faltan o cuando se
quiere evitar descartar filas por completo. Sin embargo, es importante considerar las
implicaciones potenciales de esta imputación en su análisis, ya que podría introducir
sesgos o distorsionar los patrones subyacentes en los datos.

df['Age'].fillna(df['Age'].mean(), inplace=True) es un enfoque más sofisticado, que imputa los
valores que faltan en una columna con su media. El argumento inplace=True modifica el DataFrame
directamente, conservando memoria. Este method suele preferirse cuando se supone que los valores
perdidos se distribuyen aleatoriamente y se desea mantener las propiedades estadísticas
generales de los datos.
"""
