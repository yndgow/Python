import sys
while True:
    try:
        x, y =map(int, sys.stdin.readline().rstrip().split())    
    except:
        break
    print(x+y)    