from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    registration_number= models.CharField(max_length=8,unique=True)
    campus= models.CharField(max_length=255)
    faculty= models.CharField(max_length=255)
    course= models.CharField(max_length=255)
    mode_of_study= models.CharField(max_length=255)