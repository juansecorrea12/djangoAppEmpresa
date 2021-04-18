from django.db import models
from puestos.models import Puestos


class Empleados(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    correo = models.CharField(max_length=300)
    telefono = models.CharField(max_length=50)
    ano_antiguedad = models.IntegerField()
    puestos = models.ForeignKey(
        Puestos,
        related_name='puestos',
        on_delete=models.SET_NULL,
        null=True
    )
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
