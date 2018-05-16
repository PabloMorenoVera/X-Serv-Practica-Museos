from django.contrib import admin

# Register your models here.
from .models import Museo, Usuario, Comentario, Favorito

admin.site.register(Museo)
admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Favorito)
