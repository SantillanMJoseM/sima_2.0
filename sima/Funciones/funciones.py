import os
from datetime import datetime
from Consultas import consultas as con

def limpiar_pantalla():
    os.system('cls')

def verificoPeriodo(fecInicio, fecFin, estado):
    '''Se genera el control que la fecha de ejecucion este dentro de los periodos validos'''

    # Genero variable que cambia si el incio es valido
    valido = False
    est = 0

    # Obtener la fecha actual
    fecha_actual = datetime.now()
    
    try:    
        if estado > 0: 
            if fecInicio >= fecha_actual && fecFin <= fecha_actual:
                valido = True
                est = 0
            else:
                est = 2
        else:
            est = 1 
    except:
        print(f'El proceso no puede ser validado para el dia {fecha_actual}, para inicio de periodo {fecInicio}, fin de periodo {fecFom}. Con estado {estado}. Fue validado con {est}')

# Devuelvo resultado de ejecucion
return valido, estado
