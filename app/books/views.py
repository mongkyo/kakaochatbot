import re
import json
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


def keyboard(request):

    return JsonResponse({
        'type': 'buttons',
        'buttons': ['버튼1', '버튼2']
    })

@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.load(json_str)
    datacontent = received_json_data['content']

    if datacontent == '버튼1':
        button1 = "버튼1을 누르셨습니다."

        return JsonResponse({
            'message': {
                'text': button1
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['버튼1', '버튼2']
            }
        })

    elif datacontent == '버튼2':
        button2 = "버튼2을 누르셨습니다."

        return JsonResponse({
            'message': {
                'text': button2
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['버튼1', '버튼2']
            }
        })



def create_soup(keyword):
    res = requests.get(f'https://nsulib.nsu.ac.kr/search/tot/result?st=KWRD&si=TOTAL&q={keyword}&x=0&y=0')
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def book_search(keyword):
    """
    책 검색 정보를 불러와준다
    """
    # res = requests.get(f'https://nsulib.nsu.ac.kr/search/tot/result?st=KWRD&si=TOTAL&q={keyword}&x=0&y=0')
    # html = res.text
    # soup = BeautifulSoup(html, 'html.parser')
    book_info = []
    soup = create_soup(keyword)
    ul = soup.select_one('.resultList')
    li = ul.select('.items')[0]
    book_one = dict()
    book_detail = dict()
    book_one['title'] = li.select_one('dd.title > a').get_text()
    book_one['author'] = li.select('dd.info')[0].get_text()
    book_one['publisher'] = li.select('dd.info')[1].get_text()
    book_one['publish_year'] = li.select('dd.info')[2].get_text()
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
    book_info.append(book_one)
    return book_info


def return_book_info(request):
    pass
