import sys
x = int(input())
y = list(map(int, sys.stdin.readline().rstrip().split()))
#y.sort()
#print(y[0], y[x-1])
print(min(y), max(y))