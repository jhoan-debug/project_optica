import tkinter as t
from tkinter import ttk, messagebox
from models.paciente import HistoriaClinica

NARANJA = "#FF8C00"

def ver_historias(nombre_usuario=None):
    ventana = t.Toplevel()
    ventana.title("Historias Clínicas")
    ventana.geometry("950x520")

    header = t.Frame(ventana, bg=NARANJA, height=70)
    header.pack(fill="x")
    header.pack_propagate(False)

    t.Label(header, text="Historias Clínicas", bg=NARANJA,
            fg="white", font=("Arial", 18, "bold")).pack(side="left", padx=20)
    if nombre_usuario:
        t.Label(header, text=f"Usuario conectado: {nombre_usuario}",
                bg=NARANJA, fg="white", font=("Arial", 10, "bold")).pack(side="right", padx=20)

    barra = t.Frame(ventana)
    barra.pack(fill="x", padx=20, pady=10)
    t.Button(barra, text="Menu Pacientes", command=ventana.destroy).pack(side="left")

    contenedor = t.Frame(ventana)
    contenedor.pack(fill="both", expand=True, padx=20, pady=(0, 15))

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

    for col in range(4):
        tabla.grid_columnconfigure(col, weight=1)

    encabezados = ["No. Historia", "Paciente", "Motivo", "Recomendacion"]
    for col, texto in enumerate(encabezados):
        t.Label(tabla, text=texto, font=("Arial", 11, "bold"),
                bg="#dddddd", anchor="center").grid(row=0, column=col, sticky="ew", padx=1, pady=1)

    # trae desde la db
    historias = HistoriaClinica.listar()

    if not historias:
        t.Label(tabla, text="No hay historias registradas", font=("Arial", 11)
                ).grid(row=1, column=0, columnspan=5, pady=20)
    else:
        for fila, h in enumerate(historias, start=1):
            hist_id, nombre, motivo, recomendacion = h

            t.Label(tabla, text=hist_id, font=("Arial", 10)).grid(row=fila, column=0, sticky="ew", padx=1, pady=2)
            t.Label(tabla, text=nombre, font=("Arial", 10)).grid(row=fila, column=1, sticky="ew", padx=1, pady=2)
            t.Label(tabla, text=motivo, font=("Arial", 10)).grid(row=fila, column=2, sticky="ew", padx=1, pady=2)
            t.Label(tabla, text=recomendacion, font=("Arial", 10)).grid(row=fila, column=3, sticky="ew", padx=1, pady=2)

            btn_ver_detalle = t.Button(
                tabla, text="Ver Detalle", bg="#17a2b8", fg="white",
                command=lambda hid=hist_id: ver_detalle_historia(hid)
            )
            btn_ver_detalle.grid(row=fila, column=4, padx=3, pady=2)

    ventana.mainloop()

def ver_detalle_historia(hist_id):
    datos = HistoriaClinica.obtener_por_id(hist_id)

    if datos is None:
        messagebox.showerror("Error", "No se encontró la historia clínica")
        return

    (hist_id, nombre, documento, motivo,
     estod, cilod, ejeod, estoi, ciloi, ejeoi,
     diagod, diagoi, recomendacion) = datos

    ventana = t.Toplevel()
    ventana.title(f"Detalle Historia #{hist_id}")
    ventana.geometry("500x550")
    ventana.resizable(False, False)

    t.Label(ventana, text=f"Historia Clínica #{hist_id}", font=("Arial", 16, "bold")).pack(pady=15)

    frame = t.Frame(ventana)
    frame.pack(padx=20, pady=10, fill="both", expand=True)

    campos = [
        ("Paciente", nombre),
        ("Documento", documento),
        ("Motivo de visita", motivo),
        ("Esfera OD", estod), ("Cilindro OD", cilod), ("Eje OD", ejeod),
        ("Esfera OI", estoi), ("Cilindro OI", ciloi), ("Eje OI", ejeoi),
        ("Diagnóstico OD", diagod),
        ("Diagnóstico OI", diagoi),
        ("Recomendación", recomendacion),
    ]

    for fila, (etiqueta, valor) in enumerate(campos):
        t.Label(frame, text=f"{etiqueta}:", font=("Arial", 10, "bold")
                ).grid(row=fila, column=0, sticky="w", pady=4)
        t.Label(frame, text=valor, font=("Arial", 10)
                ).grid(row=fila, column=1, sticky="w", padx=10, pady=4)

    t.Button(ventana, text="Cerrar", command=ventana.destroy).pack(pady=15)

    ventana.mainloop()