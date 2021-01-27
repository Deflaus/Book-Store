from django.db import models


class Author(models.Model):
    '''
    Модель Автора
    '''

    fio = models.CharField(max_length=100)

    class Meta:
        ordering = ('fio',)

    def __str__(self):
        return self.fio


class Book(models.Model):
    '''
    Модель Книга
    '''

    author = models.ForeignKey(Author, related_name='books', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return self.title
