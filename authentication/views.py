from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from gestion.models import Usuario  # si tu modelo personalizado está en gestion
from .forms import RegistroAlumnoForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class SignupView(CreateView):
    model = Usuario
    form_class = RegistroAlumnoForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.rol = 'alumno'
        usuario.set_password(form.cleaned_data['password1'])
        usuario.save()

        grupo, _ = Group.objects.get_or_create(name='alumno')
        usuario.groups.add(grupo)

        messages.success(self.request, "Registro exitoso. Puedes iniciar sesión.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Corrige los errores del formulario.")
        return super().form_invalid(form)
    

class RolRedirectLoginView(LoginView):
    template_name = 'registration/login.html'  # tu plantilla personalizada
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user

        # Redirección según grupo
        if user.groups.filter(name='Alumnos').exists():
            return reverse_lazy('alumno_dashboard')
        elif user.groups.filter(name='Profesores').exists():
            return reverse_lazy('profesor_dashboard')
        elif user.is_superuser or user.groups.filter(name='Administradores').exists():
            return reverse_lazy('admin_dashboard')
        else:
            return reverse_lazy('pagina_por_defecto')


class AlumnoDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboards/alumno.html'

    def test_func(self):
        return self.request.user.rol == 'alumno'


class ProfesorDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboards/profesor.html'

    def test_func(self):
        return self.request.user.rol == 'profesor'


class AdminDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboards/admin.html'

    def test_func(self):
        return self.request.user.rol == 'admin' or self.request.user.is_superuser