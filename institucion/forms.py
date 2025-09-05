from django import forms
from .models import CargoDirectivo, PersonalDirectivo, NivelEducativo
from django.contrib.auth import get_user_model

User = get_user_model()

class CargoDirectivoForm(forms.ModelForm):
    class Meta:
        model = CargoDirectivo
        fields = ['nombre', 'descripcion']

class PersonalDirectivoForm(forms.ModelForm):
    class Meta:
        model = PersonalDirectivo
        fields = ['usuario', 'cargo', 'fecha_inicio', 'activo']

class NivelEducativoForm(forms.ModelForm):
    class Meta:
        model = NivelEducativo
        fields = ['nombre', 'descripcion', 'orden']