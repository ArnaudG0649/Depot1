#!/bin/env python3

# import re 

# # ListeLigne=[]
# # with open("access.log","r") as file : 
# #     for l in file : 
# #         ListeLigne.append(l)
        

# ##ip
# pattern = re.compile(r'^(\S+)\s')           # regex à trouver
# echecs = []                           # initialisation à finir
# with open("access.log","r") as f:
#   for line in f:
#     found = pattern.search(line.strip())
#     if found:
#       print(found.groups())
#     else:
#       echecs += [line]

# print(f"\nlignes en échec de découpage : \n{echecs}")
        
# def reglog(s) : 
#     pattern = re.compile(s)           # regex à trouver
    
#     echecs = []                           # initialisation à finir
#     with open("access.log","r") as f:
#       for line in f:
#         found = pattern.search(line.strip())
#         if found:
#           print(found.groups())
#         else:
#           echecs += [line]
    
#     print(f"\nlignes en échec de découpage : \n{echecs}")

# ##timestamp    
# reglog('\[(.*)\]')

# ##page_url
# reglog('[^"]*"([^"]*)"')

# ##referer
# reglog('"{2}([^"]*)"')


###Correction###



import re
import os
import django
import datetime

#'django_extensions' ##Pour éxecuter la commande au projet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjetArnaud.settings') 
django.setup()


from monappli.models import Client, Page, Hit
from django.core.exceptions import ObjectDoesNotExist

pattern = re.compile(r'^(\S+).+\[(\S+) .*"(?:GET|POST) (.*?) HTTP.*?".*?"(.*?)"')

echecs = []
k=0
Lip=[str(i) for i in Client.objects.all()]
Lpath=[str(i) for i in Page.objects.all()]

with open("access.log", encoding="utf-8") as f:
    for line in f:
        found = pattern.search(line.strip())
        if not found:
          echecs += [line]
          continue

        print(found.groups())
                
        ip = found.group(1)
        if ip not in Lip :
            Lip.append(ip)
            cl = Client(client_ip=ip)
            cl.save()
        cl = Client.objects.get(client_ip=ip)
    

        path = found.group(3)
        if path not in Lpath :
            Lpath.append(path)
            p = Page(page_url=path)
            p.save()
        p = Page.objects.get(page_url=path)
            
        time_raw=found.group(2)
        date=time_raw[:11]
        heure=time_raw[12:]
        date=date.split(r"/")
        time="-".join([date[2],"02",date[0]])+" "+heure
        
        ref = found.group(4)
        h = Hit(timestamp=time,client=cl,page=p,referer=ref)
        h.save()
        

print(Page.objects.all()[0:min(20,len(Page.objects.all()))])
print(f"{len(echecs)} lignes écartées")

#####Correction#####

# from monappli.models import Client, Page, Hit

# pattern = re.compile(r'^(\S+).+\[(\S+) .*"(?:GET|POST) (.*?) HTTP.*?".*?"(.*?)"')

# echecs = []
# with open("accesslog", encoding="utf-8") as f:
#     for line in f:
#         found = pattern.search(line.strip())
#         if not found:
#           echecs += [line]
#           continue

#         print(found.groups())

#         ip = found.group(1)
#         try:                                     # cette IP existe-t-elle dejà ?
#           cl = Client.objects.get(client_ip=ip)  # elle existe, on ne fait rien de plus
#         except ObjectDoesNotExist as err:        # elle n'existe pas, donc on la crée
#           cl = Client(client_ip=ip)
#           cl.save()
#           print(f"ajout: ip={ip}")
        
#         path = found.group(3)
#         p = Page(page_path=path)
#         p.save()

#         time = found.group(2)
#         ref = found.group(4)
#         h = Hit(timestamp=time,client=cl,page=p,referer=ref)
#         h.save()

# print(f"{len(echecs)} lignes écartées")

#'monappli.apps.MonappliConfig',



