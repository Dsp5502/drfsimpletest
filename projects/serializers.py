from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project # Este es el modelo que se va a serializar
        fields = '__all__' # Esto son los cmapos que se van a serializar
        read_only_fields = ('created_at', ) # Esto son los campos que no  se van a poder editar
        
