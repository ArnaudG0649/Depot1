#!/bin/env python3

import re
import os
import django
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjetArnaud.settings') 
django.setup()

from monappli.models import Client, Page, Hit
from django.core.exceptions import ObjectDoesNotExist

print(Client.objects.all())
L=[str(i) for i in Client.objects.all()] ; print(L)
print(f"{('193.132.89.52' in Client.objects.all())=}")
print(f"{('193.132.89.52' in L)=}")
print(f"{('193.132.89.60' in L)=}")


Client.objects.all().delete()
Page.objects.all().delete()
Hit.objects.all().delete()


dateheure=r'12/Feb/2018:03:27:48'


def formatdateheure(dateheure):
    date=dateheure[:11]
    heure=dateheure[12:]
    date=date.split(r"/")
    date2="-".join([date[2],"02",date[0]])+" "+heure
    return date2

print(formatdateheure(dateheure))