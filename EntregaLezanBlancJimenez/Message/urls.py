from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    
    
    path('messages/', messages, name='messages'),
    path('coversacion_detalle/<usuario>', coversacion_detalle, name='coversacion_detalle'),
    path('message_crear/', message_crear, name='message_crear'),
    


]