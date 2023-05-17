# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#Engine Le dice al sqlalchemy a que BBDD se va a conectar
engine = create_engine('sqlite:///database/usuarios.db')

#Sesion
Session = sessionmaker(bind=engine)
session = Session()

#Vinculación: Transformacion de las clases a tablas
Base = declarative_base()
