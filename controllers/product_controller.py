from flask_restful import Resource, request
from werkzeug.utils import secure_filename
# from werkzeug.exceptions import RequestEntityTooLarge
from uuid import uuid4

from db import connection
from models.producto_model import Producto
from dtos.producto_dto import ProductoDto, MostrarProductoDto

from os import path

class ProductosController(Resource):
    def post(self):
        data = request.form.to_dict()

        # TODO: validar que tengamos esa llave en el formulario llamada 'imagen'
        # if  not request.files.get('imagen'):
        if  not 'imagen' in request.files:
            return { 'message': 'Campo imagen es requerido' }

        # TODO: validar que solo sean imagenes
        imagen = request.files.get('imagen')
        mimetype_valido = 'image/'
        if  mimetype_valido not in imagen.mimetype:
            return { 'message': 'El archivo no es una imagen valida.' }

        # TODO: agregar un uuid al nombre de la imagen y sea un nombre valido
        nombre = secure_filename(uuid4().hex + '_' + imagen.filename)
        data['imagen'] = 'imagenes/' + nombre

        # TODO: no recibir imagenes que pesen mas de 10Mb
        MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10MB max-limit.
        if (request.content_length > MAX_CONTENT_LENGTH):
            return {
                'message': 'La imagen es muy pesada. Max. 10MB.',
            }

        try:
            dto = ProductoDto()
            data_serializada = dto.load(data)
        
            nuevo_producto = Producto(**data_serializada)

            connection.session.add(nuevo_producto)
            imagen.save(path.join('imagenes', nombre))

            connection.session.commit()

            return { 'message': 'Producto creado exitosamente' }
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
        
        return { 'content': data }
