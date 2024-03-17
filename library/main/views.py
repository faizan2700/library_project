from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import AllowAny 
from rest_framework.pagination import PageNumberPagination 

from main.models import Book 
from main.serializers import BookSerializer 

class BookViewSet(ModelViewSet): 
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE'] 
    queryset = Book.objects.all() 
    serializer_class = BookSerializer 
    pagination_class = PageNumberPagination 
    permission_classes = [AllowAny, ] 
    
