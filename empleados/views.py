from django.shortcuts import render

from rest_framework.views import APIView
from empleados.models import Empleados
from rest_framework.response import Response
from empleados.serializers import EmpleadosSerializer, DetailEmpleadosSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


# class ViewEmpleados(APIView):
    
#     def get(self, request):
#         empleados = Empleados.objects.all()
#         serialized = EmpleadosSerializer(empleados, many=True)

#         return Response(
#             status=200,
#             data=serialized.data
#         )
    
#     def post(self, request):
#         serialized = EmpleadosSerializer(data=request.data)
#         if not serialized.is_valid():
#             return Response(
#                 status=400,
#                 data=serialized.errors
#             )

#         serialized.save()
#         return Response(status=201)
    

# class DetailView(APIView):

#     def get(self, request, empleado_id):
#         try:
#             detailEmpleado = Empleados.objects.get(id=empleado_id)
#         except ObjectDoesNotExist:
#             return Response(status=404)

#         if request.method == 'GET':
#             serialized = EmpleadosSerializer(detailEmpleado)

#             return Response(
#             status=200,
#             data=serialized.data
#             )

#     def delete(self, request, empleado_id):
#         try:
#             detailEmpleado = Empleados.objects.get(id=empleado_id)
#         except ObjectDoesNotExist:
#             return Response(status=404)
        
#         detailEmpleado.delete()
#         return Response(
#             status=204
#         )
     
#     def put(self, request, empleado_id, format=None):
#         try:
#             detailEmpleado = Empleados.objects.get(id=empleado_id)
#         except ObjectDoesNotExist:
#             return Response(status=404)
        
        
#         serialized = EmpleadosSerializer(
#             instance = detailEmpleado,
#             data=request.data
#         )
#         if not serialized.is_valid():
#             return Response(
#                 status=400,
#                 data=serialized.errors
#             )
#         serialized.save()
#         return Response(status=200)
    
    
    
class EmpleadosViewSet(viewsets.ModelViewSet):
    queryset = Empleados.objects.all()
    serializer_class = EmpleadosSerializer()
    permission_classes = (AllowAny,)
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailEmpleadosSerializer
        return EmpleadosSerializer