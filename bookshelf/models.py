from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_year = models.IntegerField()
    isbn = models.IntegerField(unique=True)
