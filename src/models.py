import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    name = Column(String(80), nullable=False)
    last_name = Column(String(80), nullable=False)

    favourites = relationship('Favourites', back_populates='user')

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    gender = Column(String(20))
    species = Column(String(100))
    birth_year = Column(String(20))
    homeworld = Column(String(100))
    skin_color = Column(String(50))
    films = Column(String(255))
    vehicles = Column(String(255))

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    climate = Column(String(100))
    terrain = Column(String(100))
    population = Column(Integer)
    films = Column(String(255))

    favourites = relationship('Favourites', back_populates='planet')

class Vehicle(Base):
    __tablename__ = 'vehicle'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    type = Column(String(100))
    max_speed = Column(String(50))
    specie = Column(String(50))
    films = Column(String(255))

    favourites = relationship('Favourites', back_populates='vehicle')

class Favourites(Base):
    __tablename__ = 'favourites'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)

    user = relationship('User', back_populates='favourites')
    planet = relationship('Planet', back_populates='favourites')
    character = relationship('Character', back_populates='favourites')
    vehicle = relationship('Vehicle', back_populates='favourites')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
