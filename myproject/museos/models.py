from django.db import models

# Create your models here.
class Museo(models.Model):
    nombre = models.CharField(max_length=128)
    distrito = models.CharField(max_length=128)
    accesibilidad = models.IntegerField()
    direccion = models.CharField(max_length=128)
    url = models.URLField(max_length=200)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=128)
    letra = models.CharField(max_length=64)
    color = models.CharField(max_length=32)
    #From https://stackoverflow.com/questions/7341066/can-i-make-an-admin-field-not-required-in-django-without-creating-a-form
    titulo = models.CharField(max_length=64, blank=True)
    def __str__(self):
        return self.nombre

class Favorito(models.Model):
    museo = models.ForeignKey(Museo)
    usuario = models.ForeignKey(Usuario)
    fecha = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.museo.nombre + " - " + self.usuario.nombre

class Comentario(models.Model):
    texto = models.TextField(null=True, blank=True)
    museo = models.ForeignKey(Museo)
    def __str__(self):
        return self.texto
