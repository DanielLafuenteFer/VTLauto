import customtkinter
from tkinter import filedialog
from tkinter import messagebox as MessageBox
import Configuracion
import custom_dialog
import json
class InterfazCrear (customtkinter.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent,*args, **kwargs)
        self.parent = parent
        self.buttonDocumento = customtkinter.CTkButton(master=self,text="Documento VL",font=("Arial", 20), border_spacing=10, command=self.buscar_archivo)
        self.buttonDocumento.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=(40,20))
        self.buttonNombre = customtkinter.CTkButton(master=self, text="Nombre VTL",font=("Arial", 20), border_spacing=10, command=self.button_poner_nombre)
        self.buttonNombre.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=20)
        self.buttonGuardarRuta = customtkinter.CTkButton(master=self,text="Ruta Guardado",font=("Arial", 20), border_spacing=10, command=self.ruta_guardado)
        self.buttonGuardarRuta.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=20)
        self.buttonRun = customtkinter.CTkButton(master=self,text="Run",font=("Arial", 20), border_spacing=10, command=self.button_function_run)
        self.buttonRun.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=(20,40))
        buttonVolver = customtkinter.CTkButton(master=self,text="Volver",fg_color="#272b28", hover_color="#333834", command=self.button_function_volver)
        buttonVolver.pack(side=customtkinter.LEFT, padx=(0,20), pady=(0,10))
        self.desplegableEstacion = customtkinter.CTkComboBox(master=self, values= None, state = "readonly",justify="center")
        self.desplegableEstacion.configure(values= ["1","2","3","4","5","6","7","8"])
        self.desplegableEstacion.pack(side= customtkinter.RIGHT, padx=(20,0), pady=(0,10))
        self.textoEstacion = customtkinter.CTkLabel(master=self, text= "Elija número de estacion:", justify = "center")
        self.textoEstacion.pack(side=customtkinter.RIGHT, padx=(0,5), pady=(0,10))
        
    def mostrar_siguiente(self, contenedor):
        self.parent.mostrar_contenedor(contenedor)
    def button_function_volver(self):
        self.mostrar_siguiente("inicio")
    def button_function_run(self):
        Configuracion.Configuracion.numero_estacion_crear = self.desplegableEstacion.get()
        self.mostrar_siguiente("informacion_crear")        
    def buscar_archivo(self):
        file_path = filedialog.askopenfilename(defaultextension= ".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path != "":
            Configuracion.Configuracion.excel_VL = file_path
            self.buttonDocumento.configure(fg_color= "green", hover_color="dark green")
    def button_poner_nombre(self):
        if Configuracion.Configuracion.nombre_VTL_creado != None:
            resultado = MessageBox.askquestion("Aviso", 
                "¿Está seguro que desea cambiar el nombre actual?")
            if resultado == "yes":
                dialog_nombre = custom_dialog.CustomDialog(text="Escribe el nombre del documento VLT:", title="VLT",parent = self.parent)
                salida_dialog_nombre = dialog_nombre.get_input()
                if salida_dialog_nombre != "" and salida_dialog_nombre != None:
                    Configuracion.Configuracion.nombre_VTL_creado = salida_dialog_nombre + ".xlsx"
                else:
                    self.buttonNombre.configure(fg_color= "#035387", hover_color = "#023E65" ) 
        else:
            dialog_nombre = custom_dialog.CustomDialog(text="Escribe el nombre del documento VLT:", title="VLT",parent = self.parent)
            salida_dialog_nombre = dialog_nombre.get_input()
            if salida_dialog_nombre != "" and salida_dialog_nombre != None:
                Configuracion.Configuracion.nombre_VTL_creado = salida_dialog_nombre + ".xlsx"
                self.buttonNombre.configure(fg_color= "green", hover_color="dark green")
    def ruta_guardado(self):
        ruta = filedialog.askdirectory()
        if ruta != "":
            Configuracion.Configuracion.ruta_guardado_crear = ruta
            self.buttonGuardarRuta.configure(fg_color= "green", hover_color="dark green")
    

