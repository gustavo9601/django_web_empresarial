from django.core.handlers.wsgi import WSGIRequest
from .models import Link

def context_dict(request: WSGIRequest):
    context = {}
    links = Link.objects.all()
    for link in links:
        context[link.key] = link.url
    return context
