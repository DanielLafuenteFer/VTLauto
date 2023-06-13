import customtkinter
import sobrescribir_VTL
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
class InterfazProgresoSobrescribir (customtkinter.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent,*args, **kwargs)
        self.parent = parent

        self.progressbar = customtkinter.CTkProgressBar(master=self)
        self.progressbar.pack(padx=20, pady=20)


        
    def iniciar_contenedor(self):
        self.iterador = sobrescribir_VTL.SobrescribirVTL(self.progressbar)
        self.iterador.start()