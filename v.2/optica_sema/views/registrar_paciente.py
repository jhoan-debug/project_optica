import tkinter as t
from tkinter import ttk, messagebox
from models.paciente import Paciente

NARANJA = "#FF8C00"
def registrar_paciente(al_terminar=None):

    ventana = t.Toplevel()
    ventana.title("Registro de Paciente")
    ventana.geometry("950x600")
    ventana.resizable(False, False)

    for columna in range(3):
        ventana.columnconfigure(columna, weight=1)

    header = t.Frame(ventana, bg=NARANJA, height=80)
    header.grid(row=0, column=0, columnspan=3, sticky="ew")
    header.grid_propagate(False)

    lbl_titulo = t.Label(header, text="Registro de Paciente", bg=NARANJA, fg="white", font=("Arial", 16, "bold"))
    lbl_titulo.pack(expand=True)

    t.Label(ventana, text="Documento", font=("Arial", 11, "bold")
    ).grid(row=1, column=0, sticky="w", padx=15, pady=(15, 5))

    t.Label(ventana, text="Nombre", font=("Arial", 11, "bold")
    ).grid(row=1, column=1, sticky="w", padx=15, pady=(15, 5))

    t.Label(ventana, text="Apellido", font=("Arial", 11, "bold")
    ).grid(row=1, column=2, sticky="w", padx=15, pady=(15, 5))

    txt_documento = t.Entry(ventana)
    txt_documento.grid(row=2, column=0, padx=15, pady=5, sticky="ew")

    txt_nombre = t.Entry(ventana)
    txt_nombre.grid(row=2, column=1, padx=15, pady=5, sticky="ew")

    txt_apellido = t.Entry(ventana)
    txt_apellido.grid(row=2, column=2, padx=15, pady=5, sticky="ew")

    t.Label(ventana, text="Dirección", font=("Arial", 11, "bold")
    ).grid(row=3, column=0, sticky="w", padx=15, pady=(10, 5))

    t.Label(ventana, text="Teléfono", font=("Arial", 11, "bold")
    ).grid(row=3, column=1, sticky="w", padx=15, pady=(10, 5))

    t.Label(ventana, text="Correo", font=("Arial", 11, "bold")
    ).grid(row=3, column=2, sticky="w", padx=15, pady=(10, 5))

    txt_direccion = t.Entry(ventana)
    txt_direccion.grid(row=4, column=0, padx=15, pady=5, sticky="ew")

    txt_telefono = t.Entry(ventana)
    txt_telefono.grid(row=4, column=1, padx=15, pady=5, sticky="ew")

    txt_correo = t.Entry(ventana)
    txt_correo.grid(row=4, column=2, padx=15, pady=5, sticky="ew")

    t.Label(ventana, text="Hobbies", font=("Arial", 11, "bold")
    ).grid(row=5, column=0, sticky="w", padx=15, pady=(15, 5))

    t.Label(ventana, text="Género", font=("Arial", 11, "bold")
    ).grid(row=5, column=1, sticky="w", padx=15, pady=(15, 5))

    t.Label(ventana, text="Estrato", font=("Arial", 11, "bold")
    ).grid(row=5, column=2, sticky="w", padx=15, pady=(15, 5))

    frame_hobbies = t.Frame(ventana)
    frame_hobbies.grid(row=6, column=0, sticky="nw", padx=15)

    vars_hobbies = {}

    try:
        hobbies = Paciente.obtener_hobbies()

        for hob_id, hob_nombre in hobbies:
            var = t.BooleanVar(value=False)

            t.Checkbutton(frame_hobbies, text=hob_nombre, variable=var
            ).pack(anchor="w")

            vars_hobbies[hob_id] = var

    except Exception as error:
        messagebox.showerror("Error",f"No se pudieron cargar los hobbies:\n{error}")

    mapa_generos = {
        nombre: id_
        for id_, nombre in Paciente.obtener_generos()
    }

    cbx_genero = ttk.Combobox(
        ventana,
        values=list(mapa_generos.keys()),
        state="readonly",
        width=25
    )

    cbx_genero.set("-- Seleccione una opción --")
    cbx_genero.grid(row=6, column=1, sticky="nw", padx=15)

    frame_estrato = t.Frame(ventana)
    frame_estrato.grid(row=6, column=2, sticky="nw", padx=15)

    var_estrato = t.IntVar(value=0)

    for estr_id, estr_nombre in Paciente.obtener_estratos():
        t.Radiobutton(
            frame_estrato,
            text=estr_nombre,
            variable=var_estrato,
            value=estr_id
        ).pack(anchor="w")

    def guardar_paciente():

        documento = txt_documento.get().strip()
        nombre = txt_nombre.get().strip()
        apellido = txt_apellido.get().strip()
        direccion = txt_direccion.get().strip()
        telefono = txt_telefono.get().strip()
        correo = txt_correo.get().strip()

        if not documento:
            messagebox.showwarning("Aviso","Debe ingresar el documento.")
            txt_documento.focus()
            return

        if not nombre:
            messagebox.showwarning("Aviso","Debe ingresar el nombre.")
            txt_nombre.focus()
            return

        if not apellido:
            messagebox.showwarning("Aviso","Debe ingresar el apellido.")
            txt_apellido.focus()
            return

        if cbx_genero.get() not in mapa_generos:
            messagebox.showwarning("Aviso","Debe seleccionar un género.")
            cbx_genero.focus()
            return

        if var_estrato.get() == 0:
            messagebox.showwarning("Aviso","Debe seleccionar un estrato.")
            return

        hobbies_seleccionados = [
            hob_id
            for hob_id, var in vars_hobbies.items()
            if var.get()
        ]

        paciente = Paciente(
            documento=documento,
            nombre=nombre,
            apellido=apellido,
            direccion=direccion,
            telefono=telefono,
            correo=correo,
            gen_id=mapa_generos[cbx_genero.get()],
            estr_id=var_estrato.get(),
            hobbies_ids=hobbies_seleccionados
        )

        try:
            paciente.guardar()
            messagebox.showinfo("Registro exitoso","Paciente registrado exitosamente.")
            if al_terminar:
                al_terminar()
            ventana.destroy()

        except ValueError as error:
            messagebox.showwarning("Aviso",str(error))

        except Exception as error:
            messagebox.showerror("Error",f"No se pudo registrar el paciente:\n{error}")

    btn_registrar = t.Button(ventana, text="Registrar Paciente",
                             command=guardar_paciente,bg=NARANJA,fg="white",font=("Arial", 12, "bold"),width=20,height=2
    )
    btn_registrar.grid(row=7,column=0,columnspan=3,pady=25)
    txt_documento.focus()