from django.shortcuts import render
from django.db.models import F 

from rest_framework.viewsets import ModelViewSet 
from rest_framework.permissions import AllowAny 
from rest_framework.pagination import PageNumberPagination 

from main.models import Book 
from main.serializers import BookSerializer 

class CustomPagination(PageNumberPagination):
    page_size = 20 


class BookViewSet(ModelViewSet): 
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE'] 
    queryset = Book.objects.all().order_by(F('download_count').desc(nulls_last=True)) 
    serializer_class = BookSerializer 
    pagination_class = CustomPagination
    permission_classes = [AllowAny, ] 

