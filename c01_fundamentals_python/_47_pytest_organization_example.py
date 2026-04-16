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

    def addToCart(self, product: Product):
        self.items.append(product)

    def calculateTotalPrice(self, taxRate: float = 0, shippingFee: float = 0) -> int | float:
        subtotal = sum(item.price * item.quantity for item in self.items)
        tax = subtotal * taxRate
        return subtotal + tax + shippingFee

    def applyDiscount(self, discountPercentage: float):
        for item in self.items:
            item.price *= (1 - discountPercentage / 100)

    def checkout(self, paymentGateway):
        total_price = self.calculateTotalPrice()
        # ...
        return True


class TestProductFunctions:

    def testAddToCartSuccessful(self):
        cart = Cart()
        product = Product('Widget', 10)
        cart.addToCart(product)
        assert len(cart.items) == 1
        assert cart.items[0] == product

    def testCalculateTotalPrice(self):
        cart = Cart()
        cart.addToCart(Product('Widget A', 15.0))
        cart.addToCart(Product("Widget N", 20.0, 2))
        total = cart.calculateTotalPrice(taxRate=0.07, shippingFee=5.0)
        expectedTotal = (15.0 + 20.0 * 2) * 1.07 + 5.0
        assert total == expectedTotal

    def testApplyDiscountCorrectly(self):
        cart = Cart()
        cart.addToCart(Product('Discounted Item', 50.0))
        cart.applyDiscount(20)
        assert cart.items[0].price == 40

    def testCheckoutSuccessfulPayment(self):
        cart = Cart()
        assert cart.checkout(paymentGateway=None) is True
