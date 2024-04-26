from django.shortcuts import render
from django.http import HttpResponse
import pandas as pds
import numpy as np
import os
import os.path as osp


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

def form(request):
    return render(request,'form.html')

def reception(request): 
    rP=request.POST
    return render(request,'URL_de_reception.html',
        {
            'mon_texte':rP['mon_texte']
                  })


def ta(request,tableau) :
    nrow=tableau.shape[0]
    M=np.asarray(tableau)
    ntableau=[[tableau.index[i]]+list(M[i,:]) for i in range(nrow)]
    return render(request,'Resultat_requete.html',
        {
            'index' : tableau.index,
            'columns' : tableau.columns,
            'L' : ntableau
                  })
    
def tapart(request) :
    famille=pds.DataFrame({'maman':[4,1],'papa':[7,9],'enfant':["issou","lol"]})
    return(ta(request,famille))
    
    
    
def grosta(request) : 
    tableau=pds.read_csv("/users/2024/ds1/122005148/Bureau/cours_django/monprojet/recherchemot.csv",index_col=(0))
    nrow=tableau.shape[0]
    M=np.asarray(tableau)
    ntableau=[[tableau.index[i]]+list(M[i,:]) for i in range(nrow)]
    return render(request,'grosta.html',
        {
            'index' : tableau.index,
            'columns' : tableau.columns,
            'L' : ntableau
                  })
    
def ouvmail(request,capture) : 
    response = HttpResponse()
    path=osp.join('/users/2024/ds1/122005148/Bureau/projet_BDDR/',capture)
    try : 
        with open(path,"r") as file :
            for ligne in file : 
                response.write('<p>'+ligne+'</p>')
    except UnicodeDecodeError :
        with open(path,"rb") as file :
            Lignes=str(file.read()).split(r'\n')
            for ligne in Lignes : 
                response.write('<p>'+ligne+'</p>')
    return response
    

    


