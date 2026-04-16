"""
CLASES

Son estructuras de comportamiento y estado a partir de las cuales podemos
crear objetos con estado y comportamiento inicial.

Son prácticamente entidades digitales que permiten definir el comportamiento
de objetos.
"""


class SomeClassName:

    def __init__(self):
        self.msg = 'Message in SomeClassName instance'

    def showMessage(self):
        print(self.msg)


if __name__ == '__main__':
    SomeClassName().showMessage()
