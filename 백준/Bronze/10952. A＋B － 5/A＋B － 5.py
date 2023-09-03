import sys
a = []
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0:
        break
    else:
        print(n+m)