from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('<h1> CRUD personajes de Rick and Morty </h1>')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')


# Create your views here.
