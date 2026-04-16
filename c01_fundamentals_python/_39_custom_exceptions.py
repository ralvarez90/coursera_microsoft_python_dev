"""
EXCEPCIONES PERSONALIZADAS

Podemos crear tipos de excepciones de manera personalizada. Únicamente es heredad de la
clase Exception.
"""


class InvalidCredentialException(Exception):
    """
    Tipo de excepción que controla si un usUario tiene o no credenciales
    válidas y/o vigentes.
    """
    pass


def validateCredentials(username: str, password: str):
    raise InvalidCredentialException('Incorrect username or password.')


def readFileContents(file_path: str) -> str | None:
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError as e:
        print(e)


# Run application
try:
    validateCredentials(username='peter', password='123@12')
    readFileContents(file_path='inexistente.txt')
except InvalidCredentialException as e:
    print(e)
except FileNotFoundError as e:
    print(e)
finally:
    print('Finally! This code is executed')
