import os, sys,time, keyboard
from dotenv import load_dotenv

from Funciones.Consultas import consultas as con
from Funciones import funciones as fu
sys.path.append('../') 

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def iniciarServicioFtp(datos):
      while True:
        if keyboard.is_pressed('esc'):
            print("Tecla 'Esc' presionada. Saliendo del bucle.")
            break

        print(os.getenv("rinicio") +' Iniciando servicio SIMA FTP ' + os.getenv("rfin"))

        # Espera 30 segundos antes de la siguiente iteración
        time.sleep(30)
