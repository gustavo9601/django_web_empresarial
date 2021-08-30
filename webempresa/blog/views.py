from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def blog(request: WSGIRequest) -> HttpResponse:
    posts = Post.objects.all()
    return render(request=request, template_name='blog/blog.html', context={'posts': posts})


def category(request: WSGIRequest, category_id: int) -> HttpResponse:
    # category = Category.objects.get(id=category_id)

    # Usando el manejador de error 404 de django
    category = get_object_or_404(Category, id=category_id)
    
    # posts = Post.objects.filter(categories=category)
    return render(request, 'blog/category.html', context={'category': category})
