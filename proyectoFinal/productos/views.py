
from difflib import Match
from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from productos.models import Articulos, Marcas, Sucursales
from django.contrib.auth.decorators import login_required

from productos.forms import Formulario_productos, Formulario_marca, Formulario_Sucursales


def inicio(request):
    productos = Articulos.objects.all().order_by('categoria')
    context = {
        'productos': productos
    }
    return render(request, 'productos/inicio.html', context=context);


def listVinos(request):
    productos = Articulos.objects.filter(categoria__icontains = 'vino')
    context = {
        'productos': productos
    }
    
    return render(request, 'productos/list_vino.html', context=context)

def listWhiskys(request):
    productos = Articulos.objects.filter(categoria = 'whisky')
    context = {
        'productos': productos
    }
    return render(request, 'productos/list_whisky.html', context=context)


def listGins(request):
    productos = Articulos.objects.filter(categoria = 'gin')
    context = {
        'productos': productos
    }
    
    return render(request, 'productos/list_gin.html', context=context)

def listGaseosas(request):
    productos = Articulos.objects.filter(categoria = 'gaseosas')
    context = {
        'productos': productos
    }
    
    return render(request, 'productos/list_gaseosas.html', context=context)

def listOtros(request):
    productos = Articulos.objects.filter(categoria  = 'otros')
    context = {
        'productos': productos
    }
    
    return render(request, 'productos/list_otros.html', context=context)         

def listProducMarca(request, pk):
    productos = Articulos.objects.filter(marca  = pk)
    context = {
        'pk': pk,
        'productos': productos
    }
    
    return render(request, 'productos/list_producmarca.html', context=context)         


def listMarca(request):
    marcas = Marcas.objects.all()
    context = {
        'marcas': marcas
    }
    return render(request, 'productos/listMarca.html', context=context);


def listSucursales(request):
    sucursales = Sucursales.objects.all()
    context = {
        'sucursales': sucursales
    }
    return render(request, 'productos/listSucursales.html', context=context);




@login_required
def CrearProducto(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_productos(request.POST, request.FILES)

            if form.is_valid():
                Articulos.objects.create(
                    name = form.cleaned_data['name'],
                    price = form.cleaned_data['price'],
                    description = form.cleaned_data['description'],
                    marca = form.cleaned_data['marca'],
                    categoria = form.cleaned_data['categoria'],
                    stock = form.cleaned_data['stock'],
                    image = form.cleaned_data['image']
                )
            return redirect(inicio)
        elif request.method == 'GET':
            form = Formulario_productos()
            context = {'form':form}
            return render(request, 'productos/crearProducto.html', context=context)
    else:
        return redirect(inicio)

@login_required
def EliminarProducto(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'GET':
            productos = Articulos.objects.get(pk = pk)
            context = {
            'productos': productos
            }
            return render(request, 'productos/deleteProduct.html', context=context)
        elif request.method == 'POST':
            productos = Articulos.objects.get(pk=pk)
            productos.delete()
            return redirect(inicio)
    else:
        return redirect(inicio)

@login_required
def EditarProducto(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_productos(request.POST, request.FILES)
            if form.is_valid():
                productos = Articulos.objects.get(id=pk)
                productos.name = form.cleaned_data['name']
                productos.price = form.cleaned_data['price']
                productos.marca = form.cleaned_data['marca']
                productos.categoria = form.cleaned_data['categoria']
                productos.description = form.cleaned_data['description']
                productos.stock = form.cleaned_data['stock']
                productos.image = form.cleaned_data['image']


                productos.save()
                return redirect(inicio)


        elif request.method == 'GET':
            productos = Articulos.objects.get(id=pk)

            form = Formulario_productos(initial={'name':productos.name, 'price':productos.price,'marca':productos.marca,'categoria':productos.categoria,'description':productos.description,'stock':productos.stock,})
            context = {'form': form}
            return render(request, 'productos/update_products.html', context=context)
    else:
        return redirect(inicio)

def search_productos(request):

    search = request.GET['search-productos']
    productos = Articulos.objects.filter(name__icontains= search)
    context = {
        'productos': productos
    }
    
    return render(request, 'productos/searchProductos.html', context=context)




@login_required
def CrearMarca(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_marca(request.POST)

            if form.is_valid():
                Marcas.objects.create(
                    name = form.cleaned_data['name'],
                    description = form.cleaned_data['description'],
                    email = form.cleaned_data['email']
                )
                
                return redirect(listMarca)

        elif request.method == 'GET':
            form = Formulario_marca()
            context = {'form':form}
            return render(request, 'productos/crearMarca.html', context=context);
    else:
        return redirect(inicio) 

@login_required
def EliminarMarca(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'GET':
            marcas =Marcas.objects.get(pk = pk )
            context = {
            'marcas': marcas
            }
            return render(request, 'productos/deleteMarca.html', context=context)
        elif request.method == 'POST':
            marcas = Marcas.objects.get(pk=pk)
            marcas.delete()
            return redirect(listMarca)
    else:
        return redirect(listMarca)

@login_required
def EditarMarca(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_marca(request.POST)
            if form.is_valid():
                marcas = Marcas.objects.get(id=pk)
                marcas.name = form.cleaned_data['name']
                marcas.email = form.cleaned_data['email']
                marcas.description = form.cleaned_data['description']
                marcas.save()
                return redirect(listMarca)


        elif request.method == 'GET':
            marcas = Marcas.objects.get(id=pk)

            form = Formulario_marca(initial={'name': marcas.name, 'email': marcas.email,'description': marcas.description })
            context = {'form': form}
            return render(request, 'productos/update_marcas.html', context=context)
    else:
        return redirect(listMarca)

def search_marcas(request):
    search = request.GET['search-marcas']
    marcas = Marcas.objects.filter(name__icontains= search)
    context = {
        'marcas': marcas
    }
    
    return render(request, 'productos/searchMarcas.html', context=context)



@login_required
def CrearSucursales(request):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_Sucursales(request.POST)

            if form.is_valid():
                Sucursales.objects.create(
                    direction = form.cleaned_data['direction'],
                    cantidadEmpleados = form.cleaned_data['cantidadEmpleados'],
                )
                
                return redirect(listSucursales)

        elif request.method == 'GET':
            form = Formulario_Sucursales()
            context = {'form':form}
            return render(request, 'productos/crearSucursal.html', context=context);
        return render(request, 'productos/crearSucursal.html');
    else:
        return redirect(inicio)

@login_required
def EliminarSucursales(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'GET':
            sucursales = Sucursales.objects.get(id=pk)
            context = {
            'sucursales': sucursales
            }
            return render(request, 'productos/deleteSucursales.html', context=context)
        elif request.method == 'POST':
            sucursales = Sucursales.objects.get(id=pk)
            sucursales.delete()
            return redirect(listSucursales)
    else:
        return redirect(listSucursales)

@login_required
def EditarSucursales(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        if request.method == 'POST':
            form = Formulario_Sucursales(request.POST)
            if form.is_valid():
                sucursales = Sucursales.objects.get(id=pk)
                sucursales.direction = form.cleaned_data['direction']
                sucursales.cantidadEmpleados = form.cleaned_data['cantidadEmpleados']
                sucursales.save()
                return redirect(listSucursales)


        elif request.method == 'GET':
            sucursales = Sucursales.objects.get(id=pk)

            form = Formulario_Sucursales(initial={'direction': sucursales.direction, 'cantidadEmpleados': sucursales.cantidadEmpleados, })
            context = {'form': form}
            return render(request, 'productos/update_sucursales.html', context=context)
    else:
        return redirect(listSucursales)





