"""
EJEMPLO

Defina una función que reciba y retorne otra. Ejemplifique el uso de funciones
anidadas.

Recuerde que una función anidada tiene acceso al scope o ámbito que del cuerpo
de la función que la contiene.
"""


def make_greet(name: str) -> str:
    name = f'Hello {name.strip()}!'
    return name


def outer_function(x: int | float) -> None:
    """
    Outer function that takes an integer x, adds 5 to it, and then calls an inner
    function.

    Args:
    x (int or float): The input value that will be used in calculations.
    """

    # Add 5 to x number input
    y = x + 5

    def _inner_function():
        """
        Inner function that multiples y by 2 and print the result.
        """
        z = y * 2
        print(f'Inside _inner_function, z = {z}')

    # invoke inner function
    _inner_function()
    print(f'Inside outerFunction, y = {y}')


def main():
    # Example 1
    my_name = input('Input your name: ')
    print(make_greet(my_name) + '\n')

    # Example 2
    outer_function(x=10)


if __name__ == '__main__':
    main()
