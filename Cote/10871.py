import sys
x, y = map(int, sys.stdin.readline().rstrip().split())
z = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0
for i in range(x):
    if z[i] < y:
       print(z[i], end=' ') 