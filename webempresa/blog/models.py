from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')
    updated_at = models.DateField(auto_now=True, verbose_name='Fecha actualizacion')

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Titulo')
    content = models.TextField(verbose_name='Contenido')
    published_at = models.DateTimeField(verbose_name='Fecha de publicacion', default=timezone.now)
    image = models.ImageField(verbose_name='Imagen', upload_to='blog', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha creacion')
    updated_at = models.DateField(auto_now=True, verbose_name='Fecha actualizacion')
    #  Campos con relaciones a otros modelos
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE,
                               related_name='get_author')  # muchos a uno
    categories = models.ManyToManyField(Category, verbose_name='Categorias',
                                        related_name='get_posts')  # relacion muchos a muchos

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'Entradas'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
