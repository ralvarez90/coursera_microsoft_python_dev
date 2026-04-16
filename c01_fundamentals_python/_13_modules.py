"""
MÓDULOS

Un módulo es un archivo de python con funciones, clases, objetos que se pueden utilizar
en otros scripts en python.
"""


def showCPUCores():
    from os import cpu_count
    print(cpu_count())


if __name__ == '__main__':
    showCPUCores()
