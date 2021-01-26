from django.db import models
from django.contrib.auth.models import User
from books.models import Book


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=11)
    comment = models.CharField(max_length=150, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id}'