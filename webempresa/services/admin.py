from django.contrib import admin
from .models import Service


# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    # Definiendo que son solo campos de lectura
    readonly_fields = ('created_at', 'updated_at')


# Registrando el modelo y su configuracion para administracion en el dashboard admin
admin.site.register(Service, ServiceAdmin)
