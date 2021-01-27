from rest_framework import serializers
from django.shortcuts import get_object_or_404
from .models import Order
from books.models import Book


class OrderSerializer(serializers.ModelSerializer):
    '''
    Сериализатор модели Заказ
    '''

    book = serializers.CharField(max_length=100) # Название книги

    class Meta:
        model = Order
        fields = ['book', 'phone_number', 'comment']
    
    def create(self, validated_data):
        validated_data['book'] = get_object_or_404(Book, title=validated_data['book'])
        return Order.objects.create(**validated_data)
