from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from dotenv import load_dotenv
from os import environ

from db import connection
from utils.enviar_correo import enviar_correo_adjuntos

from controllers.usuario_controller import RegistroController
from controllers.categoria_controller import ImagenesController, CategoriasController
from controllers.product_controller import ProductosController

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
app.config['UPLOAD_FOLDER'] = '/uploads/imagenes'

connection.init_app(app)

api = Api(app)

Migrate(app, connection)

@app.route('/prueba')
def enviar_correo_prueba():
    # enviar_correo_adjuntos('xxxxx@gmail.com', 'Correo con imagenes')
    enviar_correo_adjuntos('xxxx@gmail.com', 'Correo con imagenes por Victor Villazon')

    return { 'message': 'Correo enviado exitosamente' }

api.add_resource(RegistroController, '/registro')
api.add_resource(ImagenesController, '/imagenes', '/imagenes/<nombre>')
api.add_resource(CategoriasController, '/categorias')
api.add_resource(ProductosController, '/productos')

if __name__ == '__main__':
    app.run(debug=True)
