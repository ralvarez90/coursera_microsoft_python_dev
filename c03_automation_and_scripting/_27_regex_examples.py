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


def extract_emails(text: str) -> list[str]:
    pattern: str = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    return re.findall(pattern, text)


def is_valid_phone_number(phone: str) -> bool:
    pattern: str = r'^(\d{3}) \d{3}-\d{4}$'
    return bool(re.match(pattern, phone))


def is_valid_http_url(url: str) -> bool:
    pattern: str = r'^https?://[^\s]+'
    return bool(re.match(pattern, url))


def is_valid_email(email: str) -> bool:
    pattern: str = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return bool(re.match(pattern, email))


def run_tests_validate_email():
    emails_to_test = (
        'test@example.com',
        'invalid.email',
        'another_test@domain.co.uk',
        'not_valid@.com',
        'user+123@company.net',
    )

    for email in emails_to_test:
        print(f'Email: {email} - Valid: {is_valid_email(email)}')


# Run application
if __name__ == '__main__':

    # Example 1
    emails_txt = 'Contactos: juan@mail.com, ana_89@empresa.org, test@.com'
    emails = extract_emails(emails_txt)
    print(f'Emails: ')
    [print(f'- {email}') for email in emails]

    # Example 2
    user_input_phone = input('Phone number: ')
    if is_valid_phone_number(user_input_phone):
        print(f'Phone number is valid: "{user_input_phone}"')
    else:
        print(f'Phone number is invalid: "{user_input_phone}"')

    # Example 3
    user_input_url = input('URL: ')
    if is_valid_http_url(user_input_url):
        print(f'URL is valid: "{user_input_url}"')
    else:
        print(f'URL is invalid: "{user_input_url}"')

    # Example 4
    run_tests_validate_email()
