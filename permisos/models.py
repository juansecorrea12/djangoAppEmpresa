from django.db import models

from empleados.models import Empleados

class Permisos(models.Model):
    
    # Cuarto_hora = 'CH'
    # Media_hora = 'MH'
    # Hora = 'Hh'
    # Hora_media = 'HM'
    # Dos_horas = 'HH'
    
    # TIEMPOS_PERMISOS_EMPRESA = [
    #     (Cuarto_hora, 'Quince minutos'),
    #     (Media_hora, 'Media hora'),
    #     (Hora, 'Una hora'),
    #     (Hora_media, 'Una hora y media'),
    #     (Dos_horas, 'Dos horas'),
    # ]
    
    descripcion = models.CharField(max_length=200)
    Tiempos_permisos_empresa = models.CharField(
        max_length=200
        # choises=TIEMPOS_PERMISOS_EMPRESA,
        # default = Cuarto_hora
    )
    empleados = models.ForeignKey(
        Empleados,
        related_name='empleados',
        on_delete=models.SET_NULL,
        null=True
    )
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)

# def is_upperclass(self):
#         return self.Tiempos_permisos_empresa in {self.Media_hora, self.Hora}