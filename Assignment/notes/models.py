from datetime import datetime
from tkinter import CASCADE
from xmlrpc.client import boolean
from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


class Notes(models.Model):
    title = models.CharField(max_length=20, default="")
    text = models.CharField(max_length=200)
    date_created = models.DateField(default=str(date.today()))
    date_updated = models.DateField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    archive = models.BooleanField(default=False)
    sharedwith = models.ManyToManyField(User, related_name="shared", blank=True)

    def __str__(self):
        return self.text
