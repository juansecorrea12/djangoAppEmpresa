from rest_framework.serializers import ModelSerializer

from empleados.models import Empleados

class EmpleadosSerializer(ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('__all__')