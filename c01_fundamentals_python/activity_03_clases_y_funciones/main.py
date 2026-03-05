"""
ACTIVIDAD 3
"""
from typing import Union

number = Union[int, float]


class TemperatureData:

    # constructor
    def __init__(self, name: str, readings: list[number]):
        self.name = name
        self.readings = readings

    def calc_range(self) -> number:
        return max(self.readings) - min(self.readings)

    def calculate_average_temp(self) -> float:
        return sum(self.readings) / len(self.readings)

    def find_high_temp(self) -> number:
        return max(self.readings)

    def find_low_temp(self) -> number:
        return min(self.readings)


if __name__ == '__main__':
    # create sensor instance
    sensor_name = 'East Forest Road Sensor'
    sensor = TemperatureData(sensor_name, [75, 71, 68, 64, 88])

    # get average temperature
    average_temp = sensor.calculate_average_temp()
    print(f'Average temperature of senson "{sensor_name}": {average_temp} °F')

    # get highest and lowews temperatures
    highest = sensor.find_high_temp()
    lowest = sensor.find_low_temp()
    print(f'Temp extremes for sensor "{sensor_name}": Highest: {highest}, Lowest: {lowest}')

    # calculate range
    temp_range = sensor.calc_range()
    print(f'Temp range for sensor "{sensor_name}": {temp_range} °F')
