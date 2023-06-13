import customtkinter
from tkinter import messagebox as MessageBox
import Configuracion
import custom_dialog
class InterfazConfigurarProyecto(customtkinter.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent,*args, **kwargs)
        self.parent = parent
        self.buttonMail = customtkinter.CTkButton(master=self, text="Correo de jira", font=("Arial", 20), border_spacing=10, command=self.button_function_mail)
        self.buttonMail.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=(40,20))
        self.buttonDomain = customtkinter.CTkButton(master=self, text="Dominio del proyeto", font=("Arial", 20), border_spacing=10, command=self.button_function_domain)
        self.buttonDomain.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=20)
        self.buttonToken = customtkinter.CTkButton(master=self, text="Token api jira", font=("Arial", 20), border_spacing=10, command=self.button_function_token)
        self.buttonToken.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=20)
        self.buttonNombreProyecto = customtkinter.CTkButton(master=self, text="Nombre proyecto", font=("Arial", 20), border_spacing=10, command=self.button_function_nombre_proyecto)
        self.buttonNombreProyecto.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=(20,40))
        buttonVolver = customtkinter.CTkButton(master=self,text="Volver", fg_color="#272b28", hover_color="#333834", command=self.button_function_volver)
        buttonVolver.pack(side=customtkinter.LEFT, padx=(0,20), pady=(0,10))
    def mostrar_siguiente(self, contenedor):
        self.parent.mostrar_contenedor(contenedor)
    def button_function_volver(self):
        self.mostrar_siguiente("jira")
    def button_function_mail(self):
        if Configuracion.Configuracion.mail != None:
            resultado = MessageBox.askquestion("Aviso", 
                "¿Está seguro que desea cambiar el mail actual?")
            if resultado == "yes":
                dialog_mail = custom_dialog.CustomDialog(text="Escribe el correo asociado a jira:", title="VLT",parent = self.parent)
                salida_dialog_mail = dialog_mail.get_input()
                if salida_dialog_mail != "" and salida_dialog_mail != None:
                    Configuracion.Configuracion.mail = salida_dialog_mail
                    self.buttonMail.configure(fg_color= "green", hover_color="dark green")
                else:
                    self.buttonMail.configure(fg_color= "#035387", hover_color="#023E65")
        else:
            dialog_mail = custom_dialog.CustomDialog(text="Escribe el correo asociado a jira:", title="VLT",parent = self.parent)
            salida_dialog_mail = dialog_mail.get_input()
            if salida_dialog_mail != "" and salida_dialog_mail != None:
                Configuracion.Configuracion.mail = salida_dialog_mail
                self.buttonMail.configure(fg_color= "green", hover_color="dark green")
        print(Configuracion.Configuracion.mail)
    def button_function_domain(self):
        if Configuracion.Configuracion.domain != None:
            resultado = MessageBox.askquestion("Aviso", 
                "¿Está seguro que desea cambiar el dominio actual?")
            if resultado == "yes":
                dialog_domain = custom_dialog.CustomDialog(text="Escribe el dominio del proyecto de jira:", title="VLT",parent = self.parent)
                salida_dialog_domain = dialog_domain.get_input()
                if salida_dialog_domain != "" and salida_dialog_domain != None:
                    Configuracion.Configuracion.domain = salida_dialog_domain
                    self.buttonDomain.configure(fg_color= "green", hover_color="dark green")
                else:
                    self.buttonDomain.configure(fg_color= "#035387", hover_color="#023E65")
        else:
            dialog_domain = custom_dialog.CustomDialog(text="Escribe el dominio del proyecto de jira:", title="VLT",parent = self.parent)
            salida_dialog_domain = dialog_domain.get_input()
            if salida_dialog_domain != "" and salida_dialog_domain != None:
                Configuracion.Configuracion.domain = salida_dialog_domain
                self.buttonDomain.configure(fg_color= "green", hover_color="dark green")
    def button_function_token(self):
        if Configuracion.Configuracion.token != None:
            resultado = MessageBox.askquestion("Aviso", 
                "¿Está seguro que desea cambiar el token actual?")
            if resultado == "yes":
                dialog_token = custom_dialog.CustomDialog(text="Escribe el token de la api de jira:", title="VLT",parent = self.parent)
                salida_dialog_token = dialog_token.get_input()
                if salida_dialog_token != "" and salida_dialog_token != None:
                    Configuracion.Configuracion.token = salida_dialog_token
                    self.buttonToken.configure(fg_color= "green", hover_color="dark green")
                else:
                    self.buttonToken.configure(fg_color= "#035387", hover_color="#023E65")
        else:
            dialog_token = custom_dialog.CustomDialog(text="Escribe el token de la api de jira:", title="VLT",parent = self.parent)
            salida_dialog_token = dialog_token.get_input()
            if salida_dialog_token != "" and salida_dialog_token != None:
                Configuracion.Configuracion.token = salida_dialog_token
                self.buttonToken.configure(fg_color= "green", hover_color="dark green")
    def button_function_nombre_proyecto(self):
        if Configuracion.Configuracion.name_project != None:
            resultado = MessageBox.askquestion("Aviso", 
                "¿Está seguro que desea cambiar el nombre actual?")
            if resultado == "yes":
                dialog_name_project = custom_dialog.CustomDialog(text="Escribe el nombree del proyecto de jira:", title="VLT",parent = self.parent)
                salida_dialog_name_project = dialog_name_project.get_input()
                if salida_dialog_name_project != "" and salida_dialog_name_project != None:
                    Configuracion.Configuracion.name_project = salida_dialog_name_project
                    self.buttonNombreProyecto.configure(fg_color= "green", hover_color="dark green")
                else:
                    self.buttonNombreProyecto.configure(fg_color= "#035387", hover_color="#023E65")
        else:
            dialog_name_project = custom_dialog.CustomDialog(text="Escribe el nombree del proyecto de jira:", title="VLT",parent = self.parent)
            salida_dialog_name_project = dialog_name_project.get_input()
            if salida_dialog_name_project != "" and salida_dialog_name_project != None:
                Configuracion.Configuracion.name_project = salida_dialog_name_project
                self.buttonNombreProyecto.configure(fg_color= "green", hover_color="dark green")
            
    
 