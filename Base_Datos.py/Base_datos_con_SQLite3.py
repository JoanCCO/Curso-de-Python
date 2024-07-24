import sqlite3

conexion = sqlite3.connect('BaseDeDatos')
cursorBD = conexion.cursor() #el cursor nos va a ayudar para desplasarse dentro de la base de datos y realizar la accion que necesitemos dichas acciones son: seleccionar, incertar, actualizar y borrar 

#ok ahora creamos una estructura de como se va a generar la tabla y tambien necesitamos una funcion que verifique si existe o no una tabla

def tablaExiste(nombreTabla):
    cursorBD.execute('''SELECT COUNT(name) FROM SQLITE_MASTER WHERE TYPE = 'table' AND name = '{}' '''.format(nombreTabla))
    if cursorBD.fetchone()[0] == 1: 
       return True
    else:
       cursorBD.execute(''' CREATE TABLE PRODUCTO (CODIGO INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE TEXT, PRECIO REAL) ''')
       return False
       
tablaExiste('PRODUCTO')


    

