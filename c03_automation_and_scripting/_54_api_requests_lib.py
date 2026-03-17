"""
INTERACCIÓN DE API's MEDIANTE LIBRERÍA REQUESTS.

1. requests
Librería para realizar peticiones a API's, gestionar respuestas y
extraer datos de carga útiles en formatos json o XML. La librería
requests simplifica el proceso de hacer solicitudes HTTP, gestiona
las respuestas y permite extraer datos en formatos específicos como
json o xml.

Tenga en cuenta que al consumir datos de API's cada una de ellas viene
con sus propias reglas y protocolos. La biblioteca permite realizar
peticiones GET, POST, PUT, DELETE entre otras. Esto permite interactuar
sin problemas con las diferentes API que puede necesitar.

Da soporte además a la gestión de errores que puedan ocurrir. Una vez
que realiza una petición a una API, el servidor devuelve una respuesta
que contiene los datos solicitados o un mensaje de error y un código
de estado que proporciona información sobre el resultado de su
solicitud.

Los códigos de estado más comunes son:

200 (OK)
La solicitud se realizó con éxito

400 (Bad Request)
Significa que el servidor de la API no ha entendido
tu solicitud, generalmente es por un parámetro no válido o falta de dátos.

401 (Unauthorized))
Significa que el usuario que realiza la solicitud no tiene las credenciales
suficientes para pedir información. Es decir no está autenticado y debe proporcionar
sus respectivas credenciales.

404 (Not found)
Indica que el recurso solicitado no existe.

505 (Internal Error Server)
Indica un error del lado del servidor de la API y no tiene que ver con tu
solicitud.

La biblioteca request también proporciona mecanismos para acceder al contenido
de las respuestas en formato json o xml.

Sin la librería "requests", tendrías que escribir mucho código de bajo nivel
para manejar la mecánica de las peticiones HTTP. Tendrías que preocuparte de
cosas como abrir conexiones de red, formatear las peticiones correctamente y
analizar las respuestas. Esto puede llevar mucho tiempo y dar lugar a errores.

La biblioteca "requests" abstrae estas complejidades, proporcionando una interfaz
limpia e intuitiva para interactuar con las API.
"""
