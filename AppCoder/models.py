from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()

    def __str__(self):
        return self.nombre
    
    class Meta():
        ordering = ("nombre", "camada")

class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(null=True)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

class Profesor(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    profesion = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

class Entregable(models.Model):

    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="Avatares", blank=True, null=True)