from django.urls import path

from .views import PruebaView, CategoriaView,UnaCategoriaView, ProductosView, ProductosGenericView, UnProductoView

# urlpatterns > NOMBRE OBLIGATORIO paa definir nuestras rutas
urlpatterns = [
    path('prueba', PruebaView.as_view()),
    path('categoria', CategoriaView.as_view()),
    path('categoria/<int:id>', UnaCategoriaView.as_view()),
    path('productos', ProductosView.as_view()),
    path('productos-generic', ProductosGenericView.as_view()),
    path('producto/<int:id>', UnProductoView.as_view())
]