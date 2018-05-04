from django.db import models

# Create your models here.
class Museo(models.Model):
    nombre = models.CharField(max_length=128)
    distrito = models.CharField(max_length=128)
    url = models.URLField(max_length=200)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=128)
    museos = models.ManyToManyField(Museo)
    letra = models.CharField(max_length=64)
    color = models.CharField(max_length=32)
    def __str__(self):
        return self.nombre

class Comentario(models.Model):
    texto = models.TextField(null=True, blank=True)
    usuario = models.ForeignKey(Usuario)
    museo = models.ForeignKey(Museo)
    def __str__(self):
        return self.texto
