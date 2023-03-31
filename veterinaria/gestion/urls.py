from django.urls import path
from .views import RegistrarUsuario

# urlpatterns > NOMBRE OBLIGATORIO para definir nuestras rutas
urlpatterns = [
    path('registrar', RegistrarUsuario.as_view()),
]