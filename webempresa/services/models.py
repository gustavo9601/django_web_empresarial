from django.db import models


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitulo')
    content = models.TextField(verbose_name='Contenido')
    image = models.ImageField(verbose_name='Imagen',
                              upload_to='services')  # upload_to='services' // especifica la carpeta a subir
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    # Configuracion general del modelo y para el admin dashboard
    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created_at']  # descendente

    def __str__(self):
        return self.title
