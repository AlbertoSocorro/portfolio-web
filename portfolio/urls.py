from django.urls import path

from .views import portfolio_home

app_name = "portfolio"

urlpatterns = [
    path("", portfolio_home, name="home"),
]
