# TODO: ✔ Implementar para crear y listar a todos los maestros, utilizar los DTOs correspondientes de los maestros

from flask_restful import Resource, request
from sqlalchemy.orm import Query
from database import conexion
from models.maestro_model import Maestro
from dtos.maestro_dto import MaestroDto

class MaestroController(Resource):
    # GET, POST
    def get(self):
        query: Query = conexion.session.query(Maestro)

        # SELECT * FROM maestros:
        resultado = query.all()

        dto = MaestroDto()

        maestros = dto.dump(resultado, many=True)

        return { 'results': maestros }

    def post(self):
        data = request.json
        dto = MaestroDto()

        try:
            nombre = data.get('nombre')
            apellidos = data.get('apellidos')
            correo = data.get('correo')
            direccion = data.get('direccion')

            nuevo_maestro = Maestro(
                nombre=nombre,
                apellidos=apellidos,
                correo=correo,
                direccion=direccion
            )

            conexion.session.add(nuevo_maestro)

            conexion.session.commit()

            return { 'message': 'Maestro creado exitaosamente' }, 201
        except Exception as error:
            return {
                'message': 'Error al crear al maestro',
                'content': error.args
            }

class UnMaestroController(Resource):
    def get(self, id):
        query: Query = conexion.session.query(Maestro)
        
        maestro_encontrado = query.filter_by(id=id).first()

        # TODO: ✔ Implementar si no existe ese maestro, retornar un message diciendo que el maestro no existe
        if (not maestro_encontrado):
            return { 'message': 'Maestro no existe'}
        
        dto = MaestroDto()

        resultado = dto.dump(maestro_encontrado)

        return { 'result': resultado  }