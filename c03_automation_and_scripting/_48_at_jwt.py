"""
JSON WEB TOKENS

¿Qué son los JWT? Imagine un JWT como un tipo especial de sobre digital. Este sobre contiene
información importante y está sellado con una firma digital. Esta firma actúa como un sello
a prueba de manipulaciones, garantizando que la información que contiene no ha sido
alterada durante el transporte.

¿Qué contiene este sobre digital?
La "carga útil" de un JWT es donde se produce la magia. Es como el contenido del sobre. Esta
carga útil puede incluir varias afirmaciones o declaraciones sobre el usuario. Por ejemplo:

- Identidad del usuario: Información sobre quién es el usuario (por ejemplo, su nombre de
usuario o identificador único).

- Funciones del usuario: Los roles o grupos a los que pertenece el usuario (por ejemplo,
"admin", "user", "guest").

- Permisos de usuario: Las acciones específicas que el usuario está autorizado a
realizar dentro del sistema.

Esta información es esencialmente una instantánea del perfil de autorización del usuario.

------------------------------------------------------------------------------------------------------------------------

¿Por qué utilizamos JWT?

Los JWT ofrecen varias ventajas que los convierten en una opción popular para la seguridad de las API:

- Autónomos: Toda la información de autorización necesaria está incluida en el propio token. Esto facilita
el paso de esta información entre diferentes servicios o componentes de un sistema.

- Seguro: La firma digital garantiza que el contenido del token no ha sido manipulado. Esto ayuda a evitar
modificaciones no autorizadas o falsificaciones.

- Compactos: Los JWT están diseñados para ser compactos y eficientes, lo que los hace adecuados para su
transmisión a través de redes.

- Versátiles: Los JWT pueden utilizarse para una gran variedad de propósitos más allá de la autorización,
como el almacenamiento de preferencias de usuario o información de sesión.

------------------------------------------------------------------------------------------------------------------------

Casos de uso habituales:

- Autenticación: Los JWT pueden almacenar la identidad del usuario y la información de la sesión, lo que permite
una autenticación sin fisuras en diferentes partes de una aplicación.

- Autorización: La carga útil de un JWT puede codificar las funciones y permisos del usuario, lo que permite
un control de acceso detallado dentro de una API.

- Intercambio seguro de información: Los JWT proporcionan una forma a prueba de manipulaciones de transmitir
datos entre servicios, garantizando que la información no ha sido modificada en tránsito.

En esencia, los JWT son una potente herramienta para gestionar y transmitir de forma segura la información
de autorización dentro de los sistemas basados en API. Ofrecen una forma cómoda y fiable de garantizar que
solo los usuarios autorizados pueden acceder a los recursos que necesitan.
"""
