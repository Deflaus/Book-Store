from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''
    Админ панель для модели Заказ книги
    '''

    list_display = [
        'user',
        'book',
        'phone_number',
        'comment',
        'created',
    ]
    list_filter = [
        'user',
        'book',
        'phone_number',
        'comment',
        'created',
    ]

