from django.db import models

class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.titulo
