"""
날짜 : 2023/01/17
이름 : 김지홍
내용 : 파이썬 기상청 날씨 정보 크롤링 실습하기
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pymysql

# 가상브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

# 기상청 이동 관측 도시별 관측
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

# 전국 지역명 출력
#trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')

"""
for tr in trs:
    c1 = tr.find_element(By.CSS_SELECTOR, 'td > a').text
    print(c1, c2)
"""
weatherlist = []
trs = browser.find_elements(By.CSS_SELECTOR, '#weather_table > tbody > tr')

for i in range(1, len(trs)+1):
    dName = []
    for j in range(1,15):
        if j == 0:
            data = browser.find_element(By.CSS_SELECTOR, '#weather_table > tbody > tr:nth-child({}) > td:nth-child({}) > a'.format(i, j)).text
            if data.isspace():
                data = None
            dName.append(data)
        else:
            data = browser.find_element(By.CSS_SELECTOR, '#weather_table > tbody > tr:nth-child({}) > td:nth-child({})'.format(i, j)).text
            if data.isspace():
                data = None
            dName.append(data)
    weatherlist.append(tuple(dName))            

#print(weatherlist)

# 가상 브라우저 종료
browser.close()

# Insert 실습

conn = pymysql.connect(host='127.0.0.1',
                user='root',
                passwd='1234',
                db='java1db')

# SQL 실행객체
cur = conn.cursor()

# SQL 실행
sql = """insert into `weather` values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now())"""
cur.executemany(sql, weatherlist)
conn.commit()

# 데이터베이스 종료
conn.close()
print('insert 완료...')
 




print('프로그램 종료...')