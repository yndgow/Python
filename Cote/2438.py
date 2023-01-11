import sys
x = int(sys.stdin.readline().rstrip())
for i in range(x):
    for k in range(i+1):
        print('*', end='')
    print()
