from django.db import models


class Book_info(models.Model):
    title = models.TextField('제목')
    author = models.CharField('작가', max_length=100)
    publisher = models.CharField('출판사', max_length=100)
    publish_year = models.CharField('출판 연도', max_length=100)
    number = models.IntegerField('도서 번호')
    location = models.CharField('도서 위치', max_length=250)
    serial_number = models.CharField('도서 고유번호', max_length=200)
    status = models.CharField('도서 상태', max_length=250)
    return_date = models.CharField('반납일', max_length=200)

