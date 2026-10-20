import tkinter as t
from tkinter import ttk, messagebox
from models.paciente import Paciente, HistoriaClinica

NARANJA = "#FF8C00"
ENCABEZADOS = ["DOCUMENTO", "NOMBRE PACIENTE", "TELEFONO", "GENERO", "ESTRATO", "ACCIONES"]


def crear_historia(pac_id):
    paciente = Paciente.obtener_por_id(pac_id)
    generos = Paciente.obtener_generos()
    estratos = Paciente.obtener_estratos()

    ventana = t.Toplevel()
    ventana.title("")
    ventana.geometry("950x650")
    ventana.resizable(False, False)

    header = t.Frame(ventana, bg=NARANJA, height=60)
    header.pack(fill=t.X)

    lbl_titulo = t.Label(header, text="Registro de historia", bg=NARANJA, fg="white", font=("Arial", 16, "bold"))
    lbl_titulo.pack(expand=True)

    form = t.Frame(ventana)
    form.place(relx=0.5, rely=0.12, anchor="n")

    t.Label(form, text="Documento", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=1, column=0, sticky="ew", padx=15, pady=(15, 5))

    t.Label(form, text="Nombre", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=1, column=1, sticky="ew", padx=15, pady=(15, 5))

    t.Label(form, text="Apellido", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=1, column=2, sticky="ew", padx=15, pady=(15, 5))

    txt_documento = t.Label(form, text=paciente.documento, font=("Arial", 10))
    txt_documento.grid(row=2, column=0, padx=15, pady=5, sticky="ew")

    txt_nombre = t.Label(form, text=paciente.nombre, font=("Arial", 10))
    txt_nombre.grid(row=2, column=1, padx=15, pady=5, sticky="ew")

    txt_apellido = t.Label(form, text=paciente.apellido, font=("Arial", 10))
    txt_apellido.grid(row=2, column=2, padx=15, pady=5, sticky="ew")

    t.Label(form, text="Telefono", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=3, column=0, sticky="ew", padx=15, pady=(10, 5))

    t.Label(form, text="Genero", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=3, column=1, sticky="ew", padx=15, pady=(10, 5))

    t.Label(form, text="Estrato", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=3, column=2, sticky="ew", padx=15, pady=(10, 5))

    nombre_genero = next(nombre for id_, nombre in generos if id_ == paciente.gen_id)
    txt_genero = t.Label(form, text=nombre_genero, font=("Arial", 10))
    txt_genero.grid(row=4, column=0, padx=15, pady=5, sticky="ew")

    txt_telefono = t.Label(form, text=paciente.telefono, font=("Arial", 10))
    txt_telefono.grid(row=4, column=1, padx=15, pady=5, sticky="ew")

    nombre_estrato = next(nombre for id_, nombre in estratos if id_ == paciente.estr_id)
    txt_estrato = t.Label(form, text=nombre_estrato, font=("Arial", 10))
    txt_estrato.grid(row=4, column=2, padx=15, pady=5, sticky="ew")

    t.Label(form, text="Motivo de visita", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=5, column=0, sticky="ew", padx=15, pady=(15, 5))

    txt_motivo_vista = t.Entry(form, width=70)
    txt_motivo_vista.grid(row=6, column=0, columnspan=3, sticky="ew", padx=15, pady=5)

    t.Label(form, text="Esfera OD", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=7, column=0, sticky="ew", padx=15, pady=(15, 5))

    t.Label(form, text="cilindro OD", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=7, column=1, sticky="ew", padx=15, pady=(15, 5))

    t.Label(form, text="Eje OD", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=7, column=2, sticky="ew", padx=15, pady=(15, 5))

    txt_esferaOD = t.Entry(form)
    txt_esferaOD.grid(row=8, column=0, padx=15, pady=5, sticky="ew")

    txt_cilindroOD = t.Entry(form)
    txt_cilindroOD.grid(row=8, column=1, padx=15, pady=5, sticky="ew")

    txt_ejeOD = t.Entry(form)
    txt_ejeOD.grid(row=8, column=2, padx=15, pady=5, sticky="ew")

    t.Label(form, text="Esfera OI", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=9, column=0, sticky="ew", padx=15, pady=(15, 5))

    t.Label(form, text="cilindro OI", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=9, column=1, sticky="ew", padx=15, pady=(15, 5))

    t.Label(form, text="Eje OI", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=9, column=2, sticky="ew", padx=15, pady=(15, 5))

    txt_esferaOI = t.Entry(form)
    txt_esferaOI.grid(row=10, column=0, padx=15, pady=5, sticky="ew")

    txt_cilindroOI = t.Entry(form)
    txt_cilindroOI.grid(row=10, column=1, padx=15, pady=5, sticky="ew")

    txt_ejeOI = t.Entry(form)
    txt_ejeOI.grid(row=10, column=2, padx=15, pady=5, sticky="ew")

    t.Label(form, text="Diagnostico Ojo Derecho", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=11, column=0, sticky="ew", padx=15, pady=(15, 5))

    t.Label(form, text="Diagnostico Ojo Izquierdo", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=11, column=2, sticky="ew", padx=15, pady=(15, 5))

    txt_DiagnosticoOD = t.Entry(form)
    txt_DiagnosticoOD.grid(row=12, column=0, padx=15, pady=5, sticky="ew")

    txt_DiagnosticoOI = t.Entry(form)
    txt_DiagnosticoOI.grid(row=12, column=2, padx=15, pady=5, sticky="ew")

    t.Label(form, text="Recomendacion", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=13, column=0, sticky="ew", padx=15, pady=(15, 5))

    txt_recomendacion = t.Entry(form, width=70)
    txt_recomendacion.grid(row=14, column=0, columnspan=3, sticky="ew", padx=15, pady=5)

    def guardar_historia():
        motivo_visita = txt_motivo_vista.get().strip()
        esferaOD = txt_esferaOD.get().strip()
        cilindroOD = txt_cilindroOD.get().strip()
        ejeOD = txt_ejeOD.get().strip()
        esferaOI = txt_esferaOI.get().strip()
        cilindroOI = txt_cilindroOI.get().strip()
        ejeOI = txt_ejeOI.get().strip()
        diagnosticoOD = txt_DiagnosticoOD.get().strip()
        diagnosticoOI = txt_DiagnosticoOI.get().strip()
        recomendacion = txt_recomendacion.get().strip()

        if not esferaOD or not cilindroOD or not ejeOD or not esferaOI or not cilindroOI or not ejeOI or not diagnosticoOD or not diagnosticoOI:
            messagebox.showwarning("Aviso", "Completa todos los campos de la fórmula y el diagnóstico")
            return

        historia = HistoriaClinica(
            pac_id=pac_id,
            hist_motiv=motivo_visita,
            hist_estod=esferaOD,
            hist_cilod=cilindroOD,
            hist_ejeod=ejeOD,
            hist_estoi=esferaOI,
            hist_ciloi=cilindroOI,
            hist_ejeoi=ejeOI,
            hist_diagod=diagnosticoOD,
            hist_diagoi=diagnosticoOI,
            hist_recom=recomendacion
        )

        if historia.guardar():
            messagebox.showinfo("Aviso", "Historia clínica registrada exitosamente")
            ventana.destroy()
        else:
            messagebox.showerror("Error", "No se pudo guardar la historia clínica")

    btnEnviar = t.Button(form, text="Guardar", bg="#000000", fg="white",
                         command=lambda: guardar_historia())
    btnEnviar.grid(row=15, column=0, columnspan=3, pady=20)


