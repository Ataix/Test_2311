from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
)
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ViewSetMixin

from .models import Book

from .serializers import BookSerializer


class BookListView(ListAPIView):
    """
    Basic book object list view
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(CreateAPIView):
    """
    Basic book object create view
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


class BookViewSet(ViewSetMixin,
                  RetrieveAPIView,
                  UpdateAPIView,
                  DestroyAPIView):
    """
    Basic view set
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]
