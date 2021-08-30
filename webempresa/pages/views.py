from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404
from .models import Page


def page(request: WSGIRequest, page_id: int):
    page = get_object_or_404(Page, id=page_id)
    return render(request=request, template_name='pages/sample.html', context={'page': page})
