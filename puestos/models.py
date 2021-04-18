from django.db import models


class Puestos(models.Model):
    nombre_cargo = models.CharField(max_length=100)
    salario_cargo = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=100)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
