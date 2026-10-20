import tkinter as t
from tkinter import ttk, messagebox
import controllers.auth_login as auth_login
from config import conexion

NARANJA = "#FF8C00"
GRIS_OSCURO = "#333333"

def login():
    resultado = {"exito": False, "nombre": None, "rol_id": None, "rol_nombre": None}

    mapa_roles = {
        "Administrador": 1,
        "Optometra": 2
    }

    def llamada_login():
        if not conexion.conexion_db():
            messagebox.showerror("Aviso", "DB no conectada")

    def ejecutar_login():
        docu = txt_documento.get().strip()
        contr = txt_contraseña.get().strip()
        rol_texto = txt_rol.get()
        rol = mapa_roles.get(rol_texto)

        if not docu or not contr:
            messagebox.showwarning("Aviso", "Ingresa documento y contraseña")
            return

        if rol is None:
            messagebox.showwarning("Aviso", "Selecciona un rol válido")
            return

        verificar = auth_login.validar_login(docu, contr, rol)

        if verificar:
            nombre = auth_login.bienvenida(docu)
            messagebox.showinfo("Aviso", f"Bienvenido a la optica Sr(a). {nombre}")
            resultado["exito"] = True
            resultado["nombre"] = nombre
            resultado["rol_id"] = rol
            resultado["rol_nombre"] = rol_texto
            ventanaLogin.destroy()
        else:
            messagebox.showerror("Error", "Credenciales de acceso incorrectas. Intente nuevamente")

    ventanaLogin = t.Tk()
    ventanaLogin.title("Login - Optica Sena")
    ventanaLogin.geometry("1080x720")
    ventanaLogin.resizable(False, False)
    ventanaLogin.configure(bg="#F2F2F2")

    # header naranja
    header = t.Frame(ventanaLogin, bg=NARANJA, height=90)
    header.pack(fill="x")
    header.pack_propagate(False)

    t.Label(header, text="Optica Sena", bg=NARANJA, fg="white",
            font=("Arial", 20, "bold")).pack(expand=True)

    # form
    formulario = t.Frame(ventanaLogin, bg="white", bd=1, relief="solid")
    formulario.place(relx=0.5, rely=0.55, anchor="center", width=360, height=380)

    t.Label(formulario, text="Inicio de sesión", bg="white", fg=GRIS_OSCURO,
            font=("Arial", 15, "bold")).pack(pady=(25, 20))

    t.Label(formulario, text="Documento", bg="white", fg=GRIS_OSCURO,
            font=("Arial", 10, "bold")).pack(anchor="w", padx=40)
    txt_documento = t.Entry(formulario, font=("Arial", 11))
    txt_documento.pack(fill="x", padx=40, pady=(2, 15))

    t.Label(formulario, text="Contraseña", bg="white", fg=GRIS_OSCURO,
            font=("Arial", 10, "bold")).pack(anchor="w", padx=40)
    txt_contraseña = t.Entry(formulario, show="*", font=("Arial", 11))
    txt_contraseña.pack(fill="x", padx=40, pady=(2, 15))

    t.Label(formulario, text="Rol", bg="white", fg=GRIS_OSCURO,
            font=("Arial", 10, "bold")).pack(anchor="w", padx=40)
    txt_rol = ttk.Combobox(formulario, values=["Seleccione un rol", "Administrador", "Optometra"], state="readonly", font=("Arial", 10))
    txt_rol.set("Seleccione un rol")
    txt_rol.pack(fill="x", padx=40, pady=(2, 25))

    Btn_enviar = t.Button(
        formulario, text="Ingresar", command=ejecutar_login,
        bg=NARANJA, fg="white", font=("Arial", 11, "bold"),
        relief="flat", cursor="hand2", height=1
    )
    Btn_enviar.pack(fill="x", padx=40, ipady=6)

    llamada_login()
    ventanaLogin.mainloop()

    return resultado