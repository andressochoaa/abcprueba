from django.shortcuts import render
from django.http import HttpResponse
from .models import Personaje

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def personajes(request):
    personajes = Personaje.objects.all()
    return render(request, 'personajes/index.html', {'personajes': personajes})
def crear(request):
    return render(request, 'personajes/crear.html')


def editar(request):
    return render(request, 'personajes/editar.html')

# Create your views here.
