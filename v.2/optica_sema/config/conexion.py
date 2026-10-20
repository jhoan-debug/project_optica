import mysql.connector

def conexion_db():
    try:

        conexion_obj = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "historia_clinica"
        )

        if conexion_obj.is_connected():
            print("Conexion existosa")
            return conexion_obj

    except mysql.connector.Error:
        print("Ocurrio un error al conectar la base de datos")
        return None
