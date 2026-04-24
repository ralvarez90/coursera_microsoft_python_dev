"""
POSTMAN, REQUESTS Y HEADERS

1. API KEY
Es una secuencia de caracteres que se emplea para controlar el acceso al uso de una determinada API.
Permite saber si quien realiza una solicitud tiene acceso al servicio o datos proporcionados por
la API.

Las API keys se deben almacenar de manera segura. Es decir, en variables de entornos o en archivos
de configuración.

2. Requests
Las solicitudes tiene partes importantes, como el http methods, un url que es la dirección del
end point de la API, los headers que incluyen información adicional enviada con la solicitud que
a menudo incluye el api key, y el body que son los datos que envía el solicitante.
"""

from flask import Flask, jsonify, Response

# Create flask app instance
app = Flask(__name__)

postsDB = {
    1: {"titulo": "Mi primer post", "contenido": "Hola mundo", "autor": "Admin"},
    2: {"titulo": "Flask es genial", "contenido": "Aprendiendo rutas", "autor": "User1"}
}


@app.route("/")
def index():
    htmlContent = '''
    <!DOCTYPE html>
    <html lang="es-MX">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Home</title>
    </head>

    <body>
        <h1>Hola Mundo desde Python!</h1>
    </body>

    </html>
    '''
    return htmlContent


@app.route("/posts")
def getPosts() -> tuple[Response, int]:
    return jsonify(postsDB), 200


@app.route("/posts/<int:post_id>")
def get_post(post_id: int) -> tuple[Response, int]:
    return jsonify(postsDB.get(post_id)), 200


# Run application
if __name__ == '__main__':
    app.run(debug=True, port=5000)
