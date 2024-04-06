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
    yield 'Author table is populated successfully! records:' +  str(output) 
    output = populate_table('./main/dump/books_book.csv', Book)
    yield 'Book Table is populated successfully! records:' + str(output) 
    output = populate_table('./main/dump/books_format.csv', Format)
    yield 'Format Table is populated successfully! records' + str(output)
    output = populate_table('./main/dump/books_language.csv', Language)
    yield 'Language table is populated successfully! records:' + str(output)
    output = populate_table('./main/dump/books_subject.csv', Subject)
    yield 'Subject table is populated successfully! records:' +  str(output)
    output = populate_table('./main/dump/books_bookshelf.csv', Bookshelf) 
    yield 'Bookshelf table is populated successfully! records:' + str(output) 
    
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
    yield 'BookLanguages table is populated successfully! records:' + str(total_book_languages_records) 
    populate_many_to_many_field(Book, Author, 'authors', './main/dump/books_book_authors.csv')  
    total_book_author_records = Book.objects.annotate(author_count=Count('authors')).aggregate(author_sum=Sum('author_count')).get('author_sum') 
    yield 'BookAuthors table is populated successfully! records:' + str(total_book_author_records) 
    populate_many_to_many_field(Book, Subject, 'subjects', './main/dump/books_book_subjects.csv') 
    total_book_subject_records = Book.objects.annotate(subject_count=Count('subjects')).aggregate(subject_sum=Sum('subject_count')).get('subject_sum')  
    yield 'BookSubjects table is populated successfully! records:' + str(total_book_subject_records) 
    populate_many_to_many_field(Book, Bookshelf, 'bookshelves', './main/dump/books_book_bookshelves.csv') 
    total_book_shelves_records = Book.objects.annotate(shelves_count=Count('bookshelves')).aggregate(shelves_sum=Sum('shelves_count')).get('shelves_sum')  
    yield 'Bookshelves table is populated successfully! records:' + str(total_book_shelves_records)  

def main(): 
    
    for msg in populate_table_helper(): 
        yield msg  
    for msg in populate_many_to_many_field_helper(): 
        yield msg  
    # clean_data() 

def clean_data(): 
    Author.objects.all().delete() 
    yield 'Author table truncated!!' 
    Subject.objects.all().delete() 
    yield 'Subject table truncated!!' 
    Bookshelf.objects.all().delete() 
    yield 'Bookshelf table truncated!!' 
    Language.objects.all().delete() 
    yield 'Language table truncated!!' 
    Format.objects.all().delete() 
    yield 'Format table truncated!!' 
    Book.objects.all().delete() 
    yield 'Book table truncated!!'  

if __name__ == '__main__': 
    main() 