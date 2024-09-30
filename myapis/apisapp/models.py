from django.db import models
from django.contrib.auth.models import User 
from . db_connection import db 
from datetime import datetime
# Create your models here.
person_collection = db['Person']

class Messages(models.Model):
    name = models.CharField(max_length=40, default='')
    email = models.EmailField(default='gideonushindi94@gmail.com')
    message = models.CharField(max_length=2000, default='')

class User(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, default='0710101021')
    password = models.CharField(max_length=10)
    admission_no = models.IntegerField(default=0)
    classteacher = models.CharField(max_length=50, default='none')
    form = models.IntegerField(default=0)
    billed = models.IntegerField(default=0)
    paid = models.IntegerField(default=0)

class Message(models.Model):
    message = models.CharField(max_length=2000, default='no message')
    time = models.DateTimeField(default=datetime.now, blank=True)

#start of apis
class Store(models.Model):
    name = models.CharField(max_length=30, default='Nameless')
    email = models.EmailField(default='john@example.com')
    year = models.IntegerField(default=2024)

class Forest(models.Model):
    county = models.CharField(max_length=40, default="County")
    forest = models.CharField(max_length=40, default="forest_name")
    area_square = models.DecimalField(decimal_places=2, max_digits=10)
#end of apis

#for the bus app 

class Bus(models.Model):
    route = models.CharField(max_length=20, default='None')
    time = models.TimeField(default='00:00')    
    cost = models.IntegerField(default=0)
    seats = models.IntegerField(default=0)

class Coins(models.Model):
    username = models.CharField(max_length=45, default="username")
    email = models.EmailField(default="example@gmail.com")
    password = models.CharField(max_length=10,default="password")
    personID = models.IntegerField(default=0)
    coins = models.IntegerField(default=0)


