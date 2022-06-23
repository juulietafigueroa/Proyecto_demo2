from json import load
from pipes import Template
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader 

def saludo(request):
    return HttpResponse("Hola mundo")

def segunda_vista(request):
    return HttpResponse("Segunda vista")

def DiaDeHoy(request):
    dia = datetime.datetime.now()
    texto = "Hoy es: {}".format(dia)
    return HttpResponse(texto)

def nombre_persona(self, nombre):
    resultado = "Mi nombre es: <br> <br> {}".format(nombre)  
    return HttpResponse(resultado)  


def probando_template (self):

    nombre = 'Juli'
    apellido = 'Figueroa'
    lista_de_notas = [2, 3, 4, 5, 6]

    diccionario = {'nombre':nombre, 'apellido':apellido, 'lista_de_notas': lista_de_notas}
    #miHtml = open('Template1.html')

    #plantilla = Template(miHtml.read())
    
    #miHtml.close()

    #mi_contexto = Context(diccionario) #se usa para conectar views con Template1.html
    plantilla = loader.get_template('Template1.html')
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)