from db import connection

from flask_restful import Resource, request
from bcrypt import gensalt, hashpw

from dtos.usuario_dto import UsuarioDto
from models.usuario_model import Usuario

from utils.enviar_correo import enviar_correo

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

            enviar_correo(
                nuevo_usuario.correo,
                'Bievenido a LibreriAPP',
                '''Bienvenido a esta nueva plataforma.
                Donde encontrarás todo lo necesario para tus útiles de escritorio.'''
            )

            connection.session.commit()

            return { 'message': 'Usuario creado exitosamente' }
        except Exception as error:
            # si algo fallo todos los insert, updates y deletes quedaran sin efecto y no se guardara nada en la base de datos
            connection.session.rollback()
            
            return {
                'message': 'Error al registrar el usuario',
                'content': error.args
            }