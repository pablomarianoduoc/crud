from django.shortcuts import render, redirect
from .models import Alumno

# Create your views here.

def home(request):
    alumnosListados = Alumno.objects.all()
    return render(request, "gestionAlumnos.html", {"alumnos": alumnosListados})

def registrarAlumno(request):
    rut=request.POST['txtRut']
    nombre=request.POST['txtNombre']

    alumno = Alumno.objects.create(rut=rut, nombre=nombre)
    return redirect('/')

def eliminacionAlumno(request, rut):
    alumno = Alumno.objects.get(rut=rut)
    alumno.delete()

    return redirect('/')