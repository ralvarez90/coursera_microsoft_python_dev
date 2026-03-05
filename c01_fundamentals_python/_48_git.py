"""
INTRODUCCIÓN A GIT

La mecánica de Git: Snapshots, commits y ramas
"""

git_core_concepts: str = """
GIT CORE CONCEPTS

1. Repository (repositorio)
Es el espacio de almacenamiento central para el código e historial completo
del proyecto.

2. Commit (confirmación, compromiso)
Es una captura instantánea de todo tu proyecto en un momento determinado. Cada
commit captura todos los cambios realizados desde el commit anterior, junto con
un mensaje descriptivo.

3. Staging Area (área de preparación)
Es el espacio intermedio o sala de espera donde se colocan los cambios que se van
a incluir en el siguiente commit.

4. Branch (rama)
Es una línea de desarrollo independiente. Permiten trabajar en nuevas funcionalidades
correcciones de errores o experimentos de forma aislada si afectar la estabilidad
del proyecto principal. Cuando los cambios están completados, puede combinarlos en
la rama principal.

5. Merge (fusión)
Es el proceso de combinar los cambios de una rama en otra.

6. Pushing (empujar)
Se refiere a enviar tus commits locales a un repositorio remoto, como uno alojado 
en GitHub o GitLab.

7. Pull (jalar)
Es lo contrario al push, consiste en obtener los últimos cambios de un repositorio
remoto y fusionarlos a tu copia local.

8. Pull Request
Es una propuesta de cambios. Cuando abres una PR, estás pidiendo que el código de una 
rama (donde trabajaste tú) se fusione (merge) con otra rama (normalmente la principal, 
llamada main o master). Este no es un comando de git, es una funcionalidad de GitHub.
"""

git_commands_manual: str = """
GIT COMMANDS:

git config --global user.name "Your Name"
    Configura de manera local su nombre de usuario.
    
git config --global user.email "your_email@example.com" 
    Configura de manera local su email.
    
git config --global init.defaultBranch "mainName"
    Configura el nombre de la rama default al crear cualquier repositorio. Se
    suele poner de nombre "main".
    
git init
    Crea un nuevo repositorio local.
    
git add <file_name>
    Agrega al stage area el archivo correspondiente.
    
git add --all
    Agrega todos los archivos que tengan cambios al stage area.
    
git commit -m <commit_message>
    Crea un snapshot o copia de su proyecto agregando los cambios
    establecidos en el staging area.
    
git branch <branch_name>
git checkout -b <branch_name>
    Crea una nueva rama con su respectivo nombre.
    
git checkout <branch_name>
    Permite cambiar de la rama actual a otra rama.
    
git merge <branch_name>
    Fusiona los cambios de la rama <branch_name> en la rama posicionada.
    
git clone <repository_url>
    Clona de manera local un repositorio remoto con la respectiva url.
    
git push
    Empuja los últimos cambios de nuestro repositorio local al repositorio 
    remoto.
    
git pull
    Jala los últimos cambios provenientes del repositorio remoto a
    nuestro repositorio local.
"""

# Show concepts
print(git_core_concepts)

# Show commands
print(git_commands_manual)
