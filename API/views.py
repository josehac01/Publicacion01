#from django.shortcuts import render
from rest_framework import viewsets
from .models import Profesor
from .serializer import Profesorserializer

# Create your views here.

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset=Profesor.objects.all()
    serializer_class=Profesorserializer
    