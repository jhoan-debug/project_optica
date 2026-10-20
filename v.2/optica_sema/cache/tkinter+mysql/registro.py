import tkinter as tk
from tkinter import messagebox
import json
import listar
lista_usuarios = []
"""(ventana2, text="Nombre:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")"""
def enviar_datos(e_nombre, e_edad, e_ciudad):
    id = 0
    usuarios = {
        "id": id,
        "nombre": "",
        "edad": "",
        "ciudad": ""
    }
    id =+ 1
    nombre = e_nombre.get()
    edad = e_edad.get()
    ciudad = e_ciudad.get()
    
    if not nombre and edad and ciudad:
        messagebox.showerror("Error", "debes rellenar los siguientes espacios: nombre, edad, ciudad")
    elif not edad and ciudad:
        messagebox.showerror("Error", "Debes rellenar los siguientes espacios: edad, ciudad")
    elif not nombre and ciudad:
        messagebox.showerror("Error", "Debes rellenar los siguientes datos: nombre, ciudad")
    elif not nombre and edad:
        messagebox.showerror("Error", "Debes rellenar los siguientes datos: nombre, edad")
    else:
        usuarios = {
            "id": id,
            "nombre": nombre,
            "edad": edad,
            "ciudad": ciudad
        }
        lista_usuarios.append(usuarios.copy())
        
        with open("datos.json", "r") as archivos:
            carga_archivo = json.load(archivos)
            
        carga_archivo.append(lista_usuarios)
        
        with open("datos.json", "w") as archivos:
            json.dump(lista_usuarios, archivos, indent= 4)
            print("REgistro existoso!")
        messagebox.showinfo("", "registro enviado existosamente!")
def crear_usuario():
    ventana2 = tk.Toplevel()
    ventana2.title("registro JSON")
    ventana2.geometry("400x300")
    # 1. CREAMOS UN FRAME
    # Este será el ÚNICO que use 'pack' en la ventana2
    contenedor_principal = tk.Frame(ventana2)
    contenedor_principal.pack(expand=True, fill="both")

    # 2. TODO LO DEMÁS USA 'GRID'
    # Pero cuidado: el padre de estos widgets debe ser 'contenedor_principal'
    
    # Título
    tk.Label(contenedor_principal, text="Registro", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=15)
    
    # Nombre
    tk.Label(contenedor_principal, text="Nombre:").grid(row=1, column=0, sticky="e", padx=5, pady=20)
    e_nombre = tk.Entry(contenedor_principal)
    e_nombre.grid(row=1, column=1, sticky="w", padx=5, pady=20)
    
    tk.Label(contenedor_principal, text="Edad:").grid(row=2, column=0, sticky="e", padx=5, pady=20)
    e_edad = tk.Entry(contenedor_principal)
    e_edad.grid(row=2, column=1, sticky="w", padx=5, pady=20)
    
    tk.Label(contenedor_principal, text="Ciudad:").grid(row=3, column=0, sticky="e", padx=5, pady=20)
    e_ciudad = tk.Entry(contenedor_principal)
    e_ciudad.grid(row=3, column=1, sticky="w", padx=5, pady=20)
    
    tk.Button(contenedor_principal, text="Enviar",
              command=lambda: [enviar_datos(e_nombre, e_edad, e_ciudad), ventana2.destroy]).grid(row=4, column=1, columnspan=2, padx=10, pady=10)
    tk.Button(contenedor_principal, text="Volver", 
              command=ventana2.destroy).grid(row=4, column=3, columnspan=2, padx=10, pady=10)
    
