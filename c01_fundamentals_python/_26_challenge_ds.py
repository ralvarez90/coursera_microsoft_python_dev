"""
RETO ESTRUCTURAS DE DATOS LISTAS
"""


def create_empty_list() -> list[str]:
    return []


# Create an empty list
shopping_cart: list[str] = create_empty_list()

# Add some items
shopping_cart.append('apple')
shopping_cart.append('banana')
shopping_cart.append('milk')

# show products
for item in shopping_cart:
    print(item.title())
