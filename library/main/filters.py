from django.db.models import Q 

from django_filters import rest_framework as filters 

from main.models import Book 

class BookFilter(filters.FilterSet): 
    title = filters.CharFilter(field_name='title', lookup_expr='icontains') 
    language = filters.CharFilter(field_name='booklanguages__language__code', lookup_expr='icontains', label='language') 
    author = filters.CharFilter(field_name='bookauthors__author__name', lookup_expr='icontains', label='author') 
    topic = filters.CharFilter(method='search_topic', label='topic') 

    class Meta: 
        model = Book 
        fields = ['gutenberg_id', 'media_type', 'language', 'author']

    def search_topic(self, qs, name, value): 
        qs = qs.filter(Q(booksubjects__subject__name__icontains=value) | Q(bookshelves__bookshelf__name__contains=value)) 
        return qs 