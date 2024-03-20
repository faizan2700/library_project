# from django.db.models import Q 

# from django_filters import rest_framework as filters 

# from main.models import Book 

# class BookFilter(filters.FilterSet): 
#     gutenberg_id=filters.CharFilter(method='search_multiple_ids', label='gutenberg_id') 
#     mime_type=filters.CharFilter(method='search_multiple_mime_types', label='mime_type') 
#     title = filters.CharFilter(method='search_multiple_titles', label='title') 
#     language = filters.CharFilter(method='search_multiple_languages', label='language') 
#     author = filters.CharFilter(method='search_multiple_authors', label='author') 
#     topic = filters.CharFilter(method='search_multiple_topics', label='topic')  

#     class Meta: 
#         model = Book 
#         fields = list() 

#     def search_multiple_ids(self, qs, name, value): 
#         return qs.filter(gutenberg_id__in=value.split(',')) 
    
#     def search_multiple_languages(self, qs, name, value):
#         return qs.filter(languages__code__in=value.split(',')) 
    
#     def search_multiple_mime_types(self, qs, name, value): 
#         return qs.filter(format__mime_type__in=value.split(',')) 

#     def search_multiple_topics(self, qs, name, value): 
#         q = Q() 
#         values = value.split(',') 
#         for value in values: 
#             q |= Q(subjects__name__icontains=value) | Q(bookshelves__name__icontains=value) 
#         qs = qs.filter(q)  
#         return qs 
    
#     def search_multiple_authors(self, qs, name, value):
#         values = value.split(',') 
#         q = Q() 
#         for value in values: 
#             q |= Q(authors__name__icontains=value)  
#         return qs.filter(q) 

#     def search_multiple_titles(self, qs, name, value): 
#         q = Q() 
#         values = value.split(',') 
#         for value in values: 
#             q |= Q(title__icontains=value) 
#         return qs.filter(q) 