def editar(pac_id, al_terminar=None):
    paciente = Paciente.obtener_por_id(pac_id)
    generos = Paciente.obtener_generos()
    estratos = Paciente.obtener_estratos()
    hobbies = Paciente.obtener_hobbies()

    if paciente is None:
        messagebox.showerror("Error", "No se encontró el paciente")
        return

    mapa_generos = {nombre: id_ for id_, nombre in generos}
    mapa_estratos = {nombre: id_ for id_, nombre in estratos}

    nombre_genero_actual = next(nombre for id_, nombre in generos if id_ == paciente.gen_id)
    nombre_estrato_actual = next(nombre for id_, nombre in estratos if id_ == paciente.estr_id)

    ventana = t.Toplevel()
    ventana.title("")
    ventana.geometry("700x650")
    ventana.resizable(False, False)

    header = t.Frame(ventana, bg=NARANJA, height=60)
    header.pack(fill="x")

    lbl_titulo = t.Label(header, text="Editar Paciente", bg=NARANJA, fg="white", font=("Arial", 16, "bold"))
    lbl_titulo.pack(expand=True)

    form = t.Frame(ventana)
    form.place(relx=0.5, rely=0.12, anchor="n")

    t.Label(form, text="Documento", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=1, column=0, sticky="ew", padx=15, pady=(15, 5))

    t.Label(form, text="Nombre", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=1, column=1, sticky="ew", padx=15, pady=(15, 5))

    t.Label(form, text="Apellido", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=1, column=2, sticky="ew", padx=15, pady=(15, 5))

    lbl_documento = t.Label(form, text=paciente.documento, font=("Arial", 10))
    lbl_documento.grid(row=2, column=0, padx=15, pady=5, sticky="ew")

    txt_nombre = t.Entry(form)
    txt_nombre.insert(0, paciente.nombre)
    txt_nombre.grid(row=2, column=1, padx=15, pady=5, sticky="ew")

    txt_apellido = t.Entry(form)
    txt_apellido.insert(0, paciente.apellido)
    txt_apellido.grid(row=2, column=2, padx=15, pady=5, sticky="ew")

    t.Label(form, text="Direccion", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=3, column=0, sticky="ew", padx=15, pady=(10, 5))

    t.Label(form, text="Telefono", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=3, column=1, sticky="ew", padx=15, pady=(10, 5))

    t.Label(form, text="Correo", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=3, column=2, sticky="ew", padx=15, pady=(10, 5))

    txt_direccion = t.Entry(form)
    txt_direccion.insert(0, paciente.direccion)
    txt_direccion.grid(row=4, column=0, padx=15, pady=5, sticky="ew")

    txt_telefono = t.Entry(form)
    txt_telefono.insert(0, paciente.telefono)
    txt_telefono.grid(row=4, column=1, padx=15, pady=5, sticky="ew")

    txt_correo = t.Entry(form)
    txt_correo.insert(0, paciente.correo)
    txt_correo.grid(row=4, column=2, padx=15, pady=5, sticky="ew")

    t.Label(form, text="Hobbies", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=5, column=0, sticky="ew", padx=15, pady=(15, 5))

    t.Label(form, text="Genero", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=5, column=1, sticky="ew", padx=15, pady=(15, 5))

    t.Label(form, text="Estrato", font=("Arial", 11, "bold"), anchor="center"
    ).grid(row=5, column=2, sticky="ew", padx=15, pady=(15, 5))

    frame_hobbies = t.Frame(form)
    frame_hobbies.grid(row=6, column=0, sticky="nw", padx=15)
    vars_hobbies = {}
    for hob_id, hob_nombre in hobbies:
        var = t.BooleanVar(value=(hob_id in paciente.hobbies_ids))
        t.Checkbutton(frame_hobbies, text=hob_nombre, variable=var).pack(anchor="w")
        vars_hobbies[hob_id] = var

    cbx_genero = ttk.Combobox(form, values=[nombre for _, nombre in generos], state="readonly")
    cbx_genero.set(nombre_genero_actual)
    cbx_genero.grid(row=6, column=1, sticky="nw", padx=15)

    frame_estrato = t.Frame(form)
    frame_estrato.grid(row=6, column=2, sticky="nw", padx=15)
    var_estrato = t.StringVar(value=nombre_estrato_actual)
    for estr_id, estr_nombre in estratos:
        t.Radiobutton(frame_estrato, text=estr_nombre, variable=var_estrato, value=estr_nombre).pack(anchor="w")

    def guardar_cambios():
        hobbies_seleccionados = [hob_id for hob_id, var in vars_hobbies.items() if var.get()]

        paciente.nombre = txt_nombre.get()
        paciente.apellido = txt_apellido.get()
        paciente.direccion = txt_direccion.get()
        paciente.telefono = txt_telefono.get()
        paciente.correo = txt_correo.get()
        paciente.gen_id = mapa_generos[cbx_genero.get()]
        paciente.estr_id = mapa_estratos[var_estrato.get()]
        paciente.hobbies_ids = hobbies_seleccionados

        try:
            paciente.actualizar()
            messagebox.showinfo("Aviso", "Paciente actualizado exitosamente")
            ventana.destroy()
            if al_terminar:
                al_terminar()
        except ValueError as error:
            messagebox.showwarning("Aviso", str(error))
        except Exception as error:
            messagebox.showerror("Error", f"No se pudo actualizar: {error}")

    btn_guardar = t.Button(
        form, text="Guardar Cambios", command=guardar_cambios,
        bg="#FFC107", fg="black", font=("Arial", 12, "bold"), width=20, height=2
    )
    btn_guardar.grid(row=7, column=0, columnspan=3, pady=25)


