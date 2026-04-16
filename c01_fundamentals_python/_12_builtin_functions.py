"""
FUNCIONES INTEGRADAS

Python íntegra funciones dentro de su scope global listas para usarse
dentro de sus programas.

Algunas son:
- print
- len
- input
- type
- int
- float
- str
- min
- max
- sum
- isinstance
...

Notas:
- Algunas de las consideradas built-in functions en python en realidad
son nombres de clases, es decir tipos de datos cuyo al usarse generar una
nueva instancia.
"""


def exercise01Builtin():
    # Initial temperatures
    antarcticTemperatures: list[float] = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

    # Find the highest and lowest temperatures
    highestTemp = max(antarcticTemperatures)
    lowestTemp = min(antarcticTemperatures)
    print(f'Highest temperature: {highestTemp:.2f} °C')
    print(f'Lowest  temperature: {lowestTemp:.2f} °C')

    # Calculate average temperature
    averageTemp: float | None = round(
        sum(antarcticTemperatures) / len(antarcticTemperatures), ndigits=2,
    ) if len(antarcticTemperatures) > 0 else None

    # Test the size of the list.
    if averageTemp is None:
        raise ValueError('Antarctic temperatures lista cannot be empty.')

    # Show average result
    print(f'Average temperature: {averageTemp} °C')

    # Find the absolute value of the coldest temperature
    coldestTempAbs = abs(lowestTemp)
    print("The coldest temperature was", coldestTempAbs, "°C below freezing.")


def exercise02Builtin():
    # Init values
    intValue = 15
    fltValue = 4.1
    txtValue = '33'

    # Type of float value
    typeOfFloatValue = type(fltValue)

    # Convert txtValue to an integer
    txtValueAsInt = int(txtValue)

    # Convert intValue to text
    intValueAsText = str(intValue)

    # Print the type of fltValue
    print("fltValue type:", typeOfFloatValue)

    # Adding text_value_as_int to intValue
    print("Integer addition: Adding text_value_as_int (33) to intValue (15):", txtValueAsInt + intValue)

    # Adding (concatenating) text values
    print("Text addition: Adding txtValue (33) to intValueAsText (15):", txtValue + intValueAsText)


if __name__ == '__main__':
    exercise01Builtin()
    exercise02Builtin()
