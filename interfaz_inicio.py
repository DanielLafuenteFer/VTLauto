import customtkinter
class Inicio(customtkinter.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, parent,*args, **kwargs)
        self.parent = parent
        
        buttonCrear = customtkinter.CTkButton(master=self,text="Crear", font=("Arial", 20), border_spacing=10, command=self.button_function)
        buttonCrear.pack(side=customtkinter.TOP, fill=customtkinter.BOTH,expand=1 , padx=200, pady=(40,20))
        
        buttonReescribir = customtkinter.CTkButton(master=self,text="Sobrescribir", font=("Arial", 20), border_spacing=10, command=self.button_function1)
        buttonReescribir.pack(side=customtkinter.TOP, fill=customtkinter.BOTH, expand=1, padx=200, pady=20)
        
        buttonConfigurarJira = customtkinter.CTkButton(master=self,text="Configurar Jira",  font=("Arial", 20), border_spacing=10, command=self.button_function_configurar)
        buttonConfigurarJira.pack(side=customtkinter.TOP, padx=200, pady=(20,40))
        
        self.texto_autor=customtkinter.CTkLabel(self, text="Desarrollado por: \nDaniel Lafuente Fernandez", font=customtkinter.CTkFont(family="Calibri", size=12, slant="italic"), text_color="#707070")
        self.texto_autor.pack(side=customtkinter.RIGHT, padx=(0,20), pady=(20, 12))

        self.texto_autor=customtkinter.CTkLabel(self, text="Trabjo TFG UAH: \nIng. Sistemas de Información", font=customtkinter.CTkFont(family="Calibri", size=12, slant="italic"), text_color="#707070")
        self.texto_autor.pack(side=customtkinter.LEFT, padx=(20,0), pady=(20, 12))

    def mostrar_siguiente(self, contenedor):
        self.parent.mostrar_contenedor(contenedor)
    def button_function(self):
        print("button pressed")
        self.mostrar_siguiente("crear")
    def button_function1(self):
        print("button pressed")
        self.mostrar_siguiente("sobrescribir")  
    def button_function_configurar(self):
        print("button pressed")
        self.mostrar_siguiente("jira")
    
