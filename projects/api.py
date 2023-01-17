from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # Esto es lo que se va a mostrar
    permission_classes = [
        permissions.AllowAny # Esto es para que cualquiera pueda ver los proyectos
    ]
    serializer_class = ProjectSerializer # Esto es para que se serialicen los proyectos y se muestren en el navegador