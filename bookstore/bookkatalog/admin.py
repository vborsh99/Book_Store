from django.contrib import admin
from .models import Book, Author
# Tito 11qaz@@WSX

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','author', 'genre']
    search_fields = ['title']





