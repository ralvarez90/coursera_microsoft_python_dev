"""
RETO: USANDO EL DEBUGGER
"""
import logging

# Logging configuration
logging.basicConfig(level=logging.DEBUG)


def divide(x, y):
    try:
        result = x / y
        logging.info(f'Successfully divided {x} by {y}')
        return result
    except ZeroDivisionError:
        logging.error('Division by zero attempted!')
        return None


def calculate_discount(price: float, percentage: float) -> float:
    if percentage < 0 or percentage > 100:
        raise ValueError('Discount percentage must be between 0 and 100')
    discount_amount = price * (percentage / 100)
    return price - discount_amount


if __name__ == '__main__':
    try:
        print(calculate_discount(100, 100))
    except ValueError as e:
        print(f'Error: {e}')

    divide(10, 2)
    divide(5, 0)
