from django.contrib import admin

from bookshelf.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'publish_year',
        'isbn',
    )
