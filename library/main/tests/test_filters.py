from django.test import TestCase 

from main.filters import BookFilter 
from main.models import Book 

class TestBookFilter(TestCase): 

    @classmethod 
    def setUpTestData(cls): 
        Book.objects.create(title='book1', gutenberg_id=1) 
        Book.objects.create(title='book2', gutenberg_id=2) 

    def test_filter_by_gutenberg_id1(self): 
        filter_data = {'gutenberg_id': 1} 
        filtered_qs = BookFilter(data=filter_data).qs
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book1') 

        
    def test_filter_by_gutenberg_id2(self): 
        filtered_data = {'gutenberg_id': 2} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book2') 

    def test_filter_by_multiple_gutenberg_ids(self): 
        filtered_data={'gutenberg_id': '1,2'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 2) 
        self.assertEqual(filtered_qs.first().title, 'book1') 
        self.assertEqual(filtered_qs.last().title, 'book2') 

    def test_filter_by_title1(self): 
        filtered_data = {'title': 'ok1'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book1') 

        filtered_data = {'title': 'ok2'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 1) 
        self.assertEqual(filtered_qs.first().title, 'book2') 

    def test_filter_by_title2(self):
        filtered_data = {'title': 'book'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 2) 
        self.assertEqual(filtered_qs.first().title, 'book1') 
        self.assertEqual(filtered_qs.last().title, 'book2') 

    def test_filter_by_multiple_titles(self): 
        filtered_data = {'title': 'book1,book2'} 
        filtered_qs = BookFilter(data=filtered_data).qs 
        self.assertEqual(filtered_qs.count(), 2) 
        self.assertEqual(filtered_qs.first().title, 'book1') 
        self.assertEqual(filtered_qs.last().title, 'book2') 
    

