import pytest

"""
ORGANIZACIÓN DE PRUEBAS

Principios Clave de Organización

Las pruebas bien organizadas proporcionan claridad, facilidad de comprensión en
el propósito de cada una de ellas y fácil localización. Un conjunto de pruebas 
bien estructuradas agiliza el proceso de desarrollo.

1. Modularidad
La modularidad en las pruebas significa organizar sus pruebas en unidades pequeñas 
e independientes. Cada prueba se centra en una parte específica de su código.

2. Fixtures
Permiten proporcionar un entorno de pruebas estandarizado. Permiten definir código
de configuración y desmontaje que puede compartirse en varias pruebas, lo que 
garantiza la coherencia y reduce la redundancia. 

Al utilizar fixtures, se evita repetir el mismo código de configuración y desmontaje 
en cada prueba, lo que hace que el conjunto de pruebas sea más conciso y fácil de 
mantener. También ayuda a evitar interacciones inesperadas entre las pruebas, lo 
que conduce a resultados de las pruebas más fiables y predecibles.

3. Markers (Marcadores)
Permiten clasificar y filtrar las pruebas en función de sus características. Los
marcadores integrados como mark.slow ayudan a identificar las pruebas lentas o
dependientes de la red, mientras que los marcadores personalizados permiten agrupar
las pruebas por características o funcionalidades.

Mediante la aplicación estratégica de marcadores, puede ejecutar selectivamente 
subconjuntos específicos de pruebas, optimizando sus esfuerzos de comprobación 
y ahorrando tiempo y recursos valiosos.

4. Parametrización
La parametrización en pytest le permite probar su código ejecutando la misma 
unción de prueba varias veces con diferentes valores de entrada, asegurándose 
de que funciona correctamente en diferentes condiciones. 
"""

# Define a new data type
number = int | float


class Calculator:

    def add(self, x: number, y: number) -> number:
        return x + y

    def subtract(self, x: number, y: number) -> number:
        return x - y

    def multiply(self, x: number, y: number) -> number:
        return x * y

    def divide(self, x: number, y: number) -> number:
        if y == 0:
            raise ValueError('Division by zero!')
        return x / y


class CalculatorTest:

    @pytest.fixture
    def calculator(self) -> Calculator:
        """
        Fixture que permite obtener una instancia de Calculator para usarse
        dentro de las pruebas unitarias.
        """
        return Calculator()

    def test_add(self, calculator: Calculator):
        result = calculator.add(2, 3)
        assert result == 5

    def test_subtract(self, calculator: Calculator):
        result = calculator.subtract(5, 2)
        assert result == 3

    def test_multiply(self, calculator: Calculator):
        result = calculator.multiply(4, 3)
        assert result == 12

    def test_divide(self, calculator: Calculator):
        result = calculator.divide(10, 2)
        assert result == 5.0

    def test_divide_by_zero(self, calculator: Calculator):
        with pytest.raises(ValueError):
            calculator.divide(5, 0)
