from rest_framework import serializers
from .models import Book,Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

#source is the related_name of the foreign key
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(read_only=True,many=True,source='Books')
    class Meta:
        model = Author
        fields='__all__'