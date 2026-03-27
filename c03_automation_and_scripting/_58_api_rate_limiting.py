"""
LIMITACIONES DE VELOCIDAD Y GESTIÓN DE ERRORES

Una API defina las reglas y los protocolos con la finalidad de obtener o intercambiar datos
entre aplicaciones.

Podemos decir que una llamada a una API solicita a otra aplicación que realize una acción
específica u obtener cierta información.

Como desarrollador que usa API's debe tener en cuenta que a menudo se tienen límites de
velocidad.

Los rate limits (límites de velocidad) restringen la cantidad de solicitudes que puedes
realizar dentro de un periodo específico de tiempo. Normalmente por minuto o por hora.

Los límites de velocidad se utilizan por diversos motivos, como evitar la sobrecarga del
servidor (server overload). Demasiadas solicitudes pueden sobrecargar un servidor de API
y provocar que responda de forma lenta o incoherente y finalmente se bloquee.

Los límites de velocidad (time rate) garantizan que un servidor pueda gestionar el tráfico
entrante y ofrecer una buena experiencia de usuario.

Algunos proveedores de API's tienen modelos de precios basados en el uso que cobran más a
los usuarios si superan los límites de tarifas. Superar los límites de velocidad de la API
puede provocar que el proveedor de la API bloquee temporal o definitivamente,

Algunos tipos para gestionar los rate limit (límites de velocidad):

1. Respeta los límites de la API
Lea la documentación de la API para entender sus alcances y limitaciones.

2. Añada delays (retrasos)
Introduzca pausas estratégicas entre llamadas a la API para evitar alcanzar el límite de
velocidad.

3. Almacene el caché con frecuencia
Almaceno localmente los datos los que accede con frecuencia para evitar llamadas repetidas
a la API. Esto reduce la carga del servidor y mejora el rendimiento de las aplicaciones.

4. Actualizaciones
Realize actualizaciones, por ejemplo a otro plan de la API. Los planes de API's suelen tener
límites más altos o soluciones adaptadas a sus solicitudes.

5. Gestión de Errores
Añada soporte a posibles errores que puedan ocurrir. Use bloques try-except dentro de su
código. Coloque las llamadas a API's en bloques para detectar posibles excepciones, de modo
que pueda anticipar y gestionar errores sin que su programa se bloquee.

Otra forma elegante es utilizar mensajes informativos así como implementar mecanismos
de reintento de solicitudes en caso de que existan problemas temporales de red o
errores en el servidor.

6. Logging
Puede utilizar el módulo de registro en python para registrar los detalles de los
errores, incluidos timestamps (marcas de tiempo), información sobre excepciones
generadas y el contexto en el que se generan.
"""
