"""
CONCEPTOS Y MÉTODOS HTTP

Endpoints: Las puertas de acceso a los recursos
Los end points son los puntos de entrada para interactuar con recursos específicos dentro de una API REST. Son análogos
a las puertas de un edificio, cada una de las cuales conduce a una habitación o sección diferente. Cada punto final
está asociado a una URL específica y representa un recurso o acción distintos. Por ejemplo, en una API de Redes sociales,
un punto final como /users podría recuperar una lista de todos los usuarios, mientras que /users/12345 podría obtener
información sobre un usuario específico con ID 12345.

Métodos HTTP
Los métodos HTTP, a menudo denominados verbos, funcionan como palabras de acción en el lenguaje de las API REST.
Dictan las operaciones que los clientes pueden ejecutar en los recursos expuestos por la API. Este enfoque
estandarizado garantiza que tanto el cliente como el servidor entiendan la acción que se pretende realizar,
facilitando así una comunicación fluida y eficaz. Echemos un vistazo a los métodos HTTP más comunes.

1. GET
El GET es la herramienta perfecta para recuperar información. Es como hacer una pregunta a la API y recibir
una respuesta a cambio. Por ejemplo, si envía una solicitud GET al punto final /users, básicamente estará
pidiendo a la API que le proporcione una lista de todos los usuarios registrados en el sistema.

2. POST
El POST, se utiliza para crear nuevos recursos. Imagina que rellenas un formulario y lo envías: eso es lo que
hace una solicitud POST. Si desea añadir un nuevo usuario al sistema, deberá enviar una solicitud POST
al punto final /users, incluyendo todos los detalles necesarios sobre el nuevo usuario, como su nombre,
dirección de correo electrónico y contraseña.

3. PUT
El PUT consiste en actualizar la información existente. Piense que es como editar un documento: está haciendo
cambios en algo que ya existe. Si necesita modificar los detalles de un usuario específico, tal vez su
dirección de correo electrónico o la foto de su perfil, utilizaría una solicitud PUT. Por ejemplo,
una petición PUT a /users/123 actualizaría la información asociada al usuario cuyo ID es 123.

4. DELETE
El DELETE, que, como su nombre indica, se utiliza para eliminar recursos. Es similar a borrar un archivo de
tu ordenador. Si quieres eliminar un usuario del sistema, enviarías una petición DELETE al endpoint apropiado.
Así, una petición DELETE a /users/123 eliminaría el usuario con el ID 123.
"""
