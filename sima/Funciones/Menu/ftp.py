import os, sys,time, keyboard, json
from dotenv import load_dotenv

from Funciones.Consultas import consultas as con
from Funciones import funciones as fu
sys.path.append('../') 

# Cargar variables de entorno desde el archivo .env
load_dotenv()

argumento =  sys.argv[:]

# Se toma argumento de la empresa elegida
emp = argumento[1]

# Se toma argumento de menu elegido
menid = argumento[2]

# Se consultan los datos de la empresa para continual la gestion
datos = con.consultarDatConexion(emp)

# Obtener los parametos para la ejecucion del servicio
param = con.buscoDirectorios(datos, menid)

# Imprimo Inicio de Servicio
print(os.getenv("rinicio") +' Iniciando servicio SIMA FTP ' + os.getenv("rfin"))

# Inicio ciclo de escaneo
while True:
    if keyboard.is_pressed('esc'):
        print("Tecla 'Esc' presionada. Cerrando ejecucion de sistema FTP")
        break
  
    #parm0 = Segundos para enviar mensaje
    #parm1 = Segundos para confirmar el envio
    #parm2 = Ruta origen de imagen
    #parm3 = Ruta destino de imagen
    #parm4 = Cerrar ventada al terminar el envio
    #parm5 = A definir
    #parm6 = A definir
    #parm7 = A definir
    
    # Carpetas de Destino y origen para ftp
    rOrigen = param[0].get("parm2").replace('\\', '/')
    rDestino = param[0].get("parm3").replace('\\', '/')

    # Verifico los parametros obtenidos
    if rOrigen != None and rDestino != None:
        if os.getenv("debug"):
            print(f'El seteo de carpeta de origen es {rOrigen} el seteo de capeta desino es {rDestino}')  

        # Genero lista de los archivos que pueda haber en la ruta
        archivos = os.listdir(rOrigen)

        # Inicio recorrido de archivos en el listado 
        for archivo in archivos:

            # Divido el archivo en nombre y formato para verificar
            nombre, extencion = fu.lExtencion(archivo)

            # Verifico el formato para comprender las acciones a ejecutar
            if extencion.upper() == '.XLS' or extencion.upper() == '.XLSX':

                # Genero nevo nombre para evitar dupliciadad
                nArchivo = fu.nArchivo(nombre, extencion)

                # Divido el archivo en nombre y formato para verificar
                nombre, extencion = fu.lExtencion(nArchivo)

                print("Acciones para documentos")
            elif extencion.upper() == '.JPG' or extencion.upper() == '.JPEG' or extencion.upper() == '.BMP':    
                # Acciones para imagenes
                print("Acciones para imagenes")
            else:
                print(f"Formato no admitido por el sistema {extencion}")
    else:
        print('La ruta del sistema FTP no esta seteada')   
    # Espera 30 segundos antes de la siguiente iteración
    time.sleep(5)
