"""
PROCESAMIENTO POR LOTES

Las capacidades de manejo de archivos de Python te permiten recorrer directorios, identificar
archivos basándote en criterios específicos (como extensiones de archivo o nombres), e incluso
extraer metadatos o contenido de esos archivos. Por su parte, los comandos shell permiten realizar
acciones como redimensionar imágenes, convertir formatos de archivo o incluso ejecutar complejas
herramientas de línea de comandos directamente desde el script de Python.

Además, los mecanismos de gestión de errores de Python le permiten anticiparse y gestionar con
elegancia cualquier problema inesperado que pueda surgir durante el procesamiento por lotes. Tanto
si se trata de un archivo dañado como de un comando que no se ejecuta, puede utilizar un sólido
tratamiento de errores para garantizar que su script siga funcionando sin problemas,
incluso ante la adversidad.

La fusión de Python y los comandos shell tiene aplicaciones prácticas en diversos ámbitos. En el
ámbito de la Ciencia de datos y el Aprendizaje automático, los scripts de Python suelen aprovechar
comandos de shell como sed y awk, o incluso herramientas específicas del dominio, para pre procesar
datos sin procesar antes de introducirlos en modelos de aprendizaje automático. Este preprocesamiento
puede incluir la limpieza, la transformación y el formateo de datos, garantizando que sean adecuados
para el análisis.

En el ámbito de DevOps y la administración de sistemas, la automatización de tareas como la implementación
de servidores, el análisis de registros y el mantenimiento de sistemas depende en gran medida de la sinergia
entre las capacidades de scripting de Python y el acceso directo al sistema que ofrecen los comandos shell.

Del mismo modo, en el desarrollo web, las tareas rutinarias como la minification de archivos JavaScript,
la compilación de CSS o la ejecución de scripts de compilación suelen automatizarse mediante una combinación
de comandos de Python y shell, lo que agiliza el flujo de trabajo de desarrollo.
"""

exampleCode: str = """
import os
import subprocess
for filename in os.listdir('data_directory'):
    if filename.endswith('.csv'):
        # Convert CSV files to Excel using a shell command
        subprocess.call(['libreoffice', '--convert-to', 'xls', filename])
"""
print(exampleCode, end='\n\n')

exampleCodeWithError: str = """
import subprocess

try:
    subprocess.run(['rm', 'important_file.txt'], check=True)  # Delete a file, raise an error if it fails
except subprocess.CalledProcessError as e:
    print(f"Error deleting file: {e}")
"""
print(exampleCodeWithError, end='\n\n')

# End message
_ = input('\nPress ENTER to continue . . . ')
