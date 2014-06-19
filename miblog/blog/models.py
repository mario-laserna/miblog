from django.db import models

class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.titulo