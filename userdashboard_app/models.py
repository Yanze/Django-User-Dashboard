from django.db import models
from django import forms

# Create your models here.
class User(forms.Form):
    email = models.CharField(max_length=225)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    pwd = models.CharField(max_length=255)
