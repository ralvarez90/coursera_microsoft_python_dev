"""
LOGGING

Python cuenta con un módulo para generar registros de logging ya sea en
archivos separados o en consola.
"""
import logging

# Configuration
logging.basicConfig(level=logging.DEBUG)

# Send a logging message
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
