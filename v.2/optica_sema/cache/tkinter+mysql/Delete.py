import mysql.connector

def Delete_user(conexion, id_us):
    cursor = conexion.cursor()
    consulta = "delete from usuarios where id = %s"
    cursor.execute(consulta, (id_us,))
    conexion.commit()
    print("query exitoso")

    cursor.close()