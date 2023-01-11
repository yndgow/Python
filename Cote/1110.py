x = int(input())
a, b, c, d = 0, 0, 0, 0
cnt = 0
y = x
while True:
    cnt += 1
    a = y // 10
    b = y % 10
    c = a + b
    c %= 10
    d = b * 10 + c
    if d == x:
        print(cnt)
        break
    else: 
        y = d