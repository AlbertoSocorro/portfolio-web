from django.shortcuts import render

from .forms import ContactoForm
from .models import Estudio, Experiencia, PerfilGlobal, Proyecto, Tecnologia


def portfolio_home(request):
    # Obtener el perfil global (asumiendo que hay al menos uno registrado)
    perfil = PerfilGlobal.objects.first()

    # Obtener proyectos publicados ordenados
    proyectos = Proyecto.objects.filter(publicado=True).prefetch_related("tecnologias")

    # Obtener experiencia laboral y estudios
    experiencias = Experiencia.objects.prefetch_related("tecnologias_usadas")
    estudios = Estudio.objects.all()

    # Obtener todas las tecnologías para posibles filtros
    tecnologias = Tecnologia.objects.all()

    # Instanciar el formulario de contacto vacío
    form = ContactoForm()

    context = {
        "perfil": perfil,
        "proyectos": proyectos,
        "experiencias": experiencias,
        "estudios": estudios,
        "tecnologias": tecnologias,
        "form": form,
        "enviado": False,
    }

    return render(request, "portfolio/home.html", context)


def filtrar_proyectos(request):
    tech_slug = request.GET.get("tech")

    if tech_slug and tech_slug != "todos":
        proyectos = Proyecto.objects.filter(
            publicado=True, tecnologias__slug=tech_slug
        ).prefetch_related("tecnologias")
    else:
        proyectos = Proyecto.objects.filter(publicado=True).prefetch_related("tecnologias")

    context = {"proyectos": proyectos}

    return render(request, "components/_grid_proyectos.html", context)


def procesar_contacto(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "components/_formulario_contacto.html", {"enviado": True})
    else:
        form = ContactoForm()

    return render(request, "components/_formulario_contacto.html", {"form": form, "enviado": False})
