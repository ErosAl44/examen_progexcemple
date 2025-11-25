from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/fotos/')),  # redirige la raíz a /fotos/
    path('', include('cuentas.urls')),
    path('', include('galeria.urls')),
]
