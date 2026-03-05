"""
RETO: USANDO EL DEBUGGER
"""


def calculate_discount(price: int | float, discount_percentage: int | float):
    discount_amount = price * (discount_percentage / 100)
    discounted_price: float = price - discount_amount
    return discounted_price


if __name__ == '__main__':
    test_price = 50
    discount = 20
    final_price = calculate_discount(test_price, discount)
    print(final_price)
