from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


# Create your views here.

def home(request: WSGIRequest):
    return render(request=request, template_name='core/home.html')


def about(request: WSGIRequest):
    return render(request=request, template_name='core/about.html')


def store(request: WSGIRequest):
    return render(request=request, template_name='core/store.html')


def contact(request: WSGIRequest):
    return render(request=request, template_name='core/contact.html')

def sample(request):
    return render(request=request, template_name='core/sample.html')
