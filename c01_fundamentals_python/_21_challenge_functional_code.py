"""
RETO FUNCIONES

Escribir tres funciones Python que implementen una sencilla herramienta de 
conversión de temperatura. Ten cuidado de escribir correctamente los
nombres de los métodos.
"""
from enum import Enum

# Types
number = int | float


class TemperatureUnit(Enum):
    C = 1
    F = 2


def convertTemperature(temperature: number, unit: TemperatureUnit):
    match unit:
        case TemperatureUnit.C:
            return temperature * 9 / 5 + 32
        case TemperatureUnit.F:
            return (temperature - 32) * 5 / 9


if __name__ == '__main__':
    # Define temperatures
    temperatureC: number = 25
    temperatureF: number = 77

    # Get converted temperatures
    convertedF = convertTemperature(temperatureC, TemperatureUnit.C)
    convertedC = convertTemperature(temperatureF, TemperatureUnit.F)

    # Show results
    print(f'{temperatureC:.2f}°C is equal to {convertedF:.2f}°F')
    print(f'{temperatureF:.2f}°F is equal to {convertedC:.2f}°C')
