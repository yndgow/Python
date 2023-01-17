"""
날짜 : 2023/01/17
이름 : 김지홍
내용 : 파이썬 크롤링 가상브라우저 실습하기
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# 가상브라우저 실행
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrome_options)

# 네이버 이동
browser.get('https://naver.com')

# 로그인 클릭
loginBtn = browser.find_element(by=By.CSS_SELECTOR, value='#account > a')
loginBtn.click()

# 아이디 비번 입력
input_id = browser.find_element(By.CSS_SELECTOR, '#id')
input_pw = browser.find_element(By.CSS_SELECTOR, '#pw')
input_id.send_keys('abcd')
input_pw.send_keys('1234')

# 최종 로그인 클릭
btnSubmit = browser.find_element(By.CSS_SELECTOR, '#log\.login')
btnSubmit.click()

while True:
    pass

