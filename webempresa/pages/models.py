from django.db import models


class Page(models.Model):
    title = models.CharField(verbose_name='Titulo', max_length=200)
    content = models.TextField(verbose_name='Contenido', max_length=200)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'pagina'
        verbose_name_plural = 'paginas'
        ordering = ['-created_at']

    def __str__(self):
        return self.title