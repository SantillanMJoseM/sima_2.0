Mejora de sistema sima, incluyendo menu y multimpres empresas para la ejecucion automatica del sistema.

Se implementa la ejecucion de funciones para la obtencion de datos de conexion, para luego gestionar la misma segun sea volcado o actulizacion de datos.


Funcionamiento basico del sistema

~~1-. Lista empresas que utilizan el sistema~~

~~2-. Con todos los datos obtenidos de la empresa, empieza a generar las verificaciones.~~

~~2.1-. De la tabla whatsdetdefi obtiene el ultimo periodo para la empresa en cuestion y lo verifica contra la fecha actual.~~
  
~~2.2-. De la table whatsdetdefi el seteo de (cantidad mensajes y campañas a enviar)~~
  
~~2.3-. Con los datos de conexion obtenidos, busca la base y conecta con la misma. Teniendo esto en cuenta genera la verificacion de los sigueintes puntos.~~
  
~~2.4-. Verfica que la cantidad de campañas sea menor a la establecida en el seteo.~~
  
~~2.5-. Realiza un conteo de los mensajes en la base correspondientes a ese periodo, en cualquier estado. "Con esto deja una bandera encendida, pues falta controlar al procesar el documento que la cantidad actual mas la procesada no superen lo seteado.~~
  
2.5.1-. Ver a futuro encio parcial, solo hasta el segmento permitido por los seteos.
    
~~3-. Con todas la verificaciones muestro los menus cargados en el sistema de forma dinamica, solo estado(1 = habilitado).~~

~~4-. Con los datos obtenidos de la empresa y menu, se procede a generar la accion requerida por el menu.~~


*------ Menus basicos del sistema ------*


1-. Iniciar servicio de FTP

2-. Iniciar envio de mensajes

3-. Listar ultimas campañas enviadas. (con total de mensajes de cada una, segmentando el periodo)

4-. Listar tiempo restante en ejecucion. (referencia a los mensajes ya procesados pendientes de envio, y campañas aun no iniciadas).

*------ Fin de menu ------*


Se generan instancias que contendran los menus principales para las funciones de controles y ejecucion de cada una.

*//////// Menu de servicios FPT ////////*

1-. Tomar rutas de Origen y Destino desde la base de datos para la empresa seleccionada 

2 -. Ver si existe algo en la carpeta del ftp (Origen) 

2.1 -. De ser comprobada la existencia del mismo o mismos.

2.2 -. Generar control general de extenciones permitidas de archivos (implementar tabla te relleno para estos formatos por empresa(whatsformat dentro de base SIMA).

2.3 -. Definicion por empresa sobre archivos con extencion no validas (Borrados o movidos a carpera Errors FTP)

3 -. Si la extencion esta dentro de los validos, empiezo a procesarlo

3.1 -. Si la extencion es Imagen (Salto al punto 4)

3.2 -. Si la extencion xls, xlsx (Salto al punto 5)

3.3 -. Si la extencion es Cualquier otro dentro de los permidos(Salto a punto 6)

4 -. Teniendo el cuenta la extencion (JPG, PNG, BMP) los nombres de los archivos no deben superar C(80).
Se agregara al final del nombre enviado "_fechareal" esta incluira la fecha del procesamiento y estara atada a la
campaña que la utilice dentro del mismo dia (Fecha real) y la mencione en el excel en el lugar correspondiente a adjuntos.

5 -. Teniendo en cuenta que se trata del archivo principal a ser procesado se detallara el proceso.

5.1 -. Verificacion de la taba de crifrado, si la misma esta cargada como periodo activo para cifrado. (Los valores seran cifrado y guardados en ccelular, y cmensaje), generando la imposibilidad para que puedan ser vistos facilmente desde basa. Solo seran DS en tiempo real durante la ejecucion. (Los archivos deben ser cifrados con PGP y proveer de la llave correspondiente a cargo de la emrpesa.

5.2 -. Se tomara el excel modelo, verificando el largo de su nombre no supero los c(80) y agregarndo al final del mismo "_FechaReal" esta sera el momente en el cual se genera el procesamiento del documento.

5.3 -. Se calculara el hash del mismo y guardara en la tabla de cifrado, para con el mismo generar un cifrado de 2 niveles, unico para cada archivo enviado.

5.4 -. Se procedera a la verificacion de los campos del excel y generar todos los datos correspondientes a su almacenanmiento. 

5.5 -. Se veridicara el diccionario resultante del proceso para un ves aprobado el proceso completeto iniciar el bolcado a la base de datos de forma transaccional para evitar volcados parciales.

5.6 -. Finalizado se enviara un correo electronico ( segun los parametros obtenidos de la base de datos ) para confirmar el correcto procesamiento del mismo 

5.6.1 -. De la misma forma, de haber ocurrido un error se generara un correo electronico explicando el problema que genero el error del procesamiento.

5.6.2 -. Errores en los datos leidos no eximen el procesamiento correcto del sistema. Tales como (longitud de campos(Los mismos seran reducidos a si maximo de ser superados, cortando siempre desde el final la cantidad correspondiente), todos los datos son procesados como str para evitar errores y luego convertidos segun las necesidades del sistema.), 

6 -. (SOLO DISPONIBLE PARA SIMA 3.0 ENVIO DE ADJUNTOS TODOS) Teniendo el cuenta la extencion (No debe corresponder a ninguno de los anteriores) los nombres de los archivos no deben superar C(80).
Se agregara al final del nombre enviado "_fechareal" esta incluira la fecha del procesamiento y estara atada a la
campaña que la utilice dentro del mismo dia (Fecha real) y la mencione en el excel en el lugar correspondiente a adjuntos.

*////////FIn menu de servicios FPT ////////*



******** ADICIONAL ********

Generar AMB: 

  *Empresas
  *Periodos
  *Menus
  *Tipo mensajes
