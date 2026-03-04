"""
MODULE GLOB (GLOBAL WILDCARD)

Es como un potente motor de búsqueda para tu sistema de archivos, que te permite
encontrar archivos y directorios que coincidan con determinados patrones.

El corazón de glob es la función glob.glob(), que acepta patrones comodín.
Piensa en estos patrones como si fueran consultas de búsqueda para tu sistema
de archivos.

Ejemplos:
glob.glob('data/202*/sales_*.csv')

Escenarios Reales
1. Organizador de Fotos
2. Analizador de Archivos de Registro

Portabilidad
Python ofrece herramientas adicionales, como el módulo pathlib, que proporciona un
enfoque más orientado a objetos y potencialmente más portátil para las operaciones
de archivo. En última instancia, la decisión de priorizar la portabilidad sobre la
comodidad depende de los requisitos específicos de tu proyecto. Si la compatibilidad
entre plataformas es una preocupación crítica, puedes considerar explorar enfoques
alternativos o invertir un esfuerzo extra para asegurar que tu código maneja con
gracia cualquier peculiaridad del sistema operativo.
"""
import glob

python_files = glob.glob("*.py", recursive=True)
print(f'Python files:')
for file in python_files:
    print(f'- {file}')
