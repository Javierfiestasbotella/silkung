# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import date
import db
import datetime

class User(db.Base):
    __tablename__ = 'usuarios'
    __table_args__ = {'sqlite_autoincrement': True}
    id_user = Column(Integer, primary_key=True)
    nombre = Column(String(200), nullable=False)
    apellidos = Column(String(200), nullable=False)
    email = Column(String(20))
    curso = Column(String(10))
    edad = Column(Integer)
    perfil = Column(String(500))
    password = Column(String(10))

    def __init__(self, nombre, apellidos, email, curso, edad, perfil, password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = email
        self.curso = curso
        self.edad = edad
        self.perfil = perfil
        self.password = password


    def __str__(self):
        return f'''
            Nombre: {self.nombre}
            apellidos: {self.apellidos}
            email: {self.email}
            Curso: {self.curso}
            Edad: {self.edad}
            Perfil: {self.perfil}
            Password: {self.password}'''




#Creamos otra tabla relacionada con el user de la anterior
class NewTable(db.Base):
    __tablename__ = 'datos'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('usuarios.id_user'))
    fecha_inicio = Column(Date)
    facturas = Column(String(1000))
    lista_ejercicios = Column(String(500))
    cursos = Column(String(500))
    user = relationship("User")

    def __init__(self, user_id, fecha_inicio, facturas, lista_ejercicios, cursos):
        self.user_id = user_id
        self.fecha_inicio = fecha_inicio
        self.facturas = facturas
        self.lista_ejercicios = lista_ejercicios
        self.cursos = cursos

    def mostrar_facturacion(self):
        today = date.today().strftime('%Y-%m-%d')
        print(today-self.facturas)


    def __str__(self):
        return f'''
        User_id: {self.user_id}
        Fecha inicio: {self.fecha_inicio}
        Facturas: {self.facturas}
        Lista ejercicios: {self.lista_ejercicios}
        Cursos: {self.cursos}'''


