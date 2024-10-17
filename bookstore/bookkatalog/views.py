from django.shortcuts import render
from .models import Book


def home(request):
    return render(request, 'bookkatalog/home.html')


def books(request):
    book_list = Book.objects.all()

    return render(request, 'bookkatalog/book_list.html', context={ 'books':book_list})


def book_detail(request, book_id:int):
    book = Book.objects.get(id=book_id)
    return render(request, 'bookkatalog/book_detail.html', context={'book': book})