# examen_final/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

# examen_final/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/fotos/')), 
    path('cuentas/', include('cuentas.urls')), 
    path('fotos/', include('galeria.urls')), # Esto es correcto
]

# ESTO SOLO FUNCIONA EN LOCAL (settings.DEBUG = True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)