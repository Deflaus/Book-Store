from django.contrib import admin
from books.models import Book, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = [
        'full_name',
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
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
