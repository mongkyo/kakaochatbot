from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book


class BookSearchView(APIView):
    def get(self, request, keyword):
        book_search_info = Book.book_search(keyword)
        return Response(book_search_info)
