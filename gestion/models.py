from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

class Usuario(AbstractUser):
    ROLES = (
        ('alumno', 'Alumno'),
        ('profesor', 'Profesor'),
        ('admin', 'Administrador'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='alumno')

    def clean(self):
        # Validación coherente con el rol
        if self.rol == 'profesor' and not self.is_staff:
            raise ValidationError("Los profesores deben tener permisos de staff.")
        if self.rol == 'admin' and not self.is_superuser:
            raise ValidationError("Los administradores deben tener permisos de superusuario.")

    def save(self, *args, **kwargs):
        # Asignación automática de permisos según el rol
        if self.rol == 'profesor':
            self.is_staff = True
            self.is_superuser = False
        elif self.rol == 'admin':
            self.is_staff = True
            self.is_superuser = True
        else:  # alumno
            self.is_staff = False
            self.is_superuser = False

        super().save(*args, **kwargs)