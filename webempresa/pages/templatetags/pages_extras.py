from django import template
from pages.models import Page

register = template.Library()

# Registrando en los tags globales de django para ser accesible desde las vistas
@register.simple_tag
def get_page_list():
    return Page.objects.all()
