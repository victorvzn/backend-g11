from flask_restful import Resource, request
from sqlalchemy.orm import Query
from database import conexion
from models.nivel_model import Nivel
from dtos.nivel_dto import NivelDto

class NivelController(Resource):
    # GET, POST, PUT
    def get(self):
        query: Query = conexion.session.query(Nivel)

        # SELECT * FROM niveles;
        resultado = query.all()

        dto = NivelDto()

        # dump > es un metodo en el cual le paso la/las instancias que quiero convertir a tipos de datos genericos. si se le pasa mas de una instancia, osea una lista de instancias, se le tiene que adicionar el parametro many=True para indicar que lo tendra que iterar
        niveles = dto.dump(resultado, many=True)

        # print(resultado[0].numero)
        # print(resultado[0].descripcion)
        # niveles = []
        # for nivel in resultado:
        #     niveles.append({
        #         'id': nivel.id,
        #         'numero': nivel.numero,
        #         'descripcion': nivel.descripcion
        #     })

        return { 'results': niveles }

    def post(self):
        data = request.json
        numero = data.get('numero')
        descripcion = data.get('descripcion')
        nuevo_nivel = Nivel(numero=numero, descripcion=descripcion)
        # con el metodo add indicamos que queremos guardar ese nuevo registro
        conexion.session.add(nuevo_nivel)
        # con el metodo commit queremos guardar de manera permanente esa informacion en la base de datos
        conexion.session.commit()

        return { 'message': 'Nivel creado exitosamente'}, 201

class UnNivelController(Resource):
    def get(self, id):
        query: Nivel = conexion.session.query(Nivel)
        
        nivel_encontrado = query.filter_by(id).first()

        # TODO: Implementar si no existe ese nivel, retornar un message diciendo que el nivel no existe
        
        dto = NivelDto()

        resultado = dto.dump(nivel_encontrado)

        return { 'result': resultado  }