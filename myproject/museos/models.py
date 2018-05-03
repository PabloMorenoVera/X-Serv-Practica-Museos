from django.db import models

# Create your models here.
class Comentario(models.Model):
    id_museo = models.IntegerField()
    texto = models.TextField(null=True, blank=True)
    usuario = models.CharField(max_length=128)
    def __str__(self):
        return self.usuario

class Museo(models.Model):
    id_museo = models.IntegerField()
    usuario = models.CharField(max_length = 128)
    comentarios = models.ForeignKey(Comentario)
    def __str__(self):
        return self.usurio
