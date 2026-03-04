"""
RETO DE AUTOMATIZACIÓN

Escribir un script en Python que recorra todos los archivos del directorio
"Descargas" (ignorando los subdirectorios).

Para cada archivo, extraiga el año y el mes de su última fecha de modificación.

Crea subdirectorios dentro de tu directorio "Descargas", nombrados con el año y el mes (por ejemplo, "2024/Octubre").

Mueva cada archivo al subdirectorio correspondiente en función de su fecha de modificación.
"""
import os
import shutil

from datetime import datetime


def get_user_cwd() -> str:
    home = os.environ.get('USERPROFILE') or os.environ.get('HOME')
    return home


def get_download_path() -> str:
    return os.path.join(get_user_cwd(), 'Downloads')


# Run program
downloaded_files = [f for f in os.listdir(get_download_path()) if not f.endswith('.ini')]
for f in downloaded_files:
    file_path = os.path.join(get_download_path(), f)

    # Get the modification time of the file
    modified_time = os.path.getmtime(file_path)

    # Convert the modified time to a datetime object
    date = datetime.fromtimestamp(modified_time)
    year = date.year
    month = date.strftime('%B')

    # Print each file and their modification dates (for testing purposes)
    # print(f'{f}: {year}/{month}')

    # Create the directory path for the year and month
    directory = os.path.join(get_download_path(), f'{year}_{month}')

    # Create the directory if it doesn't exist'
    os.makedirs(directory, exist_ok=True)

    # Move the file to the new directory
    shutil.move(file_path, os.path.join(get_download_path(), f'{year}_{month}'))

    # Print confirmation message
    print(f'File {f} moved to {year}_{month} directory.')
