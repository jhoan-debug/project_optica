import tkinter as t
from tkinter import ttk
from views.listado_clientes import crear_listado
from views.registrar_paciente import registrar_paciente
from views.Visualizar_historias import ver_historias

naranja  = "#FF8C00"
gris = "#333333"
fondo = "#F2F2F2"


def abrir_menu(nombre, rol="Optometra"):
    ventana = t.Tk()
    ventana.title("Menu Principal - Optica Sena")
    ventana.geometry("1080x720")
    ventana.configure(bg=fondo)

    header = t.Frame(ventana, bg=naranja, height=90)
    header.pack(fill="x")
    header.pack_propagate(False)

    t.Label(header, text="Bienvenidos a la Optica Sena", bg=naranja, fg="white",
            font=("Arial", 18, "bold")).pack(side="left", padx=30)

    frame_usuario = t.Frame(header, bg=naranja)
    frame_usuario.pack(side="right", padx=30)

    t.Label(frame_usuario, text=f"Usuario: {nombre} | Rol {rol}", bg=naranja, fg="white",
            font=("Arial", 11, "bold")).pack(anchor="e")

    t.Button(frame_usuario, text="Cerrar sesión", bg="white", fg=naranja,
             font=("Arial", 9, "bold"), relief="flat", cursor="hand2",
             command=ventana.destroy).pack(anchor="e", pady=(5, 0))

    barra = t.Frame(ventana, bg=fondo)
    barra.pack(fill="x", padx=20, pady=10)

    t.Label(barra, text="¿Qué deseas hacer?", bg=fondo, fg=gris,
            font=("Arial", 11, "bold")).pack(side="left", padx=(0, 10))

    opciones_menu = ["Registrar paciente", "Ver historias clinicas"]
    sel_menu = ttk.Combobox(barra, values=opciones_menu, state="readonly",
                            font=("Arial", 10), width=25)
    sel_menu.set("---")
    sel_menu.pack(side="left")

    contenido = t.Frame(ventana, bg=fondo)
    contenido.pack(fill="both", expand=True, padx=20, pady=(0, 15))

    recargar_lista = crear_listado(contenido)

    def desplegable(_):
        seleccion = sel_menu.get()
        if seleccion == "Registrar paciente":
            registrar_paciente(al_terminar=recargar_lista)
        elif seleccion == "Ver historias clinicas":
            ver_historias()

        sel_menu.set("---")

    sel_menu.bind("<<ComboboxSelected>>", desplegable)

    ventana.mainloop()