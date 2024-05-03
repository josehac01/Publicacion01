from rest_framework import serializers
from .models import Profesor

class Profesorserializer(serializers.ModelSerializer):
    class Meta:
        model=Profesor
        fields='__all__'
