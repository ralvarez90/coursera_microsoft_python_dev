"""
SELECCIÓN DE ESTRUCTURAS DE DATOS

Ejemplifica la eficiencia de algoritmos dependiendo del tipo de estructura
de datos que se elige.
"""
import timeit

RANGE_LIMIT: int = 1_000_000

# List lookup
list_data = list(range(RANGE_LIMIT))
lookup_value = 999_999
list_time = timeit.timeit(lambda: lookup_value in list_data, number=1_000)

# Dictionary lookup
dict_data = {i: i for i in range(RANGE_LIMIT)}
dict_time = timeit.timeit(lambda: lookup_value in dict_data.keys(), number=1_000)

# Set lookup
set_time = timeit.timeit(lambda: lookup_value in set(list_data), number=1_000)

# show results
print(f'List lookup time: {list_time:5.2f} seconds...')
print(f'Dict lookup time: {dict_time:5.2f} seconds...')
print(f'Set  lookup time: {set_time:5.2f} seconds...')
