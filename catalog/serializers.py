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


from .models import Book, BorrowedBook

# serializers.py
from rest_framework import serializers
from .models import BorrowedBook

class BorrowedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBook
        fields = ['id', 'book', 'borrower', 'borrowed_date']

    # Optionally, you can include additional fields or customize serializer behavior.
    # For example, you might want to display the book details along with the borrowed book.

    # Add a nested serializer for the Book model
    book = BookSerializer(read_only=True)

    # Include additional fields or customize behavior as needed
