"""
RETO GENERACIÓN DE DICCIONARIO

Generar diccionario con información de un estudiante.
"""
from pprint import pprint

# Dictionary definition
someStudent = {
    'name': 'Ana García',
    'age': 16,
    'address': 'Calle Falsa 123',
    'esta_inscrito': True,
    'calificaciones': {'maths': 9.0, 'geography': 10},
    'house_coords': (123.123, 123.123),
    'intereses': ['Música', 'Futbol']
}

# Show dict
pprint(someStudent)
