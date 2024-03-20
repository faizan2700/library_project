# from rest_framework.serializers import ModelSerializer, SerializerMethodField
# from main.models import Book, Author, Language, Subject, Bookshelf, Format

# class AuthorSerializer(ModelSerializer): 
#     class Meta:
#         model = Author 
#         fields = '__all__' 

# class LanguageSerializer(ModelSerializer): 
#     class Meta: 
#         model = Language 
#         fields = '__all__' 

# class SubjectSerializer(ModelSerializer): 
#     class Meta: 
#         model = Subject 
#         fields = '__all__' 
    
# class ShelfSerializer(ModelSerializer): 
#     class Meta: 
#         model = Bookshelf 
#         fields = '__all__'  

# class FormatSerializer(ModelSerializer): 
#     class Meta: 
#         model = Format 
#         fields = '__all__' 
    

# class BookSerializer(ModelSerializer): 
#     authors = SerializerMethodField() 
#     languages = SerializerMethodField() 
#     subjects = SerializerMethodField() 
#     shelves = SerializerMethodField() 
#     formats = SerializerMethodField() 
#     class Meta: 
#         model = Book 
#         fields = ('gutenberg_id', 'title', 'authors', 'languages', 'subjects', 'shelves', 'formats', 'download_count')

#     def get_authors(self, book): 
#         return book.authors.all().values_list('name', flat=True) 
    
#     def get_languages(self, book): 
#         return book.languages.all().values_list('code', flat=True) 
    
#     def get_subjects(self, book): 
#         return book.subjects.all().values_list('name', flat=True) 

#     def get_shelves(self, book): 
#         return book.bookshelves.all().values_list('name', flat=True)   
    
#     def get_formats(self, book): 
#         return Format.objects.filter(book=book).values_list('url', flat=True) 
        