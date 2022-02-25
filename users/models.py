from django.db import models
from django.contrib.auth.models import PermissionsMixin,AbstractUser

class User(AbstractUser,PermissionsMixin):
    faculty= models.CharField(max_length=255)
    course= models.CharField(max_length=255)
    registration_number= models.CharField(max_length=8,unique=True)
    campus= models.CharField(max_length=255)
    mode_of_study= models.CharField(max_length=255)