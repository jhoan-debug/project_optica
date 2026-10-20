import mysql.connector

def Update_user(conexion, id_us):
    cursor = conexion(cursor)
    consulta = 'Update usuarios set nombre = %s, apellido = %s, edad = %s'
    cursor.execute(consulta, id_us)
    cursor.commit()
    print("query exitoso (update)")