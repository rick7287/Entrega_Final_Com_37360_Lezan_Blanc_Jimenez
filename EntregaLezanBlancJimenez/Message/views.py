from genericpath import exists
from tkinter.tix import INTEGER
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from Message.forms import *
from Message.models import *
from django.db.models import Q


#Para el login

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User

# Create your views here.



@login_required
def messages(request):

    mensaje = ""
    
    yo = request.user
    usuarios = User.objects.filter(~Q(username = yo))
    messages = Mensaje.objects.all()
    hay_mensaje = []

    if not messages:
            mensaje = 'Aun no hay mensajes'


    for usuario in usuarios:

        for message in messages:

            if ((message.sender == yo and message.receiver == usuario) or (message.sender == usuario and message.receiver == yo)):
                hay_mensaje.append(usuario)
 
    conversaciones = list(dict.fromkeys(hay_mensaje))  #Elimina los elementos duplicados

    contexto={'mensajes':messages, 'mensaje':mensaje, 'usuarios':usuarios, 'yo':yo, 'conversaciones':conversaciones}  

    return render(request, 'Message/inbox.html', contexto)

@login_required
def coversacion_detalle(request, usuario):

    mensaje = ""
   
    yo = request.user
    user_1 = User.objects.get(username = usuario)
    
    messages = Mensaje.objects.filter((Q(sender = user_1) & Q(receiver =yo)) | (Q(sender = yo) & Q(receiver =user_1))) 
    
    
    contexto={'yo':yo, 'usuario':user_1, 'messages':messages} 
    return render(request, 'Message/conversacion_detalle.html', contexto)


    #return HttpResponse(str(usuario))


@login_required
def message_crear(request):

    mensaje=''
    
    
    if (request.method == "POST"):     
        formulario = Message_Form (request.POST)
        #formulario.autor = request.user

        if formulario.is_valid():    

            informacion = formulario.cleaned_data   


            sender = informacion['sender']
            receiver = informacion['receiver']
            mensaje = informacion['mensaje']
            fechahora = informacion['fechahora']

                        
            mensaje_obj = Mensaje(sender=sender, receiver=receiver, mensaje=mensaje, fechahora=fechahora)  
            mensaje_obj.save()
            mensaje = f"Mensaje enviado exitosamente"

            return render(request, "Message/confirmacion.html", {'mensaje':mensaje})              
            
            #return render(request, "Blog/pages.html", {'mensaje':mensaje})              
            #return render(request, "Blog/inicio.html") 
        else:
            mensaje='Error con el formulario'
            return render(request, "Message/confirmacion.html", {'mensaje':mensaje})

    else: 
        formulario= Message_Form( initial={'sender':request.user})  

        #La unica opcion para sender es el user loggeado
        formulario.fields['sender'].queryset= User.objects.filter(username=request.user)

        #El user loggeado no es ta en las opciones del receiver
        formulario.fields['receiver'].queryset= User.objects.filter(~Q(username = request.user))

    return render(request, "Message/message_crear.html", {"formulario":formulario, 'mensaje':mensaje})