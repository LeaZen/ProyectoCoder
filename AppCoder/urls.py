from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('inicio', inicio, name = "Inicio"),
    path('login', loginView, name = "Login"),
    path('registrar', register, name = "Registrar"),
    path('logout', LogoutView.as_view(template_name="inicio.html"), name = "Logout"),
    path('editar-perfil/', editar_perfil, name = "EditarPerfil"),
    path('agregar-avatar/', agregar_avatar, name = "AgregarAvatar"),
    path('agrega_curso/<nombre>/<camada>', curso),
    path('listado_de_cursos/', lista_cursos),
    path('cursos/', curso_formulario, name = "CursoFormulario"),
    path('curso-formulario/', curso_formulario, name = "CursoFormulario"),
    path('lista-curso/', CursoList.as_view(), name = "ListaCursos"),
    path('detalle-curso/<pk>', CursoDetail.as_view(), name = "DetalleCursos"),
    path('crea-curso/', CursoCreate.as_view(), name = "CreaCursos"),
    path('actualiza-curso/<pk>', CursoUpdate.as_view(), name = "ActualizaCursos"),
    path('elimina-curso/<pk>', CursoDelete.as_view(), name = "EliminaCursos"),
    path('busqueda-camada/', busqueda_camada, name = "BusquedaCamada"),
    path('buscar/', buscar, name = "Buscar"),
    path('estudiantes/', estudiantes, name = "Estudiantes"),
    path('estudiante-formulario/', estudiante_formulario, name = "EstudianteFormulario"),
    path('profesores/', profesores, name = "Profesores"),
    path('profesor-formulario/', profesores_formulario, name = "ProfesorFormulario"),
    path('entregables/', entregables, name = "Entregables"),
   ]
