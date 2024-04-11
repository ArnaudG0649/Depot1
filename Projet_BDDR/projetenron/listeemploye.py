#!/bin/env python3

import os
import django

#'django_extensions' ##Pour éxecuter la commande au projet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetenron.settings') 
django.setup()

from app1.models import Employee, Emailadress
from django.core.exceptions import ObjectDoesNotExist

import xml.etree.ElementTree as ET

# with open("employes_enron.xml", encoding="utf-8") as f:
#     for l in f:
        
tree = ET.parse('employes_enron.xml')
root = tree.getroot() #=employees

root.tag #Nom de l'élément

root.attrib
Listeemployees=[]
for employee in root:
    L=[]
    L.append(employee)
    # print(employee.tag, employee.attrib)
    for element in employee:
        L.append(element)
        # print(r'   |',element.tag, element.attrib)
    Listeemployees.append(L)
#On crée un tableau d'éléments de classe etree.ElementTree.Element, ou chaque ligne (L) correspond à un employé.    
    

# for E in Listeemployees :
#     print (E[0].tag,E[0].attrib)
#     for e in E[0:] : 
#         print("   |",e.tag,e.text,e.attrib)
        
        
      
Table_employees_mails=[]        
for i in range(len(Listeemployees)):
    L=Listeemployees[i] #Chaque i correspond à un employé
    Lemail=[e.attrib["address"] for e in L[3:-1]]
    # if len(L[0].attrib)>0 : 
    #     Enregistrement=[i,L[1].text,L[2].text,L[0].attrib['category'],L[-1].text,Lemail]
    # else : 
    #     Enregistrement=[i,L[1].text,L[2].text,None,L[-1].text,Lemail]
    # Table_employees_mails.append(Enregistrement)
    if len(L[0].attrib)>0 : 
        try:
            e=Employee.objects.get(employee_id=i+1, lastname=L[1].text, firstname=L[2].text, category=L[0].attrib['category'], mailbox=L[-1].text)
        except ObjectDoesNotExist:
            e=Employee(employee_id=i+1, lastname=L[1].text, firstname=L[2].text, category=L[0].attrib['category'], mailbox=L[-1].text)
            e.save()
            print(f"L'employé.e {L[2].text} {L[1].text} a été rajouté.e à la base de données.")
    else : 
        try:
            e=Employee.objects.get(employee_id=i+1, lastname=L[1].text, firstname=L[2].text, category=None, mailbox=L[-1].text)
        except ObjectDoesNotExist:
            e=Employee(employee_id=i+1, lastname=L[1].text, firstname=L[2].text, category=None, mailbox=L[-1].text)
            e.save()
            print(f"L'employé.e {L[2].text} {L[1].text} a été rajouté.e à la base de données.")
            
    for email_a in Lemail : 
        try : 
            ea=Emailadress.objects.get(employee_id=e, emailadress_id=email_a, interne=True)
        except ObjectDoesNotExist:  
            ea=Emailadress(employee_id=e, emailadress_id=email_a, interne=True)
            ea.save()
            
    #On rajoute un employé absent dans le fichier xml

    # e=Employee(employee_id=len(Listeemployees)+1, lastname="Mims-thurston", firstname="Patrice", category=None)
    # e.save()
    # print("L'employé Patrice Mims-thurston a été rajouté à la base de données.")

    # ea=Emailadress(employee_id=e, emailadress_id="patrice.mims@enron.com", interne=True)
    # ea.save() 
    # ea=Emailadress(employee_id=e, emailadress_id="pmims@enron.com", interne=True)
    # ea.save() 
    # ea=Emailadress(employee_id=e, emailadress_id="pmims@ect.enron.com", interne=True)
    # ea.save() 
    # ea=Emailadress(employee_id=e, emailadress_id="patrice.l.mims@enron.com", interne=True)
    # ea.save() 
    # ea=Emailadress(employee_id=e, emailadress_id="mims@enron.com", interne=True)
    # ea.save() 
    # ea=Emailadress(employee_id=e, emailadress_id="l..mims@enron.com", interne=True)
    # ea.save() 
            
            
#print(Table_employees_mails)
#Voilà on a une pseudo table.







































