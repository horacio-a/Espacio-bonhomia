from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import login_request, register, EditarPerfil, Perfil, EditarPerfilImage

urlpatterns = [
    path('login/', login_request, name='login_request'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', Perfil, name='profile'),
    path('profile/editar', EditarPerfil, name='Editarprofile'),
    path('profile/editarimage', EditarPerfilImage, name='Editarprofile')
]
