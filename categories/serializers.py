from rest_framework import serializers
from categories.models import Category

class CategorySerializer(serializers.ModelSerializer):
    books= serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model= Category
        fields= ["name","description","total_books","books"]