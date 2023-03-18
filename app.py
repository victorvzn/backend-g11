from db import connection

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from dotenv import load_dotenv
from os import environ

from utils.enviar_correo import enviar_correo_adjuntos
from controllers.usuario_controller import RegistroController
from controllers.categoria_controller import ImagenesController

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['UPLOAD_FOLDER'] = '/uploads/imagenes'

connection.init_app(app)

api = Api(app)

Migrate(app, connection)

@app.route('/prueba')
def enviar_correo_prueba():
    # enviar_correo_adjuntos('victorzn23@gmail.com', 'Correo con imagenes')
    enviar_correo_adjuntos('ederiveroman@gmail.com', 'Correo con imagenes por Victor Villazon')

    return { 'message': 'Correo enviado exitosamente' }

api.add_resource(RegistroController, '/registro')
api.add_resource(ImagenesController, '/imagenes', '/imagenes/<nombre>')

if __name__ == '__main__':
    app.run(debug=True)
