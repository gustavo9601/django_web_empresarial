from django.contrib import admin
from .models import Link


# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

    # Permite añadir restricciones para campos en el damin
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='personal').exists():
            return ('created_at', 'updated_at', 'key', 'name')
        else:
            return ('created_at', 'updated_at')


# Registrando
admin.site.register(Link, LinkAdmin)
