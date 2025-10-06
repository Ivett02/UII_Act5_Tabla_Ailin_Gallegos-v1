from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=15, blank=True, null=True)

    # es para el administrador servidor admin
    def __str__(self):
        return f"{self.nombre} {self.edad}"
    