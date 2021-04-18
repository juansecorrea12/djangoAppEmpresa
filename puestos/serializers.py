from rest_framework.serializers import ModelSerializer

from puestos.models import Puestos

class PuestosSerializers(ModelSerializer):
    class Meta: 
        model = Puestos
        fields = ('__all__')