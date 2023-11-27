from django.urls import path

from bookshelf.views import BookListView, BookCreateView, BookViewSet

urlpatterns = [
    path('books_list/', BookListView.as_view()),
    path('book_create/', BookCreateView.as_view()),
    path('book/<int:pk>/', BookViewSet.as_view({
        'get': 'retrieve',
        'delete': 'destroy',
        'patch': 'partial_update',
        'put': 'update'
    })),
]
