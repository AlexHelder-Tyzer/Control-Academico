from .models import Estudiante
from .serializers import EstudianteSerializer
from rest_framework import viewsets, permissions


class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all() #muestra la lista de todos los campos de la tabla
    permission_classes = [permissions.AllowAny] #nos de todos los permisos para acceder a la clase Estudiante (GET, POST, DELETE)
    serializer_class = EstudianteSerializer # DEVUELVE COMO API EN cada consulta

    