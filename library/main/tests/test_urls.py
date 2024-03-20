from django.test import SimpleTestCase 
from django.urls import reverse, resolve 

from main.views import BookViewSet 

class TestURL(SimpleTestCase):
    """
    Test case for verifying the URL configuration.

    Methods:
    - test_url(): Test that the URL for the book list resolves to the correct viewset class.
    """
    def test_url(self):
        """Test that the URL for the book list resolves to the correct view function."""
        url = reverse('book-list')
        self.assertEqual(resolve(url).func.__name__, BookViewSet.__name__)