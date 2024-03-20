from django.test import TestCase 
from django.urls import reverse  
from rest_framework.test import APIClient 
from rest_framework import status 

from main.models import Book 
from main.serializers import BookSerializer 

class TestBookSerializer(TestCase): 
    """
    Test cases for the BookSerializer class.
    """

    def setUp(self): 
        """
        Set up for each test case.
        """
        self.client = APIClient() 
        self.url = reverse('book-list') 
        self.data = {'title': 'book1', 'gutenberg_id': 1} 
        self.model = Book.objects.create(**self.data)

    def test_api_book_get_list(self): 
        """
        Test retrieving a list of books via API.
        """
        response = self.client.get(self.url) 
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(len(response.data['results']), min(20, Book.objects.all().count())) 

    def test_api_book_create(self): 
        """
        Test creating a new book via API.
        """
        data = {'title': 'book2', 'gutenberg_id': 2}
        response = self.client.post(self.url, data=data) 
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) 
        self.assertTrue(Book.objects.filter(**self.data).exists())  

    def test_api_book_retrieve(self): 
        """
        Test retrieving a single book via API.
        """
        detail_url = reverse('book-detail', kwargs={'pk': self.model.pk}) 
        response = self.client.get(detail_url) 
        self.assertEqual(response.status_code, status.HTTP_200_OK) 
        self.assertEqual(response.data['title'], 'book1')