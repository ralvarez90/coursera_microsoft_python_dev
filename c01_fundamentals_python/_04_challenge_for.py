"""
RETO

Escribe un programa que defina una constante con un valor máximo, itere
sobre la secuencia 0, 1, 2, ..., 50 e imprime el número si es múltiplo de
3 y 4.
"""

# Set maximum value.
MAX_VALUE: int = 50

# Iterate over sequence 0, 1, ..., MAX_VALUE.
for i in range(MAX_VALUE + 1):

    # Multiplicity test.
    if i % 3 == 0 and i % 4 == 0:
        print(i)
