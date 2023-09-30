from django import forms
from .models import Curso, Avatar
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User


# class CursoFormulario(forms.Form):

#    curso = forms.CharField(required=True)
#    camada = forms.IntegerField(required=True)

class UserEditForm(UserChangeForm):
    password = forms.CharField(
        help_text="",
        widget=forms.MultipleHiddenInput(), required=False
    )
    password1 =forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 =forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    class Meta:
        model= User 
        fields = ("first_name", "last_name", 'email', 'password1', 'password2')

    def clean_password2(self):
        print (self.cleaned_data)

        psw2 = self.cleaned_data["password2"] 
        if psw2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return psw2
    
class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields =('imagen',)

class CursoFormulario(forms.ModelForm):
    class Meta:
        model= Curso 
        fields = ('__all__')


class EstudianteFormulario(forms.Form):

    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    imagen = forms.ImageField()

class ProfesorFormulario(forms.Form):

    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    materia = forms.CharField(max_length=50, required=True)
    imagen = forms.ImageField()