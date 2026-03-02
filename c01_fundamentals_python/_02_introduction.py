"""
INTRODUCCIÓN Y EJEMPLO

Ejemplo básico de definición de variables, funciones, print e
invocación de funciones.
"""


def example01():
    length = 10
    width = 5
    area = length * width
    print(f'area: {area:,.2f} u^2')


def main():
    example01()


# run application
if __name__ == '__main__':
    main()
