import os
import pyodbc
import sys
from Funciones.Consultas import consultas as con
from Funciones import funciones as fu

sys.path.append('../') 

# Genero ciclo para escanear cada cierto tiempo el directorio donde esta el ftp
while 