import mysql.connector

def Read_users(conexion):
    cursor = conexion.cursor()
    consulta = "Select id, nombre, apellido, edad from usuarios"
    cursor.execute(consulta)

    resultado = cursor.fetchall()
    cursor.close()
    return resultado