import os, sys
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
    if int(estado) == 1: 
        if fecInicio <= fecha_actual and fecFin >= fecha_actual:
            valido = True
            est = 0
        else:
            est = 2
    else:
        est = 1 
        print(f'El proceso no puede ser validado para el dia {fecha_actual}, para inicio de periodo {fecInicio}, fin de periodo {fecFin}. Con estado {est}. Fue validado con {valido}')

    # Devuelvo resultado de ejecucion
    return valido, est

def convertirDateTime(fecha, formato):
    '''Convierte el string recibido en datetime'''
    
    # Formatos  1 = datetime, 2 = date
    if formato == 1:
        fecha = datetime.strptime(fecha, "%Y-%m-%d %H:%M:%S")
    elif formato == 2:
        fecha = datetime.strptime(fecha, "%Y-%m-%d")
    else:
        fecha = datetime.strptime('1900-01-01', "%Y-%m-%d")

    return fecha

def ejecutoMenu(datos):
    '''Ejecucion de opcion del menu seleccionada'''

    # Antes de ejecutar el menu realizara todas las verificaciones correspondientes para la empresa
    # 1 - Tener un periodo valido y activo para la fecha de ejecucion del mismo 
    # 2 - Tener un total de campañas disponibles para la ejecucion a realizar 
    # 3 - Se verificaran los parametros minimos para el funcionamiento del sistema 
    # 4 - Tener disponibilidad de mensajes pendientes, luego en el proceso del archivo subido al ftp

    perInicio = convertirDateTime(str(datos[1].get("parm6")),1) 
    perFin = convertirDateTime(str(datos[1].get("parm7")),1) 
    estado = str(datos[1].get("estado")) 

    # Verifico que el periodo este dentro de termino de ejecucion o corto la misma
    estperiodo, errorcode = verificoPeriodo(perInicio, perFin , estado)          # Error 1 estado = 0, error 2 fuera de valides de periodo
        
    # Verifico cantidad de campañas ejecutadas en el periodo 
    estcampanias = con.cantCampanias(datos)
    estamensajes = True # con.cantMensajes(datos)

    if estperiodo: 
        est1 = 0
    else :
        est1 = 1 
    
    if estcampanias: 
        est2 = 0
    else: 
        est2 = 1

    if estamensajes:
        est3 = 0
    else:
        est3 = 1
    
    return est1, est2, est3

def mailAviso():
    '''Genera los correos electronicos para avisos(periodos invalidos, topes superados)'''
    print('Test')

def mailError():
    '''Genera los mail a todos los participantes de 
    la empresa y sistema, en caso de errores y excepciones'''

    print('Test')

def mailConfirmacion():
    '''Genera los mail para aviso de procesamiento exitoso'''
    print('Test')