from django.db.models import Q 

from django_filters import rest_framework as filters 

from main.models import Book 

class BookFilter(filters.FilterSet):
    """
    FilterSet for filtering books.

    Filters:
    - gutenberg_id (CharFilter): Filter books by Gutenberg ID(s).
    - mime_type (CharFilter): Filter books by MIME type(s) of their formats.
    - title (CharFilter): Filter books by title(s).
    - language (CharFilter): Filter books by language code(s).
    - author (CharFilter): Filter books by author name(s).
    - topic (CharFilter): Filter books by topic(s) found in subjects or bookshelves.

    Methods:
    - search_multiple_ids(qs, name, value): Filter queryset by multiple Gutenberg IDs.
    - search_multiple_languages(qs, name, value): Filter queryset by multiple language codes.
    - search_multiple_mime_types(qs, name, value): Filter queryset by multiple MIME types of formats.
    - search_multiple_topics(qs, name, value): Filter queryset by multiple topics found in subjects or bookshelves.
    - search_multiple_authors(qs, name, value): Filter queryset by multiple author names.
    - search_multiple_titles(qs, name, value): Filter queryset by multiple titles.
    """
    gutenberg_id = filters.CharFilter(method='search_multiple_ids', label='gutenberg_id')
    mime_type = filters.CharFilter(method='search_multiple_mime_types', label='mime_type')
    title = filters.CharFilter(method='search_multiple_titles', label='title')
    language = filters.CharFilter(method='search_multiple_languages', label='language')
    author = filters.CharFilter(method='search_multiple_authors', label='author')
    topic = filters.CharFilter(method='search_multiple_topics', label='topic')

    class Meta:
        model = Book
        fields = []

    def search_multiple_ids(self, qs, name, value):
        """Filter queryset by multiple Gutenberg IDs."""
        return qs.filter(gutenberg_id__in=value.split(','))

    def search_multiple_languages(self, qs, name, value):
        """Filter queryset by multiple language codes."""
        return qs.filter(languages__code__in=value.split(','))

    def search_multiple_mime_types(self, qs, name, value):
        """Filter queryset by multiple MIME types of formats."""
        return qs.filter(format__mime_type__in=value.split(','))

    def search_multiple_topics(self, qs, name, value):
        """
        Filter queryset by multiple topics found in subjects or bookshelves.

        A topic can be found in either subjects or bookshelves.
        """
        q = Q()
        values = value.split(',')
        for value in values:
            q |= Q(subjects__name__icontains=value) | Q(bookshelves__name__icontains=value)
        return qs.filter(q)

    def search_multiple_authors(self, qs, name, value):
        """Filter queryset by multiple author names."""
        values = value.split(',')
        q = Q()
        for value in values:
            q |= Q(authors__name__icontains=value)
        return qs.filter(q)

    def search_multiple_titles(self, qs, name, value):
        """Filter queryset by multiple titles."""
        q = Q()
        values = value.split(',')
        for value in values:
            q |= Q(title__icontains=value)
        return qs.filter(q)