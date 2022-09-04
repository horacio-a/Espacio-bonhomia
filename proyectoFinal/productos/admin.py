from django.contrib import admin
from productos.models import Articulos

@admin.register(Articulos)
class Articulos_admin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock','marca' ,'categoria' ,'description', 'date', 'image']