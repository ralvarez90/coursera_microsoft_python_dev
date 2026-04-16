import random


# caso 1, sin parámetros y sin valor de retorno
def happyBirthday(age: int | None = None, name: str | None = None):
    if age and name:
        print(f'Welcome {name.title()}, happy {age} years old!')
        return

    if age:
        print(f'Welcome, happy {age} years old!')
        return

    if name:
        print(f'Welcome {name.title()} happy birthday!')
        return

    print(f'Welcome!')


# caso 3, sin parámetros y con valor de retorno
def getLuckyNumber():
    return random.randint(1, 100)


# caso 4, parámetros y valor de retorno
def calcSalePrice(amount, member):
    percentDiscount = 0.15 if member else 0.05
    return amount - (amount * percentDiscount)


if __name__ == '__main__':
    lucky_number = getLuckyNumber()
