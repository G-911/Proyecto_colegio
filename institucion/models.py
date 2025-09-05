from django.db import models
from django.contrib.auth import get_user_model

class Colegio(models.Model):
    nombre = models.CharField(max_length=100)
    lema = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField(blank=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    sitio_web = models.URLField(blank=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class CalendarioEscolar(models.Model):
    titulo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo


class Comunicado(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    

User = get_user_model()


class CargoDirectivo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class PersonalDirectivo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    cargo = models.ForeignKey(CargoDirectivo, on_delete=models.SET_NULL, null=True)
    fecha_inicio = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.usuario.get_full_name()} - {self.cargo.nombre}"


class NivelEducativo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    orden = models.PositiveIntegerField(help_text="Orden jerárquico (ej. 1 para preescolar, 2 para primaria...)")

    def __str__(self):
        return self.nombre
