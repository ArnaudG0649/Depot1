#!/usr/bin/env python3
import os
import django

#'django_extensions' ##Pour éxecuter la commande au projet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetenron.settings') 
django.setup()

from app1.models import Employee, Emailadress
from django.core.exceptions import ObjectDoesNotExist

import os.path as osp  

print(osp.join(os.getcwd(),"maildir/"))
print(len(os.listdir('/users/2024/ds1/122005148/Bureau/projet_BDDR/maildir')))

for mb in os.listdir('/users/2024/ds1/122005148/Bureau/projet_BDDR/maildir') :
    try : 
        print(mb, bool(Employee.objects.get(mailbox=mb)))
    except ObjectDoesNotExist : 
        print(mb)
    

