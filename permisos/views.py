from django.shortcuts import render

from rest_framework.views import APIView
from permisos.models import Permisos
from rest_framework.response import Response
from permisos.serializers import PermisosSerializer, DetailPermisosSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets

class ViewPermisos(APIView):
    
    def get(self, request):
        permisos = Permisos.objects.all()
        serialized = PermisosSerializer(permisos, many=True)

        return Response(
            status=200,
            data=serialized.data
        )
    
    def post(self, request):
        serialized = PermisosSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(
                status=400,
                data=serialized.errors
            )

        serialized.save()
        return Response(status=201)
    

class DetailView(APIView):

    def get(self, request, permiso_id):
        try:
            detailEmpleado = Permisos.objects.get(id=permiso_id)
        except ObjectDoesNotExist:
            return Response(status=404)

        if request.method == 'GET':
            serialized = PermisosSerializer(detailEmpleado)

            return Response(
            status=200,
            data=serialized.data
            )

    def delete(self, request, permiso_id):
        try:
            detailPermiso = Permisos.objects.get(id=permiso_id)
        except ObjectDoesNotExist:
            return Response(status=404)
        
        detailPermiso.delete()
        return Response(
            status=204
        )
     
    def put(self, request, permiso_id, format=None):
        try:
            detailPermiso = Permisos.objects.get(id=permiso_id)
        except ObjectDoesNotExist:
            return Response(status=404)
        
        
        serialized = PermisosSerializer(
            instance = detailPermiso,
            data=request.data
        )
        if not serialized.is_valid():
            return Response(
                status=400,
                data=serialized.errors
            )
        serialized.save()
        return Response(status=200)
            

class PermisosViewSet(viewsets.ModelViewSet):
    queryset = Permisos.objects.all()
    serializer_class = PermisosSerializer()
    
    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'retrieve':
            return DetailPermisosSerializer
        return PermisosSerializer