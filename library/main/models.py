from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.

    This class represents a user in the application. It extends Django's built-in
    AbstractUser model to provide additional customizations.

    Attributes:
    - username (str): The unique username of the user.
    - first_name (str): The first name of the user.
    - last_name (str): The last name of the user.
    - email (str): The email address of the user.
    - password (str): The hashed password of the user.
    - date_joined (datetime): The date and time when the user account was created.
    - is_active (bool): A boolean indicating whether the user account is active.
    - is_staff (bool): A boolean indicating whether the user is a staff member.
    - is_superuser (bool): A boolean indicating whether the user has superuser privileges.
    """

    def __str__(self):
        """Return the username of the user."""
        return self.username

class Author(models.Model):
    """
    Model representing an author.

    Attributes:
    - birth_year (int, optional): The birth year of the author.
    - death_year (int, optional): The death year of the author.
    - name (str): The name of the author.

    Meta:
    - db_table (str): The name of the database table for this model.

    Methods:
    - __str__(): Returns the string representation of the author object.
    """
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'books_author'

    def __str__(self):
        """Return the name of the author."""
        return self.name
    
from django.db import models

class Bookshelf(models.Model):
    """
    Model representing a bookshelf.

    Attributes:
    - name (str): The name of the bookshelf. It must be unique.

    Meta:
    - db_table (str): The name of the database table for this model.

    Methods:
    - __str__(): Returns the string representation of the bookshelf object.
    """
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        db_table = 'books_bookshelf'

    def __str__(self):
        """Return the name of the bookshelf."""
        return f'{self.name}'

class Language(models.Model):
    """
    Model representing a language.

    Attributes:
    - code (str): The code representing the language. It must be unique.

    Meta:
    - db_table (str): The name of the database table for this model.

    Methods:
    - __str__(): Returns the code of the language.
    """
    code = models.CharField(unique=True, max_length=4)

    class Meta:
        db_table = 'books_language'

    def __str__(self):
        """Return the code of the language."""
        return self.code

class Subject(models.Model):
    """
    Model representing a subject.

    Attributes:
    - name (str): The name of the subject.

    Meta:
    - db_table (str): The name of the database table for this model.

    Methods:
    - __str__(): Returns the name of the subject.
    """
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'books_subject'

    def __str__(self):
        """Return the name of the subject."""
        return self.name
class Book(models.Model):
    """
    Model representing a book.

    Attributes:
    - download_count (int, optional): The number of times the book has been downloaded.
    - gutenberg_id (int, unique): The Gutenberg ID of the book.
    - media_type (str): The media type of the book.
    - title (str, optional): The title of the book.
    - authors (ManyToManyField): The authors of the book.
    - subjects (ManyToManyField): The subjects associated with the book.
    - languages (ManyToManyField): The languages of the book.
    - bookshelves (ManyToManyField): The bookshelves where the book is placed.

    Meta:
    - db_table (str): The name of the database table for this model.

    Methods:
    - __str__(): Returns a string representation of the book, consisting of its Gutenberg ID and title (if available).
    """
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField(unique=True)
    media_type = models.CharField(max_length=16)
    title = models.CharField(max_length=1024, blank=True, null=True)
    authors = models.ManyToManyField(Author, related_name='books', related_query_name='books')
    subjects = models.ManyToManyField(Subject, related_name='books', related_query_name='books')
    languages = models.ManyToManyField(Language, related_name='books', related_query_name='books')
    bookshelves = models.ManyToManyField(Bookshelf, related_name='books', related_query_name='books')

    class Meta:
        db_table = 'books_book'

    def __str__(self):
        """Return a string representation of the book."""
        return f'{self.gutenberg_id}-{self.title}'

class Format(models.Model):
    """
    Model representing a format of a book.

    Attributes:
    - mime_type (str): The MIME type of the format.
    - url (str): The URL of the format.
    - book (ForeignKey): The book associated with this format.

    Meta:
    - db_table (str): The name of the database table for this model.

    Methods:
    - __str__(): Returns a string representation of the format, consisting of its associated book and MIME type.
    """
    mime_type = models.CharField(max_length=32)
    url = models.CharField(max_length=256)
    book = models.ForeignKey(Book, models.DO_NOTHING)

    class Meta:
        db_table = 'books_format'

    def __str__(self):
        """Return a string representation of the format."""
        return f'{self.book}-{self.mime_type}'

