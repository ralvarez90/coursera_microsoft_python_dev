"""
PYTEST: CONCEPTOS Y CARACTERÍSTICAS

1. Funciones de Prueba
Son funciones simples y sencillas que designa como pruebas al iniciarlas con
nombre test. Dentro de estas funciones de pruebas se elaboran aserciones.

2. Fixtures (accesorios)
Se encargan de la configuración y el desmontaje de los recursos de los que dependen
sus pruebas. Garantizando que cada una de las pruebas se ejecuta en un entorno
prístino y aislado.

3. Parametrization (parametrización)
Permite ejecutar un diverso grupo de pruebas de acuerdo a diversos grupos de
parámetros que recibirá la función a probar.

4. Markers (Marcadores)
Actúan como etiquetas para sus pruebas, permitiendo clasificarlas en función
de los atributos o requisitos específicos. Estos permiten ejecutar selectivamente
determinados grupos de pruebas en función de sus necesidades.

4. Plugins
Son extensiones de pytest desarrollados por la comunidad, abarcando prácticamente
cualquier prueba de aplicaciones web, bases de datos, código asíncrono, o cualquier
otra cosa.
"""
from random import randint

import pytest


@pytest.fixture
def sampleListData() -> list:
    return [randint(1, 10) for _ in range(5)]


def testContainsFive(sampleListData: list):
    """Verifica si una lista de elementos contiene el 5."""
    assert 5 in set(sampleListData)
