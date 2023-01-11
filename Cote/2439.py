import sys
x = int(sys.stdin.readline().rstrip())
for i in range(x):
    for j in range(x, 0, -1):
        if j <= i+1:
            print('*', end='')
        else:
            print(' ', end='')
        
    print()
        