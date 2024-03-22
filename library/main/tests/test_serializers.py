from django.test import TestCase 

from main.models import Book, Language, Author, Format, Subject, Bookshelf
from main.serializers import BookSerializer 

class TestBookSerializer(TestCase): 
    def test_simple_fields(self): 
        book = Book.objects.all().create(title='book1', gutenberg_id=1, download_count=0) 
        data = BookSerializer(book).data 
        gutenberg_id = data.get('gutenberg_id', -1) 
        title = data.get('title', '') 
        download_count = data.get('download_count', 0) 

        self.assertEqual(gutenberg_id, 1) 
        self.assertEqual(title, 'book1') 
        self.assertEqual(download_count, 0) 

        Book.objects.all().delete() 
    
    def test_many_to_many_fields_representation(self): 
        book = Book.objects.create(title='book1', gutenberg_id=1, download_count=1) 

        author1 = Author.objects.create(name='author1') 
        language1 = Language.objects.create(code='fr') 
        subject1 = Subject.objects.create(name='subject1') 
        shelf1 = Bookshelf.objects.create(name='shelf1') 

        book.authors.add(author1) 
        book.languages.add(language1) 
        book.subjects.add(subject1) 
        book.bookshelves.add(shelf1) 

        data = BookSerializer(instance=book).data
        
        self.assertEqual(data.get('title', ''), book.title) 
        self.assertEqual(data.get('download_count', ''), book.download_count) 
        self.assertEqual(data.get('gutenberg_id', 0), book.gutenberg_id) 

        self.assertEqual(data.get('authors')[0], book.authors.first().name) 
        self.assertEqual(data.get('languages')[0], book.languages.all().first().code) 
        self.assertEqual(data.get('subjects')[0], book.subjects.first().name) 
        self.assertEqual(data.get('shelves')[0], book.bookshelves.first().name) 

        book.languages.all().delete() 
        book.subjects.all().delete() 
        book.bookshelves.all().delete() 
        book.authors.all().delete() 
        Book.objects.all().delete() 
        Author.objects.all().delete() 
        Language.objects.all().delete() 
        Bookshelf.objects.all().delete() 

    def test_formats_of_book(self): 
        book = Book.objects.create(title='book1', gutenberg_id=1) 

        format1 = Format.objects.all().create(url='url1', book=book) 
        format2 = Format.objects.all().create(url='url2', book=book) 
        format3 = Format.objects.all().create(url='url3', book=book) 

        data = BookSerializer(instance=book).data 
        self.assertEqual(data.get('formats'), [format1.url, format2.url, format3.url]) 


        