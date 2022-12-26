from django.urls import path

from app.views import *

urlpatterns = [
    path('', home, name='welcome'),
    path('a-propos', about, name='about'),
    path('contact', contact, name='contact'),
    path('erreur-404', error_page, name='error'),
    path('service', service, name='service'),
    path('notre-equipe', team, name='team'),
    
    #route pour le stockage des donnees
    path('post-email', post_mail, name='post_mail'),
    
    #route pour avoir un RDV(Rendez-Vous)
    path('get-rdv', get_rdv, name='get_rdv'),
    
    #route pour contacter bint-watara
    path('post-contact', post_contact, name='postContact')
   
]