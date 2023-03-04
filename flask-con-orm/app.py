from flask import Flask
from dotenv import load_dotenv
from os import environ
from flask_migrate import Migrate
from flask_restful import Api

from database import conexion
from models.nivel_model import Nivel
from models.maestro_model import Maestro
from models.seccion_model import Seccion
from controllers.nivel_controller import NivelController

load_dotenv() # es el encargado de leer el archivo .env si es que exise y agregarlasvariables en ese archivo como si fueran variables de entorno
 
# print(environ)

app = Flask(__name__)

# print(app.config)
# print(environ.get('DATABASE_URL'))

# dialect://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

flask_api = Api(app=app)

# si quiero crear mi conexion en otro archivo e inicializar la configuracion de mi conexion tengo que utlizar el metodo init_app y es aca donde le pasare el parametro de mi instancia de la clase Flask

conexion.init_app(app)

# ahora realizo la inicializacion de mi clase Migrate
# se le pasa la aplicacion como primer parametro y la conexion (instancia de SQLMigrate)
Migrate(app=app, db=conexion)

# defino las rutas de mi API
flask_api.add_resource(NivelController, '/niveles')

if __name__ == '__main__':
    app.run(debug=True)