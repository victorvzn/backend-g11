from db import connection

from flask_restful import Resource, request
from bcrypt import gensalt, hashpw

from dtos.usuario_dto import UsuarioDto
from models.usuario_model import Usuario

class RegistroController(Resource):
    def post(self):
        data = request.json
        try:
            dto = UsuarioDto()
            data_serializada = dto.load(data)

            # Hash del password
            salt = gensalt()
            password = bytes(data_serializada.get('password'), 'utf-8')
            hashed_password = hashpw(password, salt).decode('utf-8')

            # Actualizando el password hashed en la data serializada
            data_serializada['password'] = hashed_password
            nuevo_usuario = Usuario(**data_serializada)

            connection.session.add(nuevo_usuario)
            connection.session.commit()
            return { 'message': 'Usuario creado exitosamente' }
        except Exception as error:
            return {
                'message': 'Error al registrar el usuario',
                'content': error.args
            }