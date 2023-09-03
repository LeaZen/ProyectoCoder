from django import forms

class CursoFormulario(forms.Form):

    curso = forms.CharField(required=True)
    camada = forms.IntegerField(required=True)

class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    profesion = forms.CharField(max_length=50, required=True)