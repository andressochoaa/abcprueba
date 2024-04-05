from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

def personajes(request):
    return render(request, 'personajes/index.html')


# Create your views here.
