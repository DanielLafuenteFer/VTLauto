import customtkinter
class CustomDialog(customtkinter.CTkInputDialog):
    """Dialogo customizado para que aparezca centrado y ademas que permita que se oculte el texto introducido (para pedir una contraseña, por ejemplo)"""
    _text_protected = False

    def __init__(self, title: str = "CTkDialog", text: str = "CTkDialog", parent: object = None, text_protected: bool = False):
        super().__init__(title=title, text=text)
        windowWidth = parent.winfo_reqwidth()
        windowHeight = parent.winfo_reqheight()
        positionRight = int(self.winfo_screenwidth()/2 - windowWidth/2) + 100
        positionDown = int(self.winfo_screenheight()/2 - windowHeight/2) + 100
        self.geometry("+{}+{}".format(positionRight, positionDown))
        self._text_protected = text_protected

    def _cancel_event(self, event=None): #Por defecto el boton de cancelar es igual al de aceptar. La sobreescribo para que si le das a cancelar devuelva un None, igual que si cierras el pop up dandole a la x
        self._user_input = None
        self.grab_release()
        self.destroy()