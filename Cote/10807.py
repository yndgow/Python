import sys
x = int(sys.stdin.readline().rstrip())
y = list(map(int, sys.stdin.readline().rstrip().split()))
z = int(sys.stdin.readline().rstrip())
print(y.count(z))