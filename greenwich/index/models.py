from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phonenumber = models.CharField(max_length=16)
    phonenumber.null = True
    phonenumber.blank = True
    datebirth = models.DateField()
    datebirth.null = True
    datebirth.blank = True
    gender = models.CharField(max_length=10)
    gender.choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    gender.null = True
    gender.blank = True
