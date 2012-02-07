from django.db import models
import django.contrib.auth.models as authmodels
from django.contrib import admin
from django.conf import settings
import time

# Create your models here.
class Email(models.Model):
   address = models.CharField(max_length=250)
    
