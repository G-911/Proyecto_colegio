from django.contrib import admin
from .models import Usuario
from django.contrib.auth.models import Group

# Register your models here.

admin.site.register(Usuario)

Group.objects.get_or_create(name='Administradores')
Group.objects.get_or_create(name='Profesores')
Group.objects.get_or_create(name='Alumnos')
