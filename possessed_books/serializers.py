from rest_framework import serializers
from possessed_books.models import PossessedBook

class PossessedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model= PossessedBook
        fields= ["book","student","due_date","return_delay_fine"]
        read_only_fields= ["student","due_date","return_delay_fine"]