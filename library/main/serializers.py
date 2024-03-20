from rest_framework.serializers import ModelSerializer, SerializerMethodField
from main.models import Book, Author, Language, Subject, Bookshelf, Format

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
    """
    Serializer class for serializing Book objects.

    This serializer class converts Book model instances into JSON representations
    and vice versa. It includes fields for 'gutenberg_id', 'title', 'authors', 'languages',
    'subjects', 'shelves', 'formats', and 'download_count' of a Book object.

    SerializerMethodField() is used for customizing serialization of related many to many fields:
    - 'authors': Returns a list of author names associated with the book.
    - 'languages': Returns a list of language codes associated with the book.
    - 'subjects': Returns a list of subject names associated with the book.
    - 'shelves': Returns a list of shelf names associated with the book.
    - 'formats': Returns a list of URLs for book formats associated with the book.

    Note:
    This serializer relies on methods prefixed with 'get_' to customize serialization
    of related fields. These methods should be defined within the serializer class.
    """
    authors = SerializerMethodField() 
    languages = SerializerMethodField() 
    subjects = SerializerMethodField() 
    shelves = SerializerMethodField() 
    formats = SerializerMethodField() 
    class Meta: 
        model = Book 
        fields = ('gutenberg_id', 'title', 'authors', 'languages', 'subjects', 'shelves', 'formats', 'download_count')

    def get_authors(self, book): 
        """Return a list of author names associated with the book."""
        return book.authors.all().values_list('name', flat=True) 
    
    def get_languages(self, book): 
        """Return a list of author names associated with the book."""
        return book.languages.all().values_list('code', flat=True) 
    
    def get_subjects(self, book): 
        """Return a list of subject names associated with the book."""
        return book.subjects.all().values_list('name', flat=True) 

    def get_shelves(self, book): 
        """Return a list of shelf names associated with the book."""
        return book.bookshelves.all().values_list('name', flat=True)   
    
    def get_formats(self, book): 
        """Return a list of URLs for book formats associated with the book."""
        return Format.objects.filter(book=book).values_list('url', flat=True) 
        