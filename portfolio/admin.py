from django.contrib import admin

from .models import Estudio, Experiencia, PerfilGlobal, Proyecto, Tecnologia


@admin.register(PerfilGlobal)
class PerfilGlobalAdmin(admin.ModelAdmin):
    list_display = ("nombre_completo", "titular", "email_contacto")


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria")
    prepopulated_fields = {"slug": ("nombre",)}


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "publicado", "orden")
    prepopulated_fields = {"slug": ("titulo",)}
    list_filter = ("publicado", "tecnologias")
    search_fields = ("titulo", "descripcion_corta")


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ("puesto", "empresa", "actual", "fecha_inicio")
    list_filter = ("actual",)


@admin.register(Estudio)
class EstudioAdmin(admin.ModelAdmin):
    list_display = ("titulacion", "institucion", "fecha_inicio")
