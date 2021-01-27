from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    '''
    Сериализатор модели Книга
    '''

    class Meta:
        model = Book
        fields = ['title']


class AuthorSerializer(serializers.ModelSerializer):
    '''
    Сериализатор модели Автор
    '''

    books = BookSerializer(many=True, read_only=True)
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['fio', 'books', 'books_count']
    
    def get_books_count(self, obj):
        return obj.books.count()
