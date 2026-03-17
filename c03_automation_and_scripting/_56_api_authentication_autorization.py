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

Las claves API destacan por su simplicidad y facilidad de implementación. Son un buen punto de partida para los desarrolladores, especialmente para los que no están familiarizados con las interacciones API. Sin embargo, es crucial reconocer sus limitaciones. Aunque cómodas, las claves API sólo proporcionan una seguridad básica. Si se manipulan mal o quedan expuestas, pueden ser explotadas, permitiendo potencialmente el acceso no autorizado a datos confidenciales. Además, las claves API proporcionan un pase de acceso general; no permiten un control detallado, lo que significa que no se pueden restringir las acciones específicas que un usuario puede realizar una vez autenticado.
"""
import sys

import requests


def get_coords():
    return {'latitude': 1, 'longitude': 2}


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
