import pytest
from django.urls import reverse

from portfolio.models import MensajeContacto, Proyecto, Tecnologia


@pytest.mark.django_db
class TestPortfolioViews:
    def test_gome_status_code(self, client):
        """Verifica que la página principal carga correctamente."""
        url = reverse("portfolio:home")
        response = client.get(url)
        assert response.status_code == 200
        assert "portfolio/home.html" in [t.name for t in response.templates]

    def test_filtrar_proyectos_view(self, client):
        """Verifica que la vista de filtrado por HTMX responde correctamente."""
        url = reverse("portfolio:filtrar_proyectos")
        response = client.get(url, {"tech": "todos"})
        assert response.status_code == 200
        assert "components/_grid_proyectos.html" in [t.name for t in response.templates]

    def test_contacto_post_valido(self, client):
        """Verifica que el formulario de contacto guarda el mensaje y devuelve éxito."""
        url = reverse("portfolio:contacto")
        data = {
            "nombre": "Tester Automatizado",
            "email": "test@example.com",
            "mensaje": "Este es un mensaje de prueba desde pytest.",
        }
        response = client.post(url, data)
        assert response.status_code == 200
        assert MensajeContacto.objects.count() == 1
        assert MensajeContacto.objects.first().email == "test@example.com"
