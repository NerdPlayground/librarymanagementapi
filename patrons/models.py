from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import PermissionsMixin,AbstractUser

class Patron(AbstractUser,PermissionsMixin):
    student= models.OneToOneField('students.Student',related_name='patron',on_delete=models.CASCADE)