from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Mensaje(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name = 'sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name = 'receiver')
    mensaje = models.TextField()
    fechahora = models.DateTimeField (auto_now_add=True)
    
    def __str__(self):
            return "From: " + str(self.sender) + " | " + "To: " + str(self.receiver) + ' | ' + str(self.fechahora)
