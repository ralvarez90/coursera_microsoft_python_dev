"""
RETO SOBRE FUNCIONES

Se crea función que calcula el diámetro a partir del radio de un círculo.
"""


def calculateDiameterCircle(radius: float) -> float:
    """Return a diameter of circle with argument radius.

    Args:
        radius (float): Radio del círculo

    Returns:
        float: Diámetro del círculo
    """
    return -1 if radius < 0 else radius * 2


def main():
    radiusInput: float = float(input('Enter a radius: '))
    resultDiameter = calculateDiameterCircle(radiusInput)
    if resultDiameter == -1:
        print(f'Invalid radius: {radiusInput}')
        return

    print(f'Diameter or circle with radius {radiusInput}: {resultDiameter:.2f} Units')


if __name__ == '__main__':
    main()
