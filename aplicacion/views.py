from django.shortcuts import render
from django.http import HttpResponse

from .models import Curso
import datetime, random


# Create your views here.

def saludo(request):
    saludar = "Bienvenidos a la clase 10 de Django"
    return HttpResponse(saludar)

def bienvenida(request):
    hoy = datetime.datetime.now()
    saludo = f"""

    <html>
    <h1>Bienvenida Juanita</h1>
    <h2>Hoy es {hoy}</h2>
    <h3>¿Tenés frio? Tapate con el poncho de tu tío</h3>
    </html>
    """
    return HttpResponse(saludo)

def bienvenido(request, nombre, apellido):
    hoy = datetime.datetime.now()
    saludo = f"""

    <html>
    <h1>Bienvenido/a {nombre} {apellido}</h1>
    <h2>Hoy es {hoy}</h2>
    <h3>¿Tenés frio? Tapate con el poncho de tu tío</h3>
    </html>
    """
    return HttpResponse(saludo)

def bienvenido_tpl(request):
    hoy = datetime.datetime.now()
    contexto = {"fecha": hoy, "nombre": "Juanita", "apellido": "Demarchi"}
    return render (request, 'aplicacion/bienvenido.html', contexto)  

def nuevo_curso(request):
    comision = random.randint(10000, 99999)
    nombre = random.choices(['Python', 'Django', 'Java', 'JavaScript', 'C++'], k=1)
    curso = Curso(nombre=nombre, comision=comision)
    curso.save()
    return render(request, 'aplicacion/nuevo_curso.html', {'curso': nombre, 'comision': comision})

def inicio(request):
    return render(request, 'aplicacion/index.html')