def crear_listado(contenedor):
    """Dibuja la tabla de pacientes dentro de 'contenedor' y devuelve
    la función para recargarla."""
    canvas = t.Canvas(contenedor, highlightthickness=0)
    scroll = ttk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scroll.set)
    scroll.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    tabla = t.Frame(canvas)
    id_tabla = canvas.create_window((0, 0), window=tabla, anchor="nw")

    tabla.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda e: canvas.itemconfigure(id_tabla, width=e.width))

    def _rueda(event):
        canvas.yview_scroll(int(-event.delta / 120), "units")
    canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _rueda))
    canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

    for col in range(6):
        tabla.grid_columnconfigure(col, weight=1)

    def eliminar(pac_id):
        if not messagebox.askyesno("Confirmar", "¿Seguro que quieres eliminar este paciente?"):
            return
        try:
            Paciente.eliminar(pac_id)
            messagebox.showinfo("Aviso", "Paciente eliminado exitosamente")
            cargar_tabla()
        except Exception as error:
            messagebox.showerror("Error", f"No se pudo eliminar el paciente: {error}")

    def cargar_tabla():
        for widget in tabla.winfo_children():
            widget.destroy()

        for col, texto in enumerate(ENCABEZADOS):
            t.Label(tabla, text=texto, font=("Arial", 10, "bold"), bg="#E4E4E4",
                    anchor="w", padx=8, pady=8).grid(row=0, column=col, sticky="ew")

        try:
            pacientes = Paciente.listar()
        except Exception as error:
            messagebox.showerror("Error", f"No se pudo cargar la lista: {error}")
            return

        if not pacientes:
            t.Label(tabla, text="No hay pacientes registrados", pady=20).grid(
                row=1, column=0, columnspan=6)
            return

        for fila, (pac_id, documento, nombre, telefono, genero, estrato) in enumerate(pacientes, start=1):
            fondo = "#FFFFFF" if fila % 2 else "#F6F6F6"

            for col, valor in enumerate((documento, nombre, telefono, genero, estrato)):
                t.Label(tabla, text=valor, bg=fondo, anchor="w",
                        padx=8, pady=8).grid(row=fila, column=col, sticky="nsew")

            acciones = t.Frame(tabla, bg=fondo)
            acciones.grid(row=fila, column=5, sticky="nsew")

            t.Button(acciones, text="Crear Historia", bg="#17A2B8", fg="white",
                     command=lambda pid=pac_id: crear_historia(pid)).pack(side="left", padx=3, pady=4)
            t.Button(acciones, text="Editar", bg="#FFC107",
                     command=lambda pid=pac_id: editar(pid, al_terminar=cargar_tabla)).pack(side="left", padx=3, pady=4)
            t.Button(acciones, text="Eliminar", bg="#DC3545", fg="white",
                     command=lambda pid=pac_id: eliminar(pid)).pack(side="left", padx=3, pady=4)

    cargar_tabla()
    return cargar_tabla