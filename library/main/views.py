from django.shortcuts import render
from django.db.models import F 

from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import AllowAny 
from rest_framework.pagination import PageNumberPagination 

from django_filters import rest_framework as filters 

from main.models import Book 
from main.serializers import BookSerializer 
from main.filters import BookFilter 

class CustomPagination(PageNumberPagination):
    """ Custom pagination settings with a default page size of 20."""
    page_size = 20 


class BookViewSet(ModelViewSet): 
    """
    View set for managing books.

    This view set allows users to perform CRUD (Create, Retrieve, Update, Delete) operations
    on Book objects. It supports the following HTTP methods: GET, POST, PUT, DELETE.

    Attributes:
    - allowed_methods (list of str): List of HTTP methods allowed for this view set.
    - queryset (QuerySet): Query set representing the collection of Book objects to be displayed.
      The books are ordered by their download count in descending order, with nulls last.
      Related objects (authors, languages, subjects, bookshelves, format_set) are prefetched
      to optimize database queries.
    - serializer_class (Serializer): Serializer class used for serializing/deserializing Book objects.
    - pagination_class (Pagination): Pagination class used for paginating the queryset.
    - permission_classes (list of classes): List of permission classes that control access to this view set.
    - filter_backends (tuple of classes): Tuple of filter backend classes used for filtering the queryset.
    - filterset_class (class): Class defining the filterset used for filtering Book objects.

    Note:
    The `BookFilter` class should be defined separately and assigned to `filterset_class` to enable
    filtering functionality for Book objects.
    """
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE'] 
    queryset = Book.objects.order_by(F('download_count').desc(nulls_last=True)).prefetch_related('authors', 'languages', 'subjects', 'bookshelves', 'format_set')
    serializer_class = BookSerializer 
    pagination_class = CustomPagination
    permission_classes = [AllowAny, ] 
    filter_backends = (filters.DjangoFilterBackend, ) 
    filterset_class = BookFilter 
    

