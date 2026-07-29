from django.urls import path

from .views import filtrar_proyectos, portfolio_home, procesar_contacto

app_name = "portfolio"

urlpatterns = [
    path("", portfolio_home, name="home"),
    path("filtrar-proyectos/", filtrar_proyectos, name="filtrar_proyectos"),
    path("contacto/", procesar_contacto, name="contacto"),
]
