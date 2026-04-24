"""
ARCHIVOS DE TEXTO

1. ABRIR Y LEER ARCHIVOS
Antes de empezar a trabajar con la información almacenada en un archivo de texto,
primero tienes que abrirlo. Python tiene una herramienta integrada llamada open()
que te ayuda a hacerlo. Es como abrir la puerta de tu cuaderno digital.

Cuando utilices la función open(), tienes que decirle dos cosas: el nombre del archivo
que quieres abrir y cómo quieres utilizarlo. Esta segunda parte se llama "modo". Es
como elegir si sOlo quieres leer tus notas, escribir nuevas o añadir a las
ya existentes.

Los modos más comunes son:

"r": Este es el modo por defecto y es solo para leer. Puedes echar un vistazo dentro
del archivo, pero no puedes cambiar nada.

"w": Es para escribir. Si el archivo no existe, Python lo creará por ti. Pero ten
cuidado, porque si el fichero ya existe, este modo borrará lo que haya dentro antes
de que empieces a escribir.

"a": Esto es para anexar, lo que significa añadir nueva información al final del
archivo. Si el archivo no existe, Python lo creará.

Python ofrece un context manager usando la sentencia with, que permite ejecutar
el cierre del archivo de manera automática.

Una vez abierto el fichero, tienes a tu disposición varios métodos para acceder a su contenido. La
manera más sencilla consiste en leer el archivo en la memoria del programa de una sola vez. Esto
funciona bien con archivos pequeños en los que el uso de memoria no es un problema. Sin embargo,
cuando se trata de archivos más grandes, este enfoque puede ser problemático, ya que puede consumir
una cantidad significativa de memoria, lo que puede ralentizar el programa o incluso hacer que
se bloquee.

Para estos casos, Python ofrece la flexibilidad de leer el archivo línea por línea. Este enfoque es
mucho más eficiente en memoria, ya que sólo carga una línea del archivo en la memoria a la vez.
A continuación, puede procesar cada línea individualmente antes de pasar a la siguiente, lo que
garantiza un uso óptimo de memoria incluso cuando se trabaja con archivos de texto masivos.

Python proporciona herramientas y técnicas intuitivas para facilitar ambos enfoques de lectura,
dándote la libertad de elegir el que mejor se adapte a tus necesidades específicas y al tamaño
del archivo con el que estés trabajando.

Y no olvides cerrar el archivo cuando hayas terminado. Es como cerrar el Notebook cuando terminas
de leer o escribir. De este modo, la memoria del ordenador se libera y puede utilizarse para
otras tareas.

Python facilita el trabajo con Archivos CSV gracias a su módulo 'csv' incorporado. Este módulo
proporciona herramientas prácticas que te permiten leer datos de archivos CSV existentes y escribir
nuevos datos en ellos.

Aunque trabajar con archivos de texto suele ser sencillo, es fundamental tener en cuenta algunos problemas
que pueden surgir. Uno de ellos es la codificación de los archivos. Piense en la codificación como el
lenguaje que utiliza su ordenador para entender los caracteres de un archivo de texto. Python normalmente
asume la codificación UTF-8, que es como un lenguaje universal entendido por la mayoría de los sistemas.

Sin embargo, si encuentras archivos creados con una codificación diferente, puede que necesites especificarla
explícitamente al abrir el archivo para asegurar una interpretación precisa del contenido.

"""
import os
import time


def createFileUsingWriteMode():
    file = open('example.txt', mode='w')
    content = 'This is an example of a text file.'
    print('Writing content . . .')
    file.write(content)
    time.sleep(1)
    file.close()


def readFileUsingReadMode():
    with open('example.txt', mode='r') as file:
        print('Reading content...')
        time.sleep(1)
        content = file.read()
        print(content)


def deleteSampleFiles():
    print('Deleting sample files . . .')
    time.sleep(1)
    os.remove('example.txt')


def showCSVExampleCode():
    example = """
    import csv
    
    with open('example.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
            
    output:
    ['Name', 'Age', 'City']
    ['Alice', '24', 'New York']
    ['Bob', '27', 'Los Angeles']
    """
    print(example)


def main():
    try:
        createFileUsingWriteMode()
        readFileUsingReadMode()
        deleteSampleFiles()

        print()
        showCSVExampleCode()
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
