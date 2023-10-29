import sys
cnt = int(input())
nlist = list(map(int, sys.stdin.readline().rstrip().split()))
maxScore = max(nlist)
totalScore = 0
for n in nlist:
    n = n / maxScore * 100
    totalScore += n
print(totalScore/cnt)
