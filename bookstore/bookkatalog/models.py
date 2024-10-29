from django.db import models
from django.template.context_processors import request


class Author(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    price = models.FloatField()
    genre = models.CharField(max_length=50, null=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)
    image = models.FileField(upload_to='book_img', null=True)

    def __str__(self):
        return f'{self.title}'


class Review(models.Model):
    review = models.TextField()
    book = models.ForeignKey('Book', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.book}'



# https://www.barnesandnoble.com/w/frankenstein-shelley-mary/1126911566?ean=9781435159624