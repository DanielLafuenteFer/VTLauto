import customtkinter
class InterfazJira(customtkinter.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent,*args, **kwargs)
        self.parent = parent
        buttonConfigurarProyecto = customtkinter.CTkButton(master=self,text="Configurar Proyecto Jira", font=("Arial", 20), border_spacing=10, command=self.button_function_configurar_proyecto)
        buttonConfigurarProyecto.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=150, pady=(40,20))
        buttonConfigurarUsuarios = customtkinter.CTkButton(master=self,text="Configurar Usuarios Jira", font=("Arial", 20), border_spacing=10, command=self.button_function_configurar_usuarios)
        buttonConfigurarUsuarios.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=150, pady=(20,40))
        buttonVolver = customtkinter.CTkButton(master=self,text="Volver", fg_color="#272b28", hover_color="#333834", command=self.button_function_volver)
        buttonVolver.pack(side=customtkinter.LEFT, padx=(0,20), pady=(0,10))
    def mostrar_siguiente(self, contenedor):
        self.parent.mostrar_contenedor(contenedor)
    def button_function_volver(self):
        print("button pressed")
        self.mostrar_siguiente("inicio")
    def button_function_configurar_usuarios(self):
        print("button pressed")
        self.mostrar_siguiente("configurar_usuarios")
    def button_function_configurar_proyecto(self):
        print("button pressed")
        self.mostrar_siguiente("configurar_proyecto") 