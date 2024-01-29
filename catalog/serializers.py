from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    language = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'summary', 'isbn', 'genre', 'language']


class CustomUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    full_name = serializers.CharField(source='get_full_name')
    

from .models import Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']


# serializers.py
from .models import Genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']
        

# serializers.py
from rest_framework import serializers
from .models import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'date_of_death']

