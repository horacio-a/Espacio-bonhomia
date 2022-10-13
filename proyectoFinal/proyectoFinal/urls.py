from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import inicio
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', inicio, name ='inicio'),
    path('admin/', admin.site.urls),
    path('productos/',include('productos.urls')),
    path('users/',include('users.urls')),
    path('carrito/',include('carrito.urls')),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
