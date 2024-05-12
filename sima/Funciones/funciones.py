import os
import sys
from datetime import datetime
from Funciones.Consultas import consultas as con

sys.path.append('../') 


def limpiar_pantalla():
    '''Funcion para limpiar pantalla del terminal'''
    os.system('cls')

def verificoPeriodo(fecInicio, fecFin, estado):
    '''Se genera el control que la fecha de ejecucion este dentro de los periodos validos'''

    # Obtener la fecha actual
    fecha_actual = datetime.now()

    # Inicializo variables
    est = 0
    valido = False    
    if int(estado) > 0: 
        if fecInicio >= fecha_actual and fecFin <= fecha_actual:
            valido = True
            est = 0
        else:
            est = 2
    else:
        est = 1 
        print(f'El proceso no puede ser validado para el dia {fecha_actual}, para inicio de periodo {fecInicio}, fin de periodo {fecFin}. Con estado {est}. Fue validado con {valido}')

    # Devuelvo resultado de ejecucion
    return valido, est

def convertirDateTime(fecha):
    '''Convierte el string recibido en datetime'''

    return datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")

def mailAviso():

def mailError():

def mailConfirmacion():