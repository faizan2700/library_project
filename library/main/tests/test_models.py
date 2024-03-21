from django.test import TestCase 
from main.models import User, Book, Author, Language, Subject, Bookshelf, Format 
from django.db.models import Count, Sum 

class TestBookModel(TestCase):
    """
    Test case for the Book model.

    Methods:
    - test_books_created(): Test that books are created successfully.
    - test_books_deleted(): Test that books are deleted successfully.
    """
    def test_books_created(self):
        """Test that books are created successfully."""
        Book.objects.create(title='book1', download_count=100, gutenberg_id=1)
        Book.objects.create(title='book2', download_count=200, gutenberg_id=2)
        self.assertEqual(Book.objects.count(), 2)
        Book.objects.all().delete()

    def test_books_deleted(self):
        """Test that books are deleted successfully."""
        Book.objects.create(title='book1', gutenberg_id=1)
        Book.objects.all().delete()
        self.assertEqual(Book.objects.all().count(), 0)

class TestBookAuthors(TestCase):
    """
    Test case for the Author model.

    Methods:
    - test_authors_created(): Test that authors are created successfully.
    """
    def test_authors_created(self):
        """Test that authors are created successfully."""
        Author.objects.create(name='author1')
        self.assertEqual(Author.objects.all().count(), 1)

        Author.objects.create(name='author2')
        self.assertEqual(Author.objects.all().count(), 2)

        Author.objects.all().delete()

class TestBookSubjects(TestCase):
    """
    Test case for the Subject model.

    Methods:
    - test_subjects_created(): Test that subjects are created successfully.
    """
    def test_subjects_created(self):
        """Test that subjects are created successfully."""
        Subject.objects.create(name='subject1')
        Subject.objects.create(name='subject2')

        self.assertEqual(Subject.objects.all().count(), 2)

        Subject.objects.all().delete() 
    
class TestManyToManyFieldBook(TestCase): 
    """
    Test case for the Book model.

    Methods:
    - test_authors_added1(): Test that authors are added on book object successfully with no duplicates. 
    - test_authors_added2(): Test that authors are added on book object successfully with duplicates. 
    - test_authors_removed1(): Test that authors are removed from book object successfully (removing whats present). 
    - test_authors_removed2(): Test that authors are removed from book object successfully (removing whats not present) 
    - test_books_authors_count1(): Test if we are getting right aggregate for all authors that are added on book objects, unique records of (book_id, author_id). 
    - test_unique_authors_in_books(): Test if we are getting right aggregate for count of authors that are related to any book objects, unique records (author_id) with non-empty book_ids. 
    - test_reverse_books_authors_add1(): Test if we are correctly adding book to authors. 
    - test_reverse_books_authors_add2(): Test if we are correctly adding book to authors. 
    - test_reverse_books_authors_remove1(): Test if we are correctly removing book from author. 
    - test_reverse_books_authors_remove2(): Test if we are correctly removing book from author. 
    - test_reverse_books_authors_count(): Test if we are correctly counting all books and related authors, unique (book_id, author_id). 
    - test_reverse_unique_books_in_authors(): Test if we are getting right aggregate for count of authors that are related to any author object, unique record (book_id) with no empty author_ids. 
    """

    def test_authors_added1(self): 
        book = Book.objects.create(title='book1', gutenberg_id=1) 
        author = Author.objects.create(name='author1') 

        book.authors.add(author) 

        self.assertEqual(book.authors.count(), 1) 
        self.assertEqual(book.authors.all().first().name, 'author1') 
    
        book.authors.remove(author) 

        book.authors.set([author]) 
        self.assertEqual(book.authors.all().count(), 1) 
        self.assertEqual(book.authors.all().first().name, 'author1') 

        book.authors.clear() 
        Book.objects.all().delete() 
        Author.objects.all().delete() 
    
    def test_authors_added2(self): 
        book = Book.objects.create(title='book1', gutenberg_id=1) 
        author1 = Author.objects.create(name='author1') 
        author2 = Author.objects.create(name='author2') 

        book.authors.add(author1) 

        self.assertEqual(book.authors.all().count(), 1) 
        
        book.authors.set([author1, author2]) 
        self.assertEqual(book.authors.all().count(), 2) 

        book.authors.clear() 
        Author.objects.all().delete() 
        Book.objects.all().delete() 

    def test_authors_removed1(self): 
        book1 = Book.objects.create(title='book1', gutenberg_id=1) 
        author1 = Author.objects.create(name='author1') 
        author2 = Author.objects.create(name='author2') 

        book1.authors.add(author1) 
        self.assertEqual(book1.authors.all().count(), 1) 

        book1.authors.remove(author1) 
        self.assertEqual(book1.authors.all().count(), 0) 

        book1.authors.add([author1, author2]) 
        self.assertEqual(book1.authors.all().count(), 2) 

        book1.authors.remove([author1, author2]) 
        self.assertEqual(book1.authors.all().count(), 0) 

        book1.authors.clear() 
        Author.objects.all().delete() 
        Book.objects.all().delete() 

    def test_authors_removed1(self): 
        book1 = Book.objects.create(title='book1', gutenberg_id=1) 
        author1 = Author.objects.create(name='author1') 
        author2 = Author.objects.create(name='author2') 

        self.assertEqual(book1.authors.all().count(), 0) 

        book1.authors.add(author1) 
        self.assertEqual(book1.authors.all().count(), 1) 

        book1.authors.remove(author2) 
        self.assertEqual(book1.authors.all().count(), 1) 

        book1.authors.clear() 
        Book.objects.all().delete() 
        Author.objects.all().delete() 

    
    def test_books_authors_count1(self): 
        book1 = Book.objects.create(title='book1', gutenberg_id=1) 
        book2 = Book.objects.create(title='book2', gutenberg_id=2) 

        author1 = Author.objects.create(name='author1') 
        author2 = Author.objects.create(name='author2') 

        book1.authors.set([author1, author2]) 
        book2.authors.set([author1, author2]) 

        author_sum = Book.objects \
            .annotate(author_count=Count('authors')) \
            .aggregate(author_sum=Sum('author_count')) \
            .get('author_sum', 0) 
        self.assertEqual(author_sum, 4) 

        book1.authors.clear()
        book2.authors.clear() 
        Author.objects.all().delete() 
        Book.objects.all().delete() 

    def test_unique_authors_in_books(self): 
        
        book1 = Book.objects.create(title='book1', gutenberg_id=1) 
        book2 = Book.objects.create(title='book2', gutenberg_id=2) 

        author1 = Author.objects.create(name='author1') 
        author2 = Author.objects.create(name='author2') 
        author3 = Author.objects.create(name='author3') 

        book1.authors.set([author1, author2]) 
        book2.authors.set([author2, author3]) 

        unique_author_count = Author.objects.all() \
            .filter(books__isnull=False) \
            .annotate(num_books=Count('books')) \
            .filter(num_books__gt=0).count() 
        
        self.assertEqual(unique_author_count, 3) 

        unique_author_count = Book.objects.all() \
            .prefetch_related('authors').annotate(num_authors=Count('authors')) \
            .filter(num_authors__gt=0).values_list('authors').distinct().count() 

        self.assertEqual(unique_author_count, 3) 

