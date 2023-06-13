import customtkinter as ctk
import json
import Configuracion
import interfaz_inicio
import interfaz_crear
import interfaz_sobrescribir
import interfaz_progreso
import interfaz_progreso_sobrescribir 
import interfaz_jira
import interfaz_configurar_proyecto
import interfaz_configurar_usuarios
import interfaz_datos_crear
import interfaz_datos_sobrescribir
class AplicacionPrincipal(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):

        # Modos soportados : Light, Dark, System
        ctk.set_appearance_mode("Dark")

        # Temas soportados : green, dark-blue, blue
        ctk.set_default_color_theme("dark-blue")

        ctk.CTkFrame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        

        self.contenedor1 = interfaz_inicio.Inicio(self)
        self.contenedor2 = interfaz_crear.InterfazCrear(self)
        self.contenedor3 = interfaz_sobrescribir.InterfazSobrescribir(self)
        self.contenedor4 = interfaz_datos_crear.InterfazDatosCrear(self)
        self.contenedor5 = interfaz_datos_sobrescribir.InterfazDatosSobrescribir(self)
        self.contenedor6 = interfaz_jira.InterfazJira(self)
        self.contenedor7 = interfaz_configurar_proyecto.InterfazConfigurarProyecto(self)
        self.contenedor8 = interfaz_configurar_usuarios.InterfazConfigurarUsuaros(self)
        self.contenedor9 = interfaz_progreso.InterfazProgreso(self)
        self.contenedor10 = interfaz_progreso_sobrescribir.InterfazProgresoSobrescribir(self)
        
        # Define el tamaño y la posición de cada contenedor
        self.contenedor1.pack()
        self.contenedor2.pack_forget()
        self.contenedor3.pack_forget()
        self.contenedor4.pack_forget()
        self.contenedor5.pack_forget()
        self.contenedor6.pack_forget()
        self.contenedor7.pack_forget()
        self.contenedor8.pack_forget()
        self.contenedor9.pack_forget()
        self.contenedor10.pack_forget()

        # Configura la ventana
        self.parent.title("VTLauto")
        self.parent.resizable(False, False)
        self.parent.iconbitmap('icono.ico')

        #Centramos la ventana en funcion al Contenedor1 que es el primero que va a aparecer
        windowWidth = self.contenedor1.winfo_reqwidth()
        windowHeight = self.contenedor1.winfo_reqheight()
        positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
        root.geometry("+{}+{}".format(positionRight, positionDown))
        

        self.cargar_datos()

    def mostrar_contenedor(self, contenedor):
        if contenedor == "inicio":
            self.contenedor1.pack()
            self.contenedor2.pack_forget()
            self.contenedor3.pack_forget()
            self.contenedor4.pack_forget()
            self.contenedor5.pack_forget()
            self.contenedor6.pack_forget()
            self.contenedor7.pack_forget()
            self.contenedor8.pack_forget()
            self.contenedor9.pack_forget()
            self.contenedor10.pack_forget()   
        elif contenedor == "crear":
            self.contenedor1.pack_forget()
            self.contenedor2.pack()
            self.contenedor3.pack_forget()
            self.contenedor4.pack_forget()
            self.contenedor5.pack_forget()
            self.contenedor6.pack_forget()
            self.contenedor7.pack_forget()
            self.contenedor8.pack_forget()
            self.contenedor9.pack_forget()
            self.contenedor10.pack_forget()
        elif contenedor == "sobrescribir":
            self.contenedor1.pack_forget()
            self.contenedor2.pack_forget()
            self.contenedor3.pack()
            self.contenedor4.pack_forget()
            self.contenedor5.pack_forget()
            self.contenedor6.pack_forget()
            self.contenedor7.pack_forget()
            self.contenedor8.pack_forget()
            self.contenedor9.pack_forget()
            self.contenedor10.pack_forget()
        elif contenedor == "informacion_crear":
            self.contenedor1.pack_forget()
            self.contenedor2.pack_forget()
            self.contenedor3.pack_forget()
            self.contenedor4.pack()
            self.contenedor4.crear_texto()
            self.contenedor5.pack_forget()
            self.contenedor6.pack_forget()
            self.contenedor7.pack_forget()
            self.contenedor8.pack_forget()
            self.contenedor9.pack_forget()
            self.contenedor10.pack_forget()
        elif contenedor == "informacion_sobrescribir":
            self.contenedor1.pack_forget()
            self.contenedor2.pack_forget()
            self.contenedor3.pack_forget()
            self.contenedor4.pack_forget()
            self.contenedor5.pack()
            self.contenedor5.crear_texto()
            self.contenedor6.pack_forget()
            self.contenedor7.pack_forget()
            self.contenedor8.pack_forget()
            self.contenedor9.pack_forget()
            self.contenedor10.pack_forget()
        elif contenedor == "jira":
            self.contenedor1.pack_forget()
            self.contenedor2.pack_forget()
            self.contenedor3.pack_forget()
            self.contenedor4.pack_forget()
            self.contenedor5.pack_forget()
            self.contenedor6.pack()
            self.contenedor7.pack_forget()
            self.contenedor8.pack_forget()
            self.contenedor9.pack_forget()
            self.contenedor10.pack_forget()
        elif contenedor == "configurar_proyecto":
            self.contenedor1.pack_forget()
            self.contenedor2.pack_forget()
            self.contenedor3.pack_forget()
            self.contenedor4.pack_forget()
            self.contenedor5.pack_forget()
            self.contenedor6.pack_forget()
            self.contenedor7.pack()
            self.contenedor8.pack_forget()
            self.contenedor9.pack_forget()
            self.contenedor10.pack_forget()
        elif contenedor == "configurar_usuarios":
            self.contenedor1.pack_forget()
            self.contenedor2.pack_forget()
            self.contenedor3.pack_forget()
            self.contenedor4.pack_forget()
            self.contenedor5.pack_forget()
            self.contenedor6.pack_forget()
            self.contenedor7.pack_forget()
            self.contenedor8.pack()
            self.contenedor9.pack_forget()
            self.contenedor10.pack_forget()
        elif contenedor == "progreso":
            self.contenedor1.pack_forget()
            self.contenedor2.pack_forget()
            self.contenedor3.pack_forget()
            self.contenedor4.pack_forget()
            self.contenedor5.pack_forget()
            self.contenedor6.pack_forget()
            self.contenedor7.pack_forget()
            self.contenedor8.pack_forget()
            self.contenedor9.pack()
            self.contenedor9.iniciar_contenedor()
            self.contenedor10.pack_forget()
        elif contenedor == "progreso_rescribir":
            self.contenedor1.pack_forget()
            self.contenedor2.pack_forget()
            self.contenedor3.pack_forget()
            self.contenedor4.pack_forget()
            self.contenedor5.pack_forget()
            self.contenedor6.pack_forget()
            self.contenedor7.pack_forget()
            self.contenedor8.pack_forget()
            self.contenedor9.pack_forget()
            self.contenedor10.pack()
            self.contenedor10.iniciar_contenedor()
    def cargar_datos(self):
        with open('data.json') as file:
            data = json.load(file)
            print (data)
            if data['configuracion'] == "":
                Configuracion.Configuracion.cargar_datos = False
            else:
                lista = data['configuracion']
                Configuracion.Configuracion.domain = lista[0]["Dominio"]
                Configuracion.Configuracion.token = lista[0]["Token"]
                Configuracion.Configuracion.mail = lista[0]["Mail"]
                Configuracion.Configuracion.component_servidor = lista[0]["UsuarioServidor"]
                Configuracion.Configuracion.component_ACU = lista[0]["UsuarioACU"]
                Configuracion.Configuracion.name_project = lista[0]["Proyecto"]
if __name__ == "__main__":
    root = ctk.CTk()
    app = AplicacionPrincipal(root)
    app.pack()
    root.mainloop()