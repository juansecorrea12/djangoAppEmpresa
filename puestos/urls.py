from django.urls import path

from puestos.views import ViewPuestos, DetailView

app_name = 'puestos'
urlpatterns = [
    path('', ViewPuestos.as_view()),
    path('<int:puestos_id>/', DetailView.as_view())
]