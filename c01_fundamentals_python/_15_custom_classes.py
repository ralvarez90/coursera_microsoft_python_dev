"""
CLASES

Las clases pueden implementarse como abstractas para poder ser heredadas o
implementadas por otras clases.

Pueden tener atributos, métodos, y métodos especiales inicializadores como
__init__.
"""
from abc import ABC, abstractmethod


class BankAccount:
    """
    This class represents all accounts of any bank.
    """

    def __init__(self, balance: float = 0):
        self._balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
        else:
            print('Error: Cannot deposit negative or 0 amount in account balance.')

    def getBalance(self) -> float:
        return self._balance


class Animal(ABC):
    """
    Clase abstracta que define la interfaz a implementar de cualquier
    clase que sea un animal.
    """

    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    """
    Clase que representa a todos los lomitos del mundo, como implementa la clase
    abstracta Animal, debe implementar los métodos abstractos definidos en la
    interfaz.
    """

    def make_sound(self):
        print('Barf barf!')


class Car:
    """
    Represents all standard cars.
    """
    __is_on = False

    def __init__(self, make: str, model: str, year: int, color: str):
        self.make = make.strip().title()
        self.model = model.strip().title()
        self.year = year
        self.color = color.strip().title
        self.fuel_level = 100
        self.__is_on = False

    def start_engine(self):
        if not self.__is_on:
            self.__is_on = True
            print(f'The {self.year} {self.make} {self.model}\'s engine roars to life!')
        else:
            print(f'The {self.year} {self.make} {self.model}\'s is ON!')

    def off_engine(self):
        if self.__is_on:
            self.__is_on = False
        else:
            print('This car is off')

    def accelerate(self):
        if self.__is_on:
            print(f"The {self.color} {self.make} {self.model} picks up speed!")
        else:
            print('This car is off')

    def brake(self):
        if self.__is_on:
            print(f"The {self.make} {self.model} comes to a smooth stop.")
        else:
            print('This car is off')


if __name__ == '__main__':
    # example 1, create an account
    bbva_account = BankAccount(balance=10_000)
    bbva_account.deposit(123)
    print(f'BBVA balance: ${bbva_account.getBalance():,.2f}')

    # example 2, create an animal dog
    uma = Dog()
    uma.make_sound()

    # example 3, create a car
    mustang: Car = Car('Ford', 'Mustang', 1987, 'Black')
    mustang.start_engine()
    mustang.start_engine()
    mustang.accelerate()
    mustang.brake()
    mustang.off_engine()
    mustang.off_engine()
