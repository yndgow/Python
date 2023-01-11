import sys
x = int(sys.stdin.readline().rstrip())
for i in range(x):
    for j in range(x-i):
        print(" ")
    print("*")