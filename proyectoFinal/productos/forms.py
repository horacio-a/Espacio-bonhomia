import email
from django import forms

class Formulario_productos(forms.Form):
    name = forms.CharField(max_length=40)
    price = forms.FloatField()
    description = forms.CharField(max_length=200)
    marca = forms.CharField(max_length=40)
    categoria = forms.CharField(max_length=40)
    stock = forms.IntegerField()
    image = forms.ImageField(required=False)



class Formulario_marca(forms.Form):
    name = forms.CharField(max_length=40)
    email = forms.CharField(max_length=40)
    description = forms.CharField(max_length=1000)


class Formulario_Sucursales(forms.Form):
    direction = forms.CharField(max_length=40)
    cantidadEmpleados = forms.IntegerField()

