
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Foto
from django.urls import reverse_lazy

class ListaFotos(ListView):
    model = Foto
    template_name = 'fotos_listado.html'

class CrearFoto(CreateView):
    model = Foto
    fields = ['titulo', 'imagen']
    template_name = 'fotos_form.html'
    success_url = reverse_lazy('fotos')

class EditarFoto(UpdateView):
    model = Foto
    fields = ['titulo', 'imagen']
    template_name = 'fotos_form.html'
    success_url = reverse_lazy('fotos')

class BorrarFoto(DeleteView):
    model = Foto
    template_name = 'fotos_borrar.html'
    success_url = reverse_lazy('fotos')
