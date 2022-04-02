from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Book



# Create your views here.
class LatestBooksList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()[0:4]
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
