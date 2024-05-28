import os, sys,time, keyboard, json
from dotenv import load_dotenv

from Funciones.Consultas import consultas as con
from Funciones import funciones as fu
sys.path.append('../') 

# Cargar variables de entorno desde el archivo .env
load_dotenv()
argumento =  sys.argv[:]

emp = argumento[1]# Se toma argumento de la empresa elegida
menid = argumento[2] # Se toma argumento de menu elegido

# Se consultan los datos de la empresa para continual la gestion
datos = con.consultarDatConexion(emp)

# Obtener los parametos para la ejecucion del servicio
param = con.buscoDirectorios(datos, menid)

# Imprimo Inicio de Servicio
print(os.getenv("rinicio") +' Iniciando servicio SIMA FTP ' + os.getenv("rfin"))

# Seteo bandera en False
salir = False

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
    rOrigen = param[0].get("parm2")
    rDestino = param[0].get("parm3")

    # Genero verificacion de valores.
    rOrigen = fu.cambBarr(fu.mCompro(rOrigen))
    rDestino = fucambBarr(fu.mCompro(rDestino))

    # Verifico los parametros obtenidos, no nulos y no vacios
    if ((rOrigen != None and rDestino != None) and (rOrigen != '' and rDestino != '')):
        if os.getenv("debug"):
            print(f'El seteo de carpeta de origen es {rOrigen} el seteo de capeta desino es {rDestino}')  

        # Genero lista de los archivos que pueda haber en la ruta
        archivos = os.listdir(rOrigen)

        # Proceso solo si existen archivos
        if len(archivos) > 0:

            # Inicio recorrido de archivos en el listado 
            for archivo in archivos:

                # Divido el archivo en nombre y formato para verificar
                nombre, extencion = fu.lExtencion(archivo)

                # Verifico el formato para comprender las acciones a ejecutar
                if extencion.upper() in ['.XLS', '.XLSX']:

                    # Genero nevo nombre para evitar dupliciadad
                    nArchivo = fu.nArchivo(nombre, extencion)

                    # Divido el archivo en nombre y formato para verificar
                    nombre, extencion = fu.lExtencion(nArchivo)

                    print("Acciones para documentos")
                elif extencion.upper() in ['.JPG', '.JPEG', '.BMP']:    
                    # Acciones para imagenes
                    print("Acciones para imagenes")
                else:
                    print(f"Formato no admitido por el sistema {extencion}")
    else:
        print('La ruta del sistema FTP no esta seteada')  
        # Si es erroneo corto con bandera
        salir = True 

    # Espera 30 segundos antes de la siguiente iteración
    time.sleep(5)
    
# Verificamos si necesitamos salir del ciclo
    if salir:
        break
