#!/bin/env python3

import re
import os
import os.path as osp 
import datetime as dt
import django
import xml.etree.ElementTree as ET

#'django_extensions' ##Pour éxecuter la commande au projet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetenron.settings') 
django.setup()

from app1.models import Employee,Emailadress,Mail,To,Cc #,Re
from django.core.exceptions import ObjectDoesNotExist

from django.db import connection

jour=dt.datetime(2001,10,1)

with connection.cursor() as cursor:
    cursor.execute(
    """
    SELECT COUNT(T.mail_id) FROM (
    SELECT m.mail_id, m.subject, m.emailadress_id_id, t.dest_interne, aut.interne as exp_interne FROM app1_mail m 
        INNER JOIN 
        (SELECT t.mail_id_id, bool_and(ea.interne) as dest_interne FROM app1_to t
        INNER JOIN app1_emailadress ea ON ea.emailadress_id=t.emailadress_id_id 
        GROUP BY t.mail_id_id
        ) t ON t.mail_id_id=m.mail_id
        INNER JOIN app1_emailadress aut ON aut.emailadress_id=m.emailadress_id_id
        WHERE (m.Timedate BETWEEN %s AND %s) AND ((aut.interne=True AND t.dest_interne=false) OR (aut.interne=False AND t.dest_interne=True)) /*OU exclusive, au soit le destinataire ou soit l'expéditeur est interne mais pas les deux*/
    ) T
    """,[str(jour),str(jour+dt.timedelta(days=1))])
    nb_internes_externes = cursor.fetchone()
    
with connection.cursor() as cursor:
    cursor.execute(
    """
    SELECT COUNT(T.mail_id) FROM (
    SELECT m.mail_id, m.subject, m.emailadress_id_id, t.dest_interne, aut.interne as exp_interne FROM app1_mail m 
        INNER JOIN 
        (SELECT t.mail_id_id, bool_and(ea.interne) as dest_interne FROM app1_to t
        INNER JOIN app1_emailadress ea ON ea.emailadress_id=t.emailadress_id_id 
        GROUP BY t.mail_id_id
        ) t ON t.mail_id_id=m.mail_id
        INNER JOIN app1_emailadress aut ON aut.emailadress_id=m.emailadress_id_id
        WHERE (m.Timedate BETWEEN %s AND %s) AND (aut.interne=True AND t.dest_interne=True) 
    ) T
    """,[str(jour),str(jour+dt.timedelta(days=1))])
    nb_internes = cursor.fetchone()
    
print([jour,nb_internes_externes,nb_internes,nb_internes_externes+nb_internes])

# t1=dt.timedelta(hours=23)
# t2=dt.timedelta(hours=2)
# t3=t1+t2

# t0=dt.datetime(2001, 2, 2)
# print(t0)
# print(t0+t3)

# str(t0)


####Req_6####


with connection.cursor() as cursor:
    cursor.execute(
    """
    SELECT m.path, m.emailadress_id_id as auteur, m.subject, m.timedate FROM app1_mail m
        LEFT JOIN 
        (SELECT ea.emailadress_id, ea.interne, emp.firstname, emp.lastname FROM app1_emailadress ea /*Cette sous-requête récupère tout ce qui concerne les auteurs*/
            LEFT JOIN app1_employee emp ON emp.employee_id=ea.employee_id_id) aut 
        ON aut.emailadress_id=m.emailadress_id_id
        LEFT JOIN 
        (SELECT t.mail_id_id, bool_and(ea2.interne) as interne FROM app1_to t /*Cette sous-requête permet de dire si un mail a été envoyé qu'à des destinataires internes ou s'il y a un destinataires externes dans le mail*/
            INNER JOIN app1_emailadress ea2 
                ON t.emailadress_id_id=ea2.emailadress_id 
            GROUP BY t.mail_id_id ) dint 
        ON m.mail_id=dint.mail_id_id
        LEFT JOIN
        (SELECT t.mail_id_id, t.emailadress_id_id, eadest.firstname, eadest.lastname FROM app1_to t /*Cette sous-requête récupère tout ce qui concerne les destinataires*/
            LEFT JOIN 
            (SELECT ea.emailadress_id, emp.firstname, emp.lastname FROM app1_emailadress ea 
                LEFT JOIN app1_employee emp ON emp.employee_id=ea.employee_id_id) eadest
            ON t.emailadress_id_id=eadest.emailadress_id ) dest 
        ON m.mail_id=dest.mail_id_id
        WHERE m.Timedate > '2000-01-01' AND dest.firstname='Jeff' AND dest.lastname='King' AND aut.interne=False /*Ensuite on filtre ce qu'on veut*/
    GROUP BY m.path, m.emailadress_id_id, m.subject, m.timedate 
    """)
    result=cursor.fetchall()
    columns = [col[0] for col in cursor.description]

print(len(result))
print(dict([(columns[j],[result[0][j]]) for j in range(len(columns)-1)]+[(columns[3],[str(result[0][3])])]))

#DF=pds.FataFrame({columns[0]:result[0][0],columns[0]:result[0][0]})
#print(result.description) 
# columns = [col[0] for col in cursor.description]
# [dict(zip(columns, row)) for row in cursor.fetchall()]
DF=pds.DataFrame(dict([(columns[j],[result[0][j]]) for j in range(len(columns))]))
print(DF)

#dict([(columns[j],result[i][j]) for j in range(len(columns))])

for i in range(1,len(result)) : 
    DF=pds.concat((DF,pds.DataFrame(dict([(columns[j],[result[i][j]]) for j in range(len(columns))]), index=[i])))

print(DF)


# for i in range(1,n) : 
#     DF=pds.concat((DF,pds.DataFrame(dict([(columns[j],[result[i][j]]) for j in range(len(columns))]), index=[i])))
#     print(f"concaténation à {round(100*(i+1)/n,2)}{r'%'}")
    
# DF['OneFind']=[False for i in range(n)]
# DF['AllFind']=[False for i in range(n)]
# DF['Line']=[set(()) for i in range(n)]



# listelignemot=set(()) #=DF['Line'][i]
# mot=["have","I","feel"]
# motfind=[False for i in mot]

# try : 
#     with open("/users/2024/ds1/122005148/Bureau/projet_BDDR/ex_reponses/288.","r") as file :
#         Lignes=[ligne for ligne in file]
# except UnicodeDecodeError :
#     with open("/users/2024/ds1/122005148/Bureau/projet_BDDR/ex_reponses/288.","rb") as file :
#         Lignes=str(file.read()).split(r'\n')
# nblignes=len(Lignes)

# entexte=False
# fini=False
# k=0
# while k in range(nblignes) and not fini :
#     if not entexte : 
#         if Lignes[k]=='\n' : entexte=True
#     else :        
#         if re.search(r"---------------------- Forwarded",Lignes[k]) or re.search(r"-----Original Message-----",Lignes[k]) : 
#             fini=True
#         else : 
#             for m in range(len(mot)) : 
#                 motfind[m]=motfind[m] or bool(re.search(mot[m],Lignes[k]))
#                 if bool(re.search(mot[m],Lignes[k])) : listelignemot.add(k+1)
#     print(k+1,listelignemot)
#     k+=1
# totfind=all(motfind) #=DF['AllFind'][i]
# #DF['OneFind']=len(listelignemot>0)
# print(totfind)

# Lignes[15]
#carson-m/all_documents/149. ex fw
#'/carson-m/all_documents/149.'[1:]
#"mims-thurston-p/all_documents/9."
#osp.join(os.getcwd(),osp.join('maildir','carson-m/all_documents/149.'))









