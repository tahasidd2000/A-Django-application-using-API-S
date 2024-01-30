from rest_framework import serializers
from .models import Book
from .models import Book, BorrowedBook, Borrower, Language, Genre, Author
from .models import Book, BookInstance


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



class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    # genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all())

    genre = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_genre(self, obj):
        return [genre.name for genre in obj.genre.all()]

    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'summary', 'isbn', 'genre', 'language']

class BookInstanceSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = BookInstance
        fields = ['id', 'book', 'imprint', 'due_back', 'borrower', 'status']


# serializers.py
from rest_framework import serializers
from .models import Borrower

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = '__all__'
        
class BorrowedBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = BorrowedBook
        fields = ['id', 'book', 'borrower', 'borrowed_date']

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BookInstance

class BorrowBookSerializer(serializers.Serializer):
    book_id = serializers.UUIDField()
    user_name = serializers.CharField(max_length=100)

    def validate_book_id(self, value):
        try:
            book_instance = BookInstance.objects.get(id=value)
        except BookInstance.DoesNotExist:
            raise serializers.ValidationError("Book with this ID does not exist.")
        
        return value

    def create(self, validated_data):
        book_id = validated_data['book_id']
        user_name = validated_data['user_name']

        # Check if the user already exists
        user, created = User.objects.get_or_create(username=user_name)

       
        some_result = f"Book {book_id}"
        return some_result



from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}



