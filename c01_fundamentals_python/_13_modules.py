"""
MÓDULOS

Un módulo es un archivo de python con funciones, clases, objetos que se pueden utilizar
en otros scripts en python.
"""


def show_cpu_cores():
    from os import cpu_count
    print(cpu_count())


if __name__ == '__main__':
    show_cpu_cores()
