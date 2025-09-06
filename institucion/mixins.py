from django.contrib.auth.mixins import UserPassesTestMixin

class SoloAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='Administradores').exists()

class SoloProfesorOMasMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['Administradores', 'Profesores']).exists()

class SoloLecturaMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['Administradores', 'Profesores', 'Alumnos']).exists()