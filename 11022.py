import sys
x = int(sys.stdin.readline().rstrip())
for i in range(x):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    print('Case #{}: {} + {} = {}'.format(i+1, x, y, x+y))

