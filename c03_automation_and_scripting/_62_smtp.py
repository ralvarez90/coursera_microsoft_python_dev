"""
ENVÍO Y RECEPCIÓN DE CORREO ELECTRÓNICO

Python, con su rico ecosistema de bibliotecas, ofrece potentes herramientas para
automatizar las tareas del correo electrónico, agilizando el flujo de trabajo y
ahorrando un tiempo valioso. Python ofrece bibliotecas como smtplib y imaplib de
Python, guiándole a través del proceso de envío de correos electrónicos personalizados,
obtención de mensajes y gestión de archivos adjuntos.

1. SMTPLIB

Básicamente, smtplib actúa como un cliente que se conecta a un servidor de correo (como
el de Gmail, Outlook o Mailtrap) para entregarle un mensaje y que este lo reenvíe al
destinatario.

Para enviar un correo, Python sigue estos pasos:

1. Establecer conexión con el servidor SMTP (especificando host y puerto).
2. Iniciar una conexión segura (TLS).
3- Autenticarse con usuario y contraseña.
4. Enviar el mensaje.
5. Cerrar la conexión.


En el corazón de smtplib se encuentra la clase SMTP. Esta clase actúa como puente con
el servidor SMTP, estableciendo una conexión segura que le permite enviar sus correos
electrónicos al mundo digital.

Piénsalo así: la clase SMTP es tu fiel transportista postal. Usted les entrega su correo
electrónico cuidadosamente elaborado y ellos se aseguran de que llegue a su destino sano y
salvo. Una vez establecida la conexión, se utilizan métodos como sendmail para transmitir
el correo electrónico. Es como si el cartero depositara la carta en el buzón y la
enviara al destinatario.

Si intentas usar Gmail u Outlook, no funcionará con tu contraseña normal. Debes entrar a la
configuración de tu cuenta (Google/Microsoft) y generar una "Contraseña de aplicación" específica para Python.

No guardes la clave en el código. Usa variables de entorno o archivos .env para evitar que
tu contraseña termine en GitHub por accidente.
"""
import smtplib

from email.mime.text import MIMEText


def example_simple_email():
    smtp_server: str = 'smtp.gmail.com'
    smtp_port: int = 587

    sender_email: str = 'rodrigo.alvare.herrera@gmail.com'
    sender_password: str = 'Les900310@123'

    receiver_email: str = 'rodrigo.alvarez.100390@gmail.com'
    message: str = f'''\
    Subject: Hello From Python

    This is a test email sent from Python.'''

    server: smtplib.SMTP | None = None
    try:
        smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
        print('Email sent successfully!')
    except Exception as e:
        print(e)
    finally:
        server.quit()


def example_complex_email():
    # 1. Create the MIMEText object with the email body
    message = MIMEText('This is a email body.')

    # 2. Set the email headers like a dictionary
    # The 'Subject' header defines the email's subject line.
    message['Subject'] = 'Your Custom Subject Here.'

    # The 'From' header specifies the sender's email address
    message['From'] = 'rodrigo.alvare.herrera@gmail.com'

    # The 'To' header specifies the recipient's email address
    message['To'] = 'rodrigo.alvarez.100390@gmail.com'

    # Once configured, this 'message' object can be sent using server.send_message(message)
    body_content: str = 'Hola, adjunto el correo con <b>formato HTML</b>.'
    message.attach(MIMEText(body_content, 'html'))
