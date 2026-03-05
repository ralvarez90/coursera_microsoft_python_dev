"""
ENTORNO PARA LA AUTOMATIZACIÓN

Crea un script que pueda:
1. Aceptar la ruta a un archivo de texto de entrada.
2. Realizar un análisis simple (contar frecuencias de palabras)
3. Enviar los resultados a un nuevo archivo.
"""

import argparse
import re


def analyze_data(input_file: str, output_file: str):
    with open(input_file, 'r') as f:
        text = f.read()
    words = re.findall(r'\b\w+\b', text.lower())
    words_count = {}
    for word in words:
        words_count[word] = words_count.get(word, 0) + 1

    with open(output_file, 'w', encoding='utf-8') as f:
        for word, count in words_count.items():
            f.write(f'{word}: {count}\n')


# Create parser
parser = argparse.ArgumentParser(description='Analyze data from a file.')

# Add arguments
parser.add_argument('input_file', help='Path to the input file.')
parser.add_argument('output_file', help='Path to the output file.')

# Read content and send results in a new file
args = parser.parse_args()
try:
    analyze_data(args.input_file, args.output_file)
except Exception as e:
    print(e)
