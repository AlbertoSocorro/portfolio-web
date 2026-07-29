from django.db import models


class PerfilGlobal(models.Model):
    nombre_completo = models.CharField(max_length=100)
    titular = models.CharField(max_length=200, help_text="Ej: Desarrollador Web Backend")
    bio_corta = models.TextField()
    bio_larga = models.TextField()
    email_contacto = models.EmailField()
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Perfil Global"
        verbose_name_plural = "Perfil Global"

    def __str__(self):
        return self.nombre_completo


class Tecnologia(models.Model):
    CATEGORIAS = [
        ("backend", "Backend"),
        ("frontend", "Frontend"),
        ("db", "Bases de Datos"),
        ("tools", "Herramientas"),
    ]
    nombre = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)

    class Meta:
        ordering = ["categoria", "nombre"]

    def __str__(self):
        return self.nombre


class Proyecto(models.Model):
    titulo = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    descripcion_corta = models.TextField()
    imagen_portada = models.ImageField(upload_to="proyectos/portadas/")
    repositorio_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    tecnologias = models.ManyToManyField(Tecnologia, related_name="proyectos")
    publicado = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)
    fecha_creacion = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["orden", "-fecha_creacion"]

    def __str__(self):
        return self.titulo


class Experiencia(models.Model):
    puesto = models.CharField(max_length=150)
    empresa = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    actual = models.BooleanField(default=False)
    descripcion = models.TextField()
    tecnologias_usadas = models.ManyToManyField(Tecnologia, blank=True)

    class Meta:
        ordering = ["-actual", "-fecha_inicio"]

    def __str__(self):
        return f"{self.puesto} en {self.empresa}"


class Estudio(models.Model):
    titulacion = models.CharField(max_length=150)
    institucion = models.CharField(max_length=150)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True)

    class Meta:
        ordering = ["-fecha_inicio"]

    def __str__(self):
        return f"{self.titulacion} - {self.institucion}"
