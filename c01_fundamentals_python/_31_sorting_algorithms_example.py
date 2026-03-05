"""
ALGORITMOS DE ORDENAMIENTO

Ejemplos.
"""

import random


def simplesort(cards: list) -> list:
    """
    Función simple de ordenamiento.

    Args:
        cards (list): Lista de cartas a ordenar.

    Returns:
        list: Lista de cartas ordenadas.
    """

    # Lista vacía de cartas ordenadas.
    sorted_cards = []

    # Evalúa en true siempre que cartas no sea una lista vacía.
    while cards:
        # Obtiene carta más pequeña y la agrega a la lista de cartas ordenadas.
        lowest_card = min(cards)
        sorted_cards.append(lowest_card)

        # Remueve la primera ocurrencia de la carta más pequeña.
        cards.remove(lowest_card)

    # Retorna lista de cartas ya ordenadas.
    return sorted_cards


def quicksort(cards) -> list:
    # Caso base
    if len(cards) < 2:
        return cards

    # Obtiene pivote como primer elemento
    pivot = cards[0]

    # Obtiene lista sin el primer elemento con elementos menores al pivote
    less = [i for i in cards[1:] if i <= pivot]

    # Obtiene lista sin el primer elemento con los elementos mayores al pivote
    greater = [i for i in cards[1:] if i > pivot]

    # Paso recursivo
    return quicksort(less) + [pivot] + quicksort(greater)


if __name__ == '__main__':

    TOTAL_NUMBERS = 1_000_000

    # Generamos lista de 1_000_000 elementos
    random_integers = [random.randint(1, 1_000_001) for _ in range(TOTAL_NUMBERS)]
    print(f'random_integers generated OK...\n')

    # Ordenamiento con algoritmo quicksort
    sorted_integers = quicksort(random_integers)
    print(f'Length of sorted_integers: {len(sorted_integers)}')
    print('Sorted with quicksort is end...\n')
    exit()

    # Show numbers in a sorted list
    print('Sorted list:')
    [print(f'- {i}') for i in sorted_integers]

    # Test de contingencia
    if 1_000_000 in set(sorted_integers):
        print('1000000 exists in sorted integers')

    _ = input('\nPress any key to continue . . . ')
