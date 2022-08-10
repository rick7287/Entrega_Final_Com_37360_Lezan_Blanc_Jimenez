import datetime
from re import M
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




#--------------------------------------------------------
#Blog

#Formulario para Paginas
class Message_Form(forms.Form):

    sender = forms.ModelChoiceField(queryset=User.objects.all())
    receiver = forms.ModelChoiceField(queryset=User.objects.all())
    mensaje = forms.CharField(max_length=1000)
    #fechahora = forms.DateTimeField(auto_now_add=True)
    fechahora = forms.DateTimeField(initial=datetime.datetime.now)
    