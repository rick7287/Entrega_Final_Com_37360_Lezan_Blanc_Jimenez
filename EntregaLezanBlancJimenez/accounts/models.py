from django.db import models
from django.contrib.auth.models import User 
#para poder linkear User con Perfil:
from django.db.models.signals import post_save
from django.dispatch import receiver

# LOS MODELOS:

#mi RegisterForm me crea usuarios de User. aca extiendo, para poder tener la info del Profile. 
class Perfil(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, null=True) #q tenga los fields de User, mas los q agrego abajo.
    imagen= models.ImageField(upload_to='avatar', blank=True, null=True) #BLANK=TRUE, para q el ModelForm me tome required=False en el ModelForm!
    descripcion= models.TextField(blank=True, null=True) 
    link= models.URLField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return str(self.user) #con este me alcanza.
    


#uso signals para linkear model User con Pefil:  
@receiver(post_save, sender=User) #si creo un User me crea un Perfil.   
def create_user_perfil(sender, instance, created, **kwargs): 
    if created:
        Perfil.objects.create(user=instance)

#este signal me chillaba y no lo estoy necesitando. 
'''@receiver(post_save, sender=User) #si guardo un User me guarda el Perfil
def save_user_perfil(sender, instance, **kwargs): # uso save_user_profile. 
    instance.Perfil.save()   '''

#hace falta o no?ya esta todo funcionando, asiq lo dejo sin.
'''class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.Cascade)
    imagen'''
