"""
INTRODUCCIÓN A SCRAPY

En esencia, Scrapy es un marco de raspado web de código abierto. Está diseñado para recopilar
eficazmente datos estructurados, es decir, información organizada y predecible, de una amplia
gama de sitios web.

Scrapy proporciona una plataforma completa y bien organizada que sirve de modelo para sus
proyectos de scraping. Le permite definir con precisión las reglas para que su "araña"
navegue por los sitios web, localizar los datos exactos que necesita y gestionar la información
extraída en varios formatos.
------------------------------------------------------------------------------------------------------------------------

ARQUITECTURA Y COMPONENTES

La arquitectura de Scrapy es una fábrica bien organizada, donde cada componente desempeña un
papel específico en el proceso de extracción de datos. Este diseño modular promueve un desarrollo
y mantenimiento eficientes de sus proyectos de scraping, permitiéndole escalar y adaptarse
según sea necesario.

1. Spiders (arañas)
Las arañas son el corazón y el alma de cualquier proyecto de Scrapy. Las arañas recorren meticulosamente
la estructura del sitio web, analizando cuidadosamente el código HTML para identificar y extraer la
información que usted busca.

2. Articles (artículos, item
Son elementos contenedores meticulosamente organizados, diseñados específicamente para contener
los datos estructurados que sus arañas han recopilado diligentemente. Sirven como planos para la información
que desea capturar, definiendo los campos específicos o categorías de datos que le interesan, junto con sus
correspondientes tipos de datos. Por ejemplo, si está raspando información de productos de un sitio web de
comercio electrónico, su elemento podría incluir campos como "product_name", "price", "description" e
"image_url" Al definir estos campos y sus tipos (por ejemplo, cadena, entero, flotante), se garantiza la
coherencia y la organización de los datos extraídos, lo que facilita el trabajo y el análisis posterior.

3. Canalizaciones (pipelines)
Una vez que las arañas han recopilado con éxito los datos en bruto de la web, las canalizaciones entran en
juego como diligentes procesadores y refinadores. Piense en ellos como el departamento de control de
 calidad de su operación de extracción de datos. Las canalizaciones reciben los datos brutos de las arañas
 y realizan una serie de tareas esenciales para garantizar su precisión y utilidad. Limpian y validan
 la información, eliminando cualquier incoherencia o error que pueda haberse deslizado durante el
 proceso de extracción. Además, los pipelines pueden transformar los datos en varios formatos
 adecuados para su almacenamiento o análisis posterior. Pueden exportar los datos a formatos de
 archivo comunes, como CSV o JSON, para facilitar su uso en hojas de cálculo u otras aplicaciones.

 También pueden almacenar directamente los datos en bases de datos para facilitar su consulta y
 recuperación en el futuro. En esencia, los pipelines actúan como la etapa final de su cadena de
 montaje de extracción de datos, tomando las materias primas recogidas por las arañas y
 transformándolas en un producto pulido y valioso.


RESUMEN DEL FLUJO DE OPERACIONES
- La Spider genera una petición (Request).
- El Downloader descarga la página y devuelve una Response.
- La Spider extrae los datos usando Selectors.
- Los datos se guardan en Items.
- El Pipeline procesa, limpia y guarda los Items.
"""

scrapy_elements: str = """
1. Spiders (Arañas)
Son el corazón de Scrapy. Son clases personalizadas donde defines 
qué sitios visitar y cómo extraer la información. En ellas defines 
las URLs iniciales y la lógica para seguir enlaces o parsear 
el contenido HTML.

2. Items y Item Loaders
Items: Son contenedores de datos (similares a diccionarios) donde 
defines la estructura de la información que quieres recolectar 
(por ejemplo: precio, nombre, sku). Esto ayuda a que tus datos estén
 organizados y validados.

Item Loaders: Proporcionan un mecanismo para poblar esos Items, 
permitiéndote aplicar funciones de limpieza (como eliminar espacios 
en blanco o convertir divisas) antes de guardar el dato.

3. Selectors (CSS y XPath)
Scrapy utiliza selectores para "extraer" datos del HTML. Tienes dos opciones principales:
CSS Selectors: Más simples e intuitivos si vienes del desarrollo web.
XPath: Mucho más potente, permite navegar por la estructura del DOM de 
forma más compleja (ej. "busca el texto que está después de este icono").

4. Pipelines (Tuberías)
Una vez que la araña extrae un Item, este se envía al Item Pipeline. Es el lugar ideal para:
Limpiar datos HTML.
Validar que los datos no estén duplicados.
Almacenar los datos en una base de datos (SQL, MongoDB) o archivos locales.

5. Middlewares
Son ganchos (hooks) que permiten modificar el comportamiento de Scrapy a nivel global.
Spider Middlewares: Procesan la entrada (respuestas) y salida (items/solicitudes) de 
las arañas.
Downloader Middlewares: Se sitúan entre el motor de Scrapy y la web. Se usan 
para manejar proxies, rotación de User-Agents y reintentos de peticiones fallidas.

6. Settings (Configuración)
Es el archivo de control de tu proyecto (settings.py). Aquí ajustas parámetros críticos como:
CONCURRENT_REQUESTS: Cuántas páginas procesar al mismo tiempo.
DOWNLOAD_DELAY: El tiempo de espera entre peticiones (crucial para no ser bloqueado).
ROBOTSTXT_OBEY: Si Scrapy debe respetar o no las reglas del archivo robots.txt.

7. Scrapy Shell
Es una consola interactiva que te permite probar tus selectores (CSS/XPath) en tiempo real 
sin tener que ejecutar toda la araña. Es la herramienta de depuración más importante 
durante el desarrollo.
"""

print(scrapy_elements)
input('\nPress any key to continue . . . ')
