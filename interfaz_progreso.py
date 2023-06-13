import customtkinter
import crear_VTL
from PIL import Image
import Configuracion
class InterfazProgreso (customtkinter.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent,*args, **kwargs)
        self.parent = parent

        self.progressbar = customtkinter.CTkProgressBar(master=self)
        self.progressbar.pack(padx=20, pady=20)



    def iniciar_contenedor(self):
        self.iterador = crear_VTL.CrearVTL(self.progressbar)
        self.iterador.start()
