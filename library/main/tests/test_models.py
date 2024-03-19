from django.test import TestCase 
from main.models import User, Book, Author, Language, Subject, Bookshelf, Format 

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

class TestBookSubjects(TestCase): 
    def test_subjects_created(self): 
        Subject.objects.create(name='subject1') 
        Subject.objects.create(name='subject2') 

        self.assertEqual(Subject.objects.all().count(), 2)

        Subject.objects.all().delete() 
