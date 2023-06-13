class Configuracion(object):
    """Clase que tiene como atributo la configuracion que se carga al iniciar la aplicación. 
    Esta implementada siguiendo el patron Singleton para evitar multiples instancias de esta clase"""

    excel_VL = None
    nombre_VTL_creado = None
    nombre_VTL_sobrescrito = None # cambiar nombre
    excel_VL_sobrescribir = None
    nombre_VTL_sobrescrito_creado = None # cambiar nombre
    domain = None
    token = None
    mail = None
    component_servidor = None
    component_ACU = None
    component_global = None
    issue = None
    name_project = None
    cargar_datos = None
    ruta_guardado_crear = None
    ruta_guardado_sobrescribir = None
    numero_estacion_crear = None
    numero_estacion_sobrescribir = None 
    progreso_crear = None
    def __new__(cls):
        if not hasattr(cls, 'instance'):
          cls.instance = super(Configuracion, cls).__new__(cls)
        return cls.instance

    """def __init__(self):
        print ("hola")"""
    