"""
MANEJO DE EXCEPCIONES: try, except, else, finally

Python cuenta con los siguientes bloques de código para manejar excepciones. Se emplea
el try para contener código que pueda fallar, except para establecer determinado bloque
para determinados tipos de errores, else para ejecutarse si no existe ninguna excepción
y por último para ejecutar determinado bloque independiente si ocurre o no una excepción
durante la ejecución.
"""

try:
    int('Hello World')
except FileExistsError:
    print('Error: File not found!')
except ValueError:
    print('Error: Invalid value entered!')
except Exception as e:
    print(f'An unexpected error occurred: {e}')
else:
    print('Everything is fine!')
finally:
    print('Finally! This code always is executed')
