from django.urls import path
from .views import RegistrarUsuario, PerfilUsuario, Mascotas

from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('registrar', RegistrarUsuario.as_view()),

    path('login/', TokenObtainPairView.as_view()),

    path('perfil/', PerfilUsuario.as_view()),

    path('mascotas/', Mascotas.as_view()),
]