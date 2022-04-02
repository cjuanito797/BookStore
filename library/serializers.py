from rest_framework import serializers

from .models import Book, category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "name",
            "get_absolute_url",
            "summary",
            "price",
            "get_image",
            "get_cover_art"

        )