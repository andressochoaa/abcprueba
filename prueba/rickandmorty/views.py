from django.shortcuts import render
from django.http import HttpResponse
from .models import Personaje
from .forms import PersonajeForm

def inicio(request):
    return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def personajes(request):
    personajes = Personaje.objects.all()
    return render(request, 'personajes/index.html', {'personajes': personajes})
def crear(request):
    formulario = PersonajeForm(request.POST or None)
    return render(request, 'personajes/crear.html', {'formulario': formulario})


def editar(request):
    return render(request, 'personajes/editar.html')

# Create your views here.
