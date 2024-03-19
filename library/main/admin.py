from django.contrib import admin

from main.models import Author, Book, Bookshelf, Subject, User, Format  

admin.site.register(Author) 
admin.site.register(Book) 
admin.site.register(Bookshelf) 
admin.site.register(Subject) 
admin.site.register(User) 
admin.site.register(Format) 