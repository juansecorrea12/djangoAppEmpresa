from rest_framework.serializers import ModelSerializer

from permisos.models import Permisos

class PermisosSerializer(ModelSerializer):
    class Meta:
        model = Permisos
        fields = ('__all__')