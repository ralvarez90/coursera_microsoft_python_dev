"""
RETO

Escriba un programa que defina una lista de enteros y se indique
cual es número par e impar.
"""

# Initial integer list.
numbers: list[int] = [3, 9, 1, 10, 5, 2, 8]

# Parity test.
for n in numbers:
    if n % 2 == 0:
        print(f'{n:3d} is even.')
    else:
        print(f'{n:3d} is odd.')
