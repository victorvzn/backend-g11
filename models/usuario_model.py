from db import connection

from enum import Enum
from sqlalchemy import Column, types

class TipoUsuario(Enum):
    ADMIN = 'ADMIN'
    PERSONA = 'PERSONA'

class Usuario(connection.Model):
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text)
    apellido = Column(type_=types.Text)
    correo = Column(type_=types.Text, unique=True, nullable=False)
    password = Column(type_=types.Text, nullable=False)
    tipo = Column(type_=types.Enum(TipoUsuario), default=TipoUsuario.PERSONA)

    __tablename__ = 'usuarios'
