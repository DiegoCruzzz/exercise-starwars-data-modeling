import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

    favoritos = relationship('Favorito', back_populates='usuario')

class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    clima = Column(String(50), nullable=False)
    terreno = Column(String(50), nullable=False)
    poblacion = Column(Integer, nullable=True)

    favoritos = relationship('Favorito', back_populates='planeta')

class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), unique=True, nullable=False)
    altura = Column(String(50), nullable=True)
    peso = Column(String(50), nullable=True)
    genero = Column(String(20), nullable=True)
    color_pelo = Column(String(50), nullable=True)
    color_piel = Column(String(50), nullable=True)
    color_ojos = Column(String(50), nullable=True)

    favoritos = relationship('Favorito', back_populates='personaje')

class Favorito(Base):
    __tablename__ = 'favorito'
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'), nullable=False)
    planeta_id = Column(Integer, ForeignKey('planeta.id'), nullable=True)
    personaje_id = Column(Integer, ForeignKey('personaje.id'), nullable=True)

    usuario = relationship('Usuario', back_populates='favoritos')
    planeta = relationship('Planeta', back_populates='favoritos')
    personaje = relationship('Personaje', back_populates='favoritos')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
