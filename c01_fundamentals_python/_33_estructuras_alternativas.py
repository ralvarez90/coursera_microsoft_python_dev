"""
ESTRUCTURAS DE DATOS ALTERNATIVAS

1. Deque (colas de doble extremo)
Las colas son estructuras de datos de tipo FIFO. Son una especie de lista de elementos con
la versatilidad que permite agregar o eliminar elementos de diversas formas de manera
eficiente.

Permite implementar pilas o colas, ya que permite agregar o eliminar elementos desde ambos
extremos.

2. Heapq (Colas prioritarias)
Las colas de prioridad (heapq) es una estructura similar a una lista donde el elemento más
pequeño (o elemento con la prioridad más alta) está siempre en la parte delantera.

Se utiliza en programación de tareas, donde se necesita dar prioridad a las tareas basadas
en la urgencia o importancia.

Se emplea en el algoritmo Dijkstra para encontrar el camino más corto en una gráfica. Sirve
para implementar sistemas basados en prioridades.

En python heapq[0] siempre el elemento más pequeño.

Si necesita un maxheap, es decir que el elemento máximo sea el primer elemento, puede en
heapq.push pasar tuples, con el primer elemento el número que indicará la prioridad.

Si desea obtener los top-k elementos y no son tantos puede utilizar los métodos
heapq.nlargest y heapq.nsmallest


2. collections.Counter
Toma un iterable y cuenta las occurrencias de cada elemento única. Se puede utilizar cuando
requerimos analizar la frecuencia de palabras en un texto, recuento de elementos de una
lista, o encontrar los elementos más comunes dentro de un conjunto de datos.
"""
import heapq
from collections import deque, Counter
from random import randint

# Create a heap from a list
data = [5, 7, 9, 1, 3, 10, 2, 45, 7, 8, 99, 54, 12]
heapq.heapify(data)
print(f'Heap tras heapify: {data}')

# Insert new element
heapq.heappush(data, 4)

# Extrae el elemento más pequeño
minimum = heapq.heappop(data)
print(f'Mínimo extraído: {minimum}')
print(f'Estado del heap: {data}')

# tareas
tareas = []
heapq.heappush(tareas, (2, 'Limpiar la casa'))
heapq.heappush(tareas, (1, 'Escribir Código'))
heapq.heappush(tareas, (3, 'Ver Netflix'))
while tareas:
    priority, task = heapq.heappop(tareas)
    print(f'Ejecutando tarea "{task}" con prioridad {priority}')

# Obteniendo top-k
someData = [randint(1, 1_000) + 1 for _ in range(1_000)]

# get 3 largest
largestItems = heapq.nlargest(3, someData)
smallestItems = heapq.nsmallest(3, someData)
print(largestItems)
print(smallestItems)

# using counter
queue = deque()
queue.append('task1')
queue.append('task2')
print(queue.popleft())

# counter example
text = 'This is a sample text with some repeat words words'
wordCounts = Counter(text.split())
print(wordCounts)
