from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Profesor)
class Registrar(admin.ModelAdmin):
    list_display=('nombre','dni','distrito')
    list_filter=('dni')
