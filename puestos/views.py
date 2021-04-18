from django.shortcuts import render

from rest_framework.views import APIView
from puestos.models import Puestos
from rest_framework.response import Response
from puestos.serializers import PuestosSerializers
from django.core.exceptions import ObjectDoesNotExist

class ViewPuestos(APIView):
    
    def get(self, request):
        puestos = Puestos.objects.all()
        serialized = PuestosSerializers(puestos, many=True)

        return Response(
            status=200,
            data=serialized.data
        )
    
    def post(self, request):
        serialized = PuestosSerializers(data=request.data)
        if not serialized.is_valid():
            return Response(
                status=400,
                data=serialized.errors
            )

        serialized.save()
        return Response(status=201)
    

class DetailView(APIView):

    def get(self, request, puestos_id):
        try:
            detailPuesto = Puestos.objects.get(id=puestos_id)
        except ObjectDoesNotExist:
            return Response(status=404)

        if request.method == 'GET':
            serialized = PuestosSerializers(detailPuesto)

            return Response(
            status=200,
            data=serialized.data
            )

    def delete(self, request, puestos_id):
        try:
            detailPuesto = Puestos.objects.get(id=puestos_id)
        except ObjectDoesNotExist:
            return Response(status=404)
        
        detailPuesto.delete()
        return Response(
            status=204
        )
     
    def put(self, request, puestos_id, format=None):
        try:
            detailPuesto = Puestos.objects.get(id=puestos_id)
        except ObjectDoesNotExist:
            return Response(status=404)
        
        
        serialized = PuestosSerializers(
            instance = detailPuesto,
            data=request.data
        )
        if not serialized.is_valid():
            return Response(
                status=400,
                data=serialized.errors
            )
        serialized.save()
        return Response(status=200)
            
    
