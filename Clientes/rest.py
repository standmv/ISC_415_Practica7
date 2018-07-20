import unirest
import json

#Consultando lista de estudiantes
estudiantes_list = unirest.get("http://localhost:4567/rest/estudiantes/", headers={"Accept": "application/json"})

#Creando un estudiante
#se debe especificar en el header el tipo de contenido que va a recibir
estudiante_create = unirest.post("http://localhost:4567/rest/estudiantes/", headers={"Accept": "application/json", "Content-Type":"application/json"}, params=json.dumps({"nombre":"Stan", "correo":"stan@gmail.com", "carrera":"ISC"}))

#consultando un estudiante por su matricula
matricula = 10
estudiante_get = unirest.get("http://localhost:4567/rest/estudiantes/{}".format(matricula), headers={"Accept":"application/json"})


#Imprimiendo cada una de las consultas
#print(estudiantes_list.body)
#print(estudiante_create.body)
#print(estudiante_get.body)