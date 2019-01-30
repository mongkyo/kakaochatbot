from django.contrib import admin
from .models import Book_info


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(Book_info, BookInfoAdmin)
