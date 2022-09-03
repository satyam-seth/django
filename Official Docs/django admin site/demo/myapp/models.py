from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=10)
    birth_date = models.DateField(blank=True, null=True)


class Book(models.Model):
    author = models.ManyToManyField(Author)
    name = models.CharField(max_length=100)