# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/quickstart/#installation
# https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/config/
# https://pypi.org/project/python-dotenv/#getting-started

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ

load_dotenv() # es el encargado de leer el archivo .env si es que exise y agregarlasvariables en ese archivo como si fueran variables de entorno
 
# print(environ)

app = Flask(__name__)

# print(app.config)
print(environ.get('DATABASE_URL'))

# dialect://username:password@host:port/database
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

conexion = SQLAlchemy(app=app)

@app.route('/', methods=['GET'])
def initial():
    return {
        'message': 'Bienvenido a mi API'
    }

if __name__ == '__main__':
    app.run(debug=True)