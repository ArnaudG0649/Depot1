#!/bin/env python3

import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'monprojet.settings') 
django.setup()

from monappli.models import Client, Page, Hit 

for i in Hit.objects.all() : 
    print(i.client)
