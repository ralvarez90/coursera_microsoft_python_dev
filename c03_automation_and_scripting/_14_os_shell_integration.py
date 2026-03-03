"""
INTEGRACIÓN CON COMANDOS SHELL

Podemos combinar python con comandos del sistema operativo. El módulo subprocess actúa como un
puente entre python y comandos shell de su sistema operativo.

Una de las funciones más potentes del módulo subprocess es la posibilidad de canalizar datos
entre comandos. Piense en ello como una tubería virtual donde la salida de un comando fluye
directamente a la entrada de otro, creando una cadena de procesamiento de datos suave y
eficiente.

Popen (Process open)
"""
import subprocess

# Use grep to find files lines containing "error" in a log file.
grep_process = subprocess.Popen(['grep', 'error', 'logfile.txt'], stdout=subprocess.PIPE)

# Pass the output of grep to a python script for further analysis
python_process = subprocess.Popen(['python3', 'analyze_errors.py'], stdin=grep_process.stdout)

# Wait for the python script to finish
python_process.wait()

# Code in analyze_errors.py
codeIn = """
# Python analyze_errors.py
import sys

# Read lines containing "error" from standard input (provided by subprocess)
for line in sys.stdin:
  # Process each error line
  print(f"Found: {line.strip()}")

print("Finished analyzing errors.")
"""
print(codeIn)
