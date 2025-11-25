from django.urls import path
from .views import ListaFotos, CrearFoto, EditarFoto, BorrarFoto

urlpatterns = [
    path('fotos/', ListaFotos.as_view(), name='fotos'),
    path('fotos/crear/', CrearFoto.as_view(), name='foto_crear'),
    path('fotos/<int:pk>/editar/', EditarFoto.as_view(), name='foto_editar'),
    path('fotos/<int:pk>/borrar/', BorrarFoto.as_view(), name='foto_borrar'),
]
