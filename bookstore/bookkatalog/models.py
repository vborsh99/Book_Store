from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    title = models.CharField(max_length=50)
    overview = models.TextField()
    price = models.FloatField()
    genre = models.CharField(max_length=50, null=True)
    published_date = models.DateField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True)





# https://www.barnesandnoble.com/w/frankenstein-shelley-mary/1126911566?ean=9781435159624