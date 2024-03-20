from django.test import TestCase 

from main.filters import BookFilter 
from main.models import Book, Language, Subject, Bookshelf, Author, Format
class TestBookFilter(TestCase):
    """
    Test case for the BookFilter.

    Methods:
    - setUpTestData(): Set up test data.
    - test_filter_by_gutenberg_id1(): Test filtering by a single Gutenberg ID.
    - test_filter_by_gutenberg_id2(): Test filtering by another single Gutenberg ID.
    - test_filter_by_multiple_gutenberg_ids(): Test filtering by multiple Gutenberg IDs.
    - test_filter_by_title1(): Test filtering by a single title substring.
    - test_filter_by_title2(): Test filtering by another single title substring.
    - test_filter_by_multiple_titles(): Test filtering by multiple title substrings.
    - test_filter_by_language1(): Test filtering by a single language.
    - test_filter_by_language2(): Test filtering by another single language.
    - test_filter_by_multiple_languages(): Test filtering by multiple languages.
    - test_filter_by_author1(): Test filtering by a single author.
    - test_filter_by_author2(): Test filtering by another single author.
    - test_filter_by_multiple_authors(): Test filtering by multiple authors.
    - test_filter_by_format1(): Test filtering by a single MIME type.
    - test_filter_by_format2(): Test filtering by another single MIME type.
    - test_filter_by_multiple_formats(): Test filtering by multiple MIME types.
    - test_filter_by_topic1(): Test filtering by a single topic.
    - test_filter_by_topic2(): Test filtering by another single topic.
    - test_filter_by_multiple_topics(): Test filtering by multiple topics.
    """
    @classmethod
    def setUpTestData(cls):
        """Set up test data."""
        book1 = Book.objects.create(title='book1', gutenberg_id=1)
        book2 = Book.objects.create(title='book2', gutenberg_id=2)

        language1 = Language.objects.create(code='en')
        language2 = Language.objects.create(code='fr')

        book1.languages.add(language1)
        book2.languages.add(language2)

        subject1 = Subject.objects.create(name='subject1')
        subject2 = Subject.objects.create(name='subject2')

        book1.subjects.add(subject1)
        book2.subjects.add(subject2)

        shelf1 = Bookshelf.objects.create(name='shelf1')
        shelf2 = Bookshelf.objects.create(name='shelf2')

        book1.bookshelves.add(shelf1)
        book2.bookshelves.add(shelf2)

        format1 = Format.objects.create(mime_type='text', book=book1)
        format2 = Format.objects.create(mime_type='pdf', book=book2)

        shelf3 = Bookshelf.objects.create(name='test_shelf')
        subject3 = Subject.objects.create(name='test_subject')

        book1.subjects.add(subject3)
        book2.bookshelves.add(shelf3)

        author1 = Author.objects.create(name='author1')
        author2 = Author.objects.create(name='author2')

        book1.authors.add(author1)
        book2.authors.add(author2)

    def test_filter_by_gutenberg_id1(self):
        """Test filtering by a single Gutenberg ID."""
        filtered_data = {'gutenberg_id': 1}
        filtered_qs = BookFilter(data=filtered_data).qs
        self.assertEqual(filtered_qs.count(), 1)
        self.assertEqual(filtered_qs.first().title, 'book1')

    def test_filter_by_gutenberg_id2(self): 
        """
        Test filtering by a single Gutenberg ID (2).
        """
        filtered_data = {'gutenberg_id': 2} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book2') 

    def test_filter_by_multiple_gutenberg_ids(self): 
        """
        Test filtering by multiple Gutenberg IDs (1 and 2).
        """
        filtered_data={'gutenberg_id': '1,2'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 2) 
        self.assertEqual(filtered_qs.first().title, 'book1') 
        self.assertEqual(filtered_qs.last().title, 'book2') 

    def test_filter_by_title1(self): 
        """
        Test filtering by a single title substring ('ok1').
        """
        filtered_data = {'title': 'ok1'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book1') 

        filtered_data = {'title': 'ok2'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book2') 

    def test_filter_by_title2(self):
        """
        Test filtering by a single title substring ('book').
        """
        filtered_data = {'title': 'book'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 2) 
        self.assertEqual(filtered_qs.first().title, 'book1') 
        self.assertEqual(filtered_qs.last().title, 'book2') 

    def test_filter_by_multiple_titles(self): 
        """
        Test filtering by multiple title substrings ('book1' and 'book2').
        """
        filtered_data = {'title': 'book1,book2'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 2) 
        self.assertEqual(filtered_qs.first().title, 'book1') 
        self.assertEqual(filtered_qs.last().title, 'book2') 

    def test_filter_by_language1(self): 
        """ Test filtering books by a single language ('en'). """
        filtered_data = {'language': 'en'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book1')  
    
    def test_filter_by_language2(self): 
        """Test filtering books by a single language ('fr')."""
        filtered_data = {'language': 'fr'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book2') 
    
    def test_filter_by_multiple_languages(self): 
        """Test filtering books by multiple languages ('en,fr')."""
        filtered_data = {'language': 'en,fr'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 2) 
        self.assertEqual(filtered_qs.first().title, 'book1') 
        self.assertEqual(filtered_qs.last().title, 'book2') 

    def test_filter_by_author1(self): 
        """ Test filtering books by a single author ('author1'). """
        filtered_data = {'author': 'author1'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book1') 
    
    def test_filter_by_author2(self): 
        """ Test filtering books by a single author ('author2'). """
        filtered_data = {'author': 'author2'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book2') 
    
    def test_filter_by_multiple_authors(self): 
        """ Test filtering books by multiple authors ('author1,author2'). """
        filtered_data = {'author': 'author1,author2'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 2) 
        self.assertEqual(filtered_qs.first().title, 'book1') 
        self.assertEqual(filtered_qs.last().title, 'book2') 

    def test_filter_by_format1(self): 
        """ Test filtering books by a single format ('text'). """
        filtered_data = {'mime_type': 'text'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book1') 

    def test_filter_by_format2(self): 
        """ Test filtering books by a single format ('pdf'). """
        filtered_data = {'mime_type': 'pdf'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book2') 

    def test_filter_by_multiple_formats(self): 
        """ Test filtering books by multiple formats ('text,pdf'). """
        filtered_data = {'mime_type': 'text,pdf'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 2) 
        self.assertEqual(filtered_qs.first().title, 'book1') 
        self.assertEqual(filtered_qs.last().title, 'book2') 

    def test_filter_by_topic1(self): 
        """ Test filtering books by a single topic ('shelf1'). """
        filtered_data = {'topic': 'shelf1'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 2) 
        self.assertEqual(filtered_qs.first().title, 'book1') 

    def test_filter_by_topic2(self): 
        """ Test filtering books by a single topic ('test_subject'). """
        filtered_data = {'topic': 'test_subject'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book1') 

    def test_filter_by_multiple_topics(self): 
        """ Test filtering books by multiple topics ('test, shelf1'). """
        filtered_data = {'topic': 'test, shelf1'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 2) 
        self.assertEqual(filtered_qs.first().title, 'book1') 
        self.assertEqual(filtered_qs.last().title, 'book2')     

    
    
    

