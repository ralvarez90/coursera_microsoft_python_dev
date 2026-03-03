"""
MÓDULOS BUILT-IN

Son módulos con utilidades ya creadas y optimizadas que permiten no reinventar
la rueda.

Dentro de los módulos incluidos en el core de python tenemos:
- math
- random
- datetime
"""
from datetime import datetime
from math import factorial
from random import randint

DICE_SHOTS: int = 10


def count_vowels(text: str) -> int:
    if text in {'', None}:
        return 0

    vowels_set = set('aeiouAEIOU')
    vowels = 0
    for c in text:
        if c in vowels_set:
            vowels += 1
    return vowels


# Show factorial from some integer
print(factorial(10))

# Show some integer random
for _ in range(DICE_SHOTS):
    r = randint(1, 6)
    print(f'Dice shot: {r}')

# Show date time now
print(datetime.today())

# Count vowels
message = 'Hello World in Python3'
print(f'Vowels in "{message}" are: {count_vowels(message)}"')
