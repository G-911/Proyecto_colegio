from django.contrib import messages
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from .models import Usuario
from .forms import RegistroAlumnoForm
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import Permission

class RegistroAlumnoView(CreateView):
    model = Usuario
    form_class = RegistroAlumnoForm
    template_name = 'registro_alumno.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.rol = 'alumno'
        usuario.set_password(form.cleaned_data['password1'])
        usuario.save()
        messages.success(self.request, "Registro exitoso.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Corrige los errores del formulario.")
        return super().form_invalid(form)


class CrearProfesorView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Usuario
    form_class = RegistroAlumnoForm
    template_name = 'crear_profesor.html'
    success_url = reverse_lazy('lista_usuarios')

    def test_func(self):
        return self.request.user.rol == 'admin'

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.rol = 'profesor'
        usuario.is_staff = True
        usuario.set_password(form.cleaned_data['password1'])
        usuario.save()

        # Asignar grupo y permisos
        grupo, _ = Group.objects.get_or_create(name='profesor')
        permisos = Permission.objects.filter(codename__in=[
            'add_group', 'change_group', 'delete_group'
        ])
        grupo.permissions.set(permisos)
        usuario.groups.add(grupo)

        return super().form_valid(form)



class ListaUsuariosView(LoginRequiredMixin, ListView):
    model = Usuario
    template_name = 'lista_usuarios.html'
    context_object_name = 'usuarios'

    def get_queryset(self):
        rol = self.request.GET.get('rol')
        if rol:
            return Usuario.objects.filter(rol=rol)
        return Usuario.objects.all()


class CrearAdminView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Usuario
    form_class = RegistroAlumnoForm
    template_name = 'crear_admin.html'
    success_url = reverse_lazy('lista_usuarios')

    def test_func(self):
        return self.request.user.rol == 'admin'

    def form_valid(self, form):
        usuario = form.save(commit=False)
        usuario.rol = 'admin'
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.set_password(form.cleaned_data['password1'])
        usuario.save()

        grupo, _ = Group.objects.get_or_create(name='admin')
        grupo.permissions.set(Permission.objects.all())
        usuario.groups.add(grupo)

        return super().form_valid(form)