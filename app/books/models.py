import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from django.db import models
from selenium.webdriver.common.keys import Keys

from config.settings.base import ROOT_DIR


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

        CHROME_DIR = os.path.join(ROOT_DIR, 'crawling')
        chromedriver_dir = os.path.join(CHROME_DIR, 'chromedriver')
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        driver = webdriver.Chrome(executable_path=chromedriver_dir, chrome_options=options)
        driver.get('https://nsulib.nsu.ac.kr/')
        elem = driver.find_element_by_id('type1q')
        elem.send_keys(keyword)
        elem.send_keys(Keys.RETURN)
        a_tag = driver.find_elements_by_xpath('//a[contains(@href,"#previewLocation")]')

        for a in a_tag[:3 + 1]:
            time.sleep(1)
            a.click()
        time.sleep(1)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.select_one('.resultList')
        book_info = []
        for i in range(0, 3 + 1):
            li = ul.select('.items')[i]
            book_one = dict()
            book_one['title'] = li.select_one('dd.title > a').get_text()
            book_one['author'] = li.select('dd.info')[0].get_text()
            book_one['publisher'] = li.select('dd.info')[1].get_text()
            book_one['publish_year'] = li.select('dd.info')[2].get_text()
            book_info.append(book_one)
            tbody = li.select_one('tbody')
            try:
                for tr in tbody.find_all('tr'):
                    book_tmp = dict()
                    no = tr.select_one('.footable-first-column').get_text()
                    book_tmp['no'] = tr.select_one('.footable-first-column').get_text()
                    book_tmp['location'] = tr.select_one('.location').get_text()
                    book_tmp['serial_num'] = tr.select_one('.callNum').get_text()
                    book_tmp['status'] = tr.select_one('.status').get_text()
                    book_tmp['returnDate'] = tr.select_one('.returnDate').get_text()
                    book_one[f'{no}'] = book_tmp
            except AttributeError:
                pass

        driver.close()
        return book_info
