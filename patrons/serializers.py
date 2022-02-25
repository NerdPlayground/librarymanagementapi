from patrons.models import Patron
from rest_framework import serializers
from possessed_books.models import PossessedBook

class RegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(min_length=8,max_length=20,write_only=True)
    class Meta:
        model= Patron
        fields= ["student","username","email","password"]
    
    def create_user(self,validated_data):
        return Patron.objects.create(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password= serializers.CharField(min_length=8,max_length=20,write_only=True)
    class Meta:
        model= Patron
        fields= ["username","password"]


class PatronSerializer(serializers.ModelSerializer):
    possessedbooks= serializers.PrimaryKeyRelatedField(many=True,queryset=PossessedBook.objects.all())
    class Meta:
        model= Patron
        fields= ["student","username","possessedbooks"]