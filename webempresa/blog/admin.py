from django.contrib import admin
from .models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    # mostrar en la tabla las columnas
    # list_categories // campo personalizado con la funcion
    list_display = ('title', 'author', 'published_at', 'list_categories')
    # ordenamiento
    ordering = ('author', 'published_at')
    # busqueda por algun campo
    # author__username // modelo__campo // como es una relacion
    search_fields = ('title','content','author__username', 'categories__name')
    # generador de gerarquias
    date_hierarchy = 'published_at'
    # muestra un filtro
    # author__username // modelo__campo // como es una relacion
    list_filter = ('author__username', 'categories__name')

    # funcion que se ejecutara por cada registro, y en obj retornara la row
    def list_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all()])
    # añadiendo a la funcion la propiedad de nombre, para reflejar el titulo en la tabla
    list_categories.short_description= "Categorias"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
