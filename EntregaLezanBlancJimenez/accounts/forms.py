from django import forms
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.forms import UserCreationForm #revisar capas ya no al necesito.
from django.contrib.auth.models import User
#from django.utils.translation import ugettext_lazy as _
from .models import Perfil

#forms para Register(crea User) y Editar User:

#form para crear Usuario: en consigna, solo pide los campos username, email, pswd. 
class UserRegisterForm(UserCreationForm):
    #username=forms.CharField(max_length=50)
    email=forms.EmailField()
    password1=forms.CharField(label='contrasena', widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contrasena', widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'' for k in fields} #mas lindo sin help_texts. ver si alguno puede ser necesario.  

#para editar. 
class UserEditForm(UserCreationForm):
    username=forms.CharField(max_length=50)
    email=forms.EmailField()
    password1=forms.CharField(label='contrasena', widget=forms.PasswordInput)
    password2=forms.CharField(label='confirmar contrasena', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        help_texts={k:'campos obligatorios' for k in fields} 

#uso ModelForm!
class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('imagen', 'descripcion', 'link') #OBS: no inlcuyo el user. 
        help_texts = {'link': ('debes poner http://'),}

