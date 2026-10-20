from config import conexion


class Paciente:
    def __init__(self, documento, nombre, apellido, direccion,
                 telefono, correo, gen_id, estr_id, hobbies_ids, pac_id=None):
        self.documento = documento
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.gen_id = gen_id
        self.estr_id = estr_id
        self.hobbies_ids = hobbies_ids   # lista de hob_id, ej: [1, 3]
        self.pac_id = pac_id

    def validar(self):
        if not self.documento or not self.nombre or not self.apellido:
            raise ValueError("Documento, nombre y apellido son obligatorios")
        if not str(self.documento).isdigit():
            raise ValueError("El documento debe ser numérico")
        if not str(self.telefono).isdigit():
            raise ValueError("El telefono debe ser numérico")
        if not self.correo or "@" not in self.correo:
            raise ValueError("Ingresa un correo válido")
        if not self.gen_id:
            raise ValueError("Selecciona un genero")
        if not self.estr_id:
            raise ValueError("Selecciona un estrato")

    def guardar(self):
        self.validar()
        conexio = conexion.conexion_db()
        try:
            cursor = conexio.cursor()
            cursor.execute(
                """INSERT INTO paciente
                   (pac_documento, pac_nombre, pac_apellido, pac_direccion,
                    pac_telefono, pac_correo, gen_id, estr_id)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                (int(self.documento), self.nombre, self.apellido, self.direccion,
                 int(self.telefono), self.correo, self.gen_id, self.estr_id)
            )
            pac_id = cursor.lastrowid

            for hob_id in self.hobbies_ids:
                cursor.execute(
                    "INSERT INTO paciente_hobbies (pac_id, hob_id) VALUES (%s, %s)",
                    (pac_id, hob_id)
                )

            conexio.commit()
            cursor.close()
            self.pac_id = pac_id
        except Exception:
            conexio.rollback()
            raise
        finally:
                conexio.close()
    def actualizar(self):
        self.validar()
        conexio = conexion.conexion_db()
        try:
            cursor = conexio.cursor()
            cursor.execute(
                """UPDATE paciente SET
                       pac_nombre = %s, pac_apellido = %s, pac_direccion = %s,
                    pac_telefono = %s, pac_correo = %s, gen_id = %s, estr_id = %s
                WHERE pac_id = %s""",
                (self.nombre, self.apellido, self.direccion,
                int(self.telefono), self.correo, self.gen_id, self.estr_id, self.pac_id)
            )

        # Reemplaza los hobbies: borra los anteriores y mete los nuevos seleccionados
            cursor.execute("DELETE FROM paciente_hobbies WHERE pac_id = %s", (self.pac_id,))
            for hob_id in self.hobbies_ids:
                cursor.execute(
                    "INSERT INTO paciente_hobbies (pac_id, hob_id) VALUES (%s, %s)",
                    (self.pac_id, hob_id)
                )

            conexio.commit()
            cursor.close()
        except Exception:
            conexio.rollback()
            raise
        finally:
            conexio.close()

    @classmethod
    def obtener_por_id(cls, pac_id):
        """Trae un paciente por su pac_id, para precargar el formulario de Crear Historia"""
        conexio = conexion.conexion_db()
        try:
            cursor = conexio.cursor()
            cursor.execute(
                """SELECT pac_id, pac_documento, pac_nombre, pac_apellido, pac_direccion,
                          pac_telefono, pac_correo, gen_id, estr_id
                   FROM paciente WHERE pac_id = %s""",
                (pac_id,)
            )
            fila = cursor.fetchone()

            if fila is None:
                cursor.close()
                return None

            cursor.execute("SELECT hob_id FROM paciente_hobbies WHERE pac_id = %s", (pac_id,))
            hobbies_ids = [h[0] for h in cursor.fetchall()]
            cursor.close()

            return cls(
                pac_id=fila[0],
                documento=fila[1],
                nombre=fila[2],
                apellido=fila[3],
                direccion=fila[4],
                telefono=fila[5],
                correo=fila[6],
                gen_id=fila[7],
                estr_id=fila[8],
                hobbies_ids=hobbies_ids
            )
        finally:
            conexio.close()

    @staticmethod
    def obtener_generos():
        return Paciente._listar("SELECT gen_id, gen_nombre FROM generos")

    @staticmethod
    def obtener_hobbies():
        return Paciente._listar("SELECT hob_id, hob_nombre FROM hobbies")

    @staticmethod
    def obtener_estratos():
        return Paciente._listar("SELECT estr_id, estr_nombre FROM estratos")

    @staticmethod
    def _listar(consulta):
        conexio = conexion.conexion_db()
        try:
            cursor = conexio.cursor()
            cursor.execute(consulta)
            filas = cursor.fetchall()
            cursor.close()
            return filas
        finally:
            conexio.close()

    @staticmethod
    def listar():
        """Devuelve (pac_id, documento, nombre completo, telefono, genero, estrato)."""
        return Paciente._listar("""
            SELECT p.pac_id, p.pac_documento,
                   CONCAT(p.pac_nombre, ' ', p.pac_apellido) AS nombre,
                   p.pac_telefono, g.gen_nombre, e.estr_nombre
            FROM paciente p
            JOIN generos g ON g.gen_id = p.gen_id
            JOIN estratos e ON e.estr_id = p.estr_id
            ORDER BY p.pac_apellido, p.pac_nombre
        """)

    @staticmethod
    def eliminar(pac_id):
        conexio = conexion.conexion_db()
        try:
            cursor = conexio.cursor()
            cursor.execute("DELETE FROM paciente WHERE pac_id = %s", (pac_id,))
            conexio.commit()
            cursor.close()
        finally:
            conexio.close()


from dataclasses import dataclass


@dataclass
class HistoriaClinica:
    pac_id: int
    hist_motiv: str
    hist_estod: str
    hist_cilod: str
    hist_ejeod: str
    hist_estoi: str
    hist_ciloi: str
    hist_ejeoi: str
    hist_diagod: str
    hist_diagoi: str
    hist_recom: str

    def guardar(self):
        try:
            conexio = conexion.conexion_db()
            cursor = conexio.cursor()

            consulta = """
                INSERT INTO historias
                (hist_motiv, hist_estod, hist_cilod, hist_ejeod,
                 hist_estoi, hist_ciloi, hist_ejeoi, hist_diagod, hist_diagoi, hist_recom, pac_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(consulta, (
                self.hist_motiv, self.hist_estod, self.hist_cilod, self.hist_ejeod,
                self.hist_estoi, self.hist_ciloi, self.hist_ejeoi,
                self.hist_diagod, self.hist_diagoi, self.hist_recom, self.pac_id
            ))

            conexio.commit()
            cursor.close()
            conexio.close()
            return True

        except Exception as error:
            print(f"Error al guardar historia clínica: {error}")
            return False

    @staticmethod
    def listar():
        """Devuelve (hist_id, nombre completo del paciente, motivo, recomendacion)."""
        conexio = conexion.conexion_db()
        try:
            cursor = conexio.cursor()
            cursor.execute("""
                SELECT h.hist_id, CONCAT(p.pac_nombre, ' ', p.pac_apellido) AS nombre,
                       h.hist_motiv, h.hist_recom
                FROM historias h
                JOIN paciente p ON p.pac_id = h.pac_id
                ORDER BY h.hist_id DESC
            """)
            filas = cursor.fetchall()
            cursor.close()
            return filas
        finally:
            conexio.close()

    @staticmethod
    def obtener_por_id(hist_id):
        """Trae todos los datos de una historia específica, para el detalle."""
        conexio = conexion.conexion_db()
        try:
            cursor = conexio.cursor()
            cursor.execute("""
                SELECT h.hist_id, CONCAT(p.pac_nombre, ' ', p.pac_apellido) AS nombre,
                       p.pac_documento, h.hist_motiv,
                       h.hist_estod, h.hist_cilod, h.hist_ejeod,
                       h.hist_estoi, h.hist_ciloi, h.hist_ejeoi,
                       h.hist_diagod, h.hist_diagoi, h.hist_recom
                FROM historias h
                JOIN paciente p ON p.pac_id = h.pac_id
                WHERE h.hist_id = %s
            """, (hist_id,))
            fila = cursor.fetchone()
            cursor.close()
            return fila
        finally:
            conexio.close()