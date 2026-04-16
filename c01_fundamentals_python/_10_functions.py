"""
FUNCIONES

Son bloques de código reutilizables. Permiten además organizar el código de manera
que es más fácil de mantener.
"""

# Define a new number type.
number = int | float


def showWelcomeMessage():
    print('Welcome to Python Programming Language')


def getRectangleArea(length: number, width: number) -> number:
    """
    Calcula el área de un rectángulo dado su largo y ancho. Retorna -1
    si se ingresan valores inválidos.
    """
    if length < 0 or width < 0:
        error_msg = f'Error: length "{length}" and width: "{width}" must be >= 0.'
        raise ValueError(error_msg)

    return length * width


if __name__ == '__main__':
    showWelcomeMessage()

    try:
        print(getRectangleArea(1, 2))
        print(getRectangleArea(1.6, 1_000.45))
        print(getRectangleArea(1, -2))
    except ValueError as e:
        print(e)
