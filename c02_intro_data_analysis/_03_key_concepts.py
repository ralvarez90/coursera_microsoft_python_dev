"""
_03_key_concepts.py
"""
from utils import UtilConsole

# Lesson 1. Population definition.
lesson_population: str = '''
1. POBLACIÓN
Engloba a todos los individuos, objetos o entidades que comparten las características que pretende estudiar.
'''
UtilConsole.show_lesson(lesson_population)

# Lesson 2. Sample definition.
lesson_sample: str = '''
2. MUESTRA
Una muestra es un subconjunto cuidadosamente seleccionado de la población que actúa como su representante.
Permiten realizar investigaciones y análisis dentro de unos límites factibles.
'''
UtilConsole.show_lesson(lesson_sample)

# Lesson 3. Variables definition
lesson_variables: str = '''
3. VARIABLES
Son los atributos que observamos y medimos a partir de muestras. Son la matería prima para nuestras
investigaciones.

Como ejemplo de variables podemos tener datos demográficos de un cliente, historial de compras, 
comportamientos de navegación, dirección de cliente, comentarios o reseñas de productos, etc.

Analizando las variables, podemos descubrir patrones, tendencias y correlaciones que arrojen luz sobre 
el comportamiento.

3.1 Variables Numéricas (Cuantitativas)
Representan cantidades que pueden medirse o contarse. Pueden ser discretas o continuas.

3.2 Variables Categóricas (Cualitativos)
Representan categorías o etiquetas que clasifican los datos en grupos distintos. Tenemos los nominales
que son categorías sin un orden fijo, como colores, marcas, tipos de cocinas, etc. Las variables
categóricas ordinales son categorías con un orden o clasificación significativa, como nivel educativo,
tallas de ropa (S, M, L, XL), índices de satisfacción (malo, regular, bueno, excelente)

Comprender los distintos tipos de variables es crucial porque determinan los métodos estadísticos 
y las técnicas de visualización que conviene emplear. Por ejemplo, puede utilizar un gráfico de 
barras para visualizar la distribución de variables categóricas como los géneros de libros favoritos, 
mientras que un diagrama de dispersión podría revelar las relaciones entre variables continuas como la 
edad y el gasto.
'''
UtilConsole.show_lesson(lesson_variables)
