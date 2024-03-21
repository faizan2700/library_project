from django.test import TestCase 

from main.models import Book 
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
