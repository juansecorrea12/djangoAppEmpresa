from django.urls import path

from empleados.views import EmpleadosViewSet
# ViewEmpleados, DetailView,
from rest_framework.routers import DefaultRouter

# app_name = 'empleados'
# urlpatterns = [
#     path('', ViewEmpleados.as_view()),
#     path('<int:empleado_id>/', DetailView.as_view())
# ]

router = DefaultRouter()
router.register('', EmpleadosViewSet)

urlpatterns = router.urls