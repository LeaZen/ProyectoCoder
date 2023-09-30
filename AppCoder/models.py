from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField(blank=True, null=True)
    imagen = models.ImageField(upload_to="jpgcursos/", blank=True, null=True)
    requisitos = models.TextField(blank=True, null=True)
    duracion = models.CharField(max_length=50, blank=True, null=True)
    detalles = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
    class Meta():
        ordering = ("nombre", "camada")

class Estudiante(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    imagen = models.ImageField(upload_to="jpgestudiante/", blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

class Profesor(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(null=True)
    materia = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="jpgprofesores/", blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"

class Entregable(models.Model):

    nombre = models.CharField(max_length=50)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="Avatares", blank=True, null=True)