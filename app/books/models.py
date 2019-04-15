import os
import time
from bs4 import BeautifulSoup
# from selenium import webdriver
from django.db import models
# from selenium.webdriver.common.keys import Keys
import requests
from config.settings.base import ROOT_DIR
import re

class Book(models.Model):
    title = models.TextField('제목')
    author = models.CharField('작가', max_length=100)
    publisher = models.CharField('출판사', max_length=100)
    publish_year = models.CharField('출판 연도', max_length=100)
    number = models.IntegerField('도서 번호')
    location = models.CharField('도서 위치', max_length=250)
    serial_number = models.CharField('도서 고유번호', max_length=200)
    status = models.CharField('도서 상태', max_length=250)
    return_date = models.CharField('반납일', max_length=200)

    @staticmethod
    def book_search(keyword):
        """
        책 검색 정보를 불러와준다
        """
        res = requests.get(f'https://nsulib.nsu.ac.kr/search/tot/result?st=KWRD&si=TOTAL&q={keyword}&x=0&y=0')
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.select_one('.resultList')
        book_info = []
        for i in range(0, 2+1):
            li = ul.select('.items')[i]
            book_one = dict()
            book_detail = dict()
            book_one['title'] = li.select_one('dd.title > a').get_text()
            book_one['author'] = li.select('dd.info')[0].get_text()
            book_one['publisher'] = li.select('dd.info')[1].get_text()
            book_one['publish_year'] = li.select('dd.info')[2].get_text()
            book_info.append(book_one)
            test_text = li.get('id')
            no = re.search(r'(CAT\w+\d+)', test_text).group()
            detail_html = requests.get(f'https://nsulib.nsu.ac.kr/search/detail/{no}').text
            detail_soup = BeautifulSoup(detail_html, 'html.parser')
            div_li = detail_soup.select_one('.listTable > table')
            book_detail['no'] = div_li.select_one('td.num').get_text()
            book_detail['callNum'] = div_li.select_one('td.callNum').get_text()
            book_detail['location'] = div_li.select_one('td.location').get_text(" ", strip=True)
            book_detail['status'] = div_li.select_one('span.status').get_text()
            book_one['detail'] = book_detail
        return book_one
