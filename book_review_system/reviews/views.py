from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Book, Review
from .serializers import BookSerializer, ReviewSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book=self.kwargs['book_pk'])

from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Book Review System API. Navigate to /api/ for the API.")
