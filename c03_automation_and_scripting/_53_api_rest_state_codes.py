"""
CÓDIGOS DE ESTADO

Los códigos de estado son códigos numéricos de tres dígitos que indican el resultado de una solicitud de API.
Proporcionan información valiosa a los clientes sobre el éxito o el fracaso de sus solicitudes, junto con
información adicional sobre la naturaleza de la respuesta. Veamos algunos códigos de estado comunes que puede
encontrar al trabajar con estos métodos HTTP.

Una solicitud GET correcta suele devolver un código de estado 200 OK. Si el recurso no existe, obtendrá un
404 Not Found.

Una solicitud POST correcta suele devolver el estado 201 Created, a menudo con una cabecera de ubicación
que apunta a la URL del recurso recién creado. Si hay algún problema con la solicitud, como que falten
datos o que estos no sean válidos, es posible que aparezca 400 Bad Request.

En el caso de PUT, una actualización correcta suele devolver un 200 OK. Si el recurso no existe, obtendrás un
404 Not Found, y si hay algún problema con los datos que envías, puede que veas un 400 Bad Request.

Una eliminación correcta(DELETE) suele dar como resultado un estado 204 No Content. Si el recurso no
existe, obtendrás un 404 Not Found. En algunos casos, puede producirse un error en el servidor
durante el proceso de borrado, lo que da lugar a un 500 Internal Server Error.

Otros códigos de estado: También puedes encontrar otros códigos de estado, como un 504 Gateway Timeout
si el servidor está esperando a otro servidor, o un 202 Accepted si el servidor ha aceptado tu
petición, pero aún no la ha procesado.

Entender estos códigos de estado es crucial para interpretar la respuesta del servidor a tus peticiones,
permitiéndote manejar diferentes escenarios con elegancia y proporcionar una retroalimentación
significativa al usuario.

------------------------------------------------------------------------------------------------------------------------

Formatos de solicitud/respuesta

Las API REST intercambian datos entre clientes y servidores utilizando formatos estandarizados como JSON
(JavaScript Object Notation) o XML (Extensible Markup Language). JSON es el formato más utilizado por su
sencillez, legibilidad y compatibilidad con varios lenguajes de programación. Estructura los datos como
par clave-valor, lo que facilita su análisis y manipulación. XML, aunque menos común en las API modernas,
ofrece una forma más verbosa y estructurada de representar los datos, a menudo utilizada en sistemas
heredados o cuando se requiere una validación estricta de los datos.

Ejemplos

{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": 30
}

<user>
    <name>John Doe</name>
    <email>john.doe@example.com</email>
    <age>30</age>
</user>

Estos formatos proporcionan una forma estructurada y coherente de representar los datos, garantizando que
tanto clientes como servidores puedan interpretar y procesar la información correctamente.

------------------------------------------------------------------------------------------------------------------------

El papel de las API REST en el desarrollo moderno de software

Las API REST han revolucionado la forma en que las aplicaciones de software interactúan e intercambian datos,
fomentando un panorama de servicios interconectados y permitiendo la creación de aplicaciones web potentes y
flexibles. Proporcionan un enfoque estandarizado y escalable para construir API's, promoviendo la interoperabilidad
y simplificando la integración de diversos sistemas. Como desarrollador de Python, dominar los conceptos de las
API's REST te capacita para aprovechar el vasto ecosistema de servicios web, construir aplicaciones robustas y
escalables, y contribuir al siempre cambiante mundo del desarrollo de software.

Las API REST son un testimonio del poder de los protocolos de comunicación estandarizados en la era digital.
Constituyen la columna vertebral del desarrollo web moderno, ya que permiten un intercambio de datos fluido
y fomentan un entorno colaborativo de servicios interconectados. Al comprender los conceptos fundamentales de
las API de REST, los desarrolladores de Python pueden desbloquear un mundo de posibilidades, creando aplicaciones
escalables, robustas e interoperables que satisfagan las necesidades dinámicas del panorama digital.

Así como te embarcas en tu viaje para dominar el desarrollo en Python, recuerda que las API's REST son tu puerta
de entrada a un universo de servicios interconectados, permitiéndote crear soluciones innovadoras e impactantes
que dan forma al futuro de la tecnología.
"""
