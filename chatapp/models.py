from email.policy import default
from django.db import models
from datetime import datetime

from django.forms import CharField, DateTimeField
# Create your models here.

class Room(models.Model):
    name=models.CharField(max_length=100)
class Message(models.Model):
    value=models.CharField(max_length=100000)
    user=models.CharField(max_length=100)
    room=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now, blank=True)