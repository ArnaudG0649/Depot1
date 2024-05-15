#!/bin/env python3

import re
import os
import os.path as osp 
import datetime
import django
import xml.etree.ElementTree as ET

#'django_extensions' ##Pour éxecuter la commande au projet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetenron.settings') 
django.setup()

from app1.models import Employee,Emailadress,Mail,To,Cc #,Re
from django.core.exceptions import ObjectDoesNotExist


class Mailobj() : #On crée une classe de mails. Les attributs des tables seront les attributs des instances de cette classe.
#L'objectif de cette classe est de pouvoir extraire les informations importantes de chaque mail qui seront mises dans les tables.    

    def __init__(self,path) : 
        self.path=path[len(osp.join(os.getcwd(),"maildir/"))-1:] #Chemin qui commence après le "maildir/"
         
        try : 
            with open(path,"r") as file :
                Lignes=[ligne for ligne in file]
        except UnicodeDecodeError :
            with open(path,"rb") as file :
                Lignes=str(file.read()).split(r'\n')
        
        self.id=re.search(r"<(.*)>",Lignes[0]).group(1)
        
        Lmois=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

        d=Lignes[1].split(" ")[1:]
        nummois=Lmois.index(d[2])+1
        # delta=datetime.timedelta(hours=-int(d[-2][2]))
        # zone=datetime.timezone(delta)
        self.date=datetime.datetime(int(d[3]), nummois, int(d[1]), hour=int(d[4][:2]), minute=int(d[4][3:5]), second=int(d[4][6:]))#, tzinfo=zone)+datetime.timedelta(hours=-9)
        
        if re.search(r"From: (\S*@\S*)",Lignes[2]) : 
            self.fromm=re.search(r"From: (\S*@\S*)",Lignes[2]).group(1) 
        elif re.search(r"From: (.*>)",Lignes[2]) : 
            self.fromm=re.search(r"From: (.*>)",Lignes[2]).group(1) 
        
        i=3
        if re.search(r"To: ([^(\n)]*)",Lignes[i]): 
            s=re.search(r"To: ([^(\n)]*)",Lignes[i]).group(1)
            s=re.sub(r"\s",r"",s) #Pour enlever tous les séparateurs blancs et garder uniquement les virgules comme séparateurs entre les adresses.
            i+=1
            while bool(re.match(r'\t',Lignes[i])) :
                s+=re.sub(r"\s",r"",Lignes[i])
                i+=1
            self.to=s.split(',')
        else : 
            self.to=None
        
        if re.match(r"Subject: ([^(\n)]*)",Lignes[i]): 
            self.subject=re.match(r"Subject: ([^(\n)]*)",Lignes[i]).group(1) 
            i+=1
            if self.subject=="" : self.subject=None
        else : self.subject=None
        
        if re.search(r"Cc: ([^(\n)]*)",Lignes[i]): 
            s=re.search(r"Cc: ([^(\n)]*)",Lignes[i]).group(1)
            s=re.sub(r"\s",r"",s)
            i+=1
            while bool(re.match(r'\t',Lignes[i])) :
                s+=re.sub(r"\s",r"",Lignes[i])
                i+=1
            self.cc=s.split(',')
        else : 
            self.cc=None


def ListemailSQL(path=osp.join(os.getcwd(),"maildir"),i=[0]):
    print(path)
    for file in os.listdir(path) : 
        if osp.isfile(osp.join(path,file)) : #C'est ci_dessous que l'on collecte les données du mail
            mail=Mailobj(osp.join(path,file))
            i[0]+=1
            
            print(f"{osp.join(os.getcwd(),'maildir',mail.path)}")
            print(f"({i}) Correction de {osp.join(os.getcwd(),'maildir',mail.path)}")
            
            Mail.objects.filter(mail_id=mail.id).update(timedate=mail.date)
            
        else : ListemailSQL(osp.join(path,file),i)
        
ListemailSQL()