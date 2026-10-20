import mysql.connector

try:
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "db_python"
    )

    if conexion.is_connected():
        cursor = conexion.cursor()

        #consulta aca en adelante.

        consulta = "Select * from usuarios"

        cursor.execute(consulta)

        registro = cursor.fetchall()

        for c in registro:
            print(c)

except mysql.connector.Error:
    print("Error al conectar la base de datos")

finally:
    if conexion.is_connected():
        conexion.close()
print("Sesion DB cerrada")