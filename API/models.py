from django.db import models

# Create your models here.
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    dni=models.CharField(max_length=10)
    distrito=models.CharField(max_length=30)

