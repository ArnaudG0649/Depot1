#!/bin/env python3

import re
import os
import os.path as osp 
import datetime as dt
import django
import matplotlib.pyplot as plt
import pandas as pds

#'django_extensions' ##Pour éxecuter la commande au projet
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projetenron.settings') 
django.setup()

from app1.models import Employee,Emailadress,Mail,To,Cc #,Re
from django.core.exceptions import ObjectDoesNotExist

from django.db import connection

with connection.cursor() as cursor:
    cursor.execute(
    """
    SELECT lastname,firstname,nbmail FROM
    (SELECT emp.lastname,emp.firstname, COUNT(*) as nbmail   
        FROM app1_emailadress ea
        INNER JOIN app1_employee emp
            ON emp.employee_id=ea.employee_id_id
        INNER JOIN app1_to t
            ON t.emailadress_id_id=ea.emailadress_id
        INNER JOIN app1_mail m 
            ON m.mail_id=t.mail_id_id
        WHERE Timedate > '2001-01-01 00:00:00'
        GROUP BY emp.employee_id
    ) T
    WHERE nbmail>100
    """)
    result=cursor.fetchall()
    columns = [col[0] for col in cursor.description] 
    
DF=pds.DataFrame(result,columns=columns)
print(DF)
