from rest_framework.routers import DefaultRouter 

from main.views import BookViewSet 

router = DefaultRouter() 
router.register('books', BookViewSet)