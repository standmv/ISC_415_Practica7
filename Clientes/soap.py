import zeep
import json

#url del servicio Web a utilizarse
wsdl = 'http://localhost:7777/ws/AcademicoWebService?wsdl'

#creando el cliente
client = zeep.Client(wsdl=wsdl)

#Consultando lista de estudiantes
estudiantes_list = client.service.getAllEstudiante()

#Consultando asignatura
asignatura = 20
asignatura = client.service.getAsignatura(asignatura)

#Consultando Profesor
cedula = "402-2338506-8"
profesor = client.service.getProfesor(cedula)

#Imprimiendo cada una de las consultas
#print(asignatura)
#print(estudiantes_list)
#print(profesor)