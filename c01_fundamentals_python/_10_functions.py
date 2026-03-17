"""
FUNCIONES

Son bloques de código reutilizables. Permiten además organizar el código de manera
que es más fácil de mantener.
"""

# Define a new number type.
number = int | float


def show_welcome_message():
    print('Welcome to Python Programming Language')


def get_rectangle_area(length: number, width: number) -> number:
    """
    Calcula el área de un rectángulo dado su largo y ancho. Retorna -1
    si se ingresan valores inválidos.
    """
    if length < 0 or width < 0:
        error_msg = f'Error: length "{length}" and width: "{width}" must be >= 0.'
        raise ValueError(error_msg)

    return length * width


if __name__ == '__main__':
    show_welcome_message()

    try:
        print(get_rectangle_area(1, 2))
        print(get_rectangle_area(1.6, 1_000.45))
        print(get_rectangle_area(1, -2))
    except ValueError as e:
        print(e)
