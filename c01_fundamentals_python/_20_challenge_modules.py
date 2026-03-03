"""
RETO IMPORTACIÓN DE MÓDULOS

Podemos generar nuestras propias clases para que se adapten a nuestros problemas a resolver.
"""
from textblob import TextBlob

text = 'I love this library, it is amazing!'
blob = TextBlob(text)
print(blob.sentiment)
