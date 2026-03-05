"""
RETO SOBRE EXCEPCIONES

Cree una función que reciba un diccionario. Dependiendo de sus valores
puede lanzar o no cierto tipo de excepciones.
"""


def get_city_population(populations: dict[str, int], city: str) -> int:
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
    city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}

    # Input city name
    city_name = input('Input city: ').strip()
    try:
        city_population = get_city_population(city_populations, city_name)
        print(f'City population of "{city_name}" is {city_population}')
    except KeyError as e:
        print(e)
