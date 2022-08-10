from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView
#agrego los paths de esta app accounts
urlpatterns = [
    path('', inicio, name='inicio'), #este seria el home de accounts..
    path('login/', login_request, name='login'),
    path('signup/', register, name='signup'), #ojo notar la vista es register, no signup. 
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profile/update_perfil', update_perfil, name='update_perfil'), 
    path('deleteUser/<usuario>', deleteUser, name='deleteUser'),
    path('profile/', info_perfil, name='info_perfil'),
    
]