"""
날짜 : 2023/01/02
이름 : 김지홍
내용 : 파이썬 연산자 실습하기
"""

#대입연산자
a = 1
b = c = d = 0
e, f, g = 7, True, 'Apple'
print(a, b, c , d, e, f, g)

#산술연산자
num1 = 1
num2 = 2
num3, num4 = 3, 4

r1 = num1 + num2
r2 = num1 - num2
r3 = num2 * num3
r4 = num4 / num3
r5 = num4 // num3
r6 = num4 % num3
r7 = num3 ** num2
print(r1,r2,r3,r4,r5,r6,r7)

#복합대입연산자
num5, num6, num7, num8 = 5, 6, 7, 8

num5 += 1
num6 -= 2
num7 **= 3
num8 //= 4

print(num5, num6, num7, num8)

#비교연산자
var1 = 1 
var2 = 2

rs1 = var1 > var2
rs2 = var1 < var2
rs3 = var1 >= var2
rs4 = var1 <= var2
rs5 = var1 == var2
rs6 = var1 != var2

print(rs1, rs2, rs3, rs4, rs5, rs6)



#논리연산자
var3 = 3 
var4 = 4

res1 = var3 > 2 and var4 > 3
res2 = var3 > 2 or var4 > 5
res5 = not var3 > var4

print(res1, res2, res5)

