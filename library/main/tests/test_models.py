from django.test import TestCase 
from main.models import User, Book, Author, BookAuthors, Language, BookLanguages, Subject, BookSubjects, Bookshelf, Bookshelves, Format 

class TestBookModel(TestCase): 
    def test_books_created(self): 
        Book.objects.create(title='book1', download_count=100, gutenberg_id=1) 
        Book.objects.create(title='book2', download_count=200, gutenberg_id=2) 
        self.assertEqual(Book.objects.count(), 2) 
        Book.objects.all().delete() 
    
    def test_books_deleted(self): 
        Book.objects.create(title='book1', gutenberg_id=1) 
        Book.objects.all().delete()
        self.assertEqual(Book.objects.all().count(), 0) 

class TestBookAuthors(TestCase): 
    def test_authors_created(self): 
        Author.objects.create(name='author1') 
        self.assertEqual(Author.objects.all().count(), 1) 

        Author.objects.create(name='author2') 
        self.assertEqual(Author.objects.all().count(), 2) 

        Author.objects.all().delete() 

    
    def test_book_authors_created(self): 
        book1 = Book.objects.create(title='bookauthor1', gutenberg_id=3) 
        book2 = Book.objects.create(title='bookauthor2', gutenberg_id=4) 

        author1 = Author.objects.create(name='testauthor1') 
        author2 = Author.objects.create(name='testauthor2') 
        
        BookAuthors.objects.create(author=author1, book=book1) 
        BookAuthors.objects.create(author=author2, book=book2) 

        self.assertEqual(BookAuthors.objects.all().count(), 2) 

        Book.objects.all().delete() 
        Author.objects.all().delete() 
        BookAuthors.objects.all().delete()  

class TestBookSubjects(TestCase): 
    def test_subjects_created(self): 
        Subject.objects.create(name='subject1') 
        Subject.objects.create(name='subject2') 

        self.assertEqual(Subject.objects.all().count(), 2)

        Subject.objects.all().delete() 

    def test_book_subjects_created(self): 
        book1 = Book.objects.create(title='book1', gutenberg_id=1) 
        book2 = Book.objects.create(title='book2', gutenberg_id=2) 

        subject1 = Subject.objects.create(name='subject1') 
        subject2 = Subject.objects.create(name='subject2')

        BookSubjects.objects.create(subject=subject1, book=book1) 
        BookSubjects.objects.create(subject=subject2, book=book2) 

        Book.objects.all().delete() 
        Subject.objects.all().delete() 
        BookSubjects.objects.all().delete() 