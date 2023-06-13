import customtkinter
import Configuracion
import json
from tkinter import messagebox as MessageBox
class InterfazDatosCrear (customtkinter.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent,*args, **kwargs)
        self.parent = parent

    def crear_texto(self):
        self.textoRutaVL = customtkinter.CTkLabel(master= self,text="Ruta del documento VL: \n" + str(Configuracion.Configuracion.excel_VL))
        self.textoRutaVL.pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=1, padx=200, pady=(40,20))
        self.textoNombreVTL = customtkinter.CTkLabel(master= self,text="Nombre del documento VTL: \n" + str(Configuracion.Configuracion.nombre_VTL_creado))
        self.textoNombreVTL.pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=1, padx=200, pady=20)
        self.textoRutaGuardado = customtkinter.CTkLabel(master= self,text="Ruta de guardado: \n" + str(Configuracion.Configuracion.ruta_guardado_crear))
        self.textoRutaGuardado.pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=1, padx=200, pady=20)
        self.textoUsurioJira = customtkinter.CTkLabel(master= self,text="Mail del Jira: \n" + str(Configuracion.Configuracion.mail))
        self.textoUsurioJira.pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=1, padx=200, pady=20)
        self.textoNombreProyecto = customtkinter.CTkLabel(master= self,text="Nombre proyecto Jira: \n" + str(Configuracion.Configuracion.name_project))
        self.textoNombreProyecto.pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=1, padx=200, pady=(20,40))
        self.buttonVolver = customtkinter.CTkButton(master=self,text="Volver", fg_color="#272b28", hover_color="#333834", command=self.button_function_volver)
        self.buttonVolver.pack(side=customtkinter.LEFT, padx=(0,20), pady=(0,10))
        self.buttonAceptar = customtkinter.CTkButton(master=self,text="Aceptar", fg_color="#272b28", hover_color="#333834", command=self.button_function_aceptar)
        self.buttonAceptar.pack(side=customtkinter.RIGHT, padx=(20,0), pady=(0,10))

    def mostrar_siguiente(self, contenedor):
            self.parent.mostrar_contenedor(contenedor)

    def button_function_volver(self):
            print("button pressed")
            self.textoRutaVL.pack_forget()
            self.textoNombreVTL.pack_forget()
            self.textoRutaGuardado.pack_forget()
            self.textoUsurioJira.pack_forget()
            self.textoNombreProyecto.pack_forget()
            self.buttonAceptar.pack_forget()
            self.buttonVolver.pack_forget()
            self.mostrar_siguiente("crear")
    
    def button_function_aceptar(self):
        if self.verificar_datos() == True:
            self.datos_json()
            self.mostrar_siguiente("progreso")
    def verificar_datos(self):
        validos = False
        if Configuracion.Configuracion.excel_VL == None:
            MessageBox.showerror("Error", "Error al introducir el documento VL") 
        elif Configuracion.Configuracion.nombre_VTL_creado == None:
            MessageBox.showerror("Error", "Error al introducir el nombre del VTL")
        elif Configuracion.Configuracion.ruta_guardado_crear == None:
            MessageBox.showerror("Error", "Error al introducir la ruta de guardado")
        elif Configuracion.Configuracion.numero_estacion_crear == "":
            MessageBox.showerror("Error", "Error al introducir el número de estación")
        elif Configuracion.Configuracion.domain == None:
            MessageBox.showerror("Error", "Error al introducir el dominio de Jira")
        elif Configuracion.Configuracion.mail == None:
            MessageBox.showerror("Error", "Error al introducir el mail de Jira")
        elif Configuracion.Configuracion.token == None:
            MessageBox.showerror("Error", "Error al introducir el token de Jira")
        elif Configuracion.Configuracion.name_project == None:
            MessageBox.showerror("Error", "Error al introducir nombre del proyecto Jira")
        else:
            validos = True
        return validos
    def datos_json(self):
        data = {}
        data['configuracion'] = []
        data['configuracion'].append({
            'Dominio': Configuracion.Configuracion.domain,
            'Token': Configuracion.Configuracion.token,
            'Mail': Configuracion.Configuracion.mail,
            'UsuarioACU': Configuracion.Configuracion.component_ACU,
            'UsuarioServidor': Configuracion.Configuracion.component_servidor,
            'Proyecto': Configuracion.Configuracion.name_project})
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)