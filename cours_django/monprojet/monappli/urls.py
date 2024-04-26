from django.urls import path,re_path
from . import views



urlpatterns = [
    path('help', views.help, name='help'), 
    path('home', views.home, name='home'),
    path('clients', views.clients, name='clients'),
    path('pages', views.pages, name='pages'),
    path('hit', views.hit, name='hit'),
    re_path(r'^sum/(.*)/(.*)$', views.somme, name='somme'),
    path('', views.home, name='vide'), 
    path('form',views.form,name='form'),
    path('URL_de_reception',views.reception,name='reception'),
    path('tapart',views.tapart,name='tableau_automatique'),
    path('grosta',views.grosta,name='gros_tableau_automatique'),
    re_path(r'^(maildir/.*)$', views.ouvmail, name='ouvmail')
] 
