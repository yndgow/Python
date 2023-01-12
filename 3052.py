import sys
nList = []
for i in range(10):
    x = int(sys.stdin.readline().rstrip())
    nList.append(x%42)
nSet = set(nList)
print(len(nSet))
    