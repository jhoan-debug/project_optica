import tkinter as tk

lista_usuarios = []

def menu():
    ventana = tk.Tk()
    ventana.title("Personas JSON")
    ventana.geometry("500x550")
    
    tk.Label(ventana, text="Menu", font=("Arial", 16)).pack(pady=20)
    
    tk.Button(ventana, text="Registrar persona json",
              command=lambda:registro.crear_usuario()).pack(pady=20)
    
    tk.Button(ventana, text="Listar clientes",
              command=lambda:listar.listado()).pack(pady=20)
    
    tk.Button(ventana, text="cerrar", 
              command= ventana.destroy).pack(pady=20)
    ventana.mainloop()
menu()