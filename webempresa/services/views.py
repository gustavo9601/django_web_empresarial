from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

# Create your views here.
from .models import Service


def services(request: WSGIRequest):
    services = Service.objects.all()
    return render(request=request, template_name='services/services.html', context={'services': services})
