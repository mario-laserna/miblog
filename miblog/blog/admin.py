from django.contrib import admin
from blog.models import Entrada
from blog.models import Comentario

admin.site.register(Entrada)
admin.site.register(Comentario)