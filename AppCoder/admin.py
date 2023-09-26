from django.contrib import admin
from .models import *

class CursoAdmin (admin.ModelAdmin):
    list_display = ["nombre", "camada"]
    search_fields = ["nombre"]

# Register your models here.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Avatar)