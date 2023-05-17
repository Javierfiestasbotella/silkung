# -*- coding: utf-8 -*-
import os
import pathlib
from io import open


class Ejercicio:
    def __init__(self, musculos, tipo_respiracion, nivel, repeticiones, tipo, descripcion):
        self.musculos = musculos
        self.tipo_respiracion = tipo_respiracion
        self.nivel = nivel
        self.repeticiones = repeticiones
        self.tipo = tipo
        self.descripcion = descripcion

    def __str__(self):
        return f'''
musculos = {self.musculos}
tipo_respiracion = {self.tipo_respiracion}
nivel = {self.nivel}
repeticiones = {self.repeticiones}
tipo = {self.tipo}
descripcion = {self.descripcion}'''

#EJERCICIOS CHIKUNG

qigong_ejercicio1 = Ejercicio('Piernas', 'Respiración profunda', 'Principiante', 10, 'Qigong de las Cinco Áreas', 'Fortalece las piernas y mejora el equilibrio')
qigong_ejercicio2 = Ejercicio('Abdominales', 'Respiración abdominal', 'Intermedio', 15, 'Qigong de los Seis Sonidos', 'Ayuda a la digestión y fortalece los órganos internos')
qigong_ejercicio3 = Ejercicio('Cuello, hombros y espalda', 'Respiración torácica', 'Avanzado', 20, 'Qigong de la Grulla', 'Alivia la tensión en la parte superior del cuerpo y mejora la postura')
qigong_ejercicio4 = Ejercicio('Piernas y cadera', 'Respiración profunda', 'Principiante', 10, 'Qigong de la Tortuga', 'Fortalece las piernas y mejora la flexibilidad de las caderas')
qigong_ejercicio5 = Ejercicio('Brazos y pecho', 'Respiración torácica', 'Intermedio', 15, 'Qigong de los Ocho Brocados', 'Fortalece los brazos y mejora la respiración')
qigong_ejercicio6 = Ejercicio('Cintura y columna', 'Respiración abdominal', 'Avanzado', 20, 'Qigong del Dragón', 'Fortalece la cintura y la columna vertebral')
qigong_ejercicio7 = Ejercicio('Piernas', 'Respiración profunda', 'Principiante', 10, 'Qigong de las Seis Curvas', 'Fortalece las piernas y mejora la circulación de la sangre')
qigong_ejercicio8 = Ejercicio('Abdominales y pecho', 'Respiración torácica', 'Intermedio', 15, 'Qigong de las Tres Cabezas', 'Fortalece los abdominales y mejora la respiración')
qigong_ejercicio9 = Ejercicio('Espalda', 'Respiración abdominal', 'Avanzado', 20, 'Qigong de la Serpiente', 'Alivia la tensión en la parte superior de la espalda y mejora la flexibilidad de la columna vertebral')
qigong_ejercicio10 = Ejercicio('Piernas y cadera', 'Respiración profunda', 'Principiante', 10, 'Qigong del Mono', 'Fortalece las piernas y mejora la flexibilidad de las caderas')
qigong_ejercicio11 = Ejercicio('Cuerpo entero', 'Respiración profunda', 'Principiante', 10, 'Qigong de la Familia Wu', 'Mejora la circulación y fortalece el cuerpo')
qigong_ejercicio12 = Ejercicio('Cuello y hombros', 'Respiración abdominal', 'Intermedio', 15, 'Qigong de las Siete Palmas', 'Alivia la tensión en el cuello y los hombros')
qigong_ejercicio13 = Ejercicio('Piernas y cadera', 'Respiración profunda', 'Avanzado', 20, 'Qigong de la Serpiente y la Garza', 'Fortalece las piernas y mejora la flexibilidad de las caderas')
qigong_ejercicio14 = Ejercicio('Cintura y abdomen', 'Respiración torácica', 'Principiante', 10, 'Qigong del Caballo Salvaje', 'Fortalece la cintura y el abdomen')
qigong_ejercicio15 = Ejercicio('Cuello y espalda', 'Respiración abdominal', 'Intermedio', 15, 'Qigong de los Ocho Movimientos', 'Alivia la tensión en el cuello y la espalda')
qigong_ejercicio16 = Ejercicio('Brazos y pecho', 'Respiración profunda', 'Avanzado', 20, 'Qigong de los Cinco Animales', 'Fortalece los brazos y el pecho')
qigong_ejercicio17 = Ejercicio('Cintura y columna', 'Respiración torácica', 'Principiante', 10, 'Qigong de la Tortuga Negra', 'Fortalece la cintura y la columna vertebral')
qigong_ejercicio18 = Ejercicio('Piernas y glúteos', 'Respiración profunda', 'Intermedio', 15, 'Qigong del Pato', 'Fortalece las piernas y los glúteos')
qigong_ejercicio19 = Ejercicio('Cabeza y cuello', 'Respiración abdominal', 'Avanzado', 20, 'Qigong de la Serpiente y el Tigre', 'Alivia la tensión en la cabeza y el cuello')
qigong_ejercicio20 = Ejercicio('Brazos y hombros', 'Respiración torácica', 'Principiante', 10, 'Qigong de la Garza Blanca', 'Fortalece los brazos y los hombros')

