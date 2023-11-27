from rest_framework import serializers

from bookshelf.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'name',
            'author',
            'publish_year',
            'isbn'
        )
