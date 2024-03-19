# from django.db.models import Q 

# from django_filters import rest_framework as filters 

# from main.models import Book 

# class BookFilter(filters.FilterSet): 
#     gutenberg_id=filters.CharFilter(method='search_multiple_ids', label='gutenberg_ids') 
#     media_type=filters.CharFilter(method='search_multiple_mediatypes', label='mediatype') 
#     title = filters.CharFilter(method='search_multiple_titles', label='titles') 
#     language = filters.CharFilter(method='search_multiple_languages', label='languages') 
#     author = filters.CharFilter(method='search_multiple_authors', label='authors') 
#     topic = filters.CharFilter(method='search_multiple_topics', label='topics')  

#     class Meta: 
#         model = Book 
#         fields = list() 

#     def search_multiple_ids(self, qs, name, value): 
#         return qs.filter(gutenberg_id__in=value.split(',')) 
    
#     def search_multiple_media_types(self, qs, name, value): 
#         return qs.filter(mediatype__in=value.split(',')) 

#     def search_multiple_titles(self, qs, name, value): 
#         return qs.filter(title__in=value.split(',')) 

#     def search_multiple_languages(self, qs, name, value):
#         return qs.filter(booklanguages__language__code__in=value.split(',')) 
    
#     def search_multiple_authors(self, qs, name, value): 
#         return qs.filter(bookauthors__author__name__in=value.split(',')) 

#     def search_multiple_topics(self, qs, name, value): 
#         q = Q() 
#         values = value.split(',') 
#         for value in values: 
#             q |= Q(booksubjects__subject__name__icontains=value) | Q(bookshelves__bookshelf__name__icontains=value) 
#         qs = qs.filter(q)  
#         return qs 