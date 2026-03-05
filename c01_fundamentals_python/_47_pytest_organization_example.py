"""
PYTEST: EJEMPLO DE PRUEBAS ORGANIZADAS
"""
import random
import pytest


class Product:
    def __init__(self, name: str, price: float, quantity: int = 1):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'Product(name="{self.name}", price={self.price:.2f}, quantity={self.quantity})'


class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product: Product):
        self.items.append(product)

    def calculate_total_price(self, tax_rate: float = 0, shipping_fee: float = 0) -> int | float:
        subtotal = sum(item.price * item.quantity for item in self.items)
        tax = subtotal * tax_rate
        return subtotal + tax + shipping_fee

    def apply_discount(self, discount_percentage: float):
        for item in self.items:
            item.price *= (1 - discount_percentage / 100)

    def checkout(self, payment_gateway):
        total_price = self.calculate_total_price()
        # ...
        return True


class TestProductFunctions:

    def test_add_to_cart_successful(self):
        cart = Cart()
        product = Product('Widget', 10)
        cart.add_to_cart(product)
        assert len(cart.items) == 1
        assert cart.items[0] == product

    def test_calculate_total_price(self):
        cart = Cart()
        cart.add_to_cart(Product('Widget A', 15.0))
        cart.add_to_cart(Product("Widget N", 20.0, 2))
        total = cart.calculate_total_price(tax_rate=0.07, shipping_fee=5.0)
        expected_total = (15.0 + 20.0 * 2) * 1.07 + 5.0
        assert total == expected_total

    def test_apply_discount_correctly(self):
        cart = Cart()
        cart.add_to_cart(Product('Discounted Item', 50.0))
        cart.apply_discount(20)
        assert cart.items[0].price == 40

    def test_checkout_successful_payment(self):
        cart = Cart()
        assert cart.checkout(payment_gateway=None) is True
