"""
MENSAJES DE ERROR

1. Códigos de errores http
Son códigos de respuesta de solicitudes que no se pueden procesar
de manera adecuada.

2. Errores de conexión

3. Errores de análisis (parsing errors)
Si la estructura de un sitio web cambia o es inesperada, el parser puede
lanzar errores.

4. Errores de atributos
Estos aparecen cuando intentamos acceder a un atributo que no existe en
la estructura del HTML.

-----------------------------------------------------------------------------------------------------------------------

Existen algunos mecanismos dentro de un sitio web que limita o bloquea
que un sitio puede ser raspado. Por lo que:

- Respete los lineamientos del archivo robots.txt
- Reduzca la velocidad de y el número de solicitudes del scrapper.

- Cambie su user-agent para imitar diferentes navegadores.

- Use proxies, estos actúan como intermediarios entre su scrapper y
un sitio web. Esto puede ayudarle a ocultar su dirección ip y evitar
bloqueos de ip.

- Agregue captcha handlers, puede utilizar bibliotecas de reconocimiento
óptico. Para captcha complejos puede utilizar sistemas de resolución

- Use headless browsers, que son entornos de navegadores web sin interfaz
gráfica de usuario. Permiten la interacción programática con páginas web
a través de comandos. Esta configuración permite a herramientas como
Selenium ejecutar JavaScript, cargar contenido dinámico y simular interacciones
de usuario para pruebas automatizadas o web scrapping.
"""
