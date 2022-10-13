
from django.urls import path
from productos.views import inicio,listMarca, listSucursales, CrearProducto, CrearMarca, CrearSucursales, search_productos, search_marcas, EliminarProducto, EditarProducto 
from productos.views import listVinos, listWhiskys, listGins, listGaseosas, listOtros, listProducMarca, EliminarMarca
from productos.views import EditarMarca, EditarSucursales, EliminarSucursales
urlpatterns = [
    path('list-product/', inicio, name='inicio',),
    path('list-marcas/', listMarca, name='marcas',),
    path('list-sucursales/', listSucursales, name='Sucursales',),


    path('list-product/vinos', listVinos, name='listVinos' ),
    path('list-product/whisky', listWhiskys, name='listWhiskys' ),
    path('list-product/gin', listGins, name='listGins' ),
    path('list-product/gaseosas', listGaseosas, name='listGaseosas' ),
    path('list-product/otros', listOtros, name='listOtros' ),
    path('list-product/marca/<str:pk>', listProducMarca, name='listProducMarca' ),


    path('create-product/', CrearProducto, name='CrearProducto'),
    path('create-marcas/', CrearMarca, name='CrearMarca'),
    path('create-sucursales/', CrearSucursales, name='Crearsucursales'),


    path('delete-producto/<int:pk>', EliminarProducto, name='EliminarProducto'),
    path('delete-marca/<int:pk>', EliminarMarca, name='EliminarMarca'),
    path('delete-sucursales/<int:pk>', EliminarSucursales, name='EliminarSucursales'),


    path('uptade-producto/<int:pk>', EditarProducto, name= 'EditarProducto'),
    path('uptade-marca/<int:pk>', EditarMarca, name= 'EditarMarca'),
    path('uptade-sucursales/<int:pk>', EditarSucursales, name= 'EditarSucursales'),


    path('search-productos/', search_productos, name='search_productos'),
    path('search-marcas/', search_marcas, name='search_marcas'),
]
