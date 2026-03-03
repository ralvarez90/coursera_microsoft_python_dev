#!/usr/bin/env python3

"""
LIBRERÍA ARGPARSE

El módulo argparse es la herramienta estándar de Python para crear interfaces de línea
de comandos (CLI) de manera profesional. Su función principal es permitir que tus scripts
acepten argumentos o parámetros directamente desde la terminal al momento de ser
ejecutados.

La librería argparse es la solución para manejar los argumentos de la línea de comandos
en Python. Piensa en ella como un meticuloso organizador que aporta orden y claridad al
potencialmente caótico mundo de las entradas de usuario. Con argparse, puedes definir
explícitamente los tipos de argumentos que tu script espera, especificar sus formatos
esperados (por ejemplo, cadenas, números o selecciones de una lista), e incluso crear
mensajes informativos que guíen a los usuarios si tropiezan con errores o incertidumbres.

Es como tener un recepcionista bien formado que no solo da la bienvenida a los huéspedes,
sino que también se asegura de que tengan toda la información y el apoyo necesarios para
navegar por las funcionalidades de su script sin problemas.

Para los scripts que realizan tareas repetitivas, las CLI ofrecen una vía de personalización
y automatización. Al aceptar parámetros como valores de entrada, directorios de salida o modos
de procesamiento como argumentos de línea de comandos, permite a los usuarios adaptar las
acciones del script sin alterar su lógica central. Esto agiliza los flujos de trabajo y reduce
el riesgo de errores asociados a las modificaciones manuales del código.
"""
import argparse
import sys

# Create the main parser object
parser = argparse.ArgumentParser(description='A friendly greeting script.')

# Add name argument
parser.add_argument('name', help='The name of the person to greet.')
args = parser.parse_args()
print(f'Hello {args.name}!')

# Using sys module
print('First argument', sys.argv[1] if len(sys.argv) > 1 else 'None')
