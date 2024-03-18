from django.contrib import admin

# Register your models here.
from .models import Client,Page,Hit

admin.site.register(Client) 
admin.site.register(Page)
admin.site.register(Hit) 

