from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.maestro_model import Maestro

class MaestroDto(SQLAlchemyAutoSchema):
    class Meta:
        # model > para indicar que modelo tiene que utilizar para poder hacer el mapeo y validaciones de los atributos
        model = Maestro