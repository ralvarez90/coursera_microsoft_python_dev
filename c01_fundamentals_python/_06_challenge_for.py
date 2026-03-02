"""
RETO

Itera sobre la secuencia 10, 9, ..., 0 y muestra un mensaje cuando la mitad
haya sido recorrida.
"""

# Global message
MIDPOINT_MESSAGE: str = 'Midpoint reached.'

# Sequence 10, 9, ..., 0.
for x in range(10, -1, -1):
    if x == 5:
        print(MIDPOINT_MESSAGE)
        continue
    print(x)
