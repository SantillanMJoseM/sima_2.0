Mejora de sistema sima, incluyendo menu y multimpres empresas para la ejecucion automatica del sistema.

Se implementa la ejecucion de funciones para la obtencion de datos de conexion, para luego gestionar la misma segun sea volcado o actulizacion de datos.


Funcionamiento basico del sistema

1-. Lista empresas que utilizan el sistema
2-. Con todos los datos obtenidos de la empresa, empieza a generar las verificaciones.
  2.1-. De la tabla whatsdetdefi obtiene el ultimo periodo para la empresa en cuestion y lo verifica contra la fecha actual.
  2.2-. De la table whatsdetdefi el seteo de (cantidad mensajes y campañas a enviar)
  2.3-. Con los datos de conexion obtenidos, busca la base y conecta con la misma. Teniendo esto en cuenta genera la             verificacion de los sigueintes puntos.
  2.4-. Verfica que la cantidad de campañas sea menor a la establecida en el seteo.
  2.5-. Realiza un conteo de los mensajes en la base correspondientes a ese periodo, en cualquier estado. "Con esto deja una     bandera encendida, pues falta controlar al procesar el documento que la cantidad actual mas la procesada no superen lo         seteado. 
    2.5.1-. Ver a futuro encio parcial, solo hasta el segmento permitido por los seteos.
3-. Con todas la verificaciones muestro los menus cargados en el sistema de forma dinamica, solo estado(1 = habilitado).
4-. Con los datos obtenidos de la empresa y menu, se procede a generar la accion requerida por el menu.

*------ Menus basicos del sistema ------*

1-. Iniciar servicio de FTP
2-. Iniciar envio de mensajes
3-. Listar ultimas campañas enviadas. (con total de mensajes de cada una, segmentando el periodo)
4-. Listar tiempo restante en ejecucion. (referencia a los mensajes ya procesados pendientes de envio, y campañas aun no iniciadas).

*------ Fin de menu ------*

******** ADICIONAL ********
Generar AMB: 

  *Empresas
  *Periodos
  *Menus
  *Tipo mensajes
