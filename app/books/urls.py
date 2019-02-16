from django.urls import path

from books import apis

urlpatterns = [
    path('<str:keyword>/', apis.BookSearchView.as_view()),
]
