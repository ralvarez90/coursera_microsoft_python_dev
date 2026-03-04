"""
MÓDULO OS (OPERATIVE SYSTEM)

Es tu línea directa con el sistema operativo. Podemos crear y eliminar archivos
y/o directorios. Obtener información de mi directorio actual, navegar dentro del
arbol de archivos de mi sistema etc.

os.mkdir
    Permite crear un directorio.

os.rmdir
    Permite eliminar un directorio.

os.mknod
    Permite crear un archivo vacío.

os.remove
    Permite eliminar un archivo.

os.rename
    Permite cambiar el nombre de un archivo, incluso cambiarlo de ubicación.

os.getcwd
    Obtiene el directorio de trabajo actual.

os.chdir
    Permite moverte de ubicación dentro del arbol de archivos.

os.listdir
    Obtiene una lista de todos los archivos y directorios.

os.stat
    Permite obtener información detallada sobre un archivo o
    directorio.

os.path
    Submódulo que la ayuda a navegar por el sistema de rutas.

os.path.join
    Permite unir diferentes partes de una ruta.

os.path.basename
    Obtiene solo el nombre de un archivo de una ruta.

os.path.exits
    Permite verificar si una ruta existe.

"""

import os

print(f'os.path.dirname(__file__)')
print(f'\t{os.path.dirname(__file__)}')

print(f'os.getcwd()')
print(f'\t{os.getcwd()}')

print('os.listdir()')
for item in os.listdir(os.getcwd()):
    print(f'\t{item}')

print('os.altsep')
print(f'\t{os.altsep}')
