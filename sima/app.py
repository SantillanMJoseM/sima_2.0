import os, subprocess, sys, keyboard, json

from Funciones import funciones as fu
from Funciones.Consultas import consultas as con

# Consulta  de empresas disponibles en el sistema
empresas = con.consultaEmpresas()
print('''Listado de empresas en el sistema
      ''')    

# Impresion de empresas encontradas
for empresa in empresas: 
    print('('+str(empresa.get("defiid"))+') - '+str(empresa.get("defnom")))

# Ingreso empresa elegida
emp = input('Ingrese la empresa correspondiente a trabajar: ')

# Limpieza de la pantalla 
fu.limpiar_pantalla()

# Traigo datos de la tabla para poder generar la coneccion
datos = con.consultarDatConexion(emp)

# Disparo las verificaciones para la ejecucion del menu.
result = con.veriEmpresa(datos)

# Si las verificaciones resultan correctas muestro el menu
if result:
    menus = con.consultaMenu()
    print('''Listado de menus en el sistema
          ''')    
    # Impresion de menus encontrados
    for menu in menus: 
        print('('+str(menu.get("menid"))+') - '+str(menu.get("mendesc")))

    # Opciones disponbles en la seleccion del menu
    opcion = input('Ingrese la opcion de menu correspondiente: ')

    # Limpieza de la pantalla 
    fu.limpiar_pantalla()

    # Inicio menu en falso
    menid_encontrado = False

    # Iterar sobre los diccionarios en la lista
    for menu in menus:
        if "menid" in menu and str(menu["menid"]) == opcion:
            menid_encontrado = True
            break

    # Verificar si se encontró el menid
    if menid_encontrado:

       # Armar ruta del menú a ejecutar
        menu_script = os.path.abspath('sima/Funciones/Menu/' + str(menu.get("menpy"))).replace('\\', '/')

        # Armar ruta del entorno virtual
        entorno = os.path.abspath('sima/Scripts/activate').replace('\\', '/')

        # Convierto diccionario en cadena
        #datos_str = ' '.join(map(str, datos))
        datos_str = json.dumps(datos)
        # Activar el entorno virtual y ejecutar el menú seleccionado
        resu = subprocess.run(['python', menu_script, datos_str, str(menu.get("menid"))], text=True, shell=True)

    else:
        print("No se encontró el menid en la lista.")

else: 
    print('La empresa en cuestion no tiene, limite disponible de mensajes, campañas o se encuentra en un periodo habilitado')