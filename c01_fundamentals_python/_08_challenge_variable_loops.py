"""
RETO

Crea una lista de temperaturas y genera un ciclo for que retorne el
equivalente en otra escala.
"""

# Type definitions
number = int | float


def main():
    # Temperaturas en grados Celsius.
    celsius_temperatures: list[number] = [0, 10, 25, 32, 100]

    # Crea lista vacía de resultados.
    fahrenheit_temperatures: list[number] = []

    # Itera sobre lista de Celsius y genera el equivalente en Fahrenheit,
    for celsius in celsius_temperatures:
        _auxTemp = (celsius * 9 / 5) + 32
        fahrenheit_temperatures.append(_auxTemp)

    # Show results
    print(f'Celsius Temperatures    : {celsius_temperatures}')
    print(f'Fahrenheit Temperatures : {fahrenheit_temperatures}')


# Run application
if __name__ == '__main__':
    main()
