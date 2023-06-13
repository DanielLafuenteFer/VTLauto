import requests
import json
import Configuracion

class JiraUsuario():
    def asignar_usuario(self):
        url = "https://"+ Configuracion.Configuracion.domain +".atlassian.net//rest/api/3/issue/" + Configuracion.Configuracion.issue + "/assignee"
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload=json.dumps(
            {
                "accountId":Configuracion.Configuracion.component_global
            }
        )
        response=requests.request("PUT",url,headers=headers,data=payload,auth=(Configuracion.Configuracion.mail,Configuracion.Configuracion.token))