"""
_29_linear_search.py

Algorítmo básico que revisa elemento por elemento. Es de fácil uso para colecciones
pequeñas.
"""
from random import randint


def linear_search(data: list, target):
    """
    Retorna el índice de la primer coincidencia de target dentro de la lista
    data.
    """

    # Validate if input data is a list
    if not isinstance(data, list):
        raise ValueError('Invalid Input: data must be a list')

    # Handle the case of an empty list
    if not data:
        return -1

    # Iterate through the list using the index
    for i in range(len(data)):
        if data[i] == target:
            return i

    # If the loop completes without finding the target, return -1.
    return -1


if __name__ == '__main__':
    # Example 1, using linear search
    list_example = ['Hello', 'World', 'Good', 'Day', 'To', 'You']
    search_1 = linear_search(list_example, 'Day')
    print(f'Result of searching "Day": {search_1}')
