"""
LÍNEA DE COMANDOS

La línea de comandos o consola es un medio de interacción con el sistema operativo. Permite
- Manejar archivos y directorios
- Ejecutar scripts y programas
- Instalar y administrar software
- Trabajar con sistemas de control de versiones
- Administrar Sistemas
- Administrar Redes

Variables de Entorno
Una variable de entorno es un valor dinámico alojado dentro del sistema operativo que puede
afectar el comportamiento de los procesos o programas que se ejecutan en la computadora.

El PATH es una variable de entorno que contiene una lista de rutas a carpetas. Cuando escribes
python o java en la terminal, el sistema operativo revisa el PATH para saber en qué carpeta
exacta está escondido ese programa y poder ejecutarlo.
"""

lesson: str = """
mv
\tSe emplea para mover como renombrar archivos y directorios

mkdir
\tCrea nuevos directorios

ls
\tLista los archivos y directorios.

cd
\tCambia de directorio.

touch
\tPermite crear un nuevo archivo.

rm
\tElimina un archivo o directorio.

rmdir
\tElimina un directorio.

python --version
\tMuestra la versión instalada en su sistema.

pip --version
\tMuestra la versión del gestor de paquetes en python instalda.

python -m venv name_env
\tCrea un entorno virtual en la carpeta name_env.

activate
\tInicia el entorno virtual ejecutándolo dentro de la carpeta Scripts dentro
\tdel entorno virtual.

pip install package_name
\tInstala el paquete package_name dentro del entorno virtual.

deactivate
\tCierra el entorno virtual. Regresando a la configuración global de su instalación
\tPython.
"""

print('COMANDOS BÁSICOS')
print(lesson)

# End application
_ = input('\nPress ENTER to quit . . . ')
