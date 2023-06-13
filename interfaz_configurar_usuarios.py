import customtkinter
from tkinter import messagebox as MessageBox
import Configuracion
import custom_dialog
class InterfazConfigurarUsuaros(customtkinter.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent,*args, **kwargs)
        self.parent = parent
        self.buttonUsuarioServidor = customtkinter.CTkButton(master=self,text="Usuario Servidor", font=("Arial", 20), border_spacing=10, command=self.button_function_usuario_servidor)
        self.buttonUsuarioServidor.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=(40,20))
        self.buttonUsuarioACU = customtkinter.CTkButton(master=self,text="Usuario ACU", font=("Arial", 20), border_spacing=10, command=self.button_function_usuario_ACU)
        self.buttonUsuarioACU.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=(20,40))
        buttonVolver = customtkinter.CTkButton(master=self,text="Volver", fg_color="#272b28", hover_color="#333834", command=self.button_function_volver)
        buttonVolver.pack(side=customtkinter.LEFT, padx=(0,20), pady=(0,10))
    def mostrar_siguiente(self, contenedor):
        self.parent.mostrar_contenedor(contenedor)
    def button_function_volver(self):
        self.mostrar_siguiente("jira")
    def button_function_usuario_servidor(self):
        if Configuracion.Configuracion.component_servidor != None:
            resultado = MessageBox.askquestion("Aviso", 
                "¿Está seguro que desea cambiar el usuario actual encargado del servidor?")
            if resultado == "yes":
                dialog_servidor = custom_dialog.CustomDialog(text="Escribe el codigo del usuario encargado del servidor:", title="VLT",parent = self.parent)
                salida_dialog_usuario_servidor = dialog_servidor.get_input()
                if salida_dialog_usuario_servidor != "" and salida_dialog_usuario_servidor != None:
                    Configuracion.Configuracion.component_servidor = salida_dialog_usuario_servidor
                    self.buttonUsuarioServidor.configure(fg_color= "green", hover_color="dark green")
                else:
                    self.buttonUsuarioServidor.configure(fg_color= "#035387", hover_color="#023E65")
        else:
            dialog_servidor = custom_dialog.CustomDialog(text="Escribe el codigo del usuario encargado del servido:", title="VLT",parent = self.parent)
            salida_dialog_usuario_servidor = dialog_servidor.get_input()
            if salida_dialog_usuario_servidor != "" and salida_dialog_usuario_servidor != None:
                Configuracion.Configuracion.component_servidor = salida_dialog_usuario_servidor
                self.buttonUsuarioServidor.configure(fg_color= "green", hover_color="dark green")
    def button_function_usuario_ACU(self):
        if Configuracion.Configuracion.component_ACU != None:
            resultado = MessageBox.askquestion("Aviso", 
                "¿Está seguro que desea cambiar el usuario actual encargado del ACU?")
            if resultado == "yes":
                dialog_ACU = custom_dialog.CustomDialog(text="Escribe el codigo del usuario encargado del ACU:", title="VLT",parent = self.parent)
                salida_dialog_usuario_ACU = dialog_ACU.get_input()
                if salida_dialog_usuario_ACU != "" and salida_dialog_usuario_ACU != None:
                    Configuracion.Configuracion.component_ACU = salida_dialog_usuario_ACU
                    self.buttonUsuarioACU.configure(fg_color= "green", hover_color="dark green")
                else:
                    self.buttonUsuarioACU.configure(fg_color= "#035387", hover_color="#023E65")
        else:
            dialog_ACU = custom_dialog.CustomDialog(text="Escribe el codigo del usuario encargado del ACU:", title="VLT",parent = self.parent)
            salida_dialog_usuario_ACU = dialog_ACU.get_input()
            if salida_dialog_usuario_ACU != "" and salida_dialog_usuario_ACU != None:
                Configuracion.Configuracion.component_ACU = salida_dialog_usuario_ACU
                self.buttonUsuarioACU.configure(fg_color= "green", hover_color="dark green")