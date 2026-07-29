from django.urls import path

from .views import portfolio_home, filtrar_proyectos

app_name = "portfolio"

urlpatterns = [
    path("", portfolio_home, name="home"),
    path("filtrar-proyectos/", filtrar_proyectos, name="filtrar_proyectos"),
]
