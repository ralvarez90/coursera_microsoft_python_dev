"""
EXCEPCIONES

Mecanismo mediante el cual se puede controlar el flujo de una aplicación
durante eventos inesperados en la ejecución de un programa.

Cuando ocurre un problema de este tipo, python crea una instancia de la
clase Exception, permitiendo extraer información sobre dicha excepción,
esto nos permite manejar nuestro código ante diferentes posibles escenarios
de error.

Python proporciona try-exception-else para el manejo de las excepciones.
Son muy similares.

Podemos agregar múltiples bloques de excepción para poder manejar y controlar
diversos tipos específicos de excepciones como ValueError, FileNotFoundError,
PermissionError, etc.

Dentro de las excepciones más comunes tenemos:

NameError
Se genera cuando intentamos acceder a una variable no definida previamente.

ZeroDivisionError
Cuando se intenta realizar una división entre 0.

FileNotFoundError
Cuando se desea acceder a un archivo inexistente.

TypeError
Cuando se intenta realizar una operación no soportado por un determinado
tipo de dato.

ValueError
Cuando se intenta pasar un argumento a una función pero su tipo es inválido.

IndexError
Cuando intenta acceder a un elemento de una lista mediante un índice fuera
del rango.

ImportError
Se genera cuando se requiere importar un módulo de python pero este no
existe.

KeyError
Se genera cuando si intenta usar una llave en un diccionario pero dicho key
no existe en su interior.

AttributeError
Se genera cuando se intenta acceder a un atributo de un objeto pero dicho atributo
no existe.

SyntaxError
Se produce cuando hay un error de sintaxis en el código.
"""
from random import randint, choice

# Global constants
LOWER_BOUND = 0
UPPER_BOUND = 1000

# New types
number = int | float


def getIntegerDivision(x: number, y: number) -> float:
    return x / y


if __name__ == '__main__':

    # For example, 1.
    intents: int = 0

    # For example 2.
    myDict = {'a': 1, 'b': 2}
    randomKey: str = choice(list('abc'))

    # For example, 3.
    num1 = randint(LOWER_BOUND, UPPER_BOUND)
    num2 = randint(LOWER_BOUND, UPPER_BOUND)
    try:
        # Example 1.
        result = getIntegerDivision(num1, num2)
        print(f'{num1:3d} / {num2:3d} = {result:5.2f}')
        intents += 1

        # Example 2.
        print(f'my_dict[{randomKey}] -> {myDict[randomKey]}')
    except ZeroDivisionError:
        errMsg = f'Error al dividir x: {num1}/{num2}: Error en el intento {intents}.'
        print(errMsg)
    except KeyError:
        errMsg = f'Error al acceder al key {randomKey}.'
        print(errMsg)
    finally:
        print('Saliendo del programa. . . \n')

    # End message.
    input('\nPress any key to continue . . . ')
