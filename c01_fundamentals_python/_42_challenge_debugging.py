"""
RETO: USANDO EL DEBUGGER
"""


def calculateDiscount(price: int | float, discountPercentage: int | float):
    discountAmount = price * (discountPercentage / 100)
    discountedPrice: float = price - discountAmount
    return discountedPrice


if __name__ == '__main__':
    testPrice = 50
    discount = 20
    finalPrice = calculateDiscount(testPrice, discount)
    print(finalPrice)
