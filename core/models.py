from django.db import models
import django.utils.timezone

class Tarea(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(default=django.utils.timezone.now)



