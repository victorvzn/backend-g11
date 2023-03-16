from flask_restful import Resource, request

from db import connection

class RegistroController(Resource):
    def post(self):
        data = request.json
        try:
            pass
        except Exception as error:
            return {
                'message': 'Error al registrar el usuario',
                'content': error.args
            }