from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home_view(request):
#     return HttpResponse("¡Hola, mundo!")

def home_view(request):
    return render(request, 'core/home.html')

def greet_view(request, name):
    return HttpResponse(f"¡Hola, {name.capitalize()}!")

def greet_view(request, name):
    if not name.isalpha():
        return HttpResponse("Nombre inválido.", status=400)
    return HttpResponse(f"¡Hola, {name.capitalize()}!")
