"""
RETO

Crea una lista de temperaturas y genera un ciclo for que retorne el
equivalente en otra escala.
"""

# Type definitions
number = int | float


def main():
    # Temperaturas en grados Celsius.
    celsiusTemperatures: list[number] = [0, 10, 25, 32, 100]

    # Crea lista vacía de resultados.
    fahrenheitTemperatures: list[number] = []

    # Itera sobre lista de Celsius y genera el equivalente en Fahrenheit,
    for celsius in celsiusTemperatures:
        _auxTemp = (celsius * 9 / 5) + 32
        fahrenheitTemperatures.append(_auxTemp)

    # Show results
    print(f'Celsius Temperatures    : {celsiusTemperatures}')
    print(f'Fahrenheit Temperatures : {fahrenheitTemperatures}')


# Run application
if __name__ == '__main__':
    main()
