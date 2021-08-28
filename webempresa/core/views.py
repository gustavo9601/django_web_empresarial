from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, HttpResponse


# Create your views here.

def home(request: WSGIRequest):
    print(type(request))
    return HttpResponse('Inicio')


def about(request: WSGIRequest):
    return HttpResponse('Inicio')


def services(request: WSGIRequest):
    return HttpResponse('Inicio')


def store(request: WSGIRequest):
    return HttpResponse('Inicio')


def contact(request: WSGIRequest):
    return HttpResponse('Inicio')


def blog(request):
    return HttpResponse('Inicio')


def sample(request):
    return HttpResponse('Inicio')
