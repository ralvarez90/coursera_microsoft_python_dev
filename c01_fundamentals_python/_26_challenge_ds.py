"""
RETO ESTRUCTURAS DE DATOS LISTAS
"""


def createEmptyList() -> list[str]:
    return []


# Create an empty list
shoppingCart: list[str] = createEmptyList()

# Add some items
shoppingCart.append('apple')
shoppingCart.append('banana')
shoppingCart.append('milk')

# show products
for item in shoppingCart:
    print(item.title())
