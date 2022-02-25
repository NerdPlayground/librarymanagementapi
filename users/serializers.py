from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ["id","first_name","last_name","username","registration_number","campus","faculty","course","mode_of_study"]
    
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)