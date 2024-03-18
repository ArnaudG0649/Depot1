from django.shortcuts import render
from django.http import HttpResponse


import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '../monprojet.settings') 
django.setup()

from monappli.models import Client, Page, Hit


def home(request):
    return HttpResponse("<p>Cette vue est une page d'accueil basique pour l'application <code>monappli</code> de mon projet.</p>")

def help(request):
    response = HttpResponse()
    response.write("<h1>Explications</h1>")
    response.write("<p>Ce site est une ébauche d'une page web crée avec Django dans un but pédagogique.</p>")
    response.write("<p>Si vous voyez ce message cela signifie que cet exercice est un succés.</p>")
    return response

def clients(request):
    response = HttpResponse()
    response.write("<h1>Liste des clients de la base de données</h1>")
    for client in Client.objects.all() : 
        response.write(f'<p>{client}</p>')
    return response

def pages(request):
    return render(request,'temp1.html', 
        {                                          
            'pages': Page.objects.all(),
            'nb': Page.objects.count(),
            'rien': Page.objects.count()==0
        })

def hit(request):
    return render(request,'tmp_hit.html', 
        {                                          
            'hit': Hit.objects.all(),
            'nb': Hit.objects.count(),
            'rien': Hit.objects.count()==0
        })

def somme(request,capture1,capture2) : 
    response = HttpResponse()
    lnbr=range(int(capture1),int(capture2)+1)
    txt=" + ".join([str(i) for i in lnbr])
    txt+=" = "
    txt+=str(sum(lnbr))
    response.write('<p>'+txt+"</p>")
    return response