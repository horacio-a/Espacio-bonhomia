from tabnanny import verbose
from django.db import models

class Articulos(models.Model):
    name = models.CharField(max_length=40)
    price = models.FloatField()
    description = models.CharField(max_length=1000)
    stock = models.IntegerField()
    marca = models.CharField(max_length=40, blank= True)
    categoria = models.CharField(max_length=40, blank= True)
    date = models.DateField(auto_now_add=True,null=True, blank= True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    
    def __str__(self):
        return self.name
    class  Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'


class Marcas(models.Model):
    name = models.CharField(max_length=40)
    email = models.CharField(max_length=40)
    description = models.CharField(max_length=1000)

class Sucursales(models.Model):
    direction = models.CharField(max_length=40)
    cantidadEmpleados = models.IntegerField()


    