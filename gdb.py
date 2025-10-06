from tkinter import *
from tkinter import ttk
import LogicaDB as lg
from tkinter import messagebox as ms


class ventanas:
    def __init__(self):
        #   Ventana principal
        self.ventana = Tk()
        self.ventana.title("Bienvenido a gdb")

        #   Definimos el notebook
        self.notebook = ttk.Notebook(self.ventana)
        self.notebook.grid(padx=10, pady=10)

        #   Creo los frame
        self.frame1 = ttk.Frame(self.notebook)

        self.labelframeFrame1Conexion = ttk.Labelframe(self.frame1, text="Conexion")
        self.labelframeFrame1Conexion.grid(padx=10, pady=10)
        #   Etiqueta Host
        self.frame1EtiquetaHost = Label(self.labelframeFrame1Conexion, text="Host")
        self.frame1EtiquetaHost.grid(column=0, row=0)
        #   Stringvar de la entrada host
        self.frame1datosEntradaHost = StringVar()
        self.frame1EntradaHost = Entry(
            self.labelframeFrame1Conexion, textvariable=self.frame1datosEntradaHost
        )
        self.frame1EntradaHost.grid(column=1, row=0, padx=10, pady=10)
        #   Label Usuario
        self.frame1EtiquetaUsuario = Label(
            self.labelframeFrame1Conexion, text="Usuario"
        )
        self.frame1EtiquetaUsuario.grid(column=0, row=1, padx=10, pady=10)
        #   Stringvar de la entrada Usuario
        self.frame1datoEntradaUsuario = StringVar()
        #   Entrada Usuario
        self.frame1EntradaUsuario = Entry(
            self.labelframeFrame1Conexion, textvariable=self.frame1datoEntradaUsuario
        )
        self.frame1EntradaUsuario.grid(column=1, row=1, padx=10, pady=10)
        #   Etiqueta Clave
        self.frame1etiquetaClave = Label(self.labelframeFrame1Conexion, text="Clave")
        self.frame1etiquetaClave.grid(column=0, row=2, padx=10, pady=10)
        #   Stringvar de la Clave
        self.frame1datoEntradaClave = StringVar()
        #   Entrada de la Clave
        self.frame1datoEntradaClave = Entry(
            self.labelframeFrame1Conexion, textvariable=self.frame1datoEntradaClave
        )
        self.frame1datoEntradaClave.grid(column=1, row=2, padx=10, pady=10)
        #   Etiqueta de Puerto
        self.frame1etiquetaPuerto = Label(self.labelframeFrame1Conexion, text="Puerto")
        self.frame1etiquetaPuerto.grid(column=0, row=3, padx=10, pady=10)
        #   Stringvar del Puerto
        self.frame1datoEntradaPuerto = StringVar()
        #   Entry del puerto
        self.frame1EntradaPuerto = Entry(
            self.labelframeFrame1Conexion, textvariable=self.frame1datoEntradaPuerto
        )
        self.frame1EntradaPuerto.grid(column=1, row=3, padx=10, pady=10)

        #   Boton de Probar Conexion
        self.frame1BotonPruebaConexion = Button(
            self.labelframeFrame1Conexion, text="Prueba de Conexion",command=self.probar_conexion
        )
        self.frame1BotonPruebaConexion.grid(column=1, row=4, padx=10, pady=10)

        #   Creo los frame
        self.frame2 = ttk.Frame(self.notebook)
        #   Creo los frame
        self.frame3 = ttk.Frame(self.notebook)

        #   Agrego los frame al notebook
        self.notebook.add(self.frame1, text="Prueba de Conexion al Servidor")
        self.notebook.add(self.frame2, text="Listado DBs")
        self.notebook.add(self.frame3, text="tab3")

        self.ventana.mainloop()

    def probar_conexion(self):
        prueba = lg.gestordb()
        resultado = prueba.prueba_Conectividad(
            self.frame1datosEntradaHost.get(),
            self.frame1datoEntradaUsuario.get(),
            self.frame1datoEntradaClave.get(),
            int(self.frame1datoEntradaPuerto.get())
        )
        if resultado == "Prueba de conectividad a la db Exitosa":
            ms.showinfo("Exitoso", f"{resultado}")
        else:
            ms.showinfo("Exitoso", "Revise los datos ingresados")


prueba = ventanas()
