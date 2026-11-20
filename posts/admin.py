from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("titulo", "fecha_creacion","autor", "estado")
    search_fields = ("titulo", "contenido", "autor")
    list_filter = ("estado", "fecha_creacion")
    list_editable = ("estado",)
