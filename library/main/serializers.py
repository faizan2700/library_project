from rest_framework.serializers import ModelSerializer, SerializerMethodField
from main.models import Book, Author, BookAuthors, BookLanguages, Language, Subject, Bookshelf, Bookshelves, BookSubjects, Format

class AuthorSerializer(ModelSerializer): 
    class Meta:
        model = Author 
        fields = '__all__' 

class LanguageSerializer(ModelSerializer): 
    class Meta: 
        model = Language 
        fields = '__all__' 

class SubjectSerializer(ModelSerializer): 
    class Meta: 
        model = Subject 
        fields = '__all__' 
    
class ShelfSerializer(ModelSerializer): 
    class Meta: 
        model = Bookshelf 
        fields = '__all__'  

class FormatSerializer(ModelSerializer): 
    class Meta: 
        model = Format 
        fields = '__all__' 
    

class BookSerializer(ModelSerializer): 
    authors = SerializerMethodField() 
    languages = SerializerMethodField() 
    subjects = SerializerMethodField() 
    shelves = SerializerMethodField() 
    formats = SerializerMethodField() 
    class Meta: 
        model = Book 
        fields = '__all__' 

    def get_authors(self, book): 
        qs1 = BookAuthors.objects.filter(book=book).values_list('author', flat=True) 
        qs2 = Author.objects.filter(id__in=qs1) 
        # return AuthorSerializer(qs2, many=True).data 
        return qs2.values_list('name', flat=True) 
    
    def get_languages(self, book): 
        qs1 = BookLanguages.objects.filter(book=book).values_list('language', flat=True) 
        qs2 = Language.objects.filter(id__in=qs1)
        # return LanguageSerializer(qs2, many=True).data 
        return qs2.values_list('code', flat=True) 
    
    def get_subjects(self, book): 
        qs1 = BookSubjects.objects.filter(book=book).values_list('subject', flat=True) 
        qs2 = Subject.objects.filter(id__in=qs1) 
        # return SubjectSerializer(qs2, many=True).data 
        return qs2.values_list('name', flat=True) 

    def get_shelves(self, book): 
        qs1 = Bookshelves.objects.filter(book=book).values_list('bookshelf', flat=True) 
        qs2 = Bookshelf.objects.filter(id__in=qs1)  
        # return ShelfSerializer(qs2, many=True).data 
        return qs2.values_list('name', flat=True)   
    
    def get_formats(self, book):
        qs1 = Format.objects.filter(book=book) 
        # return FormatSerializer(qs1, many=True).data 
        return qs1.values_list('mime_type', flat=True) 