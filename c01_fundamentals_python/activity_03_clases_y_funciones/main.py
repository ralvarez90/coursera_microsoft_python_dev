"""
ACTIVIDAD 3
"""
from typing import Union

number = Union[int, float]


class TemperatureData:

    def __init__(self, name: str, readings: list[number]):
        self.name = name
        self.readings = readings

    def calcRange(self) -> number:
        return max(self.readings) - min(self.readings)

    def calculateAverageTemp(self) -> float:
        return sum(self.readings) / len(self.readings)

    def findHighTemp(self) -> number:
        return max(self.readings)

    def findLowTemp(self) -> number:
        return min(self.readings)


if __name__ == '__main__':
    # create sensor instance
    sensorName = 'East Forest Road Sensor'
    sensor = TemperatureData(sensorName, [75, 71, 68, 64, 88])

    # get average temperature
    averageTemp = sensor.calculateAverageTemp()
    print(f'Average temperature of sensor "{sensorName}": {averageTemp} °F')

    # get highest and lowews temperatures
    highest = sensor.findHighTemp()
    lowest = sensor.findLowTemp()
    print(f'Temp extremes for sensor "{sensorName}": Highest: {highest}, Lowest: {lowest}')

    # calculate range
    tempRange = sensor.calcRange()
    print(f'Temp range for sensor "{sensorName}": {tempRange} °F')
