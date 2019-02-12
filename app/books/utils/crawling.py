from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import lxml
import sys
import time
import re
import urllib.request


class Book:
    def __init__(self, title, author, location):
        self.title = title
        self.author = author
        self.location = location

    def __repr__(self):
        return self.title


class Crawler:
    def show_book_info(self):
        """
        책 검색 정보를 불러와준다
        """

        chromedriver_dir = '/Users/mongkyo/Projects/kakao-chatbot/crawling/chromedriver'
        driver = webdriver.Chrome(chromedriver_dir)
        driver.get('https://nsulib.nsu.ac.kr/')
        elem = driver.find_element_by_id('type1q')
        elem.send_keys(self)
        elem.send_keys(Keys.RETURN)
        a_tag = driver.find_elements_by_xpath('//a[contains(@href,"#previewLocation")]')

        for a in a_tag[:3+1]:
            a.click()
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.select_one('.resultList')
        book_info = []
        for i in range(0, 2+1):
            li = ul.select('.items')[i]
            book_one = dict()
            book_one['title'] = li.select_one('dd.title > a').get_text()
            book_one['author'] = li.select('dd.info')[0].get_text()
            book_one['publisher'] = li.select('dd.info')[1].get_text()
            book_one['publish_year'] = li.select('dd.info')[2].get_text()
            book_info.append(book_one)
            tbody = li.select_one('tbody')
            for tr in tbody.find_all('tr'):
                book_tmp = dict()
                no = tr.select_one('.footable-first-column').get_text()
                book_tmp['no'] = tr.select_one('.footable-first-column').get_text()
                book_tmp['location'] = tr.select_one('.location').get_text()
                book_tmp['serial_num'] = tr.select_one('.callNum').get_text()
                book_tmp['status'] = tr.select_one('.status').get_text()
                book_tmp['returnDate'] = tr.select_one('.returnDate').get_text()
                book_one[f'{no}'] = book_tmp

            return book_one


if __name__ == '__main__':
    a = input()
    Crawler.show_book_info(a)