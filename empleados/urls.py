from django.urls import path

from empleados.views import ViewEmpleados, DetailView

app_name = 'empleados'
urlpatterns = [
    path('', ViewEmpleados.as_view()),
    path('<int:empleado_id>/', DetailView.as_view())
]