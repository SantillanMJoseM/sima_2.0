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

# Impresion de opciones del menu
print('''
Selecciona la opcion correcta para continuar
      
(1) - Seleccione para iniciar servicio de archivos FTP
(2) - Seleccione para iniciar el envio de los mensajes
(3) - Ver ultimas campañas enviadas
(4) - Ver mensajes pendientes y tiempo
''')

# Traigo datos de la tabla para poder generar la coneccion
datos = con.consultarDatConexion(emp)

# Opciones disponbles en la seleccion del menu
opcion = input('Ingrese la opcion correspondiente: ')

# Limpieza de la pantalla 
funciones.limpiar_pantalla()

# Inicio de acciones segun la eleccion
if opcion == '1':
    print(f'ingresaste al modulo {opcion}')
elif opcion == '2':
    print(f'ingresaste al modulo {opcion}')
elif opcion == '3':
    print(f'ingresaste al modulo {opcion}')
elif opcion == '4':
    print(f'ingresaste al modulo {opcion}')
