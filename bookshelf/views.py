from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
)
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ViewSetMixin

from bookshelf.models import Book

from bookshelf.serializers import BookSerializer


class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


class BookViewSet(ViewSetMixin,
                  RetrieveAPIView,
                  UpdateAPIView,
                  DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
