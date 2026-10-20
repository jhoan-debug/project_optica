import mysql.connector

def Create_user(conexion, nom, ape, ed):
    cursor = conexion.cursor()
    consulta = 'insert into usuarios (nombre, apellido, edad) values (%s, %s, %s)'
    datos = (nom, ape, ed)

    cursor.execute(consulta, datos)

    conexion.commit()

    cursor.close()
    print("query exitoso (create)")
