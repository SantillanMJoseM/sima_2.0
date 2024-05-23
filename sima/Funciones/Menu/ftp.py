import os, sys,time, keyboard, json
from dotenv import load_dotenv

from Funciones.Consultas import consultas as con
from Funciones import funciones as fu
sys.path.append('../') 

# Cargar variables de entorno desde el archivo .env
load_dotenv()

argumento =  sys.argv[:]

#datos = json.dumps(argumento[0])
#datos = json.loads(argumento[0])
datos = argumento[1]
print(datos)

# Dividir la cadena en fragmentos de diccionarios
dict_strs = datos.split("} {")

# Corregir 
dict_strs[0] = dict_strs[0].strip("{")
dict_strs[-1] = dict_strs[-1].strip("}")

# Convertir cada fragmento en un diccionario Python
dic = [eval(d) for d in dict_strs]

print(type(dic))
print(len(datos))
print(dic)


while True:
    if keyboard.is_pressed('esc'):
        print("Tecla 'Esc' presionada. Cerrando ejecucion de sistema FTP")
        break
    print(os.getenv("rinicio") +' Iniciando servicio SIMA FTP ' + os.getenv("rfin"))
  
    # Obtener los parametos para la ejecucion del servicio
    #param = con.buscoDirectorios(datos, argumento[1])


    #print(datos.get("parm2"))

    #parm0 = Segundos para enviar mensaje
    #parm1 = Segundos para confirmar el envio
    #parm2 = Ruta origen de imagen
    #parm3 = Ruta destino de imagen
    #parm4 = Cerrar ventada al terminar el envio
    #parm5 = A definir
    #parm6 = A definir
    #parm7 = A definir
    
    #rOrigen = param.get("parm2")
    #rDestino = param.get("parm3")
    #print(rDestino, rOrigen)

    # Verifico los parametros obtenidos
    #if rOrigen != None and rDestino != None:
    #    if os.getenv("debug"):
    #        print(f'El seteo de carpeta de origen es {rOrigen} el seteo de capeta desino es {rDestino}')
    #    
    #else:
    #    print('La ruta del sistema FTP no esta seteada')   
    # Espera 30 segundos antes de la siguiente iteración
    time.sleep(5)
