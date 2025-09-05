# urls.py
from django.urls import path, include
from .views import RegistroAlumnoView, CrearProfesorView, ListaUsuariosView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registro/', RegistroAlumnoView.as_view(), name='registro_alumno'),
    path('crear-profesor/', CrearProfesorView.as_view(), name='crear_profesor'),
    path('usuarios/', ListaUsuariosView.as_view(), name='lista_usuarios'),
]