from django.core.management.base import BaseCommand
from portfolio.models import PerfilGlobal, Tecnologia, Proyecto, Experiencia, Estudio


class Command(BaseCommand):
    help = 'Pobla la base de datos con datos ficticios realistas para el portfolio'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('Limpiando datos anteriores...'))
        
        Proyecto.objects.all().delete()
        Experiencia.objects.all().delete()
        Estudio.objects.all().delete()
        Tecnologia.objects.all().delete()
        PerfilGlobal.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creando perfil global...'))
        PerfilGlobal.objects.create(
            nombre_completo="Tu Nombre",
            titular="Desarrollador Web Full Stack & Especialista en Backend",
            bio_corta="Apasionado por crear arquitecturas limpias, escalables y eficientes utilizando tecnologías modernas.",
            bio_larga="Soy un desarrollador enfocado en el backend con una sólida experiencia en el ecosistema de Python y Django.",
            email_contacto="tu.correo@ejemplo.com",
            github_url="https://github.com/tu-usuario",
            linkedin_url="https://linkedin.com/in/tu-usuario"
        )

        self.stdout.write(self.style.SUCCESS('Creando tecnologías...'))
        tech_django = Tecnologia.objects.create(nombre="Django", slug="django", categoria="backend")
        tech_python = Tecnologia.objects.create(nombre="Python", slug="python", categoria="backend")
        tech_tailwind = Tecnologia.objects.create(nombre="Tailwind CSS", slug="tailwind-css", categoria="frontend")
        tech_htmx = Tecnologia.objects.create(nombre="HTMX", slug="htmx", categoria="frontend")
        tech_postgresql = Tecnologia.objects.create(nombre="PostgreSQL", slug="postgresql", categoria="db")
        tech_docker = Tecnologia.objects.create(nombre="Docker", slug="docker", categoria="tools")

        self.stdout.write(self.style.SUCCESS("Creando proyectos..."))
        p1 = Proyecto.objects.create(
            titulo="E-commerce Modular con Django",
            slug="ecommerce-modular-django",
            descripcion_corta=(
                "Plataforma de comercio electrónico con pasarela de pago y panel"
                " de administración avanzado. Desarrollo completo optimizado"
                " para conversión."
            ),
            repositorio_url="https://github.com/tu-usuario/ecommerce-django",
            demo_url="https://demo-ecommerce.com",
            publicado=True,
            orden=1,
        )
        p1.tecnologias.set([tech_django, tech_python, tech_postgresql, tech_tailwind])

        p2 = Proyecto.objects.create(
            titulo="Dashboard de Analíticas con HTMX",
            slug="dashboard-analiticas-htmx",
            descripcion_corta=(
                "Panel de control interactivo en tiempo real sin recargas de"
                " página, visualizando métricas de rendimiento con HTMX."
            ),
            repositorio_url="https://github.com/tu-usuario/dashboard-htmx",
            demo_url="https://demo-dashboard.com",
            publicado=True,
            orden=2,
        )
        p2.tecnologias.set([tech_django, tech_htmx, tech_tailwind, tech_docker])

        self.stdout.write(self.style.SUCCESS('Creando experiencia laboral...'))
        Experiencia.objects.create(
            puesto="Desarrollador Backend Senior",
            empresa="Innovaciones Tecnológicas S.L.",
            fecha_inicio="2023-01-01",
            actual=True,
            descripcion="Liderazgo en el diseño de APIs RESTful y optimización de consultas ORM."
        )

        self.stdout.write(self.style.SUCCESS('Creando estudios...'))
        Estudio.objects.create(
            titulacion="Grado Superior en Desarrollo de Aplicaciones Web (DAW)",
            institucion="Centro Educativo Tecnológico",
            fecha_inicio="2019-09-01",
            fecha_fin="2021-06-01",
            descripcion="Formación especializada en programación orientada a objetos."
        )

        self.stdout.write(self.style.SUCCESS('¡Base de datos poblada con éxito!'))