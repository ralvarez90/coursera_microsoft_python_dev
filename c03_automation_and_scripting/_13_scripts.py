"""
SCRIPTS

Para ejecutar un script de python, usamos el siguiente comando:
python script_name.py
"""
import argparse

# Trigger a string output from the terminal
print('Hello from the command line!')

# Instantiate the Argparse package
parser = argparse.ArgumentParser()

# Create an argument called name.
parser.add_argument('--name', help='Creates a ne name.')
args = parser.parse_args()

# Output the name
if args.name:
    print(f'My name is {args.name}')
else:
    print('Hello!')
