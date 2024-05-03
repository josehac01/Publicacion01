from django.urls import path,include
from rest_framework import routers
from .views import ProfesorViewSet

ruta=routers.DefaultRouter()
ruta.register('profesor',ProfesorViewSet)

urlpatterns = [
    path('',include(ruta.urls)),
]