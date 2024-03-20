import csv 
import os 
from pathlib import Path 
from django.db.models import Count, Sum 

from ..models import *

def read_file(file): 
    output = list()  
    with open(file, 'r', encoding='utf-8') as f: 
        csvreader = csv.reader(f) 
        keys = None 
        for row in csvreader: 
            if keys is None: 
                keys = row
                continue 
            current = list() 
            for a in row: 
                if a == '': 
                    current.append(None) 
                else: 
                    current.append(a) 
            d = dict() 
            for i in range(len(keys)): 
                d[keys[i]] = current[i] 
            yield d  

def populate_table(file_path, model): 
    gen = read_file(file_path) 
    for d in gen: 
        try: 
            model.objects.all().create(**d)
        except Exception as error: 
            print(str(error)) 
    return model.objects.all().count() 

def populate_table_helper(): 
    output = populate_table('./main/dump/books_author.csv', Author)
    print('Author table is populated successfully! records:', output) 
    output = populate_table('./main/dump/books_book.csv', Book)
    print('Book Table is populated successfully! records:', output) 
    output = populate_table('./main/dump/books_format.csv', Format)
    print('Format Table is populated successfully! records', output)
    output = populate_table('./main/dump/books_language.csv', Language)
    print('Language table is populated successfully! records:', output)
    output = populate_table('./main/dump/books_subject.csv', Subject)
    print('Subject table is populated successfully! records:', output) 
    output = populate_table('./main/dump/books_bookshelf.csv', Bookshelf) 
    print('Bookshelf table is populated successfully! records:', output) 
    
    

def populate_many_to_many_field(model1, model2, manager, file): 
    gen = read_file(file) 
    for d in gen: 
        row = d.values() 
        _, key1, key2 = tuple(row) 
        obj1 = model1.objects.get(id=key1) 
        obj2 = model2.objects.get(id=key2) 
        getattr(obj1, manager).add(obj2)  

def populate_many_to_many_field_helper(): 
    populate_many_to_many_field(Book, Language, 'languages', './main/dump/books_book_languages.csv') 
    total_book_languages_records = Book.objects.annotate(lang_count=Count('languages')).aggregate(lang_sum=Sum('lang_count')).get('lang_sum')
    print('BookLanguages table is populated successfully! records:', total_book_languages_records) 
    populate_many_to_many_field(Book, Author, 'authors', './main/dump/books_book_authors.csv')  
    total_book_author_records = Book.objects.annotate(author_count=Count('authors')).aggregate(author_sum=Sum('author_count')).get('author_sum') 
    print('BookAuthors table is populated successfully! records:', total_book_author_records) 
    populate_many_to_many_field(Book, Subject, 'subjects', './main/dump/books_book_subjects.csv') 
    total_book_subject_records = Book.objects.annotate(subject_count=Count('subjects')).aggregate(subject_sum=Sum('subject_count')).get('subject_sum')  
    print('BookSubjects table is populated successfully! records:', total_book_subject_records) 
    populate_many_to_many_field(Book, Bookshelf, 'bookshelves', './main/dump/books_book_bookshelves.csv') 
    total_book_shelves_records = Book.objects.annotate(shelves_count=Count('bookshelves')).aggregate(shelves_sum=Sum('shelves_count')).get('shelves_sum')  
    print('Bookshelves table is populated successfully! records:', total_book_shelves_records)  

def main():
    populate_table_helper() 
    populate_many_to_many_field_helper() 
    # clean_data() 

def clean_data(): 
    Author.objects.all().delete() 
    Subject.objects.all().delete() 
    Bookshelf.objects.all().delete() 
    Language.objects.all().delete() 
    Format.objects.all().delete() 
    Book.objects.all().delete() 
    print('All tables are truncated succesfully!') 
    print('Author, Subject, Bookshelf, Language, Format, Book.') 

if __name__ == '__main__': 
    main() 