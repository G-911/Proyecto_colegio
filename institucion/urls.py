from django.urls import path
from .views import (
    ColegioView, ListaComunicadosView,
    CargoDirectivoListView, CargoDirectivoCreateView,
    PersonalDirectivoListView, PersonalDirectivoCreateView,
    NivelEducativoListView, NivelEducativoCreateView,
    HomePageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('colegio/', ColegioView.as_view(), name='colegio_info'),
    path('comunicados/', ListaComunicadosView.as_view(), name='comunicados'),
    path('cargos/', CargoDirectivoListView.as_view(), name='cargo_list'),
    path('cargos/nuevo/', CargoDirectivoCreateView.as_view(), name='cargo_create'),
    path('directivos/', PersonalDirectivoListView.as_view(), name='directivo_list'),
    path('directivos/nuevo/', PersonalDirectivoCreateView.as_view(), name='directivo_create'),
    path('niveles/', NivelEducativoListView.as_view(), name='nivel_list'),
    path('niveles/nuevo/', NivelEducativoCreateView.as_view(), name='nivel_create'),

]