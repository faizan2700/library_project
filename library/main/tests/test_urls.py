from django.test import SimpleTestCase 
from django.urls import reverse, resolve 

from main.views import BookViewSet 

class TestURL(SimpleTestCase): 
    def test_url(self): 
        url = reverse('book-list') 
        self.assertEqual(resolve(url).func.__name__, 'BookViewSet') 