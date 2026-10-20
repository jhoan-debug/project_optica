import tkinter as tk
import mysql.connector

try:
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "db_python"
    )

    if conexion.is_connected():
        print("Conexion existosa")

except mysql.connector.Error:
    print("Ocurrio un error al conectar la base de datos")

finally:
    conexion.close()
print("Conexion cerrada")