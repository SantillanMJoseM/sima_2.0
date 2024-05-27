import os, sys,time, keyboard, json
from dotenv import load_dotenv

from Funciones.Consultas import consultas as con
from Funciones import funciones as fu
sys.path.append('../') 

# Cargar variables de entorno desde el archivo .env
load_dotenv()

argumento =  sys.argv[:]

# Se toma argumento de la empresa elegida
datos = argumento[1]

# Se consultan los datos de la empresa para continual la gestion
datos = con.consultarDatConexion(argumento[0])


while True:
    if keyboard.is_pressed('esc'):
        print("Tecla 'Esc' presionada. Cerrando ejecucion de sistema FTP")
        break
    print(os.getenv("rinicio") +' Iniciando servicio SIMA FTP ' + os.getenv("rfin"))
  
    # Obtener los parametos para la ejecucion del servicio
    param = con.buscoDirectorios(datos, argumento[1])

    #parm0 = Segundos para enviar mensaje
    #parm1 = Segundos para confirmar el envio
    #parm2 = Ruta origen de imagen
    #parm3 = Ruta destino de imagen
    #parm4 = Cerrar ventada al terminar el envio
    #parm5 = A definir
    #parm6 = A definir
    #parm7 = A definir
    
    # Carpetas de Destino y origen para ftp
    rOrigen = param.get("parm2")
    rDestino = param.get("parm3")
    print(rDestino, rOrigen)

    # Verifico los parametros obtenidos
    if rOrigen != None and rDestino != None:
        if os.getenv("debug"):
            print(f'El seteo de carpeta de origen es {rOrigen} el seteo de capeta desino es {rDestino}')    
    else:
        print('La ruta del sistema FTP no esta seteada')   
    # Espera 30 segundos antes de la siguiente iteración
    time.sleep(5)
