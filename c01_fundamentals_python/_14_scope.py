"""
SCOPE (ÁMBITO O ALCANCE)

El scope o alcance es el acceso a datos dentro de nuestro código. Existe variables, funciones, objetos
y clases que están accesibles en el scope global, existe además el scope local dentro de métodos y
funciones.

Notas:
Los bloques if, while y try NO crean un nuevo scope, es decir, los bloques de control de flujo (bucles,
condicionales y manejos de error) comparten el mismo scope del entorno en el que se encuentran (ya sea
un scope global o el de una función)
"""

# Global variable
COMPANY_NAME = 'Global Tech Solutions'


def printWelcomeMsg():
    print(f'Welcome to {COMPANY_NAME.upper()}')


def printContactInfo():
    print(f'Contact {COMPANY_NAME} at info@globalsolutions.com')


if __name__ == '__main__':
    printWelcomeMsg()
    printContactInfo()
