from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        field = (
            'title',
            'author',
            'publisher',
            'publish_year',
            'no',
            'location',
            'serial_num',
            'status',
            'returnDate',
        )