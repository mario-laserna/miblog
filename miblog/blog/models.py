from django.db import models

class Entrada(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.titulo

class Comentario(models.Model):
	fechacreacion = models.DateTimeField(auto_now_add=True)
	autor = models.CharField(max_length=100)
	mensaje = models.TextField()
	identrada = models.ForeignKey(Entrada)

	def __unicode__(self):
		return self.mensaje[:20]