"""
PYTEST

Pytest es un framework de pruebas que facilita la escritura d pruebas pequeñas, legibles
y escalables para admitir pruebas funcionales complejas para sus aplicaciones y
bibliotecas.

Ayuda a detectar errores en las primeras etapas de desarrollo. Sus principales características
son:
- Es simple y legible
- Flexible y extensible
- Cuenta con poderosas características

Pytest permite crear desde pruebas unitarias hasta pruebas de integración.

Pytest además soporta fixtures (accesorios), que son funciones que proporcionan una
base para realizar pruebas más confiables.

Los accesorios (fixtures) se utilizan para establecer condiciones previas a
que las pruebas deben ejecutarse correctamente, como la inicialización de las
bases de datos, creación de pruebas, o configuraciones previas.

Los fixtures se definen mediante el decorador fixture. Los fixtures en pytest
funcionan definiendo una función y marcándola como un fixture.

Por default, un fixture tiene un scope de función, lo que quiere decir
que se configura y desactiva para cada prueba que lo usa. Este comportamiento
se puede modificar para que tenga alcance de módulo, clase o una sesión si es
necesaria.
"""
import pytest


def add(x: int | float, y: int | float) -> int | float:
    return x + y


def test_add_no_parametrize():
    assert add(1, 2) == 3


@pytest.mark.parametrize("x, y, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(x, y, expected):
    assert add(x, y) == expected


# Define fixture
@pytest.fixture
def sample_data():
    data = [1, 2, 3, 4, 5]
    return data


@pytest.fixture
def enhanced_data():
    print('Setting up enhanced data fixture. . . ')

    # Create a list of numbers
    data = [i * 10 for i in range(1, 6)]

    # Perform an enhanced calculation: e.g., double each value in list
    return [x * 2 for x in data]


def test_sum(sample_data):
    assert sum(sample_data) == 15


def test_max(sample_data):
    assert max(sample_data) == 5


def test_min(sample_data):
    assert min(sample_data) == 1


def test_sum_enhanced(enhanced_data):
    assert sum(enhanced_data) == 300
