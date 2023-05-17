# -*- coding: utf-8 -*-
#!/usr/bin/python
import os
import pathlib
from io import open
import datetime
from datetime import datetime
import time

'''ESte archivo.py lo que hace es recoger todas las excepciones que creemos en el codigo
 y almacenarlas en archivos diariamente paa poder tener un informe detallado de los errores
 más comunes para ir solventando u optimizando'''

#origen = seudo=pathlib.Path(__file__).parent.absolute()
fecha = datetime.now().strftime('%Y-%m-%d')

def crea_fichero(name):
    print(fecha +'.txt')
    hora =datetime.now().strftime('%H:%M')

    if os.path.exists('static\\errores\\'+fecha+'.txt' )==True:
        fichero =open(str('{}.txt'.format('static\\errores\\'+fecha)) ,'a')
        fichero.write("\n{}---> Hora: {}\n".format(name ,hora))
        fichero.close()
    else:
        lista =[]
        fichero =open(str('{}.txt'.format('static\\errores\\'+fecha)) ,'a' ,encoding="utf-8")
        fichero.write("\n{}---> Hora: {}\n".format(name ,hora))
        fichero.close()

