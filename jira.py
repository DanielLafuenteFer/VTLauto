import requests
import json
import Configuracion

class Jira():
    def __init__(self):
        summary = summary
    def conexion(self,summary,description):
        url="https://" + Configuracion.Configuracion.domain + ".atlassian.net//rest/api/2/issue"
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload=json.dumps(
        {
        "fields": {
            "project":
            {
                "key": Configuracion.Configuracion.name_project
            },
            "summary": summary,
            "description": description,
            "issuetype": {
                "name": "Task"
            }
        }
        }
        )
        response=requests.post(url,headers=headers,data=payload,auth=(Configuracion.Configuracion.mail,Configuracion.Configuracion.token))
        data=response.json()