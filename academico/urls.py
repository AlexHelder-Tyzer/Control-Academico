from rest_framework import routers
from .api import EstudianteViewSet


route = routers.DefaultRouter()
route.register('api/estudiante', EstudianteViewSet, 'academico') # registrar la ruta de como se llama, enlazarlo, y apuntar a la aplicacion

urlpatterns = route.urls