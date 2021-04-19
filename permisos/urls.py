
from django.urls import path
from permisos.views import PermisosViewSet
# ViewPermisos, DetailView,
from rest_framework.routers import DefaultRouter

# app_name = 'permisos'
# urlpatterns = [
#     path('', ViewPermisos.as_view()),
#     path('<int:permiso_id>/', DetailView.as_view())
# ]

router = DefaultRouter()
router.register('', PermisosViewSet)

urlpatterns = router.urls