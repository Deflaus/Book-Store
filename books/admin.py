from django.contrib import admin
from books.models import Book, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    '''
    Админ панель для модели Автор
    '''

    list_filter = [
        'fio',
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    '''
    Админ панель для модели Книга
    '''

    list_display = [
        'author',
        'title',
        'price',
    ]
    list_filter = [
        'author',
        'title',
        'price',
    ]
    list_editable = [
        'price',
    ]
