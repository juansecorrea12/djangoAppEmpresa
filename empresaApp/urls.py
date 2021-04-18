
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('empleados/', include('empleados.urls')),
    path('permisos/', include('permisos.urls')),
    path('puestos/', include('puestos.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
