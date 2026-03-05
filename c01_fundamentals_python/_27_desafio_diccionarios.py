"""
RETO
Uso de diccionarios.
"""


class Product:

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
        }


products = {
    'SKU123': Product('Widget A', 19.99, 50).to_dict(),
    'SKU456': Product('Gadget B', 34.95, 25).to_dict(),
    'SKU789': Product('Gizmo C', 9.99, 100_1000).to_dict(),
}

# Search product
sku_to_find = 'SKU123'
for sku in products.keys():
    if sku == sku_to_find:
        print('-' * 50)
        print(products[sku])
        print(f'The price of {products[sku]["name"]} is ${products[sku]["price"]:,.2f}')
        print('-' * 50)

# Show all products
for product in products.values():
    print(f'- {product}')
