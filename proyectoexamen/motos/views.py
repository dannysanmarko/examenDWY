from django.shortcuts import render
from django.urls import path

# Create your views here.

def home(request):
    return render(request, "portada.html")
def galeria(request):
    return render(request, "galeria.html")
def categoria(request):
    return render(request, "categoria.html")
def somos(request):
    return render(request, "somos.html")
def cotizar(request):
    return render(request, "cotizar.html")

