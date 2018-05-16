from django.db import models

# Create your models here.
class Museo(models.Model):
    ID_ENTIDAD = models.TextField()
    NOMBRE = models.TextField()
    DESCRIPCION = models.TextField()
    HORARIO = models.TextField()
    TRANSPORTE = models.TextField()
    ACCESIBILIDAD = models.TextField()
    CONTENT_URL = models.URLField(max_length=200)
    NOMBRE_VIA = models.TextField()
    CLASE_VIAL = models.TextField()
    TIPO_NUM = models.TextField()
    NUM = models.TextField()
    LOCALIDAD = models.TextField()
    PROVINCIA = models.TextField()
    CODIGO_POSTAL = models.TextField()
    BARRIO = models.TextField()
    DISTRITO = models.TextField()
    COORDENADA_X = models.TextField()
    COORDENADA_Y = models.TextField()
    LATITUD = models.TextField()
    LONGITUD = models.TextField()
    TELEFONO = models.TextField()
    FAX = models.TextField()
    EMAIL = models.TextField()
    def __str__(self):
        return self.NOMBRE

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
        return self.museo.NOMBRE + " - " + self.usuario.nombre

class Comentario(models.Model):
    texto = models.TextField(null=True, blank=True)
    museo = models.ForeignKey(Museo)
    def __str__(self):
        return self.texto
