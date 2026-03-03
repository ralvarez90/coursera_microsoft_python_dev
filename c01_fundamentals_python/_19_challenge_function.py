"""
RETO SOBRE FUNCIONES

Se crea función que calcula el diámetro a partir del radio de un círculo.
"""


def calculate_diameter_circle(radius: float) -> float:
    """Return a diameter of circle with argument radius.

    Args:
        radius (float): Radio del círculo

    Returns:
        float: Diámetro del círculo
    """
    return -1 if radius < 0 else radius * 2


def main():
    radius_input: float = float(input('Enter a radius: '))
    result_diameter = calculate_diameter_circle(radius_input)
    if result_diameter == -1:
        print(f'Invalid radius: {radius_input}')
        return

    print(f'Diameter or circle with radius {radius_input}: {result_diameter:.2f} Units')


if __name__ == '__main__':
    main()