#EJERCICIOS DE PILATES
pilates_ejercicio1 = Ejercicio('Abdominales', 'Inhalación', 'Principiante', 10, 'Roll Up', 'Fortalece los abdominales y la columna vertebral')
pilates_ejercicio2 = Ejercicio('Piernas', 'Exhalación', 'Intermedio', 15, 'Single Leg Circle', 'Mejora la flexibilidad de las caderas y fortalece las piernas')
pilates_ejercicio3 = Ejercicio('Brazos', 'Inhalación', 'Avanzado', 20, 'Push Up', 'Fortalece los brazos, el pecho y los abdominales')
pilates_ejercicio4 = Ejercicio('Espalda', 'Exhalación', 'Principiante', 10, 'Swan Dive', 'Fortalece la espalda y mejora la postura')
pilates_ejercicio5 = Ejercicio('Piernas y glúteos', 'Inhalación', 'Intermedio', 15, 'Side Kick Series', 'Fortalece las piernas y los glúteos')
pilates_ejercicio6 = Ejercicio('Brazos y hombros', 'Exhalación', 'Avanzado', 20, 'Teaser', 'Fortalece los brazos, los hombros y los abdominales')
pilates_ejercicio7 = Ejercicio('Abdominales', 'Inhalación', 'Principiante', 10, 'Hundred', 'Mejora la respiración y fortalece los abdominales')
pilates_ejercicio8 = Ejercicio('Piernas', 'Exhalación', 'Intermedio', 15, 'Rolling Like a Ball', 'Fortalece los abdominales y la columna vertebral')
pilates_ejercicio9 = Ejercicio('Brazos', 'Inhalación', 'Avanzado', 20, 'Saw', 'Mejora la flexibilidad de la columna vertebral y fortalece los brazos y las piernas')
pilates_ejercicio10 = Ejercicio('Espalda', 'Exhalación', 'Principiante', 10, 'Spine Stretch', 'Mejora la postura y fortalece la espalda')
pilates_ejercicio11 = Ejercicio('Piernas y glúteos', 'Inhalación', 'Intermedio', 15, 'Leg Pull Front', 'Fortalece los glúteos y las piernas')
pilates_ejercicio12 = Ejercicio('Brazos y hombros', 'Exhalación', 'Avanzado', 20, 'Swan', 'Fortalece los brazos, los hombros y la espalda')
pilates_ejercicio13 = Ejercicio('Abdominales', 'Inhalación', 'Principiante', 10, 'Double Leg Stretch', 'Fortalece los abdominales y la columna vertebral')
pilates_ejercicio14 = Ejercicio('Piernas', 'Exhalación', 'Intermedio', 15, 'Criss Cross', 'Fortalece los abdominales y mejora la flexibilidad de la columna vertebral')
pilates_ejercicio15 = Ejercicio('Brazos', 'Inhalación', 'Avanzado', 20, 'Control Balance', 'Fortalece los brazos, los hombros y el abdomen')
pilates_ejercicio16 = Ejercicio('Abdominales', 'Exhalación al esfuerzo', 'Intermedio', 10, 'Mat', 'Llevar el cuello hacia adelante sin tensión')
pilates_ejercicio17 = Ejercicio('Espalda', 'Inhalación en la preparación, exhalación en el movimiento', 'Principiante', 8, 'Reformer', 'Trabajar los extensores de la columna en posición prona')
pilates_ejercicio18 = Ejercicio('Piernas', 'Inhalación en la preparación, exhalación en el movimiento', 'Intermedio', 12, 'Silla', 'Fortalecer los cuádriceps en posición sentada')
pilates_ejercicio19 = Ejercicio('Glúteos', 'Inhalación en la preparación, exhalación en el movimiento', 'Avanzado', 15, 'Wall', 'Tonificar los glúteos en posición de pared')
pilates_ejercicio20 = Ejercicio('Abdominales', 'Exhalación al esfuerzo', 'Principiante', 8, 'Mat', 'Fortalecer la musculatura abdominal en posición supina')





lista_qigong=[qigong_ejercicio1,qigong_ejercicio2,qigong_ejercicio3,qigong_ejercicio4,qigong_ejercicio5,qigong_ejercicio6,qigong_ejercicio7,qigong_ejercicio8,qigong_ejercicio9,qigong_ejercicio10,qigong_ejercicio11,qigong_ejercicio12,qigong_ejercicio13,qigong_ejercicio14,qigong_ejercicio15,qigong_ejercicio16,qigong_ejercicio17,qigong_ejercicio18,qigong_ejercicio19,qigong_ejercicio20]

lista_pilates=[pilates_ejercicio1,pilates_ejercicio2,pilates_ejercicio3,pilates_ejercicio4,pilates_ejercicio5,pilates_ejercicio6,pilates_ejercicio7,pilates_ejercicio8,pilates_ejercicio9,pilates_ejercicio10,pilates_ejercicio11,pilates_ejercicio12,pilates_ejercicio13,pilates_ejercicio14,pilates_ejercicio15,pilates_ejercicio16,pilates_ejercicio17,pilates_ejercicio18,pilates_ejercicio19,pilates_ejercicio20]

# crea una lista que contenga ambas listas
todas_las_listas = [lista_qigong, lista_pilates]

# crea un archivo de texto
ruta_archivo = pathlib.Path("static/ejercicios.txt")
archivo = open(ruta_archivo, mode="w", encoding="utf-8")

# itera sobre la lista de listas y luego sobre cada lista de ejercicios
for lista in todas_las_listas:
    for ejercicio in lista:
        archivo.write(str(ejercicio))
        archivo.write("\n")

# cierra el archivo
archivo.close()
#def tabla_ejercicios(tipo,nombre):
#if pathlib.Path(f"static/{nombre}.txt"):

def crear_ejercicios(curso, cantidad):
    lista = []
    lista_nueva=[]
    if curso == 'Pilates':
        lista = lista_pilates.copy()
    elif curso == 'Chikung':
        lista = lista_qigong.copy()

    n = cantidad.split(",")
    for numero_ejercicio in n:
        lista_nueva.append(lista[int(numero_ejercicio)])
    return lista_nueva


