from db import connection

from flask import Flask
from flask_migrate import Migrate
from dotenv import load_dotenv
from os import environ

load_dotenv()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

connection.init_app(app)

Migrate(app, connection)

if __name__ == '__main__':
    app.run(debug=True)