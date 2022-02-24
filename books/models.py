from django.db import models

class Book(models.Model):
    isbn= models.CharField(max_length=13)
    category= models.ForeignKey('categories.Category',related_name='books',on_delete=models.CASCADE)
    name= models.CharField(max_length=255)
    description= models.TextField()
    language= models.CharField(max_length=255)
    pages= models.IntegerField()
    year_published= models.IntegerField()
    publisher= models.CharField(max_length=255)