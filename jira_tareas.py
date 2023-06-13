import requests
import json
import Configuracion
class JiraTareas():
    def ultima_tarea(self):
        url="https://" + Configuracion.Configuracion.domain + ".atlassian.net/rest/api/3/search"
        headers={
        "Accept": "application/json",
            "Content-Type": "application/json"
        }

        query = {
        'jql': 'project =' + Configuracion.Configuracion.name_project
        }

        response=requests.get(url,headers=headers,params=query,auth=(Configuracion.Configuracion.mail,Configuracion.Configuracion.token))
        data=response.json()
        issues=data["issues"]
        lista_tareas = []
        for issue in issues:
            lista_tareas.append(issue["key"])
        Configuracion.Configuracion.issue = lista_tareas[0]