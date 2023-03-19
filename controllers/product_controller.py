from flask_restful import Resource, request
from db import connection
from models.producto_model import Producto
from dtos.producto_dto import ProductoDto, MostrarProductoDto
from os import path

class ProductosController(Resource):
    def post(self):
        data = request.form.to_dict()
        # TODO: validar que tengamos esa llave en el formulario llamada 'imagen'
        # TODO: validar que solo sean imagenes
        imagen = request.files.get('imagen')
        # TODO: agregar un uuid al nombre de la imagen y sea un nombre valido
        # TODO: no recibir imagenes que pesen mas de 10Mb
        data['imagen'] = imagen.filename
        try:
            dto = ProductoDto()
            data_serializada = dto.load(data)
            nuevo_producto = Producto(**data_serializada)

            connection.session.add(nuevo_producto)
            imagen.save(path.join('imagenes', data['imagen']))

            connection.session.commit()

            return {
                'message': 'Producto creado exitosamente'
                }
        except Exception as error:
            connection.session.rollback()
            return {
                'message': 'Error al crear el producto',
                'content': error.args
            }
        
    def get(self):
        resultado = connection.session.query(Producto).all()
        dto = MostrarProductoDto()
        data = dto.dump(resultado, many=True)
        return {
            'content': data
        }
