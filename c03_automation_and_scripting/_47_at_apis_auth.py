"""
AUTORIZACIÓN DE API: Definición de Niveles de Acceso

Ahora que hemos verificado quién intenta acceder a la API (autenticación), es el momento de
decidir qué puede hacer. Aquí es donde entra en juego la autorización. Piense en ello como
un sistema de permisos dentro de una empresa. No cualquiera tiene acceso a todos los archivos
o funcionalidades. Del mismo modo, la autorización de API controla a qué acciones y
recursos puede acceder un cliente autenticado.

Existen un par de modelos principales para gestionar estos permisos:

1. Control de Acceso Basado en Roles (RBAC)
Este es un enfoque común y directo. Es como asignar puestos de trabajo en una empresa. Usted
tiene sus "administradores" con acceso completo, "usuarios normales" con permisos estándar, y
tal vez incluso "invitados" con capacidades de visualización limitadas. Cada rol viene con un
conjunto predefinido de permisos para interactuar con la API.

2. Control de acceso basado en reclamaciones (CBAC)
Se trata de un enfoque más matizado. En lugar de basarse únicamente en las funciones, tiene en
cuenta atributos específicos o "afirmaciones" sobre el usuario o cliente. Estas afirmaciones
pueden incluir aspectos como el departamento, la participación en el proyecto o incluso el
nivel de habilitación de seguridad. Esto permite tomar decisiones de autorización más
flexibles y adaptadas al contexto.
"""
