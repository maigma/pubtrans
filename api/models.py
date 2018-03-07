from django.db import models
import datetime

# Create your models here.

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class AppUsersModel(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=128,null=False) 
#    last_login = models.DateTimeField(default=datetime.date.today)
    username = models.CharField(max_length=50, default=' ')
    email = models.EmailField(max_length=70,blank=True)
#    date_joined = models.DateTimeField(default=datetime.date.today)
    

class AppStopsModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=False)
    address = models.CharField(max_length=150, null=False)
    latitude = models.FloatField() # max_digits=8, decimal_places=6
    longitude = models.FloatField() # max_digits=9, decimal_places=6
    user_id = models.IntegerField(null=False)

    
    
