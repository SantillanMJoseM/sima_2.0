import os 
import pyodbc
import sys

from dotenv import load_dotenv
from Funciones import funciones as fu
sys.path.append('../') 


def consultaMenu():
    '''Consulta de todas los menus disponibles'''

    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    # Levanto las variables ya definidas
    server = os.getenv("servidor")
    bd = os.getenv("bd")
    user = os.getenv("user")
    password = os.getenv("password")

    try:
        conexion = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+password)

        # Crear un cursor
        cursor = conexion.cursor()

        # Consulta ejecutada
        cursor.execute('SELECT * FROM whatsdefimenu')

        # Obtener los nombres de las columnas
        columna_nombre = [columna[0] for columna in cursor.description]

        # Obtener todos los resultados en una lista de tuplas
        resu = cursor.fetchall()

        # Crear una lista de diccionarios con los resultados
        resultado = []

        for fila in resu:
            diccionario = {}
            for columna, value in zip(columna_nombre, fila):
                diccionario[columna] = value
            resultado.append(diccionario)

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

        # Retornar los resultados como un array
        return(resultado)

    except:
        print(f'Error en la coneccion a la base de datos {bd}')
        

def consultaEmpresas():
    '''Consulta de todas las empresas cargadas'''

    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    # Levanto las variables ya definidas
    server = os.getenv("servidor")
    bd = os.getenv("bd")
    user = os.getenv("user")
    password = os.getenv("password")

    try:
        conexion = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+password)

        # Crear un cursor
        cursor = conexion.cursor()

        # Consulta ejecutada
        cursor.execute('SELECT * FROM whatscabdefi')

        # Obtener los nombres de las columnas
        columna_nombre = [columna[0] for columna in cursor.description]

        # Obtener todos los resultados en una lista de tuplas
        resu = cursor.fetchall()

        # Crear una lista de diccionarios con los resultados
        resultado = []

        for fila in resu:
            diccionario = {}
            for columna, value in zip(columna_nombre, fila):
                diccionario[columna] = value
            resultado.append(diccionario)

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

        # Retornar los resultados como un array
        return(resultado)

    except:
        print(f'Error en la coneccion a la base de datos {bd}')
        

def consultarDatConexion(defiid):
    '''Consulta los datos de coneccion a la base de datos de la empresa seleccionada'''

    # Cargar variables de entorno desde el archivo .env
    load_dotenv()

    # Levanto las variables ya definidas
    server = os.getenv("servidor")
    bd = os.getenv("bd")
    user = os.getenv("user")
    password = os.getenv("password")

    try:
        conexion = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+server+';DATABASE='+bd+';UID='+user+';PWD='+password)

        # Crear un cursor
        cursor = conexion.cursor()

        # Consulta ejecutada
        cursor.execute('SELECT * FROM whatscabdefi where defiid = ' + str(defiid))

        # Obtener los nombres de las columnas
        columna_nombre = [columna[0] for columna in cursor.description]

        # Obtener todos los resultados en una lista de tuplas
        resu = cursor.fetchall()

        # Crear una lista de diccionarios con los resultados
        resultado = []

        for fila in resu:
            diccionario = {}
            for columna, value in zip(columna_nombre, fila):
                diccionario[columna] = value
            resultado.append(diccionario)

        # Consulto segunda tabla 
        cursor.execute('SELECT * FROM whatsdetdefi where defiid = ' + str(defiid) + ' and detid = (select max(detid) from whatsdetdefi where defiid = '+str(defiid)+' and estado = 1 )')

        # Obtener los nombres de las columnas
        columna_nombre = [columna[0] for columna in cursor.description]

        # Obtener todos los resultados en una lista de tuplas
        resu = cursor.fetchall()

        for fila in resu:
            diccionario = {}
            for columna, value in zip(columna_nombre, fila):
                diccionario[columna] = value
            resultado.append(diccionario)

        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

        # Retornar los resultados como un array
        return(resultado)

    except:
        print(f'Error en la coneccion a la base de datos {bd}')
    
def conexionBdEmpresa(datos):
    '''Se genera el parceo y generacion de la conexion'''

    # Cargar variables de entorno desde el archivo .env
    load_dotenv()
    
    # Levanto las variables ya definidas
    server = os.getenv("servidor")

    # Obtengo los parametos para generar toda la conexion
    empresa = str(datos[0].get("defnom"))
    sql_base = str(datos[0].get("defdb"))
    sql_user = str(datos[0].get("defdbuser"))
    sql_pass = str(datos[0].get("defdbpass"))
    emp_estado = str(datos[0].get("estado"))

    # Obtengo los datos de para el periodo en cuestion de la empresa 
    # y verifico la habilitacion de la misma
    detid = str(datos[1].get("detid"))                              # Id incremental para fila activa en el detalle (por periodo)
    parm0 = str(datos[1].get("parm0"))                              # A definir smallint
    parm1 = str(datos[1].get("parm1"))                              # A definir smallint
    parm2 = str(datos[1].get("parm2"))                              # Cantidad limite de mensajes a enviar
    parm3 = str(datos[1].get("parm3"))                              # Cantidad limite de campañas a enviar
    parm4 = str(datos[1].get("parm4"))                              # Correos a informar
    parm5 = str(datos[1].get("parm5"))                              # Correos a informar CC
    parm6 = fu.convertirDateTime(str(datos[1].get("parm6")))        # Fecha inicio de periodo 
    parm7 = fu.convertirDateTime(str(datos[1].get("parm7")))        # Fecha fin de periodo
    parm8 = str(datos[1].get("parm8"))                              # A definir
    parm9 = str(datos[1].get("parm9"))                              # A definir
    parm10 = str(datos[1].get("parm10"))                            # Cantidad de mensajes enviados 
    parm11 = str(datos[1].get("parm11"))                            # Cantidad de campañas enviadas
    periodo = str(datos[1].get("periodo"))                          # Periodo en ejecucion
    estado = str(datos[1].get("estado"))                            # Estado del periodo (0 = inactivo, 1 = Activo)

def consultarConfEmpresa():
    '''Consultar los tipos de mensajes habilitados para la empresa'''



    
def consultarConfEmpresa():
    '''Consultar los tipos de mensajes habilitados para la empresa'''