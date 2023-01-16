"""
날짜 : 2023/01/16
이름 : 김지홍
내용 : 파이썬 네이버 뉴스 크롤링 실습하기
"""

import requests as req
from bs4 import BeautifulSoup as bs
from openpyxl import workbook
import time

# HTML 요청
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230'
html = req.get(url,headers={'User-Agent':'Mozilla/5.0'}).text
#print(html)
# print(html)
dom = bs(html, 'html.parser')
tit = dom.select_one('#main_content > div.list_header.newsflash_header > h3').text
print(tit)
# 문서객체 생성
lis = dom.select('#main_content > div.list_body.newsflash_body > ul > li')

# 문서파싱
for li in lis:
    title = li.select_one(' dl > dt:not(.photo) > a').text
    print(title.strip())
