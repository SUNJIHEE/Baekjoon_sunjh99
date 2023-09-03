import sys
res = int(input())
N = int(input())

a = []
for _ in range(N):
    n, m = map(int,sys.stdin.readline().split())
    a.append(n*m)

result = 0
for i in range(N):
    result += a[i]
if result == res:
    print('Yes')
else:
    print('No')