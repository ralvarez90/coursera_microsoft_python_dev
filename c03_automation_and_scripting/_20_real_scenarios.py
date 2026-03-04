"""
ESCENARIOS REALES

1. Acceso a Datos y Procesamiento
2. Automatización de Flujos de Trabajo
3. Organización de Archivos y Transformación
4. Compresión y Archivado
5. Desarrollo de Software Eficiente

os.access
Puedes utilizar la función os.access() de Python para verificar si tienes los permisos necesarios.
"""

# Example 1
renaming_example: str = """
import os
for i in range(1, 10):
    old_name = f'IMG_{i:03d}.jpg'
    new_name = f'vacation_photo_{i}.jpg'
    os.rename(old_name, new_name)
"""
print(renaming_example)

# Example 2
searching_example: str = """
import glob
pdf_files = glob.glob('*.pdf')
for pdf in pdf_files:
    print(pdf)
"""
print(searching_example)
