"""
GUÍA DE REFERENCIA DE APIS

En el mundo del desarrollo de software moderno, las interfaces de programación de aplicaciones (API)
sirven de puentes fundamentales que permiten que distintos sistemas de software se comuniquen e
interactúen a la perfección.

Sin embargo, esta interconexión conlleva una necesidad crucial de seguridad. Los mecanismos de
autenticación y autorización de las API son los guardianes que garantizan que solo las entidades
legítimas accedan a los recursos de las API y los utilicen adecuadamente.

Esta guía explora los entresijos de la autenticación y autorización de API, centrándose en conceptos
clave como las claves de API, la autenticación abierta (OAuth) y los tokens web.

-----------------------------------------------------------------------------------------------------------------------

1. Autenticación de API: Verificación de Identidad

La autenticación de una API verifica la identidad de la entidad (usuario u otra aplicación) que intenta
acceder a los recursos de la API.

Existen dos métodos principales de autenticación de API:

Claves de API (API KEY)
Las claves API son identificadores únicos utilizados para autenticar las solicitudes,
pero no verifican intrínsecamente la identidad del solicitante. Para mejorar la seguridad,
las claves API se combinan a menudo con otros mecanismos, como listas blancas de IP o
límites de uso, para mitigar los riesgos asociados a la fuga de claves.

OAuth (Open Authorization)
OAuth, un protocolo de acceso delegado, ofrece un enfoque más sofisticado de la autenticación
de API's. Permite a los usuarios conceder un acceso limitado a sus recursos en un servicio sin
compartir sus contraseñas reales. En lugar de autenticarse directamente con el servidor de la
API, el cliente interactúa con un servicio de terceros, concediéndole permiso para acceder a
información específica. Este servicio de terceros emite entonces un "token de autorización"
temporal al cliente, que actúa como pase seguro para acceder a la API.

En términos más técnicos, OAuth implica la obtención de un token de acceso, que se utiliza para
las solicitudes de la API, y a veces un token de actualización, que puede intercambiarse por un
nuevo token de acceso cuando caduca el original. Este enfoque mejora la seguridad y
proporciona un control granular sobre los permisos de acceso.

------------------------------------------------------------------------------------------------------------------------

¿Por qué es tan importante la autenticación de la API?

Sin una autenticación adecuada, cualquiera podría acceder a los datos de una API y manipularlos.
Esto podría provocar:

Filtraciones de datos:
Información sensible como datos de usuario, registros financieros o propiedad intelectual podría ser robada.

Transacciones no autorizadas:
Actores malintencionados podrían realizar compras o transferencias no autorizadas.

Caídas del sistema:
Las API sobrecargadas o comprometidas podrían interrumpir o bloquear sistemas enteros.
"""
