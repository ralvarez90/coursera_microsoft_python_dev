"""
TÉCNICAS AVANZADAS DE AUTOMATIZACIÓN (API's)

Son un mecanismo que nos permite intercomunicar aplicaciones y así
compartir información.

Las API's o interfaces de programación de aplicaciones son puentes
de comunicación entre diferentes aplicaciones de software.

Definen un conjunto de reglas y protocolos que permiten la interacción
de diferentes componentes de software.

Al usar una API, podemos usar una aplicación para acceder a las funciones
y los datos de otra aplicación. Esto abre un mundo de posibilidades para
la automatización y la integración. Existen diferentes tipos de API's.

Las API's permiten a los desarrolladores crear aplicaciones más potentes
al aprovechar las ventajas de los servicios existentes.

1. RESTful. Las API's RESTful permiten que los servicios web se comuniquen a través
de HTTP al definir cómo se deben de mostrar y manipular las cosas. Son muy
flexibles.

2. SOAP. Las API's tipo SOAP implementan un modelo de comunicación web más
rígida que se usa para sistemas que tienen niveles de seguridad altos.

3. GraphQL. Se utiliza en aplicaciones con muchos datos, ya que permite
solicitar solo la información específica que necesitas.
"""

lesson_content: str = """
1. REST (Representational State Transfer)
Es el estándar más popular en la web actual. No es un protocolo estricto, sino un estilo de 
arquitectura que utiliza los métodos nativos de HTTP. 

Cómo funciona: Se basa en "recursos" (URLs). Si quieres datos de un usuario, vas a /usuarios/1.
Formato: Casi siempre usa JSON, que es ligero y fácil de leer.
Filosofía: "Cada cosa tiene su propia dirección".
Ventajas: Es simple, escalable y muy fácil de implementar en cualquier lenguaje.

2. SOAP (Simple Object Access Protocol)
Es el "abuelo" robusto y formal. A diferencia de REST, SOAP es un protocolo estricto con reglas 
muy definidas.
Cómo funciona: Utiliza un archivo llamado WSDL (un contrato) que define exactamente qué puedes 
pedir y qué recibirás.
Formato: Solo utiliza XML. Es mucho más "pesado" que JSON porque lleva mucha metadata.
Filosofía: "Seguridad y estructura ante todo".
Ventajas: Es extremadamente seguro (estándares bancarios) y tiene manejo de errores integrado. 
Se usa mucho en sistemas financieros y gubernamentales antiguos.

3. GraphQL
Es el "chico nuevo" (creado por Facebook) que vino a solucionar los problemas de 
eficiencia de REST.
Cómo funciona: En lugar de tener muchas URLs, solo tienes un único punto de acceso (endpoint). 
El cliente envía una consulta especificando exactamente qué campos quiere.
Formato: JSON.
Filosofía: "Pídeme solo lo que necesites, ni más ni menos".
Ventajas: Evita el over-fetching (traer datos de más) y el under-fetching (tener que hacer 
5 llamadas a la API para mostrar una sola pantalla).
"""
print(lesson_content)
_ = input('\nPress ENTER to quit . . . ')
