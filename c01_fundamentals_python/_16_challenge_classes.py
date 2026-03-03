"""
RETO SOBRE CLASES

Diseñe e implemente una clase Dog que cuente con las propiedades
nombre y raza.
"""


class Dog:
    """
    Represents all dogs in a basic template.
    """

    def __init__(self, name: str, breed: str):
        self.name = name.strip().title()
        self.breed = breed.strip().title()

    def bark(self):
        print(f'Woof! My name is {self.name} and I\'m a {self.breed}')


if __name__ == '__main__':
    myDog = Dog('Buddy', 'Golden Retriever')
    myDog.bark()
