from django.views.generic import TemplateView ,DetailView, ListView, CreateView
from .models import Colegio, Comunicado, CargoDirectivo, PersonalDirectivo, NivelEducativo
from .forms import CargoDirectivoForm, PersonalDirectivoForm, NivelEducativoForm
from django.urls import reverse_lazy
from .mixins import SoloAdminMixin, SoloLecturaMixin, SoloProfesorOMasMixin

class HomePageView(TemplateView):
    template_name = 'home.html'


class ColegioView(DetailView, SoloLecturaMixin):
    model = Colegio
    template_name = 'institucion/colegio.html'


class ListaComunicadosView(ListView):
    model = Comunicado
    template_name = 'institucion/comunicados.html'
    context_object_name = 'comunicados'


# Cargo Directivo
class CargoDirectivoListView(ListView, SoloProfesorOMasMixin):
    model = CargoDirectivo
    template_name = 'institucion/listas/cargo_list.html'


class CargoDirectivoCreateView(CreateView, SoloAdminMixin):
    model = CargoDirectivo
    form_class = CargoDirectivoForm
    template_name = 'institucion/cargo_form.html'
    success_url = reverse_lazy('cargo_list')


# Personal Directivo
class PersonalDirectivoListView(ListView):
    model = PersonalDirectivo
    template_name = 'institucion/listas/directivo_list.html'


class PersonalDirectivoCreateView(CreateView):
    model = PersonalDirectivo
    form_class = PersonalDirectivoForm
    template_name = 'institucion/forms/directivo_form.html'
    success_url = reverse_lazy('directivo_list')


# Nivel Educativo
class NivelEducativoListView(ListView):
    model = NivelEducativo
    template_name = 'institucion/listas/nivel_list.html'

class NivelEducativoCreateView(CreateView):
    model = NivelEducativo
    form_class = NivelEducativoForm
    template_name = 'institucion/forms/nivel_form.html'
    success_url = reverse_lazy('nivel_list')

