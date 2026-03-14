"""
CONSIDERACIONES ÉTICAS SOBRE WEB SCRAPPING

1. Sobre carga de servidores (overloading server)
La sobrecarga de los servidores es uno de los principales problemas del web
scrapping. Demasiadas solicitudes de tu script puede ralentizar o incluso
bloquear un sitio web.

Use técnicas como la limitación de velocidad, que separa tus solicitudes, y
el almacenamiento en caché, que almacena los datos en forma local para que
no tengas que seguir solicitando al sitio web la misma información una y
otra vez.

2. Copyright
Otra consideración es la infracción de derechos de autor. Si estás extrayendo
contenido protegido por derechos de autor, es crucial obtener el permiso
del propietario del sitio y acreditarlo adecuadamente.

3. Privacidad
Respeta la privacidad del usuario. La extracción de datos personales sin
consentimiento no es ético y puede tener consecuencias legales.

4. Términos y Condiciones
Consulte siempre antes los términos y condiciones del servicio web. Utilize
el user-agent en sus encabezados para identificar tu scrapper.

5. Archivo robots.txt
Piense en este archivo como el guardián digital de un sitio web. Es un
archivo de texto que indica a los rastreadores (crawlers) y scrappers a
qué partes del sitio web pueden acceder y qué partes están prohibidas.

Ignorar e archivo robots es como entrar sin autorización a una propiedad
de otra persona.
"""
