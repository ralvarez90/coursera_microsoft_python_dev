"""
RETO SOBRE EXCEPCIONES

Cree una función que reciba un diccionario. Dependiendo de sus valores
puede lanzar o no cierto tipo de excepciones.
"""


def getCityPopulation(populations: dict[str, int], city: str) -> int:
    # Test type error for populations dictionary
    if not isinstance(populations, (dict, dict[str, int])):
        raise TypeError('populations argument in invalid')

    # Test for a city string type
    if not isinstance(city, str):
        raise TypeError('city argument is invalid')

    # Test for city in populations keys
    if city not in populations.keys():
        raise KeyError(f'City "{city}" not found in population info')

    # Ok
    return populations[city]


if __name__ == '__main__':

    # Data source dict
    populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

    # Input city name
    city = input('Input city: ').strip()
    try:
        population = getCityPopulation(populations, city)
        print(f'City population of "{city}" is {population}')
    except KeyError as e:
        print(e)
