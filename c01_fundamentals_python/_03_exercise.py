"""
EJERCICIO

Almacena enteros por consola, se usan condicionales y se muestra resultado
por consola.jn
"""

# Age input data
userAge: int = int(input('Your age: '))

# Set the initial value for a ticket
priceTicket: int | None = None

# If, elif and else block
if userAge < 12:
    priceTicket = 8
elif 12 <= userAge <= 64:
    priceTicket = 12
else:
    priceTicket = 10

# Show results
if not priceTicket is None:
    print(f'Your price is: ${priceTicket:,.2f}')
