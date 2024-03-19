# from django.test import TestCase 

# from main.filters import BookFilter 
# from main.models import Book, Language, Subject, Bookshelf, Author, Format
# class TestBookFilter(TestCase): 

#     @classmethod 
#     def setUpTestData(cls): 
#         book1 = Book.objects.create(title='book1', gutenberg_id=1) 
#         book2 = Book.objects.create(title='book2', gutenberg_id=2) 

#         language1 = Language.objects.create(code='en') 
#         language2 = Language.objects.create(code='fr') 

#         book_language1 = BookLanguages.objects.create(book=book1, language=language1) 
#         book_language2 = BookLanguages.objects.create(book=book2, language=language2) 

#         subject1 = Subject.objects.create(name='subject1') 
#         subject2 = Subject.objects.create(name='subject2')

#         book_subject1 = BookSubjects.objects.create(book=book1, subject=subject1)
#         book_subject2 = BookSubjects.objects.create(book=book2, subject=subject2) 

#         shelf1 = Bookshelf.objects.create(name='shelf1') 
#         shelf2 = Bookshelf.objects.create(name='shelf2') 

#         book_shelf1 = Bookshelves.objects.create(book=book1, bookshelf=shelf1) 
#         book_shelf2 = Bookshelves.objects.create(book=book2, bookshelf=shelf2) 

#         format1 = Format.objects.create(mime_type='text', book=book1) 
#         format2 = Format.objects.create(mime_type='pdf', book=book2) 

#         shelf3 = Bookshelf.objects.create(name='test_shelf') 
#         subject3 = Subject.objects.create(name='test_subject') 

#         Bookshelves.objects.create(book=book1, bookshelf=shelf3) 
#         BookSubjects.objects.create(book=book2, subject=subject3) 

#         author1 = Author.objects.create(name='author1') 
#         author2 = Author.objects.create(name='author2') 

#         BookAuthors.objects.create(book=book1, author=author1) 
#         BookAuthors.objects.create(book=book2, author=author2) 

#     def test_filter_by_gutenberg_id1(self): 
#         filter_data = {'gutenberg_id': 1} 
#         filtered_qs = BookFilter(data=filter_data).qs
#         self.assertEqual(filtered_qs.count(), 1) 
#         self.assertEqual(filtered_qs.first().title, 'book1') 

        
#     def test_filter_by_gutenberg_id2(self): 
#         filtered_data = {'gutenberg_id': 2} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 1) 
#         self.assertEqual(filtered_qs.first().title, 'book2') 

#     def test_filter_by_multiple_gutenberg_ids(self): 
#         filtered_data={'gutenberg_id': '1,2'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 2) 
#         self.assertEqual(filtered_qs.first().title, 'book1') 
#         self.assertEqual(filtered_qs.last().title, 'book2') 

#     def test_filter_by_title1(self): 
#         filtered_data = {'title': 'ok1'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 1) 
#         self.assertEqual(filtered_qs.first().title, 'book1') 

#         filtered_data = {'title': 'ok2'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 1) 
#         self.assertEqual(filtered_qs.first().title, 'book2') 

#     def test_filter_by_title2(self):
#         filtered_data = {'title': 'book'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 2) 
#         self.assertEqual(filtered_qs.first().title, 'book1') 
#         self.assertEqual(filtered_qs.last().title, 'book2') 

#     def test_filter_by_multiple_titles(self): 
#         filtered_data = {'title': 'book1,book2'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 2) 
#         self.assertEqual(filtered_qs.first().title, 'book1') 
#         self.assertEqual(filtered_qs.last().title, 'book2') 

#     def test_filter_by_language1(self): 
#         filtered_data = {'language': 'en'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 1) 
#         self.assertEqual(filtered_qs.first().title, 'book1')  
    
#     def test_filter_by_language2(self): 
#         filtered_data = {'language': 'fr'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 1) 
#         self.assertEqual(filtered_qs.first().title, 'book2') 
    
#     def test_filter_by_multiple_languages(self): 
#         filtered_data = {'language': 'en,fr'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 2) 
#         self.assertEqual(filtered_qs.first().title, 'book1') 
#         self.assertEqual(filtered_qs.last().title, 'book2') 

#     def test_filter_by_author1(self): 
#         filtered_data = {'author': 'author1'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 1) 
#         self.assertEqual(filtered_qs.first().title, 'book1') 
    
#     def test_filter_by_author2(self): 
#         filtered_data = {'author': 'author2'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 1) 
#         self.assertEqual(filtered_qs.first().title, 'book2') 
    
#     def test_filter_by_multiple_authors(self): 
#         filtered_data = {'author': 'author1,author2'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 2) 
#         self.assertEqual(filtered_qs.first().title, 'book1') 
#         self.assertEqual(filtered_qs.last().title, 'book2') 

#     def test_filter_by_format1(self): 
#         filtered_data = {'mime_type': 'text'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 1) 
#         self.assertEqual(filtered_qs.first().title, 'book1') 

#     def test_filter_by_format2(self): 
#         filtered_data = {'mime_type': 'pdf'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 1) 
#         self.assertEqual(filtered_qs.first().title, 'book2') 

#     def test_filter_by_multiple_formats(self): 
#         filtered_data = {'mime_type': 'text,pdf'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 2) 
#         self.assertEqual(filtered_qs.first().title, 'book1') 
#         self.assertEqual(filtered_qs.last().title, 'book2') 

#     def test_filter_by_topic1(self): 
#         filtered_data = {'topic': 'shelf1'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 1) 
#         self.assertEqual(filtered_qs.first().title, 'book1') 

#     def test_filter_by_topic2(self): 
#         filtered_data = {'topic': 'test_subject'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 1) 
#         self.assertEqual(filtered_qs.first().title, 'book2') 

#     def test_filter_by_multiple_topics(self): 
#         filtered_data = {'topic': 'test, shelf1'} 
#         filtered_qs = BookFilter(data=filtered_data).qs 
#         self.assertEqual(filtered_qs.count(), 2) 
#         self.assertEqual(filtered_qs.first().title, 'book1') 
#         self.assertEqual(filtered_qs.last().title, 'book2')     

    
    
    

