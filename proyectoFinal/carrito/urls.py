from django.urls import path
from django.urls import include
from .views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, tienda


urlpatterns = [
        path('', tienda, name="Tienda"),
    path('agregar/<int:producto_id>/<str:pagina>', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),


]
