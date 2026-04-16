"""
SELECCIÓN DE ESTRUCTURAS DE DATOS

Ejemplifica la eficiencia de algoritmos dependiendo del tipo de estructura
de datos que se elige.
"""
import timeit

RANGE_LIMIT: int = 1_000_000

# List lookup
listData = list(range(RANGE_LIMIT))
lookupValue = 999_999
listTime = timeit.timeit(lambda: lookupValue in listData, number=1_000)

# Dictionary lookup
dictData = {i: i for i in range(RANGE_LIMIT)}
dictTime = timeit.timeit(lambda: lookupValue in dictData.keys(), number=1_000)

# Set lookup
setTime = timeit.timeit(lambda: lookupValue in set(listData), number=1_000)

# show results
print(f'List lookup time: {listTime:5.2f} seconds...')
print(f'Dict lookup time: {dictTime:5.2f} seconds...')
print(f'Set  lookup time: {setTime:5.2f} seconds...')
