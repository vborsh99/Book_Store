from django.contrib import admin
from .models import Book, Author

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','author', 'genre']
    search_fields = ['title']


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)