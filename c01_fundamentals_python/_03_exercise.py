"""
EJERCICIO

Almacena enteros por consola, se usan condicionales y se muestra resultado
por consola.jn
"""

# Age input data
user_age: int = int(input('Your age: '))

# Set the initial value for a ticket
price_ticket: int | None = None

# If, elif and else block
if user_age < 12:
    price_ticket = 8
elif 12 <= user_age <= 64:
    price_ticket = 12
else:
    price_ticket = 10

# Show results
if not price_ticket is None:
    print(f'Your price is: ${price_ticket:,.2f}')
