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
















