from django.urls import path
from .views import *

urlpatterns = [
    path('agrega_curso/<nombre>/<camada>', curso),
    path('listado_de_cursos/', lista_cursos),
    path('inicio', inicio, name = "Inicio"),
    path('cursos/', curso_formulario, name = "CursoFormulario"),
    path('profesores/', profesores, name = "Profesores"),
    path('estudiantes/', estudiantes, name = "Estudiantes"),
    path('entregables/', entregables, name = "Entregables"),
    path('curso-formulario/', curso_formulario, name = "CursoFormulario"),
    path('busqueda-camada/', busqueda_camada, name = "BusquedaCamada"),
    path('buscar/', buscar, name = "Buscar"),
    path('estudiante-formulario/', estudiante_formulario, name = "EstudianteFormulario"),
    path('profesor-formulario/', profesores_formulario, name = "ProfesorFormulario"),
   ]
