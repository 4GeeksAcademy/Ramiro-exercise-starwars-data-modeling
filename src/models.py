import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Personas(Base):
    __tablename__ = 'personas'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    heigth= Column(Integer)
    mass= Column(Integer)
    hair_color= Column(String(250))
    sking_color= Column(String(250))
    eye_color= Column(String(250))
    gender= Column(String(250))
    birth_year= Column(String(50))

class Planetas(Base):
    __tablename__ = 'planetas'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    gravity = Column(Integer)
    diamer = Column(Integer)
    climate = Column(String(250))
    population = Column(Integer)
    terrain = Column(String(250))

    def to_dict(self):
        return {}

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    modelo=Column(String(100))
    vehicle_class=Column(String(100))
    passangres=Column(Integer)
    length=Column(Integer)
    consumables=Column(String(100))

    def to_dict(self):
        return {}


class Usuarios(Base):
    __tablename__ = 'usuarios'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre=Column(String(50))
    apellido=Column(String(50))
    nombre_de_usuario=Column(String(50))
    contraseña=Column(String(50))
    email= Column(String(50))
    edad=Column(Integer)
    DNI =Column(Integer, nullable=False)

    def to_dict(self):
        return {}
    
class Favoritos(Base):
    __tablename__ = 'favoritos'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    personas_id = Column(Integer, ForeignKey('personas.id'))
    planetas_id = Column(Integer, ForeignKey('planetas.id'))
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))
    usuarios_DNI = Column(String(15), ForeignKey('usuarios.DNI'), nullable=False )

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
