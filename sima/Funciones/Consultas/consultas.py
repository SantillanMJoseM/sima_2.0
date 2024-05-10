import os 
import pyodbc
from dotenv import load_dotenv

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
        cursor.execute('SELECT * FROM whatsdetdefi where defiid = ' + str(defiid))

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
    