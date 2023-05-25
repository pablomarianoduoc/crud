from django.db import models

# Create your models here.

class Alumno(models.Model):
    rut = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=60)
