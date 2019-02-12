from books.utils.crawling import Crawler
from library.models import Book_info


def get_book_info(self, title):
    self.title = title
    Crawler.show_book_info(self.title)
