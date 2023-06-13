import customtkinter
from tkinter import messagebox as MessageBox
import tkinter
from tkinter import filedialog
import Configuracion
import custom_dialog
class InterfazSobrescribir (customtkinter.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent,*args, **kwargs)
        self.parent = parent
        self.buttonDocumentoVL = customtkinter.CTkButton(master=self,text="Documento VL", font=("Arial", 20), border_spacing=10, command=self.buscar_archivo_VL)
        self.buttonDocumentoVL.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=(40,20))
        self.buttonDocumentoVTL = customtkinter.CTkButton(master=self,text="VTL para sobrescribir", font=("Arial", 20), border_spacing=10, command=self.buscar_archivo_VTL)
        self.buttonDocumentoVTL.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=20)
        self.buttonRun = customtkinter.CTkButton(master=self,text="Run", font=("Arial", 20), border_spacing=10, command=self.button_function_run)
        self.buttonRun.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=(20,40))
        buttonVolver = customtkinter.CTkButton(master=self,text="Volver", fg_color="#272b28", hover_color="#333834", command=self.button_function_volver)
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
        resultado = MessageBox.askquestion("Aviso", 
        "¿Está seguro que desea sobreescribir el fichero actual?")

        if resultado == "yes":
            Configuracion.Configuracion.nombre_VTL_sobrescrito_creado = Configuracion.Configuracion.nombre_VTL_sobrescrito
            Configuracion.Configuracion.numero_estacion_crear = self.desplegableEstacion.get()
            print (self.desplegableEstacion.get())
            self.mostrar_siguiente("informacion_sobrescribir")
        else:
            dialog = custom_dialog.CustomDialog(text="Escribe el nombre del documento VLT:", title="VLT",parent = self.parent)
            salida_dialog = dialog.get_input()
            if salida_dialog != "" and salida_dialog != None:
                Configuracion.Configuracion.nombre_VTL_sobrescrito_creado = salida_dialog + ".xlsx"
                self.ruta_guardado()
                Configuracion.Configuracion.numero_estacion_sobrescribir = self.desplegableEstacion.get()
                print (self.desplegableEstacion.get())
                self.mostrar_siguiente("informacion_sobrescribir")
            else :
                MessageBox.showerror("Error", "Error al introducir el nombre")     
    def buscar_archivo_VL(self):
        file_path_VL = filedialog.askopenfilename(defaultextension= ".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path_VL != "":
            Configuracion.Configuracion.excel_VL_sobrescribir = file_path_VL
            self.buttonDocumentoVL.configure(fg_color= "green", hover_color="dark green")
    def buscar_archivo_VTL(self):
        file_path_VTL = filedialog.askopenfilename(defaultextension= ".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if file_path_VTL != "":
            Configuracion.Configuracion.nombre_VTL_sobrescrito = file_path_VTL
            self.buttonDocumentoVTL.configure(fg_color= "green", hover_color="dark green")
    def ruta_guardado(self):
        ruta = filedialog.askdirectory()
        if ruta == "" or ruta ==None:
            MessageBox.showerror("Error", "Error al introducir la ruta de guardado")
        else:
            Configuracion.Configuracion.ruta_guardado_sobrescribir = ruta