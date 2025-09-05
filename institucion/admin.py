from django.contrib import admin
from .models import Colegio, CalendarioEscolar, Comunicado

admin.site.register(Colegio)
admin.site.register(CalendarioEscolar)
admin.site.register(Comunicado)