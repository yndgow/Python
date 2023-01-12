import sys
nlist = []
for i in range(9):
    x = int(sys.stdin.readline().rstrip())
    nlist.append(x)
print(max(nlist),nlist.index(max(nlist))+1, sep='\n')
