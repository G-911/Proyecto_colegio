from django.urls import path, include
from .views import SignupView
from .views import (
    RolRedirectLoginView ,AlumnoDashboardView,
    ProfesorDashboardView, AdminDashboardView
)
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup', SignupView.as_view(), name = 'signup'),

    path('login/', RolRedirectLoginView.as_view(), name='login'),
    path('alumno/', AlumnoDashboardView.as_view() , name='alumno_dashboard'),
    path('profesor/', ProfesorDashboardView.as_view(), name='profesor_dashboard'),
    path('admin/', AdminDashboardView.as_view(), name='admin_dashboard'),
]