from django.db import models
from django.contrib.auth.models import User


class Persona(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)


class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
