# Create your views here.
from django.shortcuts import render,  redirect

# Create your views here.
from carrito.Carrito import Carrito
from productos.models import Articulos

def tienda(request):
    productos = Articulos.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def agregar_producto(request, producto_id, pagina):
    carrito = Carrito(request)
    producto = Articulos.objects.get(id=producto_id)
    carrito.agregar(producto)
    if pagina == 'inicio':
        return redirect('inicio')
    if pagina == 'tienda':
        return redirect('Tienda')
    if pagina == 'vino':
        return redirect('listVinos')
    if pagina == 'whisky':
        return redirect('listWhiskys')
    if pagina == 'gin':
        return redirect('listGins')
    if pagina == 'gaseosas':
        return redirect('listGaseosas')
    if pagina == 'otos':
        return redirect('listOtros')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Articulos.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Articulos.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")