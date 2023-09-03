import sys
N = int(input())
a = []
for _ in range(N):
    n, m = map(int, sys.stdin.readline().split())
    a.append(n+m)

for i in range(N):
    print(a[i])