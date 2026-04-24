"""
RETO: CREAR UNA LISTA DE TAREAS

Está trabajando en un proyecto personal para crear una aplicación de lista de tareas
pendientes en línea de comandos. Desea permitir a los usuarios almacenar sus tareas
en un archivo de texto y agregar fácilmente nuevas tareas a medida que surgen.
"""

import os
import time

FILE_NAME = 'todo.txt'

taskToDo: tuple = (
    'Read a book',
    'Practice python',
    'Develop unit test',
    'Buy some food',
    'Call my mom',
)

with open(FILE_NAME, mode='w') as file:
    for task in taskToDo:
        file.write(f'{task}\n')

print('Making task list in file todo.txt. . . ')
time.sleep(10)

os.remove(FILE_NAME)
