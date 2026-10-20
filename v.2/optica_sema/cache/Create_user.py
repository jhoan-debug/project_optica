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

        nombre = str(input("INgrese el nombre a enviar: "))
        apellido = str(input('Ingrese el apellido: '))
        edad = str(input('ingrese la edad a enviar: '))

        consulta = 'insert into usuarios(nombre, apellido, edad) values(%s, %s, %s)'

        datos = (nombre, apellido, edad)

        cursor.execute(consulta, datos)

        conexion.commit()
        
        print("Usuario creado exitosamente")

except mysql.connector.Error:
    print("Error al conectar la base de datos")

finally:
    if conexion.is_connected:
        conexion.close()
print("DB sesion cerrada")