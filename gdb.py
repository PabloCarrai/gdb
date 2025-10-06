from tkinter import *
from tkinter import ttk
import LogicaDB as lg


class ventanas:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Bienvenido a gdb")

        self.notebookConexion = ttk.Notebook(self.ventana)
        self.notebookConexion.grid(column=0, row=0, padx=10, pady=10)

        self.frameConexion = ttk.Frame(self.notebookConexion, width=400, height=280)
        self.frameConexion.grid(column=0, row=0, padx=10, pady=10)

        self.labelframeConexion = ttk.LabelFrame(
            self.frameConexion, text="Datos de Conexion"
        )
        self.labelframeConexion.grid(column=0, row=0, padx=10, pady=10)

        self.etiquetaConexionNombreDB = Label(self.labelframeConexion, text="Host")
        self.etiquetaConexionNombreDB.grid(column=0, row=0, padx=10, pady=10)

        self.datoEntradaConexionNombreDB = StringVar()
        self.entradaConexionNombreDB = ttk.Entry(
            self.labelframeConexion, textvariable=self.datoEntradaConexionNombreDB
        )
        self.entradaConexionNombreDB.grid(column=1, row=0, padx=10, pady=10)

        self.etiquetaConexionUsuarioDB = Label(self.labelframeConexion, text="Usuario")
        self.etiquetaConexionUsuarioDB.grid(column=0, row=1, padx=10, pady=10)

        self.datoEntradaConexionUsuarioDB = StringVar()
        self.entradaConexionUsuarioDB = Entry(
            self.labelframeConexion, textvariable=self.datoEntradaConexionUsuarioDB
        )
        self.entradaConexionUsuarioDB.grid(column=1, row=1, padx=10, pady=10)

        self.etiquetaConexionClaveDB = Label(self.labelframeConexion, text="Clave")
        self.etiquetaConexionClaveDB.grid(column=0, row=2, padx=10, pady=10)

        self.datoEntradaConexionClaveDB = StringVar()
        self.entradaConexionClaveDB = Entry(
            self.labelframeConexion, textvariable=self.datoEntradaConexionClaveDB
        )
        self.entradaConexionClaveDB.grid(column=1, row=2, padx=10, pady=10)

        self.etiquetaConexionPuertoDB = Label(self.labelframeConexion, text="Puerto")
        self.etiquetaConexionPuertoDB.grid(column=0, row=3, padx=10, pady=10)

        self.datoEntradaConexionPuertoDB = StringVar()
        self.entradaConexionPuertoDB = Entry(
            self.labelframeConexion, textvariable=self.datoEntradaConexionPuertoDB
        )
        self.entradaConexionPuertoDB.grid(column=1, row=3, padx=10, pady=10)

        self.botonConexionDB = Button(
            self.labelframeConexion,
            text="Probar Conexion",
            command=self.probar_conexion,
        )
        self.botonConexionDB.grid(column=1, row=4, padx=10, pady=10)

        self.ventana.mainloop()

    def probar_conexion(self):
        prueba = lg.gestordb(
            self.entradaConexionNombreDB.get(),
            self.entradaConexionUsuarioDB.get(),
            self.entradaConexionClaveDB.get(),
            self.entradaConexionPuertoDB.get(),
        )
        print(prueba)


prueba = ventanas()
