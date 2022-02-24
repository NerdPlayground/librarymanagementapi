from pyexpat import model
from books.models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model= Book
        fields= ['isbn','category','name','description','language','pages','year_published','publisher']