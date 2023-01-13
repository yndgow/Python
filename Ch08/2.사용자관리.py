"""
날짜 : 2023/01/13
이름 : 김지홍
내용 : 파이썬 데이터베이스 실습하기
"""
import pymysql
import pandas as pd
from tabulate import tabulate

def formpret():
    users= []
    for row in cur.fetchall():
        users.append(row)
    df = pd.DataFrame(users, columns=['아이디', '비밀번호', '이름', '휴대폰', '나이'])
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=True))


conn = pymysql.connect(host='127.0.0.1',
                user='root',
                passwd='1234',
                db='java1db',
                charset='utf8')

# SQL 실행객체
cur = conn.cursor()


while True:
    print('0:종료, 1:등록, 2:조회, 3:검색, 4:삭제')
    answer = 0
    
    try:
        answer = int(input('선택 : '))
    except Exception as e:
        print('다시 입력하세요.', e)
        continue
    
    if answer == 0:
        break
    elif answer == 1:
        uid = input('아이디 : ')
        password = input('비밀번호 : ')
        name = input('이름 : ')
        hp = input('휴대폰 : ')
        age = input('나이 : ')  
        
        sql = "insert into `user1` set `uid` = %s, `pass`=%s,`name`=%s,`hp`=%s,`age`=%s"
        data = [uid, password, name, hp, age]
        cur.execute(sql, data)
        conn.commit()
    elif answer == 2:
        sql = "select * from user1"
        cur.execute(sql)
        conn.commit()
        formpret()
    elif answer == 3:
        uid = input('검색할 아이디 : ')
        sql = "select * from user1 where uid = %s"
        data = [uid]
        cur.execute(sql, data)
        formpret()
    elif answer == 4:
        uid = input('삭제할 아이디 : ')
        sql = "delete from user1 where uid = %s"
        data = [uid]
        cur.execute(sql, data)
        conn.commit()
    else:
        print('0~4 중에 입력하세요')

# 데이터 베이스 종료
conn.close()
print('프로그램 종료...')  