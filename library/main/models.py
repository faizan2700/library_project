from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    def __str__(self): 
        return self.username 

class Author(models.Model):
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128) 

    class Meta:
        db_table = 'books_author'

    def __str__(self): 
        return self.name 
    
class Bookshelf(models.Model):
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        db_table = 'books_bookshelf'

    def __str__(self): 
        return f'{self.name}' 

class Language(models.Model):
    code = models.CharField(unique=True, max_length=4)

    class Meta:
        db_table = 'books_language'

    def __str__(self): 
        return self.code 

class Subject(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'books_subject'

    def __str__(self): 
        return self.name 
    
class Book(models.Model):
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField(unique=True)
    media_type = models.CharField(max_length=16)
    title = models.CharField(max_length=1024, blank=True, null=True) 
    authors = models.ManyToManyField(Author, related_name='books', related_query_name='books') 
    subjects = models.ManyToManyField('Subject', related_name='books', related_query_name='books') 
    languages = models.ManyToManyField('Language', related_name='books', related_query_name='books') 
    bookshelves = models.ManyToManyField('Bookshelf', related_name='books', related_query_name='books') 

    class Meta:
        db_table = 'books_book'

    def __str__(self): 
        return f'{self.gutenberg_id}-{self.title}'

class Format(models.Model):
    mime_type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    book = models.ForeignKey(Book, models.DO_NOTHING)

    class Meta:
        db_table = 'books_format'

    def __str__(self): 
        return f'{self.book}-{self.mime_type}' 
    

