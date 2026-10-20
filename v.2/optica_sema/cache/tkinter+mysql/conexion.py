import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import Read, Create, Delete, Update

def menu():
    ventana = tk.Tk()
    ventana.title("Login")
    ventana.geometry ("620x640")

    tk.Label(ventana,
             text='Bienvenido',
             font=('Bond', 16)).pack(pady=1, padx=1)
    tk.Label(ventana,
             text='Inicio Sesion',
             font=('Bond', 16)).pack(pady=3, padx=1)
    
    tk.Label(ventana,
             text='Ingrese por favor las credenciales',
             font=('Arial', 14)).pack(pady=10, padx=1)

    form = tk.Frame(ventana)
    form.pack(pady=20)
    

    form.grid_columnconfigure(0, weight=1)

    # El Label del Usuario (Fila 0 del contenedor)
    usuario = tk.Label(form, text='Usuario', font=("Arial", 12))
    usuario.grid(row=0, column=0, pady=(10, 2))
    
    usuario = tk.Entry(form, font=("Arial", 12), width=30)
    usuario.grid(row=1, column=0, pady=(0, 10))

    contraseña= tk.Label(form, text='Contraseña', font=("Arial", 12))
    contraseña.grid(row=2, column=0, pady=(10, 2))
     
    contraseña = tk.Entry(form, font=("Arial", 12), width=30)
    contraseña.grid(row=3, column=0, pady=(0, 10))

    tk.Button(ventana,
              text='Ingresar',
              command= lambda: val(usuario, contraseña, ventana)).pack(pady=30, padx=1)


    ventana.mainloop()

def val(usuario, contraseña, ventana):

    user = 'admin'
    password = '1234'

    u = usuario.get()
    p = contraseña.get()

    flag = False

    if u == user and p == password:
        flag = True

    if not flag:
        messagebox.showinfo("Login", "Credenciales incorrectas.")
    else:
        messagebox.showinfo("Login", "Acceso concedido")
        ventana.destroy()
        main()

def actualizar(tabla):

    for i in tabla.get_children():
        tabla.delete(i)
    
    datos = Read.Read_users(conexion)

    for c in datos:
        tabla.insert("", tk.END, values=c)

def insert(nombre, apellido, edad):
    nom = nombre.get()
    ape = apellido.get()
    ed = edad.get()
    Create.Create_user(conexion, nom, ape, ed)

def act(tabla):
    sel = tabla.selection()

    if not sel:
        messagebox.showwarning("Editar", "Por favor, selecciona un usuario")
        return

    valor = tabla.item(sel)['values']
    id_us = valor[0]
    nombre_u = valor[1]

    confirmar = messagebox.askyesno("Confirmar", f"Estas seguro que deseas editar a {nombre_u}")

    if confirmar:
        Update.Update_user(conexion, id_us)
        actualizar()
        # PENDIENTE CRAER LA VENTANA DE LA EDICION!
        messagebox.showinfo("Exito", "Usuario elimi correctamente.")


def elim(tabla):
    sel = tabla.selection()

    if not sel:
        messagebox.showwarning("Eliminar", "Por favor, selecciona un usuario")
        return

    valor = tabla.item(sel)['values']
    id_us = valor[0]
    nombre_u = valor[1]

    confirmar = messagebox.askyesno("Confirmar", f"Estas seguro que deseas eliminar a {nombre_u}")

    if confirmar:
        Delete.Delete_user(conexion, id_us)

        messagebox.showinfo("Exito", "Usuario eliminado correctamente.")
        actualizar(tabla)
        
def main():
    menuu = tk.Tk()
    menuu.title('Menu principal')
    menuu.geometry("720x640")

    tk.Label(menuu,
             text='Lista de usuarios',
             font=('Bond', 16)).pack(pady=10, padx=1)
    
    
    columnas = ("id", "nombre", "apellido", "edad")
    tabla = ttk.Treeview(menuu, columns=columnas, show="headings")

    tabla.heading("id", text="ID")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("apellido", text="Apellido")
    tabla.heading("edad", text="Edad")

    tabla.column("id", width=50)
    tabla.column("nombre", width=150)
    tabla.column("apellido", width=150)
    tabla.column("edad", width=100)

    #resolver carga de datos del crud
    actualizar(tabla)
    tabla.pack(pady=15, fill=tk.BOTH, expand=True)

    tk.Button(menuu,
              text='Registrar usuario',
              command=lambda: [menuu.destroy(), registro()]).pack(pady=20, padx=10)
    
    boton_elim = tk.Button(menuu,
                           text='Eliminar',
                           command=lambda: elim(tabla), fg="white", bg="red")
    boton_elim.pack(pady=10)

    boton_update = tk.Button(menuu,
                           text='Editar',
                           command=lambda: elim(tabla), fg="black", bg="yellow")
    boton_update.pack(pady=10)

def registro():
    regist = tk.Tk()
    regist.title("Registro usuarios")
    regist.geometry("620x680")
    
    tk.Label(regist,
             text='Registro usuario',
             font=("Bond", 16)).pack(pady=10, padx=1)
    
    formulario = tk.Frame(regist)
    formulario.pack(pady=20)

    formulario.grid_columnconfigure(0, weight=1)

    # El Label del Usuario (Fila 0 del contenedor)
    nombre = tk.Label(formulario, text='Nombre', font=("Arial", 12))
    nombre.grid(row=0, column=0, pady=(10, 2))
    
    nombre = tk.Entry(formulario, font=("Arial", 12), width=30)
    nombre.grid(row=1, column=0, pady=(0, 10))

    apellido= tk.Label(formulario, text='Apellido', font=("Arial", 12))
    apellido.grid(row=2, column=0, pady=(10, 2))
     
    apellido = tk.Entry(formulario, font=("Arial", 12), width=30)
    apellido.grid(row=3, column=0, pady=(0, 10))

    edad= tk.Label(formulario, text='Edad', font=("Arial", 12))
    edad.grid(row=4, column=0, pady=(10, 2))
     
    edad = tk.Entry(formulario, font=("Arial", 12), width=30)
    edad.grid(row=5, column=0, pady=(0, 10))

    tk.Button(regist,
              text='Registrar',
              command=lambda: [insert(nombre, apellido, edad), regist.destroy(), main()]).pack(pady=10, padx=1)
try: 
    conexion = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'db_python'
    )

    if conexion.is_connected():
        print("Ejecutando DB y Aplicacion...")
        menu()
        cursor = conexion.cursor()
        print("conectado")

except mysql.connector.Error:
    print("Error al conectar con la base de datos.")
    print("Aplicacion no iniciada.")