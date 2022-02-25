from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin,AbstractUser

class User(AbstractUser,PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=150, blank=False)
    last_name = models.CharField(_('last name'), max_length=150, blank=False)
    faculty= models.CharField(max_length=255)
    course= models.CharField(max_length=255)
    registration_number= models.CharField(max_length=8,unique=True)
    campus= models.CharField(max_length=255)
    mode_of_study= models.CharField(max_length=255)