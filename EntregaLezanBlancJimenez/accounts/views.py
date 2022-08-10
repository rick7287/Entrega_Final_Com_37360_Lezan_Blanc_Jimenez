from django.shortcuts import render, redirect #el redirect capaz no lo uso. 
from django.http import HttpResponse
from accounts.models import * #solo es Perfil! 
from accounts.forms import *  #importo todos xq igual son pocos. 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.contrib import messages #podria no usarlo pero ya esta...


#vista home de accounts.
def inicio(request):   
    return render(request, 'accounts/inicio.html')


#login. 
def login_request(request):
    if request.method=='POST':
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario= request.POST['username'] 
            contrasena= request.POST['password'] 
            user=authenticate(username=usuario, password=contrasena)
            if user is not None: #ie si hace match con alguno
                login(request, user) #aca uso el login q importe de django.
                return render(request, 'accounts/inicio.html', { 'mensaje':f'bienvenido  {usuario}'}) 
            else:
                return render(request, 'accounts/login.html', {'form':form, 'mensaje':'usuario o clave incorrecta'})    
        else:
            return render(request, 'accounts/login.html', {'form':form, 'mensaje':'FORMULARIO INVALIDO'} )
    else:  #si es GET
        form=AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form}) #lo mando al login con el form vacio






#registro. Obs: guarda en model User, pero esta linkeado en models, con el post_save, ent guarda tmb en Perfil.
def register(request):
    if request.method=='POST':
        formulario=UserRegisterForm(request.POST) 
        if formulario.is_valid():
            username=formulario.cleaned_data['username'] 
            contrasena=formulario.cleaned_data['password1'] 
            formulario.save()
            user = authenticate(username=username, password=contrasena)
            login(request, user) #hago login para que el usuario ya quede logueado!
            return render(request, 'accounts/inicio.html', {'mensaje':f'usuario creado:{username}'})
        else: #si no ponia este else, daba un error en el navegador, cuando in_valid=False...
            form=UserRegisterForm() 
            return render(request, 'accounts/signup.html', {'form':form, 'mensaje':'Formulario Invalido'})
    else: #ie si no es POST.
        form=UserRegisterForm() 
    return render(request, 'accounts/signup.html', {'form':form})







'''

#registro. Obs: guarda en model User, pero esta linkeado en models, con el post_save, ent guarda tmb en Perfil.
def register(request):
    if request.method=='POST':
        formulario=UserRegisterForm(request.POST) 
        if formulario.is_valid():
            username=formulario.cleaned_data['username'] 
            email=formulario.cleaned_data['email'] #medio al pedo me estoy guardando email y contrasena aca?, xq no tengo q hacer authenticate.
            contrasena=formulario.cleaned_data['password1'] 
            formulario.save()
            form= AuthenticationForm(request, data=request.POST) #lo mando al login con este form, y ya me completa el nombre.   
            return render(request, 'accounts/login.html', {'form':form, 'mensaje':f'usuario creado:{username} AHORA LOGUEATE!' })

        else:

            form=UserRegisterForm() 
            return render(request, 'accounts/signup.html', {'form':form, 'mensaje':'Formulario Invalido'})

            #return HttpResponse('formulario invalido')
    else:
        form=UserRegisterForm() 
    return render(request, 'accounts/signup.html', {'form':form})
'''

    
#editar perfil:
@login_required
def update_perfil(request): 
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user) 
        perfil_form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil) 
        #uso ambos forms a la vez y los valido:
        if user_form.is_valid() and perfil_form.is_valid():
            usuario=user_form.save()  #me guardo usuario asi lo paso por contexto..
            perfil_form.save()
            usu = request.user #agrego tal cual info_perfil p q me muestre los datos actualizados. o directamente podria hcer q llame a info_perfil...?
            perfil = Perfil.objects.get(user = usu)
            return render(request, 'accounts/profile.html', {'mensaje': 'TU USUARIO HA SIDO ACTUALIZADO' , 'perfil':perfil})
        else:
            messages.error(request, 'Fijate este error!:') #tmb podria pasarle return render(...mensage)
    else:
        user_form = UserEditForm(instance=request.user) #hace falta q vayan instanciados aca? es para q me los rellene...
        perfil_form = PerfilForm(instance=request.user.perfil)
    return render(request, 'accounts/update_perfil.html', {'user_form': user_form, 'perfil_form': perfil_form })

#para ver perfil:
@login_required
def info_perfil(request):
    usuario = request.user
    perfil = Perfil.objects.get(user = usuario)
    
    return render(request, 'accounts/profile.html', {'perfil':perfil})


#vista para eliminar usuario (tmb eliminda su perfil). 
@login_required
def deleteUser(request, usuario): 
    usu=request.user 
    logout(request) #meto esto antes del delete, asi se desloguea!
    usu.delete()
    #y si lo mando a login?
    return render(request, 'accounts/inicio.html', {'mensaje':'Su usuario ha sido eliminado'})

