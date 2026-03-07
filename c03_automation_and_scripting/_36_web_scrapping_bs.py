"""
INTRODUCCIÓN A BEAUTIFUL SOUP

Herramienta especializada y diseñada específicamente para analizar documentos HTML y XML,
BeautifulSoup transforma la estructura a menudo caótica de las páginas web en una representación
ordenada en forma de árbol, lo que facilita la navegación y la extracción de los datos
exactos que necesitas.

Permite además actualizar el contenido existente, eliminar elementos no deseados o incluso
crear estructuras HTML completamente nuevas dentro del documento analizado. Tanto si estás
construyendo un raspador web, limpiando datos desordenados, o automatizando interacciones web,
BeautifulSoup proporciona una interfaz potente e intuitiva para lograr tus objetivos.
------------------------------------------------------------------------------------------------------------------------

CONCEPTOS Y FUNCIONES BÁSICAS

1. Sopa
Creamos un objeto tipo de árbol donde se almacenarán los elementos dentro del documento
a analizar.

2. Parser
Emplea un parser para analizar un html, ya que por sí solo no puede hacerlo. Python
incluye 'html.parser' sin necesidad de instalaciones extras.

El 'motor' o parser 'lxml' es muy rápido y tolerante a fallas de sintaxis. Requiere instalación
aparte. Por último el parser 'html5lib' analiza el texto tal cual como si fuera un navegador.

Las funciones find() y find_all() son tus herramientas principales para buscar dentro del HTML
analizado. La función find() localiza eficientemente el primer elemento que cumple los criterios
especificados, mientras que find_all() devuelve una lista completa de todos los elementos
coincidentes.

Para búsquedas aún más específicas, la función select() le permite aprovechar la potencia de
los selectores CSS, el mismo lenguaje utilizado para dar estilo a las páginas web, proporcionando
una precisión milimétrica.

Una vez identificado el elemento deseado, get_text() extrae su contenido de texto puro, eliminando
cualquier etiqueta HTML y dejándole solo la información que necesita.

Por último, la propiedad attrs sirve como un práctico diccionario para acceder a los atributos
de un elemento, como class, id o href.

La función select_one se emplea para encontrar el primer elemento que cumpla con la regla css
y select retorna una lista.
------------------------------------------------------------------------------------------------------------------------

RETROS

Los sitios web evolucionan constantemente. Sufren actualizaciones, rediseños y cambios en su
estructura HTML. Esto puede romper los scripts de BeautifulSoup que dependen de elementos
específicos o patrones en el HTML. Es crucial probar y mantener regularmente el código para
asegurarse de que sigue funcionando correctamente, incluso cuando los sitios web que está
raspando evolucionan.

Respete siempre los Términos de servicio del sitio web y cualquier restricción indicada en
su archivo robots.txt. Evite hacer peticiones excesivas que puedan sobrecargar el servidor
e interrumpir el funcionamiento normal del sitio web. Recuerde que el web scraping debe ser
un proceso mutuamente beneficioso, no una carga para los propietarios de los sitios web.

Por último, BeautifulSoup se centra principalmente en el análisis sintáctico de HTML estático.
Aunque sobresale en la extracción de datos de páginas web bien estructuradas, puede tener
limitaciones cuando se trata de contenido dinámico. Muchos sitios web modernos dependen en
gran medida de JavaScript o AJAX para cargar contenido de forma dinámica después de la carga
inicial de la página. En estos casos, es posible que BeautifulSoup no pueda acceder aL contenido
a menos que se combine con otras herramientas o técnicas que puedan procesar JavaScript
y simular las interacciones del usuario.
"""

from bs4 import BeautifulSoup, Tag


def example_bs_01():
    html_content: str = """
    <!DOCTYPE html>
    <html lang="es">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Panadería</title>
    </head>

    <body>
        <div>
            <header id="header">
                <ul>
                    <li>Inicio</li>
                    <li>¿Quienes Somos?</li>
                    <li>Pedidos</li>
                    <li>Atención a Clientes</li>
                    <li>Ubicación</li>
                </ul>
            </header>
        </div>

        <div>
            <h1>Panadería Local Mamalona</h1>

            <div>
                <ul>
                    <li>Pan de Muerto</li>
                    <li>Concha</li>
                    <li>Dona</li>
                    <li>Dona Glaseada</li>
                </ul>
            </div>
        </div>

        <p>Form Example</p>
        <p class='special'>This is other paragraph</p>

        <form action="/enviar-mensaje" method="post">
            <div>
                <label for="nombre">Nombre:</label>
                <input type="text" name="nombre" id="nombre" required>
            </div>

            <div>
                <label for="email">Correo electrónico:</label>
                <input type="email" id="email" name="user_email" required>
            </div>

            <div>
                <label for="mensaje">Mensaje:</label>
                <textarea id="mensaje" name="user_message" rows="4"></textarea>
            </div>
        </form>

    </body>

    </html>
    """

    # Create a hierarchical tree
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the document title
    title: str = soup.title.text
    print(f'Title of html document: {title.upper()}')

    # Find the first 'p' element
    first_paragraph: Tag | None = soup.find('p')
    print(f'First paragraph: {first_paragraph} with type: {type(first_paragraph)}')

    # Find all p elements
    all_paragraphs: list[Tag] = soup.find_all('p')
    for p in all_paragraphs:
        print(f'- {p.text}')

    # Find first p element with html class
    special_paragraph: Tag | None = soup.find('p', class_='special')
    print(f'special_paragraph: {special_paragraph}')


def example_bs_02():
    # Content
    html_content: str = """
    <html>
        <body>
            <div id="main-content">
                <h1>This is a heading</h1>
                <p class="important">This is an important paragraph.</p>
                <a href="https://www.example.com">Visit Example</a>
            </div>
        </body>
    </html>
    """

    # Parse html
    soup = BeautifulSoup(html_content, 'html.parser')

    # Use CSS selector to find 'div' with id 'main-content'.
    main_content: Tag = soup.select_one('#main-content')
    print(f'#main-content:\n{main_content}')

    # Select first p with class important
    important_paragraph: Tag | None = main_content.select_one('.important')
    paragraph_text = important_paragraph.get_text() if important_paragraph else 'Empty'
    print(paragraph_text)

    # Find the 'a' element within 'main-content'
    link = main_content.select_one('a')

    # Access the 'href' attribute of the link
    link_url = link['href'] if link else None
    print(link_url)  # Output: https://www.example.com


if __name__ == '__main__':
    example_bs_01()
    print('-' * 64)

    example_bs_02()
    print('-' * 64)
