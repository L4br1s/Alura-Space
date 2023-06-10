from django.urls import path
from Apps.galeria.views import index, imagem, buscar, nova_imagem,\
    editar_imagem, deletar_imagem, filtro
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar', buscar, name='buscar'),
    path('nova_imagem', nova_imagem, name='nova_imagem'),
    path('editar_imagem/<int:foto_id>', editar_imagem , name='editar_imagem'),
    path('deletar_imagem/<int:foto_id>',deletar_imagem, name='deletar_imagem'),
    path('filtro/<str:categoria>', filtro, name='filtro'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)