"""
INTRODUCCIÓN A LAS LISTAS

Las listas son instancias de la clase list. Son secuencias iterables de valores
donde cada elemento puede ser accedido por su índice. Podemos crear listas mediante
expresiones.

Son on colecciones mutables, indexadas de elementos que pueden ser de cualquier
tipo.

Se pueden crear de forma literal o por compresión mediante expresiones de la 
forma:
    [expression for item in iterable]

Son objetos con propiedades y métodos, dentro de los más comunes tenemos:

len(list)
    Indica el número de elementos de la lista.

.append(x)
    Agrega x al final de la lista.

.insert(i, x)
    Agrega x en el índice i.

.remove(x)
    Elimina el primer elemento x dentro de la lista.

.sort()
    Ordena la lista

.reverse()
    Invierte el orden de los elementos de la lista

.count(x)
    Retorna el número de veces de x contenida en la lista

x in list
    Comprueba la existencia de x en la lista

.index(x)
    Retorna primera posición de x en index
"""

# List with score test
test_scores: list[int] = [55, 70, 78, 52, 68]

# Calculation
curve_amount = 10
curved_grades = [score + curve_amount for score in test_scores]

# Results
print(f'Original scores: {test_scores}')
print(f'Curved scores  : {curved_grades}')
