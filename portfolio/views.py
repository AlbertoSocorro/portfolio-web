from django.shortcuts import render

from .models import Estudio, Experiencia, PerfilGlobal, Proyecto, Tecnologia

def portfolio_home(request):
    # Obtener el perfil global (asumiendo que hay al menos uno registrado)
    perfil = PerfilGlobal.objects.first()

    # Obtener proyectos publicados ordenados
    proyectos = Proyecto.objects.filter(publicado=True).prefetch_related('tecnologias')

    # Obtener experiencia laboral y estudios
    experiencias = Experiencia.objects.prefetch_related('tecnologias_usadas')
    estudios = Estudio.objects.all()

    # Obtener todas las tecnologías para posibles filtros
    tecnologias = Tecnologia.objects.all()

    context = {
        "perfil": perfil,
        "proyectos": proyectos,
        "experiencias": experiencias,
        "estudios": estudios,
        "tecnologias": tecnologias,
    }

    return render(request, "portfolio/home.html", context)
