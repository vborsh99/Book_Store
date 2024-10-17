from . import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('books', views.books, name='books'),
    path('book_detail/<int:book_id>', views.book_detail, name='book_detail')
]