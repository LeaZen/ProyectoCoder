from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.list import ListView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from .models import Curso, Estudiante, Profesor, Entregable, Avatar
from .forms import *

# Create your views here.

def loginView(request):

    if request.method == "POST":
        miFormulario = AuthenticationForm(request, data=request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psw =  data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(request, user) 
                return render(request,"inicio.html", {"mensaje": f"Hola {usuario}"})
            else:
                return render(request,"inicio.html", {"mensaje": "Datos Incorrectos"})
        else:
                return render(request,"inicio.html", {"mensaje": "Formulario Inválido"})  
          
    else:
        miFormulario = AuthenticationForm()
        return render(request,"login.html", {"miFormulario":miFormulario})
    

def register(request):

    if request.method == "POST":
        miFormulario = UserCreationForm(request.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data ["username"]
            miFormulario.save()

            return render(request,"inicio.html", {"mensaje": f"Usuario {usuario} creado con éxito"})
               
        else:
            return render(request,"inicio.html", {"mensaje": "Formulario Inválido"})  
          
    else:
        miFormulario = UserCreationForm()
        return render(request,"registro.html", {"miFormulario":miFormulario})
    
def editar_perfil (request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST, instance=request.user)

        if miFormulario.is_valid():

           data = miFormulario.cleaned_data

           usuario.first_name = data ["first_name"]
           usuario.last_name = data ["last_name"]
           usuario.email = data ["email"]
           usuario.set_password(data["password1"])
           usuario.save()
           #miFormulario = AuthenticationForm()
           return render(request,"inicio.html", {"mensaje": "Perfil actualizado con éxito"})
            
        else:
            return render(request,"editar_perfil.html", {"miFormulario":miFormulario})


    else:
        miFormulario = UserEditForm(instance=request.user)
        return render(request,"editar_perfil.html", {"miFormulario":miFormulario})

def inicio (request):

    try:
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, "inicio.html", {"url": avatar.imagen.url})
    except:

    #return HttpResponse ("Vista de Inicio")
        return render(request, "inicio.html")
    
def agregar_avatar(request):

    if request.method == "POST":
        miFormulario = AvatarFormulario(request.POST, request.FILES)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            avatar = Avatar(user=request.user, imagen=data["imagen"])
            avatar.save()

            return render(request,"inicio.html", {"mensaje": f"Avatar actualizado con éxito"})
               
        else:
            return render(request,"inicio.html", {"mensaje": "Formulario Inválido"})  
          
    else:
        miFormulario = AvatarFormulario
        return render(request,"agregarAvatar.html", {"miFormulario":miFormulario})

def curso (request, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    return HttpResponse(f"""
                        <p> Curso: {curso.nombre} - Camada: {curso.camada} agregado! </p>
                        """)


def lista_cursos (request):
    lista = Curso.objects.all()

    return render(request, "Lista_cursos.html", {"lista_cursos" : lista})

def cursos (request):
    return render(request, "cursos.html")
    

class CursoList(ListView):
    model = Curso
    template_name = "curso_list.html"
    context_object_name = "cursos"

class CursoDetail(LoginRequiredMixin, DetailView):
    model = Curso
    template_name = "curso_detail.html"
    context_object_name = "curso"

class CursoCreate(CreateView):
    model = Curso
    template_name = "curso_create.html"
    fields = ["nombre", "camada"]
    success_url = '/app-coder/inicio'

class CursoUpdate(UpdateView):
    model = Curso
    template_name = "curso_update.html"
    fields = ("__all__")
    success_url = '/app-coder/inicio'

class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_delete.html"
    success_url = '/app-coder/inicio'


def curso_formulario (request: HttpRequest):

    print("method", request.method)
    print("post", request.POST)

    miFormulario = CursoFormulario(request.POST) 

    if request.method == "POST":

        if miFormulario.is_valid():
            print (miFormulario.cleaned_data)
            data = miFormulario.cleaned_data

            curso = Curso (nombre=data ["curso"], camada=data ["camada"])
            curso.save()
            return render(request, "inicio.html", {"mensaje" : "Curso creado con éxito"})
        else:
            return render(request, "inicio.html", {"mensaje" : "Formulario inválido"})
    else:    
        miFormulario = CursoFormulario()
        return render(request, "curso_formulario.html", {"miFormulario":miFormulario})
    

def busqueda_camada(request):
    
    return render(request, "busqueda_camada.html")

def buscar(request):

    if request.GET ["camada"]:
        camada = request.GET ["camada"]
        curso = Curso.objects.get(camada=camada)
        if curso:
            return render(request, "resultado_buqueda.html", {"curso":curso})
        
    else:
        return HttpResponse("No escribió una camada existente")

    #else:
    #return HttpResponse("No escribió una camada existente")

    
#return HttpResponse(f"Estoy buscando la camada {request.GET['camada']}")

def estudiantes (request):
    return render(request, "estudiantes.html")
    


def estudiante_formulario (request: HttpRequest):

    print("method", request.method)
    print("post", request.POST)

    elFormulario = EstudianteFormulario(request.POST) 

    if request.method == "POST":

        if elFormulario.is_valid():
            print (elFormulario.cleaned_data)
            data = elFormulario.cleaned_data

            estudiante = Estudiante (nombre=data ["nombre"], apellido=data ["apellido"], email=data ["email"])
            estudiante.save()
            return render(request, "inicio.html", {"mensaje" : "Estudiante ingresado a la base de datos con éxito"})
        else:
            return render(request, "inicio.html", {"mensaje" : "Estudiante no ingresado"})
    else:    
        elFormulario = EstudianteFormulario()
        return render(request, "estudiante_formulario.html", {"elFormulario":elFormulario})




def profesores (request):
    return render(request, "profesores.html")

#@login_required
@staff_member_required(login_url='/app-coder/login')
def profesores_formulario (request: HttpRequest):

    print("method", request.method)
    print("post", request.POST)

    liFormulario = ProfesorFormulario(request.POST) 

    if request.method == "POST":

        if liFormulario.is_valid():
            print (liFormulario.cleaned_data)
            data = liFormulario.cleaned_data

            profesor = Profesor (nombre=data ["nombre"], apellido=data ["apellido"], email=data ["email"], profesion=data ["profesion"]  )
            profesor.save()
            return render(request, "inicio.html", {"mensaje" : "Profesor ingresado a la base de datos con éxito"})
        else:
            return render(request, "inicio.html", {"mensaje" : "Profesor no ingresado"})
    else:    
        liFormulario = ProfesorFormulario()
        return render(request, "profesor_formulario.html", {"liFormulario":liFormulario})



def entregables (request):
    return render(request, "entregables.html")