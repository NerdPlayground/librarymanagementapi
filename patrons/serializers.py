from rest_framework import serializers
from django.contrib.auth.models import User
from possessed_books.models import PossessedBook

class RegisterSerializer(serializers.ModelSerializer):
    password= serializers.CharField(min_length=8,max_length=20,write_only=True)
    class Meta:
        model= User
        fields= ["student","username","email","password"]
    
    def create_user(self,validated_data):
        return User.objects.create(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password= serializers.CharField(min_length=8,max_length=20,write_only=True)
    class Meta:
        model= User
        fields= ["username","password"]


class UserSerializer(serializers.ModelSerializer):
    possessedbooks= serializers.PrimaryKeyRelatedField(many=True,queryset=PossessedBook.objects.all())
    class Meta:
        model= User
        fields= ["student","username","possessedbooks"]