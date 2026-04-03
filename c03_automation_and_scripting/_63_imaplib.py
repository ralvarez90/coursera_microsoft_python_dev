"""
LA VERSATILIDAD DE IMAPLIB

Mientras que smtplib se centra en el envío de correos electrónicos, imaplib le ofrece la
posibilidad de gestionar e interactuar directamente con su bandeja de entrada. Es como tener
un mando a distancia para tu correo electrónico, que te permite realizar diversas acciones
sin ni siquiera abrir tu cliente de correo.

Piensa en imaplib como tu asistente personal de correo electrónico, que trabaja diligentemente
entre bastidores para ayudarte a mantenerte organizado. Puedes ordenarle que busque nuevos
mensajes, que busque mensajes específicos por remitente, asunto o fecha, que los marque como
leídos o no leídos, e incluso que los mueva o los elimine.

Este nivel de control abre interesantes posibilidades de automatización. Imagine que recibe
un gran volumen de correos electrónicos y necesita identificar rápidamente los mensajes urgentes
de clientes específicos o que contienen determinadas palabras clave. Con imaplib, puedes escribir
un script que analice automáticamente tu bandeja de entrada, filtre los correos importantes e
incluso te envíe notificaciones o desencadene otras acciones en función de su contenido. Es como
tener un filtro inteligente que tamiza tu bandeja de entrada y te muestra los mensajes más
relevantes.

------------------------------------------------------------------------------------------------------------------------

Obtención y Gestión de Corres Electrónicos.

La clase IMAP4_SSL de imaplib es la clave para establecer una conexión segura y cifrada con el
servidor de correo electrónico. Esto garantiza que tu información confidencial, como tus credenciales
de acceso y el contenido de tu correo electrónico, permanezca protegida de miradas indiscretas mientras
viaja por Internet. Piensa en ello como un túnel amurallado que protege la comunicación con tu
bandeja de entrada.

Una vez establecida esta conexión segura, puedes empezar a interactuar con tus correos electrónicos
utilizando varios métodos proporcionados por imaplib. La función select te permite elegir un buzón
específico, como tu "Bandeja de entrada" o cualquier otra carpeta que hayas creado. Es como abrir un
cajón concreto de un archivador para acceder a los correos que contiene.

La función de búsqueda es donde se produce la verdadera magia. Te permite encontrar mensajes específicos
en función de una serie de criterios, como el remitente, el asunto, la fecha o incluso las palabras clave
del mensaje. Es como tener un potente motor de búsqueda en tu bandeja de entrada, que te permite localizar
exactamente los mensajes que estás buscando.

------------------------------------------------------------------------------------------------------------------------

Aplicaciones Reales

Exploremos algunas situaciones reales en las que la automatización del correo electrónico puede brillar
con luz propia. Imagine que tiene la tarea de generar y enviar informes de ventas semanales a su equipo.
Recopilar datos manualmente, crear gráficos y enviar el informe por correo electrónico cada semana puede
ser una tarea tediosa. Con la automatización del correo electrónico, puede programar un script de Python
para que se encargue del proceso. Puede recopilar los datos necesarios, generar un informe visualmente
atractivo utilizando una biblioteca como matplotlib y, a continuación, enviarlo automáticamente por correo
electrónico a los destinatarios pertinentes. Ahorrará un tiempo valioso y se asegurará de que su equipo
esté informado sin ningún esfuerzo manual por su parte.

En el ámbito de la atención al cliente, la automatización del correo electrónico puede cambiar las reglas
del juego. Supongamos que su empresa recibe consultas de los clientes por correo electrónico. En lugar de
comprobar constantemente su bandeja de entrada, puede utilizar imaplib para supervisarla. La secuencia de
comandos puede identificar mensajes urgentes basándose en palabras clave o remitentes específicos y, a
continuación, activar acuses de recibo automáticos para que los clientes sepan que se ha recibido su consulta.

Incluso puede ir un paso más allá y dirigir los mensajes al agente de asistencia adecuado en función de su
contenido, garantizando respuestas puntuales y eficaces.

Las notificaciones de Redes sociales son otro ámbito en el que la automatización del correo electrónico puede
simplificarle la vida. Puedes configurar un script para que compruebe periódicamente tus cuentas de Redes sociales
en busca de nuevas menciones o mensajes. Si se encuentra alguno, el script puede enviarle una notificación por
correo electrónico, manteniéndole al tanto sin necesidad de comprobar constantemente sus feeds. De este modo,
te mantienes informado de las interacciones importantes sin tener que preocuparte por las constantes
distracciones de las redes sociales.

Por último, la automatización del correo electrónico puede ser un salvavidas cuando se trata de copias de
seguridad y archivo. Puedes crear secuencias de comandos para hacer copias de seguridad periódicas de toda
tu bandeja de entrada o de carpetas específicas, para asegurarte de que nunca pierdes información importante.

Además, puedes automatizar el archivado de correos antiguos para liberar espacio en la bandeja de entrada,
mantenerla despejada y mejorar su rendimiento.

------------------------------------------------------------------------------------------------------------------------

Buenas Prácticas y Consideraciones

ASÍ COMO EN CUALQUIER TRABAJO DE PROGRAMACIÓN, el cumplimiento de las mejores prácticas es crucial para el
éxito de la automatización del correo electrónico. La gestión de errores debe ser una prioridad. Los
contratiempos en la red, las credenciales de inicio de sesión incorrectas o los formatos de correo
electrónico inesperados pueden interrumpir sus scripts de automatización. Mediante la implementación de
una gestión integral de errores, puede asegurarse de que sus scripts gestionan con elegancia estas
situaciones, proporcionando mensajes informativos o tomando medidas correctivas en lugar de
bloquearse abruptamente.

La seguridad es primordial en la automatización del correo electrónico. Sus credenciales de correo
electrónico son información confidencial, y es esencial protegerlas de accesos no autorizados. Evite
codificarlas directamente en sus scripts, ya que esto supone un riesgo de seguridad importante. En su
lugar, considere la posibilidad de almacenarlas de forma segura utilizando variables de entorno o
técnicas de cifrado. Esto añade una capa extra de protección y ayuda a evitar que tus credenciales
caigan en las manos equivocadas.

Ten en cuenta los límites de velocidad de tu proveedor de correo electrónico. Estos límites restringen
el número de mensajes que puedes enviar en un periodo de tiempo determinado. Superar estos límites
puede activar los filtros de spam o incluso provocar la suspensión temporal de la cuenta. Es crucial
tener en cuenta estas restricciones y diseñar sus scripts de automatización en consecuencia,
asegurándose de que operan dentro de los límites permitidos. Una estrategia eficaz es aprovechar la
función time.sleep() antes de cada bucle de correo electrónico en su script. Esto introduce una pausa
deliberada, lo que le permite controlar el ritmo de envío de su correo electrónico y mantenerse
dentro de los límites de velocidad impuestos por su proveedor.

Por último, es indispensable realizar pruebas exhaustivas antes de desplegar los scripts de automatización
en un entorno real. Cree un entorno de pruebas controlado en el que pueda simular varios escenarios y
casos extremos. Esto ayuda a identificar y abordar cualquier problema o error potencial antes de que afecte
a su flujo de trabajo de correo electrónico real. Recuerde, ¡un script bien probado es un script fiable!


"""
import imaplib

# Replace with your email provider
imap_server = 'imap.your_email_provider.com'
imap_port = 993
email_address = 'your_email_example@example.com'
email_password = 'your_password'

ail: imaplib.IMAP4_SSL | None = None
try:
    mail: imaplib.IMAP4_SSL = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(email_address, email_password)
    mail.select('Inbox')
    status, messages = mail.search(None, 'ALL')
    if status == 'OK':
        for num in messages[0].split():
            status, data = mail.fetch(num, '(RFC822)')
            if status == 'OK':
                # Fetched the email data (data[0][1]) here...'
                print('Fetched an unread email...')
    else:
        print('Error searching for unread emails...')
except Exception as e:
    print(e)
finally:
    # mail.close()
    # mail.logout()
    print('Good bye...')
