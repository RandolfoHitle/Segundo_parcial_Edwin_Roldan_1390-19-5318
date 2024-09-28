from django.contrib import admin
from .models import Profesor, Mascota

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['cedula', 'nombre', 'apellido', 'genero']
    search_fields = ['nombre', 'apellido']

@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ['id_mascota', 'nombre', 'raza', 'genero', 'cedula']
    search_fields = ['nombre', 'raza']
    list_filter = ['genero', 'cedula']
