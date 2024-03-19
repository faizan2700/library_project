import csv 
import os 
from pathlib import Path 

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


def populate_author_table(): 
    file_path = './main/dump/books_author.csv'
    gen = read_file(file_path) 
    
    for row in gen: 
        id, birth_year, death_year, name = tuple(row) 
        if birth_year == '': 
            birth_year = None 
        if death_year == '': 
            death_year = None 
        if name == '': 
            name = None 
        Author.objects.create(id=id, birth_year=birth_year, death_year=death_year, name=name)

def populate_book_table(): 
    # id, download_count, gutenberg_id, media_type, title 
    file_path = './main/dump/books_book.csv' 
    gen = read_file(file_path) 
    for d in gen: 
        Book.objects.create(**d) 
    return Book.objects.all().count() 

def populate_format_table(): 
    file_path = './main/dump/books_format.csv' 
    gen = read_file(file_path) 
    for d in gen: 
        Format.objects.create(**d) 
    return Format.objects.all().count() 

def populate_table(file_path, model): 
    gen = read_file(file_path) 
    for d in gen: 
        try: 
            model.objects.all().create(**d)
        except Exception as error: 
            print(str(error)) 
    return model.objects.all().count() 

def populate_table_helper(): 
    print(populate_table('./main/dump/books_language.csv', Language))
    #print(populate_table('./main/dump/books_subject.csv', Subject)) 
    #print(populate_table('./main/dump/books_bookshelf.csv', Bookshelf)) 
    


def populate_many_to_many_field(model1, model2, manager, file): 
    gen = read_file(file) 
    for d in gen: 
        row = d.values() 
        _, key1, key2 = tuple(row) 
        obj1 = model1.objects.get(id=key1) 
        obj2 = model2.objects.get(id=key2) 
        getattr(obj1, manager).add(obj2)  

def populate_many_to_many_field_helper(): 
    # populate_many_to_many_field(Book, Language, 'languages', './main/dump/books_book_languages.csv') 
    # populate_many_to_many_field(Book, Author, 'authors', './main/dump/books_book_authors.csv') 
    populate_many_to_many_field(Book, Subject, 'subjects', './main/dump/books_book_subjects.csv') 
    populate_many_to_many_field(Book, Bookshelf, 'bookshelves', './main/dump/books_book_bookshelves.csv') 



def main():
    populate_author_table()

if __name__ == '__main__': 
    main() 