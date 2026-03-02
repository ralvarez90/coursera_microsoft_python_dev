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


def exercise01_builtin():
    # Initial temperatures
    antarctic_temperatures: list[float] = [-25.5, -28.0, -26.3, -23.8, -27.1, -24.9, -29.2]

    # Find the highest and lowest temperatures
    highest_temp = max(antarctic_temperatures)
    lowest_temp = min(antarctic_temperatures)
    print(f'Highest temperature: {highest_temp:.2f} °C')
    print(f'Lowest  temperature: {lowest_temp:.2f} °C')

    # Calculate average temperature
    average_temp: float | None = round(
        sum(antarctic_temperatures) / len(antarctic_temperatures), ndigits=2,
    ) if len(antarctic_temperatures) > 0 else None

    # Test the size of the list.
    if average_temp is None:
        raise ValueError('Antarctic temperatures lista cannot be empty.')

    # Show average result
    print(f'Average temperature: {average_temp} °C')

    # Find the absolute value of the coldest temperature
    coldest_temp_abs = abs(lowest_temp)
    print("The coldest temperature was", coldest_temp_abs, "°C below freezing.")


def exercise02_builtin():
    # Init values
    int_value = 15
    float_value = 4.1
    text_value = '33'

    # Type of float value
    type_of_float_value = type(float_value)

    # Convert text_value to an integer
    text_value_as_int = int(text_value)

    # Convert int_value to text
    int_value_as_text = str(int_value)

    # Print the type of float_value
    print("float_value type:", type_of_float_value)

    # Adding text_value_as_int to int_value
    print("Integer addition: Adding text_value_as_int (33) to int_value (15):", text_value_as_int + int_value)

    # Adding (concatenating) text values
    print("Text addition: Adding text_value (33) to int_value_as_text (15):", text_value + int_value_as_text)


if __name__ == '__main__':
    exercise01_builtin()
    exercise02_builtin()
