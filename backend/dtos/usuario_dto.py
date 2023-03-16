from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema, fields
from models.usuario_model import Usuario

class UsuarioDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario

class LoginDto(Schema):
    # Validar el siguiente patron (expresion regular) xxxxx@xxxxx.xx
    correo = fields.Email(required=True, error_messages={ 'required': 'el correo es requerido' })
    password = fields.String(required=True, error_messages={ 'required': 'el password es requerido' })
