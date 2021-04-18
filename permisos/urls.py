
from django.urls import path
from permisos.views import ViewPermisos, DetailView

app_name = 'permisos'
urlpatterns = [
    path('', ViewPermisos.as_view()),
    path('<int:permiso_id>/', DetailView.as_view())
]