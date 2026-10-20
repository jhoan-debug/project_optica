from config.conexion import conexion_db
import mysql.connector


def validar_login(dc, cont, rl):
    """esto se encarga de validar el login, comparando documento, clave y rol"""
    conexio = None
    try:
        conexio = conexion_db()
        cursor = conexio.cursor(buffered=True)

        consulta = "SELECT usu_clave, rol_id FROM usuarios WHERE usu_docum = %s"
        cursor.execute(consulta, (dc,))
        resultado = cursor.fetchone()
        cursor.close()

        if resultado is not None:
            contraseña_db, rol_db = resultado
            if cont == contraseña_db and rl == rol_db:
                print(f"Acceso concedido para el documento {dc} con rol {rol_db}")
                return True

        return False

    except mysql.connector.Error as error:
        print(f"Error en la lectura de la base de datos: {error}")
        return False
    finally:
        if conexio is not None:
            conexio.close()


def bienvenida(dc):
    # se encarga de extraer el usuario el cual accedio al sistema
    conexio = None
    try:
        conexio = conexion_db()
        cursor = conexio.cursor(buffered=True)

        consulta = "SELECT usu_nombre FROM usuarios WHERE usu_docum = %s"
        cursor.execute(consulta, (dc,))
        resultado = cursor.fetchone()
        cursor.close()

        return resultado[0] if resultado is not None else None

    except mysql.connector.Error as error:
        print(f"Error en la lectura de la base de datos: {error}")
        return None
    finally:
        if conexio is not None:
            conexio.close()


def obtener_roles():
    # lee los roles desde db
    conexio = None
    try:
        conexio = conexion_db()
        cursor = conexio.cursor()
        cursor.execute("SELECT rol_id, rol_nombre FROM roles")
        roles = {nombre: id_ for id_, nombre in cursor.fetchall()}
        cursor.close()
        return roles
    except mysql.connector.Error as error:
        print(f"Error al leer los roles: {error}")
        return {}
    finally:
        if conexio is not None:
            conexio.close()


def token():
    return False