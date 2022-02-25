from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields=[
            "id","first_name","last_name",
            "registration_number","campus",
            "faculty","course","mode_of_study"
        ]