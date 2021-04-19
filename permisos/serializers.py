from rest_framework.serializers import ModelSerializer

from permisos.models import Permisos
from empleados.serializers import EmpleadosSerializer

class PermisosSerializer(ModelSerializer):
    class Meta:
        model = Permisos
        fields = ('__all__')
        
class DetailPermisosSerializer(ModelSerializer):
    empleados = EmpleadosSerializer()
    class Meta:
        model = Permisos
        fields = ('__all__')