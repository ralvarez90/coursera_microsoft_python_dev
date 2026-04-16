"""
ARGUMENTOS VARIABLES

Empleamos en python los argumentos *args y **kwargs, donde args será una tuple con los
elementos que se pasan como argumento y kwargs un diccionario cuyas claves serán los
nombres de las variables que se usen.
"""


def flexibleFun(*args, **kwargs):
    print('Show args:')
    for item in args:
        print(f'- {item}')

    print()
    for k, v in kwargs.items():
        print(f'kwargs[{k}] -> {v}')


if __name__ == '__main__':
    # Example 1, no arguments
    flexibleFun()
    print('-' * 30)

    # Example 2, with variable arguments
    flexibleFun(1, 2, 3, 'Hello', 'World')
    print('-' * 30)

    # Example 3, con argumentos con nombre que se almacenan en kwargs
    flexibleFun(name='Peter', lastname='Parker', age=35)
    print('-' * 30)

    # Example 4, con argumentos que se almacenan en la tuple y en diccionario
    flexibleFun(1, 'Hello World', message='Welcome to Python!')
    print('-' * 30)

    # Example 5, destructuring
    some_numbers = [i ** 2 for i in range(1, 11)]
    print(f'some_numbers: {some_numbers}')
    flexibleFun(*some_numbers, final_msg='Bye!')
    print('-' * 30)
