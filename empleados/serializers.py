from rest_framework.serializers import ModelSerializer

from empleados.models import Empleados
from puestos.serializers import PuestosSerializers

class EmpleadosSerializer(ModelSerializer):
    class Meta:
        model = Empleados
        fields = ('__all__')
        
class DetailEmpleadosSerializer(ModelSerializer):
    puestos = PuestosSerializers()
    class Meta:
        model = Empleados
        fields = ('__all__')