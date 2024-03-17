from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    def __str__(self): 
        return self.username 
    
class Author(models.Model): 
    name = models.CharField(max_length=100) 
    popularity = models.IntegerField(null=True) 
    nationality = models.CharField(max_length=100) 
    gender = models.CharField(max_length=100, null=True, blank=True) 
    website = models.CharField(max_length=100) 
    email = models.EmailField() 
    mobile = models.CharField(max_length=100, null=True, blank=True) 

    def __str__(self): 
        return self.name 
    
    def save(self, *args, **kwargs): 
        if self.popularity is not None and (self.popularity < 1 or self.popularity > 10): 
            raise ValueError('Popularity of author must be between 1 and 10!') 
        if self.gender is not None and (self.gender not in ['Male', 'Female']): 
            raise ValueError('Gender can either be Male or Female!') 
        if self.mobile is not None and len(self.mobile) != 10: 
            raise ValueError('Mobile must be of length 10!') 
        super().save(*args, **kwargs) 


class Genre(models.Model): 
    name = models.CharField(max_length=100) 

    def __str__(self): 
        return self.name 

class Book(models.Model): 
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 
    genre = models.ManyToManyField(Genre, related_name='books', related_query_name='genres') 
    title = models.CharField(max_length=100) 
    language = models.CharField(max_length=100) 

class Link(models.Model): 
    url = models.URLField(blank=False, null=False) 
    mime_type = models.CharField(max_length=100) 
    book = models.ForeignKey(Book, on_delete=models.CASCADE) 

class Bookshelf(models.Model): 
    name = models.CharField(max_length=100) 
    books = models.ManyToManyField(Book, related_name='shelves', related_query_name='shelves') 

class Subject(models.Model): 
    name = models.CharField(max_length=100) 
    books = models.ManyToManyField(Book, related_name='subjects', related_query_name='subjects') 
    
