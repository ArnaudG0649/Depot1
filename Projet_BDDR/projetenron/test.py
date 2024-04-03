#!/usr/bin/env python3

import re
import os 
import os.path as osp 
import datetime
from chercheur_mails import Mailobj

import django

#'django_extensions' ##Pour éxecuter la commande au projet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetenron.settings') 
django.setup()

from app1.models import Employee,Emailadress,Mail,To,Cc,Re

from django.core.exceptions import ObjectDoesNotExist

#reponse=Mail.objects.all(emailadress_id_id="mike.carson@enron.com")
# reponse=Mail.objects.all().filter(emailadress_id_id="mike.carson@enron.com")
# print(reponse)

Lmois=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

nummois=Lmois.index("Jan")+1
delta=datetime.timedelta(hours=-8)
zone=datetime.timezone(delta)
dt=datetime.datetime(2002,nummois,day=25, hour=5, minute=45,tzinfo=zone) #second=int(d[4][6:]), tzinfo=zone)

# reponse=Mail.objects.all().filter(timedate__date=datetime.date(2002,nummois,25),timedate__hour=5)
# print(reponse)

Mailbase=Mailobj("/users/2024/ds1/122005148/Bureau/projet_BDDR/projetenron/9.")
print(dt.year)
#subject="Lets get this ball rolling....",
reponse=Mail.objects.all().filter(subject="Lets get this ball rolling....")#timedate__date=datetime.date(2002,nummois,25))#,timedate__hour=5,timedate__minute=45)
print(reponse)