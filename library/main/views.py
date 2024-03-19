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
    page_size = 20 


class BookViewSet(ModelViewSet): 
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE'] 
    queryset = Book.objects.order_by(F('download_count').desc(nulls_last=True)).prefetch_related('authors', 'languages', 'subjects', 'bookshelves', 'format_set')
    serializer_class = BookSerializer 
    pagination_class = CustomPagination
    permission_classes = [AllowAny, ] 
    filter_backends = (filters.DjangoFilterBackend, ) 
    filterset_class = BookFilter 
    

