from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=100)

    class Meta:
        ordering = ('full_name',)

    def __str__(self):
        return self.full_name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('title',)
    
    def __str__(self):
        return self.title
