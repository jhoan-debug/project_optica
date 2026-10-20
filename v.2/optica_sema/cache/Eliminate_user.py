import mysql.connector

try:
    conexion = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'db_python'
    )

    if conexion.is_connected():

        cursor = conexion.cursor()

        consulta = 'Select * from usuarios'

        print("Log")
        cursor.execute(consulta)
        print("Log")
        datos = cursor.fetchall()

        print("Usuarios registrados")

        for c in datos:
            print(c)

        find = int(input("Ingrese el id del usuario a eliminar"))

        encontrado = False
        for c in datos:
            if find == c[0]:
                consulta = 'delete from usuarios where id = %s'
                cursor.execute (consulta, (find,))
                conexion.commit()
                encontrado = True
                break

        if not encontrado:
            print("No se encontro dicho id")

except mysql.connector.Error:
    print("error al conectar a la base de datos")
finally:
    if conexion.is_connected:
        conexion.close()
print("DB sesion cerrada")
