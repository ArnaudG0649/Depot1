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
] 
