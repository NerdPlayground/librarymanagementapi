from patrons.models import Patron
from rest_framework import serializers

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
    class Meta:
        model= Patron
        fields= ["student","username"]