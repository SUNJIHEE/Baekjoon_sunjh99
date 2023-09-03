import sys
a = []
while True:
    try:
        n, m = map(int, sys.stdin.readline().split())
        if n == '':
            break
        print(n+m)
    except:
        break