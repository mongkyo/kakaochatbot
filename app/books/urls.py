from django.urls import path

from books import apis

urlpatterns = [
    path('', apis.BookSearchView.as_view()),
]
