from django.urls import path
from galeria.views import index, imagem, buscar
from django.conf import settings
from django.conf.urls.static import static
from usuarios.views import login, cadastro,logout

urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout',logout, name='logout')


]
