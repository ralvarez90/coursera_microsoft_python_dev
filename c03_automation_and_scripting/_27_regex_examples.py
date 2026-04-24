"""
EJEMPLOS DE USO

1. Patrón: \d+
Coincide con 1 o más dígitos.

2. Patrón: [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
Este patrón coincide con direcciones de correo electrónico. Busca una parte local
(nombre de usuario) que contenga letras, números y símbolos específicos,
seguida de un símbolo '@', un nombre de dominio con letras, números, guiones y
puntos, y un dominio de nivel superior (por ejemplo, .com, .org) de al
menos dos letras.

3. Patrón: \b\w+\b
Coincide con las palabras individuales. \b indica los límites de las palabras, lo que
garantiza que coincide con palabras completas, \w coincide con cualquier carácter de
palabra (letras, números y guiones bajos)

4. Patrón: \d{3}-d{3}-\d{4}
Este patrón coincide con números de teléfono con el formato 'XXX-XXX-XXXX'. \d{3}
coincide exactamente con tres dígitos, y los guiones coinciden con
guiones literales.

5. Patrón: https?://[^\s]+
Este patrón coincide con URL (direcciones web).
"""
import re


def extractEmails(text: str) -> list[str]:
    pattern: str = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.findall(pattern, text)


def isValidPhoneNumber(phone: str) -> bool:
    pattern: str = r'^(\d{3}) \d{3}-\d{4}$'
    return bool(re.match(pattern, phone))


def isValidHttpURL(url: str) -> bool:
    pattern: str = r'^https?://[^\s]+'
    return bool(re.match(pattern, url))


def isValidEmail(email: str) -> bool:
    pattern: str = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return bool(re.match(pattern, email))


def runTestsValidateEmail():
    emails_to_test = (
        'test@example.com',
        'invalid.email',
        'another_test@domain.co.uk',
        'not_valid@.com',
        'user+123@company.net',
    )

    for email in emails_to_test:
        print(f'Email: {email} - Valid: {isValidEmail(email)}')


# Run application
if __name__ == '__main__':

    # Example 1
    emailsTxt = 'Contactos: juan@mail.com, ana_89@empresa.org, test@.com'
    emails = extractEmails(emailsTxt)
    print(f'Emails: ')
    for email in emails:
        print(f'- {email}')

    # Example 2
    userInputPhone = input('Phone number: ')
    if isValidPhoneNumber(userInputPhone):
        print(f'Phone number is valid: "{userInputPhone}"')
    else:
        print(f'Phone number is invalid: "{userInputPhone}"')

    # Example 3
    userInputURL = input('URL: ')
    if isValidHttpURL(userInputURL):
        print(f'URL is valid: "{userInputURL}"')
    else:
        print(f'URL is invalid: "{userInputURL}"')

    # Example 4
    runTestsValidateEmail()
