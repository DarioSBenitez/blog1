from django.db import models


# Create your models here.

class Posteo(models.Model):
    nombre = models.CharField(max_length=30)
    direccionor = models.TextField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=7)

    
