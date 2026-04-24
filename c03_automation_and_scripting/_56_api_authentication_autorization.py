"""
AUTENTICACIÓN Y AUTORIZACIÓN

En el mundo del desarrollo web, las API (Interfaces de Programación de Aplicaciones) actúan
como puentes que conectan distintas aplicaciones de software, permitiéndoles compartir datos
y funcionalidades. Pero, como cualquier puente, una API necesita medidas de seguridad para
controlar el acceso y proteger la información sensible. Ahí es donde entran en juego la
autenticación y la autorización.

La autenticación verifica quién intenta acceder a la API, mientras que la autorización determina
qué se le permite hacer. Piense en la autenticación como si mostrara su DNI en la puerta, y en
la autorización como si se le concedieran permisos específicos una vez dentro.

------------------------------------------------------------------------------------------------------------------------

1. Claves API (API key)

Imagine las claves API como llaves digitales personalizadas que abren la puerta a datos o
servicios específicos dentro de una aplicación. Cada clave es única, lo que garantiza que
solo los usuarios o aplicaciones autorizados puedan acceder a los recursos a los que están
destinadas. Cuando quiera interactuar con una API, presente su clave, normalmente colocándola
en la cabecera o como parámetro en su solicitud. A continuación, el servidor de la API
comprueba si la clave coincide con sus registros y, en caso afirmativo, le permite acceder
a los datos o funciones solicitados.

Pongamos en práctica este concepto. Imagina que estás desarrollando una aplicación meteorológica.
Decide utilizar una API meteorológica de terceros para obtener los últimos datos meteorológicos.
Para ello, primero tendrá que obtener una clave API del proveedor del servicio meteorológico.

Es como obtener una tarjeta especial para acceder a su base de datos meteorológica. Una vez que
tengas esta clave, la incorporas a todas las solicitudes que tu aplicación envíe a la API,
lo que permite recuperar sin problemas la información meteorológica que necesitas
mostrar a tus usuarios.

Veamos ahora cómo se traduce esto en código Python real. A continuación se muestra un ejemplo
simplificado de cómo realizar una solicitud a una API meteorológica utilizando una clave API.

Las claves API destacan por su simplicidad y facilidad de implementación. Son un buen punto
de partida para los desarrolladores, especialmente para los que no están familiarizados con
las interacciones API. Sin embargo, es crucial reconocer sus limitaciones. Aunque cómodas,
las claves API solo proporcionan una seguridad básica. Si se manipulan mal o quedan expuestas,
pueden ser explotadas, permitiendo potencialmente el acceso no autorizado a datos confidenciales.

Además, las claves API proporcionan un pase de acceso general; no permiten un control detallado,
lo que significa que no se pueden restringir las acciones específicas que un usuario puede
realizar una vez autenticado.

Para mantener la seguridad de sus claves API, es crucial evitar almacenarlas directamente en
repositorios de código (como GitHub). Esto se debe a que otras personas pueden acceder a los
repositorios, especialmente a los públicos, lo que podría dar lugar a un uso no autorizado o
a la exposición de sus claves. Si una clave API se ve comprometida, puede dar lugar a un uso
indebido del servicio asociado, violaciones de datos y pérdidas financieras. Aunque el ejemplo
anterior muestra la clave API en texto plano, la implementación debería ser diferente si la
clave se encuentra en un repositorio público.

Aunque las claves API ofrecen una forma cómoda de autenticar las aplicaciones, es crucial
gestionarlas de forma segura para evitar accesos no autorizados y posibles filtraciones de
datos.

Rotación periódica: La rotación periódica de las claves API es una práctica de seguridad
fundamental. Limita las posibilidades de que un atacante explote una clave comprometida.
Establecer un calendario para la rotación de claves, por ejemplo cada 30, 60 o 90 días,
dependiendo de la sensibilidad de los datos a los que se accede, puede reducir
significativamente el riesgo.

Custodia de claves: Los almacenes de claves proporcionan una ubicación centralizada y
segura para guardar las claves API. Ofrecen un cifrado robusto y controles de acceso,
garantizando que solo las personas o servicios autorizados puedan recuperar las claves.

Los proveedores de nube más populares ofrecen servicios de bóveda de claves, como Azure
Key Vault y AWS Key Management Service (KMS), que se integran perfectamente con otras
aplicaciones basadas en la nube.

------------------------------------------------------------------------------------------------------------------------

OAUTH (Estándar Abierto de Autorización)

Su objetivo principal es permitir que una aplicación acceda a datos de un
usuario en otro servicio (como Google, GitHub o Facebook) sin que el usuario
tenga que entregarle su contraseña a la aplicación tercera.

OAuth, u Open Authorization (Autorización Abierta), mejora la seguridad en comparación con las
claves API básicas. Es un protocolo que permite a los usuarios conceder a aplicaciones de terceros
un acceso limitado a sus datos en otro servicio, esto sin tener que revelar sus preciadas contraseñas.

Es como darle a un amigo una llave temporal de tu casa para que riegue tus plantas mientras estás
fuera: puede entrar, pero solo para hacer esa tarea específica.

Imaginemos que estás creando una aplicación para redes sociales en la que los usuarios pueden compartir
fotos directamente desde OneDrive. No querrías pedir a los usuarios su contraseña, ¿verdad? Ahí es donde
entra OAuth. Integrarías OAuth en tu aplicación y, cuando un usuario quisiera compartir una foto, sería
redirigido al sitio web de Microsoft. Allí, verían un mensaje pidiéndoles que autoricen a tu aplicación
a acceder a su Drive. Una vez que dan luz verde, tu aplicación obtiene un token especial que puede utilizar
para acceder a Drive del usuario, pero solo en la medida en que lo hayan permitido.

La implementación de OAuth en Python suele implicar el uso de librerías como requests_oauthlib o SDK
(Kit de desarrollo de software) específicos del proveedor. Estas herramientas se encargan de los complejos
apretones de manos e intercambios de tokens implicados en el proceso de OAuth, haciéndote la vida un poco
más fácil.

La implementación exacta variará en función del servicio con el que te estés integrando y del flujo OAuth
específico que elijas.

------------------------------------------------------------------------------------------------------------------------

JWT

Los JSON Web Tokens, o JWT, sirven como una especie de pasaporte digital en el mundo de la transmisión segura
de datos. Imagínatelos como paquetes de información compactos y autónomos que pueden transmitirse de forma
segura entre distintas partes, de forma parecida a como un pasaporte verifica tu identidad cuando viajas. Estos
tokens se codifican como objetos JSON, lo que facilita su uso en distintos lenguajes de programación.

Cada JWT tiene tres secciones distintas: la cabecera, la carga útil y la firma. La cabecera proporciona metadatos
sobre el token en sí, como el algoritmo utilizado para la firma. La carga útil es donde reside la información real,
que contiene afirmaciones o declaraciones sobre el usuario (como su ID o rol) y cualquier otro dato relevante. Piense
en esto como la página de información personal de su pasaporte. Por último, la firma actúa como un sello digital
que garantiza la autenticidad del token y que no ha sido manipulado durante su transporte.

Digamos que estás desarrollando una API RESTful, que es esencialmente una forma de que diferentes aplicaciones se
comuniquen entre sí a través de la web. Quiere asegurarse de que solo los usuarios autenticados pueden acceder
a ciertos recursos protegidos dentro de su API. Los JWT ofrecen una solución elegante. Tras un inicio de sesión
satisfactorio, puede emitir un JWT al usuario. A continuación, el usuario incluye este token en el encabezado
de las solicitudes posteriores a su API. Su servidor verifica la firma del token y, si es válida, concede acceso a los
recursos solicitados.

Los JWT ofrecen varias ventajas. No tienen estado, lo que significa que su servidor no necesita mantener ninguna
información de sesión sobre el usuario. Esto puede simplificar su arquitectura y mejorar la escalabilidad. Además,
los JWT son relativamente fáciles de implementar y se pueden utilizar en diferentes dominios, lo que los convierte
en una opción flexible para diversas aplicaciones.

Aunque los JWT son potentes, hay que tener en cuenta algunos puntos. Si se introducen demasiados datos en la
carga útil, el token puede llegar a ser bastante grande, lo que podría afectar al rendimiento. Y lo que es
más importante, la clave secreta que se utiliza para firmar el token debe ser absolutamente confidencial. Si
se ve comprometida, la integridad de sus JWT está en peligro.

------------------------------------------------------------------------------------------------------------------------

El coste de tomar atajos

Ahora, abordemos una posible preocupación que algunos podrían plantear. Implementar mecanismos robustos de
autenticación y autorización, como los que hemos discutido, puede añadir una capa de complejidad al proceso
de desarrollo. Requiere una planificación cuidadosa, la integración de bibliotecas o SDK y un manejo meticuloso
de claves y tokens sensibles. No se puede negar que esto puede introducir cierta sobrecarga, especialmente en
las fases iniciales del desarrollo.

Sin embargo, es crucial sopesar este esfuerzo inicial con las posibles consecuencias de una seguridad inadecuada.
Una filtración de datos, en la que quede expuesta información confidencial de los usuarios, puede ser devastadora
tanto para sus usuarios como para su reputación. Acceso no autorizado puede interrumpir la funcionalidad de su
aplicación y comprometer su integridad. Y lo más importante, perder la confianza de sus usuarios puede ser
increíblemente difícil de recuperar.

En el ámbito de la seguridad de las API, no existe una solución única. El mecanismo de autenticación ideal
depende de las necesidades específicas de su aplicación y del nivel de seguridad que requiera. Si se trata
de una situación sencilla en la que solo necesita identificar la aplicación que llama, las claves de API
pueden ser suficientes. Sin embargo, si lo que necesita es que los usuarios concedan a aplicaciones de
terceros acceso a sus datos sin exponer sus contraseñas, OAuth es la solución.

Y para una comunicación segura y sin estado entre distintas partes de la aplicación o entre distintos dominios,
los JWT son la solución.

Recuerda, independientemente del mecanismo que elijas, la clave es implementarlo correctamente y con diligencia.
La autenticación y la autorización no son solo palabras de moda; son pilares fundamentales de la seguridad de
las API. Al dominar estas técnicas, elevarás tus habilidades como desarrollador Python y te convertirás en un
activo invaluable en la elaboración de aplicaciones que son robustas y confiables.
"""
import jwt
import requests


def example01APICall():
    API_KEY: str = '240cf62c8846bd8a948db87e9c178de3'
    url = 'https://api.weatherapi.com/v1/current.json'
    params = {'key': API_KEY, 'q': 'London'}

    try:
        response = requests.get(url, params)
        response.raise_for_status()
        print(response.json())
    except requests.exceptions.RequestException as err:
        print(err)
    except Exception as err:
        print(err)


def example02CreateJWT():
    # This is only for
    secretKey = 'This_is_a_secret_key123@123*1234523453$%3'

    # Exp -> time expiration
    payload = {
        'user_id': 123,
        'exp': 1633543343,
    }

    # Generate token
    token = jwt.encode(payload, secretKey, algorithm='HS256')
    print(token)


def main():
    example01APICall()
    print()

    example02CreateJWT()
    print()


if __name__ == '__main__':
    main()
    
    # End application
    _ = input('\nPress ENTER to quit . . .  ')
