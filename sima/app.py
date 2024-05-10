from Funciones import funciones
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

funciones.limpiar_pantalla()


menus = con.consultaMenu()
print('''Listado de menus en el sistema
      ''')    
# Impresion de menus encontrados
for menu in menus: 
    print('('+str(menu.get("menid"))+') - '+str(menu.get("mendesc")))

# Traigo datos de la tabla para poder generar la coneccion
datos = con.consultarDatConexion(emp)

# Opciones disponbles en la seleccion del menu
opcion = input('Ingrese la opcion de menu correspondiente: ')

# Limpieza de la pantalla 
funciones.limpiar_pantalla()

# Inicio menu en falso
menid_encontrado = False

# Iterar sobre los diccionarios en la lista
for menu in menus:
    if "menid" in menu and str(menu["menid"]) == opcion:
        menid_encontrado = True
        break

# Verificar si se encontró el menid
if menid_encontrado:
    print("Se encontró el menid en la lista.")
else:
    print("No se encontró el menid en la lista.")