"""
RETO

Cree un arreglo de enteros con números duplicados y utilize el tipo de dato
set para eliminar los elementos duplicados.
"""

# List with some integers
array: list[int] = [1, 2, 2, 3, 1, 4, 5, 3]

# Remove repeated numbers
uniqueSet = set(array)

# List with unique integers
uniqueArray = list(uniqueSet)
print(uniqueArray)
