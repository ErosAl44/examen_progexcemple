

# galeria/urls.py (SOLUCIÓN)
from django.urls import path
from .views import ListaFotos, CrearFoto, EditarFoto, BorrarFoto

urlpatterns = [
    path('', ListaFotos.as_view(), name='inicio_galeria'), # La URL /fotos/
    path('crear/', CrearFoto.as_view(), name='foto_crear'), # La URL /fotos/crear/
    path('<int:pk>/editar/', EditarFoto.as_view(), name='foto_editar'), # La URL /fotos/1/editar/
    path('<int:pk>/borrar/', BorrarFoto.as_view(), name='foto_borrar'), # La URL /fotos/1/borrar/
]
# Eliminamos la línea path('fotos/', ListaFotos.as_view(), name='fotos')