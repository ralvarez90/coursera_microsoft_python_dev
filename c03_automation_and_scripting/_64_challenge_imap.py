"""
Reto de codificación: Enviar un correo electrónico de confirmación y comprobar si hay respuestas

Su tarea:

1. Escribir un script en Python que utilice smtplib para enviar un correo electrónico
de confirmación a un cliente con el asunto "Confirmación de pedido" desde su dirección
de correo electrónico.

2. El cuerpo del correo electrónico debe decir "¡Gracias por su pedido, [Nombre del cliente]!".

3. Inmediatamente después de enviar el correo electrónico, utilice imaplib para comprobar si
hay algún mensaje no leído de ese cliente en su bandeja de entrada.

4. Si encuentra un mensaje sin leer, imprima "¡Nuevo mensaje de [Nombre del cliente]!".
Si no, imprime "Todavía no hay mensajes nuevos"

5. Asuma los siguientes detalles para sus conexiones de servidor:
    Servidor SMTP: smtp.ejemplo.com
    Puerto SMTP: 587
    Servidor IMAP: imap.ejemplo.com
    Puerto IMAP: 993
    Su correo electrónico: orders@example.com
    ¡Tu Contraseña: Coursera1000!

Si quieres poner esto en práctica en un entorno real, tendrás que sustituir la información
de los servidores SMTP e IMAP, tu correo electrónico y tu contraseña por los datos y credenciales reales
de tu servidor de correo electrónico. Ten en cuenta que esto puede no funcionar con tu cuenta de
correo electrónico estándar; puede que necesites encontrar un servidor SMTP online gratuito para
correo electrónico. En una lectura anterior, configuraste SendGrid, que puede ser utilizado para
este propósito.
"""
import imaplib
import smtplib
from email.mime.text import MIMEText

# Setup for email connection
smtpServer = 'smtp.example.com'
smtpPort = 587

imapServer = 'imap.example.com'
imapPort = 993

emailUser = 'orders.examole.com'
emailPassword = 'Coursera1000'


def sendConfirmationEmail(clientEmail: str, clientName: str):
    server: smtplib.SMTP | None = None
    try:
        server = smtplib.SMTP(smtpServer, smtpPort)
        if not server:
            raise Exception('Cannot connect to server')

        server.starttls()
        server.login(emailUser, emailPassword)
        server.sendmail(emailUser, clientEmail, f'''
        ¡Gracias por su pedido, {clientName.title()}!
        ''')
    except Exception as e:
        print(e)
    finally:
        if server:
            server.quit()


def checkNewMessages(clientEmail: str, clientName: str):
    mail: imaplib.IMAP4_SSL | None = None
    try:
        mail: imaplib.IMAP4_SSL = imaplib.IMAP4_SSL(imapServer, imapPort)
        mail.login(emailUser, emailPassword)
        mail.select('Inbox')
        status, messages = mail.search(None, 'ALL')
        if status == 'OK':
            for num in messages[0].split():
                print(num)
                status, data = mail.fetch(num, '(RFC822)')
    except Exception as e:
        print(e)
    else:
        pass


# Example usage
if __name__ == '__main__':
    client_email = "john.smith@example.com"
    client_name = "John Smith"
    sendConfirmationEmail(client_email, client_name)
    checkNewMessages(client_email, client_name)
