from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.BooksList.as_view(), name='books_list'),
    path('authors/', views.AuthorsList.as_view(), name='authors_list'),
]
